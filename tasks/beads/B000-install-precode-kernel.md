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
  - "*.md"
  - .github
  - .gitignore
  - _maintainer
  - adapters
  - maintainer
  - NOTICE
  - scripts
  - tasks
  - TRADEMARK
checks:
  - bash scripts/record-check.sh -- bash scripts/validate-memory.sh
  - bash scripts/record-check.sh -- python3 scripts/version-check.py
  - bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check
  - bash scripts/record-check.sh -- python3 scripts/public-repo-check.py
  - bash scripts/record-check.sh -- python3 scripts/files-in-play-check.py
  - bash scripts/record-check.sh -- python3 scripts/completion-check.py
verification_type:
  - doc validation
  - static advisory
---

# B000 — Install Precode Package Baseline
<!-- ANCHOR: b000-install-precode-kernel -->

> AUTHORITY: Starter bead for installing and validating the PrecodeOS active-memory kernel in a target project.
> NOT_AUTHORITY: Product feature scope, app implementation, route structure, schema definitions, or generated progress.
> LOAD_WHEN: Bootstrapping a clean PrecodeOS project.
> CLASS: active-task

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-17

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

Install and review PrecodeOS as an install-ready package baseline, including the active-memory kernel, package docs, agent shims, adapters, reference protocols, support scripts, generated-output policy, and public/private maintainer boundary.

## Done When

- Active memory remains exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- PrecodeOS is documented as an install-ready package, with the repository root as the workspace.
- Package-owned root docs, agent shims, adapters, reference protocols, support scripts, and package hygiene checks are in scope for B000.
- Generated reports such as `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, and files under `logs/` are treated as generated evidence, not package source or active memory.
- Maintainer-only files live under `_maintainer/`; old `maintainer/` paths are intentionally removed from public package scope.
- Project-specific package checks are listed in the active bead and recorded before acceptance.
- Manual verification and review evidence explicitly cover the broad package baseline so it is accepted as current-bead work, not drift.

## Files In Play

- `*.md`
- `.github`
- `.gitignore`
- `_maintainer`
- `adapters`
- `maintainer`
- `NOTICE`
- `scripts`
- `tasks`
- `TRADEMARK`

## Checks

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- python3 scripts/version-check.py`
- `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
- `bash scripts/record-check.sh -- python3 scripts/public-repo-check.py`
- `bash scripts/record-check.sh -- python3 scripts/files-in-play-check.py`
- `bash scripts/record-check.sh -- python3 scripts/completion-check.py`

## Verification Type

- doc validation
- static advisory

## Stop If

- Product app code or external runtime setup needs to be changed.
- Product feature scope appears before PRD approval.
- A new unresolved project decision appears that belongs in `DECISIONS.md`.
- Package-readiness work crosses into a new product feature, installer mutation flow, external publishing, deployment, or repository-host mutation.

## Closeout Evidence

- Checks run: `python3 scripts/loop-health.py --json` -> pass (exit 0) at 2026-05-19T20:17:34.624848+00:00; log `logs/check-output/20260519T201734Z-python3-scripts-loop-health.py-json.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-19T20:17:37.701235+00:00; log `logs/check-output/20260519T201737Z-bash-scripts-validate-memory.sh.log` | `python3 scripts/version-check.py` -> pass (exit 0) at 2026-05-19T20:17:40.606169+00:00; log `logs/check-output/20260519T201740Z-python3-scripts-version-check.py.log` | `python3 scripts/file-inventory.py --check` -> pass (exit 0) at 2026-05-19T20:17:43.814891+00:00; log `logs/check-output/20260519T201743Z-python3-scripts-file-inventory.py-check.log` | `python3 scripts/public-repo-check.py` -> pass (exit 0) at 2026-05-19T20:17:48.358993+00:00; log `logs/check-output/20260519T201747Z-python3-scripts-public-repo-check.py.log` | `python3 scripts/files-in-play-check.py` -> pass (exit 0) at 2026-05-19T20:18:01.274591+00:00; log `logs/check-output/20260519T201801Z-python3-scripts-files-in-play-check.py.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-19T20:18:04.385713+00:00; log `logs/check-output/20260519T201804Z-python3-scripts-completion-check.py.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-19T20:18:31.928274+00:00; log `logs/check-output/20260519T201831Z-python3-scripts-completion-check.py.log`
- Result: latest recorded command status is pass (exit 0)
- Manual verification: Who checked: Codex. What was checked: ran the new Build Loop Health command in compact, verbose, and JSON modes; inspected lifecycle one-line integration in `scripts/checkpoint.sh` and `scripts/session-close.sh`; added deterministic `clarity-scenario-check.py` coverage for clear builder work, vague done-when, multiple active beads, no active bead with implementation changes, bounded explorer mode, explorer without an explicit question, and review closeout; reviewed public docs for lightweight Build Loop Health vocabulary and maintainer roadmap notes for v2 live drift detection and future `next-step.py` integration. Environment: local repository root `/Users/danielsears/Projects/precode-os` on 2026-05-19. Result: pass for Build Loop Health v1 implementation after fresh recorded checks. Remaining uncertainty: `public-repo-check.py` reports `scripts/loop-health.py` as an untracked public candidate until the new script is committed or otherwise tracked, and completion-check still reports evidence newer than the latest session close until a new closeout is recorded; next bead selection remains intentionally unactivated.
- Files changed: 10 changed path(s) at last evidence update
- Next bead: none
- Review decision: accepted for B000 package-baseline scope; broad package-readiness changes are approved current-bead work, not drift, and no next bead is activated by this acceptance.
- Drift observed: none recorded
- Lesson to promote: none
- Follow-up bead needed: not evaluated
- Blocked escape: not needed while status is `in_progress`
- Evidence source: `logs/check-results.jsonl`

## Handback

- Package-baseline scope is accepted.
- Do not activate a next bead until Dan approves a separate transition proposal with `python3 scripts/bead-transition.py --approve`.
