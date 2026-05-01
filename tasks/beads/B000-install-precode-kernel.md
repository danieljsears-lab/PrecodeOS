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
  - PROJECT-CONTEXT.md
checks:
  - bash scripts/record-check.sh -- bash scripts/validate-memory.sh
verification_type:
  - doc validation
---

# B000 — Install Precode Kernel
<!-- ANCHOR: b000-install-precode-kernel -->

> AUTHORITY: Starter bead for installing and validating the Precode OS active-memory kernel in a target project.
> NOT_AUTHORITY: Product feature scope, app implementation, route structure, schema definitions, or generated progress.
> LOAD_WHEN: Bootstrapping a clean Precode OS project.
> CLASS: active-task

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

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
- `PROJECT-CONTEXT.md` names the target project's stack, conventions, and integration boundaries.
- Project-specific checks are listed in the active bead.
- Memory validation passes.

## Files In Play

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`
- `PROJECT-CONTEXT.md`

## Checks

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`

## Verification Type

- doc validation

## Stop If

- App code needs to be changed.
- Product feature scope appears before PRD approval.
- The target project needs a decision that belongs in `DECISIONS.md`.

## Closeout Evidence

- Checks run: `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-27T16:52:49.055373+00:00; log `logs/check-output/20260427T165248Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-27T17:19:26.328250+00:00; log `logs/check-output/20260427T171926Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-27T20:39:24.762485+00:00; log `logs/check-output/20260427T203924Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-27T21:27:25.651710+00:00; log `logs/check-output/20260427T212725Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-27T22:28:23.516733+00:00; log `logs/check-output/20260427T222823Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-28T17:45:40.637258+00:00; log `logs/check-output/20260428T174540Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-28T17:58:00.109089+00:00; log `logs/check-output/20260428T175759Z-bash-scripts-validate-memory.sh.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-04-28T18:19:05.893523+00:00; log `logs/check-output/20260428T181905Z-bash-scripts-validate-memory.sh.log`
- Result: latest recorded command status is pass (exit 0)
- Manual verification: not recorded
- Files changed: none at last evidence update
- Next bead: not evaluated
- Review decision: not reviewed
- Drift observed: none recorded
- Lesson to promote: none
- Follow-up bead needed: not evaluated
- Blocked escape: not needed while status is `in_progress`
- Evidence source: `logs/check-results.jsonl`

## Handback

- Replace scaffold placeholders with target-project facts.
- Run recorded validation before accepting this bead.
