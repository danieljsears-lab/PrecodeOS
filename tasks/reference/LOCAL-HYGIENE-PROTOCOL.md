# Precode OS -- Local Hygiene Protocol
<!-- ANCHOR: local-hygiene-protocol -->

> AUTHORITY: Local hygiene categories, advisory cleanup policy, cache/build-output boundaries, bulky log-output retention rules, dry-run preview behavior, and cleanup protection rules for Precode OS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, bead state, cleanup approval, archive approval, delete approval, external mutation approval, or generated progress state.
> LOAD_WHEN: Reviewing local clutter, cache/build outputs, bulky generated logs, unexpected files under `logs/`, cleanup candidates, or dry-run cleanup previews.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-03

## Purpose

Local Hygiene keeps a Precode workspace understandable without letting cleanup destroy project truth or evidence.

Beginner rule:

> Truth is not cleanup; evidence is preserved; caches are disposable only when ignored and regeneratable.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## V1 Behavior

Local Hygiene v1 is non-destructive.

Allowed:

- advisory check
- dry-run preview
- generated preview manifests

Forbidden in v1:

- deleting files
- archiving files
- moving files
- compacting ledgers
- rewriting evidence rows
- clearing tool/session state

## Hygiene Categories

| Category | Examples | V1 treatment |
|---|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Never cleanup candidates. |
| Authority docs | PRDs, beads, reference docs, owner files | Never cleanup candidates. |
| Reviewed memory | `memory/cards/*.md` | Never cleanup candidates. |
| Generated reports and sidecars | `OS-HEALTH.md`, `logs/*.json`, generated `logs/*.md` | Regeneratable evidence, not cleanup targets in v1. |
| Append-only ledgers | `logs/*.jsonl` | Preserve; never mutate in v1. |
| Bulky log outputs | `logs/check-output/*`, `logs/scheduled-audit-output/*` | Archive candidates only when older than 90 days and not protected. |
| Cache/build outputs | `.cache`, `.pytest_cache`, `__pycache__`, `.next`, `.turbo`, `.vite`, `dist`, `build`, `target`, `coverage`, `node_modules`, `.venv` | Delete candidates only when ignored or untracked. |
| Temp files | OS/editor files under generated areas | Advisory warning until policy is explicit. |
| Tool/session state | auth caches, dashboard sessions, private local state | Never clear automatically. |

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
- files that are not proven ignored or untracked
- tool/session state

If a file is confusing but protected, report it as protected or unexpected. Do not suggest removing it.

## Bulky Log Retention

Default retention for bulky timestamped generated output is 90 days.

Only these families are v1 bulky log candidates:

- `logs/check-output/*`
- `logs/scheduled-audit-output/*`

Old bulky log outputs are future archive candidates, not delete candidates.

## Cache And Build Outputs

Cache/build outputs may become future delete candidates only when all are true:

- the path matches a known disposable cache/build/dependency pattern
- the path is ignored or untracked
- the path is not active memory, authority, reviewed memory, generated evidence ledger, or current/unaccepted bead evidence

When `git` status cannot prove ignored or untracked state, do not mark the path as a cleanup candidate.

## Dry-Run Preview

`scripts/local-hygiene-dry-run.py` writes generated preview manifests:

- `logs/local-hygiene-preview.json`
- `logs/local-hygiene-preview.md`

The preview may classify rows as:

- `would_archive_log_output`
- `would_delete_cache`
- `protected`

The preview must clearly say it does not move, delete, archive, compact, or rewrite candidate files.

## Commands

Use:

```bash
python3 scripts/local-hygiene-check.py
python3 scripts/local-hygiene-dry-run.py
```

Record these through `record-check.sh` only when they are part of bead evidence.

## Advisory Check

`scripts/local-hygiene-check.py` is advisory. It may warn about bulky logs past retention, unexpected files under `logs/`, missing referenced check-output files, ignored/untracked cache candidates, and protected evidence.

Warnings are generated evidence only. They do not approve cleanup, archive files, delete caches, choose tasks, or replace user judgment.
