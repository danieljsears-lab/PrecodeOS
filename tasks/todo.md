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
Document version: v0.1.0
Last updated: 2026-04-26

## Current Bead

- `tasks/beads/B000-install-precode-kernel.md`
- State: `in_progress`
- Build lane: Precode OS adoption
- Active feature window: Kernel setup

## Done When

- The Precode OS kernel is installed and validated.
- The target project has chosen its app directory and project-specific checks.
- The first real product PRD or setup bead can be created.

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

## Explicit Out-of-Scope

- Do not write app code during kernel setup.
- Do not add product features before a PRD shard exists.

## Next Up

- Replace scaffold placeholders with the target project's product, stack, roles, and checks.
- Create the first PRD shard or setup bead.

## Open Questions

- What app directory and project-specific checks should this installation use?

## Noticed

- This is a clean Precode OS scaffold. App-specific facts should be added only by the adopting project.
