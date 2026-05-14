---
current_bead: tasks/beads/B000-install-precode-kernel.md
current_state: in_progress
build_lane: PrecodeOS adoption
active_feature_window: Install-ready package baseline
primary_authority: tasks/reference/IDEA-TO-PRD-WORKFLOW.md
---

# PrecodeOS — Active Work File
<!-- ANCHOR: active-work -->

> AUTHORITY: Current task, done-when target, primary authority file, files in play, checks to run, immediate next-up queue, open questions, and noticed execution facts.
> NOT_AUTHORITY: Resolved decisions, feature requirements, generated progress, or long-range roadmap commitments.
> LOAD_WHEN: Start and end of every session and whenever task scope materially changes.
> CLASS: active-memory

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-03

## Current Bead

- `tasks/beads/B000-install-precode-kernel.md`
- State: `in_progress`
- Build lane: PrecodeOS adoption
- Active feature window: Install-ready package baseline

## Done When

- PrecodeOS is reviewed as an install-ready package baseline.
- Active memory remains exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.
- PrecodeOS itself uses the repository root as the app/workspace directory.
- Package docs, shims, adapters, reference protocols, scripts, generated-output policy, maintainer boundary, and package hygiene are in B000 scope.
- Project-specific package checks for B000 are defined and recorded.
- B000 has exact manual verification and review evidence requirements.

## Primary Authority File

- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`

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

## Checks To Run

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- python3 scripts/version-check.py`
- `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
- `bash scripts/record-check.sh -- python3 scripts/public-repo-check.py`
- `bash scripts/record-check.sh -- python3 scripts/files-in-play-check.py`
- `bash scripts/record-check.sh -- python3 scripts/completion-check.py`

## Explicit Out-of-Scope

- Do not write product app code during package baseline review.
- Do not add product features before a PRD shard exists.
- Do not publish, deploy, mutate external repository settings, or start an installer mutation flow during B000 closeout.

## Next Up

- B000 package-baseline scope is accepted for review closeout.
- Propose the next PRD or setup bead without activating it until `python3 scripts/bead-transition.py --approve` is explicitly approved.

## Open Questions

- none

## Noticed

- This repository is PrecodeOS itself and should be install-ready as an OS package. The app/workspace directory is `.`.
- No product feature work is active during B000.
- The broad package file set is intentional current-bead scope for B000 package-readiness review, not drift.
- Generated root reports and `logs/` remain generated evidence only, not active memory or package authority.
- Maintainer-only planning now lives under `_maintainer/`; old `maintainer/` paths are intentionally outside public package scope.
