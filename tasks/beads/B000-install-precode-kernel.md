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

- Checks run: `python3 scripts/version-check.py` -> pass (exit 0) at 2026-05-14T04:38:15.078989+00:00; log `logs/check-output/20260514T043814Z-python3-scripts-version-check.py.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-14T04:38:50.089803+00:00; log `logs/check-output/20260514T043850Z-bash-scripts-validate-memory.sh.log` | `python3 scripts/file-inventory.py --check` -> pass (exit 0) at 2026-05-14T04:38:50.124965+00:00; log `logs/check-output/20260514T043850Z-python3-scripts-file-inventory.py-check.log` | `python3 scripts/version-check.py` -> pass (exit 0) at 2026-05-14T04:38:50.131252+00:00; log `logs/check-output/20260514T043850Z-python3-scripts-version-check.py.log` | `python3 scripts/files-in-play-check.py` -> pass (exit 0) at 2026-05-14T04:39:00.207378+00:00; log `logs/check-output/20260514T043900Z-python3-scripts-files-in-play-check.py.log` | `python3 scripts/public-repo-check.py` -> pass (exit 0) at 2026-05-14T04:39:00.870320+00:00; log `logs/check-output/20260514T043900Z-python3-scripts-public-repo-check.py.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-14T04:39:04.707899+00:00; log `logs/check-output/20260514T043904Z-python3-scripts-completion-check.py.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-14T04:39:20.764171+00:00; log `logs/check-output/20260514T043920Z-python3-scripts-completion-check.py.log`
- Result: latest recorded command status is pass (exit 0)
- Manual verification: Who checked: Codex. What was checked: inspected the B000 package baseline scope, the public GitHub `README.md` restructure, and the related `PRECODE-FILE-INVENTORY.md` description; confirmed the README now opens with badges and a builder-first promise, gives copyable clone/validation quickstart commands, points exhaustive navigation to the file inventory, preserves Precode metadata in the parser-visible top section and document footer, keeps generated reports as evidence only, and does not activate a next bead. Environment: local repository root `/Users/danielsears/Projects/precode-os` on 2026-05-14. Result: pass for B000 package-baseline acceptance after fresh recorded checks. Remaining uncertainty: completion-check still reports evidence newer than the latest session close until a new closeout is recorded; next bead selection remains intentionally unactivated.
- Files changed: 3 changed path(s) at last evidence update
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
