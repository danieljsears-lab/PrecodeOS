# PRD-053 -- Tier-2 Indentation Complexity
<!-- ANCHOR: prd-053-tier-2-indentation-complexity -->

> AUTHORITY: Public requirements for the advisory Tier-2 indentation-depth extension to Product Code Quality Snapshot.
> NOT_AUTHORITY: Code-quality certification, lint replacement, approval, acceptance, release readiness, or generated proof.
> LOAD_WHEN: Planning, implementing, reviewing, or validating Tier-2 indentation complexity.
> CLASS: prd

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-09-29

## Intent

Product Code Quality Snapshot may expose a language-agnostic structural cue when eligible changed files contain unusually deep leading indentation. The cue helps a human decide where to look; it does not judge whether the code is good.

## Requirements

| Requirement | Behavior | Priority |
|---|---|---:|
| PRD-053-FR01 | Existing active-bead and whole-codebase Snapshot modes emit an additive `indentation_complexity` group. | P0 |
| PRD-053-FR02 | Analysis reads only leading whitespace and ignores blank lines, common comment-only lines, excluded noise, binary-like files, and files over the bounded size limit. | P0 |
| PRD-053-FR03 | Spaces and tabs count as structural indentation units without interpreting language syntax; mixed indentation is reported as uncertainty. | P0 |
| PRD-053-FR04 | A file reaching depth 6 or greater may emit its maximum depth, deep-line count, and capped sample line numbers. | P0 |
| PRD-053-FR05 | Output identifies Tier-2 structural evidence, observed facts, uncertainty, and human-look interpretation without scoring, certification, gating, approval, or command execution. | P0 |
| PRD-053-FR06 | Unreadable, non-UTF-8, binary-like, mixed-indentation, and empty/shallow inputs remain explicit uncertainty or no-signal cases; absence of a signal is not evidence of health. | P0 |

## Validation

```bash
python3 scripts/product-code-quality-snapshot.py --self-test
python3 scripts/product-code-quality-snapshot.py --active-bead --json
python3 scripts/product-code-quality-snapshot.py --whole-codebase --json
```

The signal remains advisory evidence for human review. It does not run project checks, replace tests or linters, create proof, choose work, activate beads, accept implementation, approve review or release, or mutate external systems.
