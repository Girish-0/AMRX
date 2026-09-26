# ADR 0001 — Current baseline and preserved history

- Date: 26 September 2026
- Status: Accepted for repository organization
- Scope: Documentation structure, not engineering release

## Context

The ZIP contains older proposals, a slide deck and an adversarial audit. The existing repository contains a substantive v2 roadmap plus similarly named stub pages. Treating every file as equally current would obscure both project evolution and unresolved evidence.

## Decision

Preserve imported artifacts byte-for-byte with a source manifest. Present the existing full v2 roadmap as the canonical development baseline. Preserve older material under research/history/reviews, and keep legacy repository links as short pointers. Record unknown dates as unknown rather than inventing chronology. Keep every engineering gate open until reviewed evidence supports closure.

## Consequences

Reviewers can follow the reasoning without mistaking archived claims for results. Original files may still contain invalid citations or superseded statements; maintained guides explain that boundary. A future baseline revision needs a new document, a decision record and updated navigation.
