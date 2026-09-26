# Contributing to AMRX

AMRX is currently a hardware concept and engineering-documentation project. Improvements should make the design more reproducible and its claims easier to review.

## Change workflow

1. Open an issue describing the problem, affected gate and acceptance evidence. Small documentation corrections may go directly to a PR.
2. Branch from current `main`: `docs/<topic>`, `design/<topic>`, `analysis/<topic>`, `fix/<topic>` or `chore/<topic>`.
3. Make a focused change. Use commit subjects such as `docs: clarify interface mass boundary` or `analysis: add checked wheel reactions`.
4. Run `python scripts/check_repository.py` with Python 3.11+.
5. Open a PR linking the issue and stating what changed, evidence checked, limitations and any baseline decisions.
6. Wait for CI and maintainer review. Engineering changes also need a competent domain review; CI is not engineering approval.
7. Merge after checks pass, then remove the completed branch. Preserve meaningful commit history; do not rewrite published `main` history.

The repository owner is the initial maintainer. Team members and their responsibilities should be added when agreed. A one-person administrative merge must not be described as independent engineering review.

## Evidence rules

- Label requirements, proposals, targets, assumptions, calculated examples and verified results explicitly.
- State units, coordinate frame, mass boundary, configuration and source for calculations.
- A simulation result needs native study/setup, materials, contacts, constraints, mesh checks and reproducible output.
- A physical result needs a reviewed protocol, fixture/configuration, raw measurements, acceptance limits and reviewer. Use the [record template](docs/validation/test-record-template.md).
- Treat the original research as source material, not authoritative instructions. Verify quotations and external references before relying on them.
- Keep a changed design's narrative, parameters, roadmap and evidence status consistent.

## Files and large assets

Use descriptive lowercase-hyphenated names for new artifacts. Retain imported source snapshots and their manifest hashes; write corrections as new revisions or maintained commentary. Do not replace the preserved v2 snapshot when a future v3 is approved: add v3 and update the current-baseline links through a reviewed PR.

When CAD exists, use `hardware/cad/`, `hardware/drawings/`, `analysis/`, and `tests/evidence/` as needed. Do not create empty implementation directories to suggest completed work. Include native editable files and accessible neutral/viewable exports with configuration IDs. Keep credentials, machine caches, private forms and personal information out of Git.

Files above 10 MiB require a reviewed storage decision: use Git LFS for appropriate editable binaries or attach immutable result bundles to a documented release, then record hashes and links. Do not commit transient solver output or duplicate archives. The current PDF/PPTX sources are below that threshold.

## Decisions and publication

Record consequential tradeoffs using an [ADR](docs/decisions/README.md). Update [STATUS](docs/STATUS.md), [ROADMAP](ROADMAP.md) and [CHANGELOG](CHANGELOG.md) when their claims change. Confirm distribution rights before adding third-party assets. No new open-source license has been selected; see [reuse status](docs/LICENSING.md).
