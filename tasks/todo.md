---
current_bead: tasks/beads/B000-install-precode-kernel.md
current_state: in_progress
build_lane: Precode OS adoption
active_feature_window: Kernel setup
primary_authority: tasks/reference/IDEA-TO-PRD-WORKFLOW.md
---

# Precode OS — Active Work File
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
- Build lane: Precode OS adoption
- Active feature window: Kernel setup

## Done When

- The Precode OS kernel is installed and validated.
- Precode OS itself uses the repository root as the app/workspace directory.
- Project-specific checks for B000 are defined and recorded.
- B000 has exact manual verification and review evidence requirements.

## Primary Authority File

- `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`

## Files In Play

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`
- `tasks/beads/B000-install-precode-kernel.md`
- `PROJECT-CONTEXT.md`

## Checks To Run

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- python3 scripts/version-check.py`
- `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
- `bash scripts/record-check.sh -- python3 scripts/completion-check.py`

## Explicit Out-of-Scope

- Do not write app code during kernel setup.
- Do not add product features before a PRD shard exists.

## Next Up

- Review B000 closeout evidence.
- After B000 is accepted, propose the next PRD or setup bead without activating it until `python3 scripts/bead-transition.py --approve` is explicitly approved.

## Open Questions

- none

## Noticed

- This repository is Precode OS itself. The app/workspace directory is `.`.
- No product feature work is active during B000.
