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

- Checks run: `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-18T02:44:08.183322+00:00; log `logs/check-output/20260518T024408Z-python3-scripts-completion-check.py.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-18T02:44:31.556313+00:00; log `logs/check-output/20260518T024431Z-bash-scripts-validate-memory.sh.log` | `python3 scripts/completion-check.py` -> pass (exit 0) at 2026-05-18T02:44:34.281901+00:00; log `logs/check-output/20260518T024434Z-python3-scripts-completion-check.py.log` | `python3 scripts/version-check.py` -> pass (exit 0) at 2026-05-18T02:44:50.004303+00:00; log `logs/check-output/20260518T024449Z-python3-scripts-version-check.py.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-18T03:05:34.149217+00:00; log `logs/check-output/20260518T030534Z-bash-scripts-validate-memory.sh.log` | `python3 scripts/file-inventory.py --check` -> pass (exit 0) at 2026-05-18T03:05:34.185337+00:00; log `logs/check-output/20260518T030534Z-python3-scripts-file-inventory.py-check.log` | `python3 scripts/version-check.py` -> pass (exit 0) at 2026-05-18T03:05:34.194903+00:00; log `logs/check-output/20260518T030534Z-python3-scripts-version-check.py.log` | `bash scripts/validate-memory.sh` -> pass (exit 0) at 2026-05-18T21:02:17.854975+00:00; log `logs/check-output/20260518T210217Z-bash-scripts-validate-memory.sh.log`
- Result: latest recorded command status is pass (exit 0)
- Manual verification: Who checked: Codex. What was checked: inspected the new `docs/PRECODE-GUIDED-SETUP.md`, README/user-guide/explainer/file-inventory navigation updates, and maintainer roadmap setup notes; confirmed the guide starts by pulling PrecodeOS from the public GitHub repo, treats PrecodeOS as a package source rather than an app runtime, provides new-project and existing-project setup paths, keeps copy guidance grouped without replacing `docs/PRECODE-FILE-INVENTORY.md`, excludes private/generated/local/secret material from user setup, and keeps future bootstrap/CLI language maintainer-roadmap-only. Environment: local repository root `/Users/danielsears/Projects/precode-os` on 2026-05-18. Result: pass for guided setup documentation implementation after fresh recorded checks. Remaining uncertainty: `public-repo-check.py` reports the new guide as an untracked public candidate until it is staged or committed; completion-check still reports evidence newer than the latest session close until a new closeout is recorded; next bead selection remains intentionally unactivated.
- Files changed: 1 changed path(s) at last evidence update
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
