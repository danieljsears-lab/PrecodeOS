---
bead_id: B000
status: in_progress
execution_mode: builder
bead_kind: setup
primary_authority: tasks/reference/IDEA-TO-PRD-WORKFLOW.md
depends_on: []
parent_prd: none
requirement_ids: []
files_in_play:
  - AGENT.md
  - DECISIONS.md
  - tasks/todo.md
  - tasks/beads/B000-install-precode-kernel.md
  - PROJECT-CONTEXT.md
checks:
  - bash scripts/record-check.sh -- bash scripts/validate-memory.sh
  - bash scripts/record-check.sh -- python3 scripts/version-check.py
  - bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check
  - bash scripts/record-check.sh -- python3 scripts/completion-check.py
verification_type:
  - doc validation
  - static advisory
---

# B000 — Install Precode Kernel
<!-- ANCHOR: b000-install-precode-kernel -->

> AUTHORITY: Starter bead for installing and validating the Precode OS active-memory kernel in a target project.
> NOT_AUTHORITY: Product feature scope, app implementation, route structure, schema definitions, or generated progress.
> LOAD_WHEN: Bootstrapping a clean Precode OS project.
> CLASS: active-task

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-03

## State

- ID: `B000`
- Status: `in_progress`
- Execution mode: `builder`
- Bead kind: `setup`

## Primary Authority

- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`

## Depends On

- none

## Parent PRD

- none

## Requirement IDs

- none

## Objective

Install the smallest working Precode OS kernel and adapt placeholders for the target project.

## Done When

- Active memory is exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- `PROJECT-CONTEXT.md` names Precode OS itself, its stack, roles, repository-root app directory, conventions, checks, and integration boundaries.
- Project-specific checks are listed in the active bead.
- Memory validation passes.
- Manual verification and review evidence requirements are exact enough for a reviewer to accept, revise, split, or block B000.

## Files In Play

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`
- `tasks/beads/B000-install-precode-kernel.md`
- `PROJECT-CONTEXT.md`

## Checks

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- python3 scripts/version-check.py`
- `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
- `bash scripts/record-check.sh -- python3 scripts/completion-check.py`

## Verification Type

- doc validation
- static advisory

## Stop If

- App code needs to be changed.
- Product feature scope appears before PRD approval.
- A new unresolved project decision appears that belongs in `DECISIONS.md`.

## Closeout Evidence

- Checks run: `env PYTHONPYCACHEPREFIX=/private/tmp/precode-pycache python3 -m py_compile scripts/os_compiler.py scripts/os-health.py scripts/local-hygiene-check.py scripts/local-hygiene-dry-run.py` -> pass (exit 0) at 2026-05-04T03:17:18.159395+00:00; log `logs/check-output/20260504T031718Z-env-PYTHONPYCACHEPREFIX-private-tmp-precode-pycache-python3-m-py_compile-scripts-os_compiler.py-scripts-os-health.py-scripts-local-hygiene-check.py-scripts-local-hygiene-dry-run.py.log` | `python3 scripts/context-check.py` -> pass (exit 0) at 2026-05-04T03:17:22.017846+00:00; log `logs/check-output/20260504T031721Z-python3-scripts-context-check.py.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-04T03:17:26.017161+00:00; log `logs/check-output/20260504T031725Z-python3-scripts-completion-check.py.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-07T23:35:38.096135+00:00; log `logs/check-output/20260507T233538Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-07T23:40:58.344137+00:00; log `logs/check-output/20260507T234058Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-08T14:11:37.859318+00:00; log `logs/check-output/20260508T141137Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-08T14:44:51.443514+00:00; log `logs/check-output/20260508T144451Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-08T15:14:35.647894+00:00; log `logs/check-output/20260508T151435Z-bash-scripts-validate-memory.sh.log`
- Result: latest recorded command status is pass (exit 0)
- Manual verification: Who checked: Codex. What was checked: inspected `PROJECT-CONTEXT.md`, `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`, and `tasks/beads/B000-install-precode-kernel.md`; confirmed B000 now describes Precode OS itself, names the repository root as the app/workspace directory, lists the product stack, roles, integrations, project-specific checks, review evidence, and no next-bead activation. Environment: local repository root `/Users/danielsears/Projects/precode-os` on 2026-05-03. Result: pass for review preparation. Remaining uncertainty: Dan/reviewer still needs to make the formal review decision.
- Files changed: none at last evidence update
- Next bead: not evaluated
- Review decision: blocked from transition until Dan/reviewer accepts, revises, splits, or blocks B000; evidence is ready for review.
- Drift observed: none recorded
- Lesson to promote: none
- Follow-up bead needed: not evaluated
- Blocked escape: not needed while status is `in_progress`
- Evidence source: `logs/check-results.jsonl`

## Handback

- Review the recorded checks and manual verification statement.
- Accept, revise, split, or block B000 without activating the next bead.
