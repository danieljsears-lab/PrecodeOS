# PrecodeOS -- Local Hygiene Protocol
<!-- ANCHOR: local-hygiene-protocol -->

> AUTHORITY: Local hygiene categories, advisory cleanup policy, preview classification, cache/build-output boundaries, bulky log-output retention rules, protected generated evidence rules, dry-run preview behavior, and cleanup protection rules for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, cleanup approval, archive approval, delete approval, external mutation approval, generated progress state, generated evidence truth, or future cleanup-apply permission.
> LOAD_WHEN: Reviewing local clutter, cache/build outputs, bulky generated logs, unexpected files under `logs/`, protected generated evidence, cleanup candidates, or dry-run cleanup previews.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.2.0
Last updated: 2026-06-14

## Purpose

Local Hygiene keeps a Precode workspace understandable without letting cleanup destroy project truth or evidence.

Beginner rule:

> Truth is not cleanup; evidence is preserved; caches are disposable only when ignored and regeneratable.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## V2 Behavior

Local Hygiene v2 is still non-destructive. It hardens the preview and protection layer before any cleanup mutation exists.

Allowed:

- advisory check
- dry-run preview
- generated preview manifests
- stable preview row classifications
- protected generated evidence classification
- deterministic preview-classification self-test

Forbidden in v2:

- deleting files
- archiving files
- moving files
- compacting ledgers
- rewriting evidence rows
- clearing tool/session state
- treating preview output as cleanup approval
- applying cleanup from generated output alone

Any future delete, archive, move, compact, or rewrite behavior needs a separate approved PRD or semantic-change proposal with explicit approval gates, rollback notes, archive or restore policy, and validation.

## Hygiene Categories

| Category | Examples | V2 treatment |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Never cleanup candidates. |
| Authority docs | PRDs, beads, reference docs, owner files | Never cleanup candidates. |
| Reviewed memory | `memory/cards/*.md` | Never cleanup candidates. |
| Generated reports and sidecars | `OS-HEALTH.md`, `logs/*.json`, generated `logs/*.md` | Regeneratable evidence; not cleanup targets in v2. |
| Protected generated evidence families | `logs/os-checkpoints/*` | Protected generated evidence, not generic clutter. |
| Append-only ledgers | `logs/*.jsonl` | Preserve; never mutate in v2. |
| Bulky log outputs | `logs/check-output/*`, `logs/scheduled-audit-output/*` | Future archive candidates only when older than 90 days and not protected. |
| Cache/build outputs | `.cache`, `.pytest_cache`, `__pycache__`, `.next`, `.turbo`, `.vite`, `dist`, `build`, `target`, `coverage`, `node_modules`, `.venv` | Future delete candidates only when ignored or untracked. |
| Temp files | OS/editor files under generated areas, such as `logs/.DS_Store` | `unexpected_review`; do not delete or archive from preview alone. |
| Tool/session state | auth caches, dashboard sessions, private local state | Never clear automatically. |

## Preview Classifications

`scripts/local-hygiene-dry-run.py` emits preview rows with these classifications:

| Classification | Meaning | Mutation allowed now |
|---|---|---|
| `candidate` | A future cleanup action could be considered after review and explicit approval. | No |
| `protected` | The path is evidence, authority, current/unaccepted work evidence, or another protected surface. | No |
| `unexpected_review` | The path is not a known expected log file or family and needs human review before policy applies. | No |
| `not_candidate` | The path looked relevant but is not proven safe for cleanup. | No |

Preview rows include:

- `candidate_id`
- `classification`
- `action`
- `path`
- `mutates_now: false`
- `approval_required`
- `protection_reason` or `review_reason`
- `rollback_note`

`approval_required` means approval would be needed before a future cleanup action. It does not mean the current preview can mutate files.

## Protection Rules

Never list these as cleanup candidates:

- active memory
- PRDs
- beads
- reviewed memory cards
- owner files
- append-only JSONL ledgers
- current-bead evidence
- unaccepted-bead evidence
- protected generated evidence families such as `logs/os-checkpoints/*`
- files that are not proven ignored or untracked
- tool/session state
- secrets, credentials, auth caches, or private local state

If a file is confusing but protected, report it as `protected` or `unexpected_review`. Do not suggest removing it.

## Bulky Log Retention

Default retention for bulky timestamped generated output is 90 days.

Only these families are bulky log candidates:

- `logs/check-output/*`
- `logs/scheduled-audit-output/*`

Old bulky log outputs are future archive candidates, not delete candidates. Protected current or unaccepted bead evidence stays `protected` even when old.

## Cache And Build Outputs

Cache/build outputs may become future delete candidates only when all are true:

- the path matches a known disposable cache/build/dependency pattern
- the path is ignored or untracked
- the path is not active memory, authority, reviewed memory, generated evidence ledger, protected generated evidence, or current/unaccepted bead evidence

When `git` status cannot prove ignored or untracked state, do not mark the path as a cleanup candidate. Mark it `not_candidate`.

## Dry-Run Preview

`scripts/local-hygiene-dry-run.py` writes generated preview manifests:

- `logs/local-hygiene-preview.json`
- `logs/local-hygiene-preview.md`

The preview must clearly say it does not move, delete, archive, compact, or rewrite candidate files.

Generated preview manifests are evidence only. They do not approve cleanup, choose tasks, prove completion, or override owner files.

## Commands

Use:

```bash
python3 scripts/local-hygiene-check.py
python3 scripts/local-hygiene-dry-run.py
python3 scripts/local-hygiene-dry-run.py --self-test
```

Record the check and dry-run commands through `record-check.sh` only when they are part of bead evidence.

## Advisory Check

`scripts/local-hygiene-check.py` is advisory. It may warn about bulky logs past retention, unexpected files under `logs/`, missing referenced check-output files, ignored/untracked cache candidates, and protected evidence.

Warnings are generated evidence only. They do not approve cleanup, archive files, delete caches, choose tasks, or replace user judgment.
