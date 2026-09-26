#!/usr/bin/env python3
"""Check repository hygiene and provenance, not engineering results.

Historical citations, external URLs and heading anchors are not checked.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 10 * 1024 * 1024
REQUIRED = (
    'README.md', 'ROADMAP.md', 'CONTRIBUTING.md', 'CHANGELOG.md', 'SECURITY.md',
    'docs/README.md', 'docs/STATUS.md', 'docs/LICENSING.md',
    'docs/history/README.md', 'docs/engineering/ARCHITECTURE.md',
    'docs/provenance/source-manifest.json', '.github/CODEOWNERS',
    '.github/workflows/repository-quality.yml',
)
SECRET_PATTERNS = (
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'\bgh[pousr]_[A-Za-z0-9]{30,}\b'),
    re.compile(r'\bgithub_pat_[A-Za-z0-9_]{40,}\b'),
    re.compile(r'\bAKIA[0-9A-Z]{16}\b'),
)


def check():
    errors = []
    for name in REQUIRED:
        if not (ROOT / name).is_file():
            errors.append(f'Missing required file: {name}')
    try:
        manifest = json.loads((ROOT / 'docs/provenance/source-manifest.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [f'Cannot read provenance manifest: {exc}'] + errors
    originals = set()
    for entry in manifest['files']:
        name = entry['path']
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT):
            errors.append(f'Manifest path leaves repository: {name}')
            continue
        originals.add(name)
        if not path.is_file():
            errors.append(f'Missing source artifact: {name}')
            continue
        content = path.read_bytes()
        if len(content) != entry['bytes'] or hashlib.sha256(content).hexdigest() != entry['sha256']:
            errors.append(f'Source integrity mismatch: {name}')
    try:
        output = subprocess.check_output(
            ['git', '-c', f'safe.directory={ROOT.as_posix()}', 'ls-files',
             '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        return errors + [f'Cannot enumerate repository files: {exc}']
    names = sorted(set(output.decode('utf-8').rstrip('\0').split('\0')))
    link_count = 0
    markdown_count = 0
    for name in names:
        if not name:
            continue
        path = ROOT / name
        if not path.is_file():
            errors.append(f'Tracked file is missing: {name}')
            continue
        if path.stat().st_size > MAX_BYTES:
            errors.append(f'File exceeds 10 MiB; review storage policy: {name}')
        if (path.name == '.env' or path.name.startswith('.env.')) and path.name != '.env.example':
            errors.append(f'Environment file must not be committed: {name}')
        if path.suffix.lower() in {'.pem', '.key'}:
            errors.append(f'Potential credential file: {name}')
        if path.suffix.lower() not in {'.md', '.txt', '.json', '.yml', '.yaml', '.py', '.toml'}:
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            errors.append(f'Expected UTF-8 text: {name}')
            continue
        if any(pattern.search(text) for pattern in SECRET_PATTERNS):
            errors.append(f'Potential credential detected (value omitted): {name}')
        if path.suffix != '.md' or name in originals:
            continue
        markdown_count += 1
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'!?\[[^\]\n]*\]\(([^\n]+?)\)', prose):
            target = target.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            link_count += 1
            linked = (path.parent / unquote(parsed.path)).resolve()
            if not linked.is_relative_to(ROOT) or not linked.exists():
                errors.append(f'Broken relative file link in {name}: {target}')
    print(f'Checked {len(names)} files, {len(originals)} preserved artifacts, '
          f'{markdown_count} maintained Markdown documents and {link_count} local links.')
    return errors


if __name__ == '__main__':
    failures = check()
    if failures:
        for failure in failures:
            print(f'ERROR: {failure}', file=sys.stderr)
        sys.exit(1)
    print('Repository checks passed. Engineering validation remains separate.')
