---
current_bead: tasks/beads/B002-add-difficulty-filter.md
current_state: in_progress
build_lane: PrecodeOS beginner demo
active_feature_window: First-use survival loop
primary_authority: tasks/reference/DEMO-WORKFLOW.md
---

# Active Work

## Current Bead

- `tasks/beads/B002-add-difficulty-filter.md`
- State: `in_progress`
- Build lane: PrecodeOS beginner demo
- Active feature window: First-use survival loop

## Done When

- Claude Code can run `bash scripts/session-start.sh`.
- Active memory validates.
- The current bead, primary authority, files in play, checks, and stop conditions are clear.
- The next product bead is visible but not active until transition approval.

## Primary Authority File

- `tasks/reference/DEMO-WORKFLOW.md`

## Files In Play

- `AGENT.md`
- `DECISIONS.md`
- `tasks/**`
- `scripts/**`
- `DEMO-NARRATION.md`

## Checks To Run

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- npm run check:docs`
- `bash scripts/record-check.sh -- python3 scripts/next-step.py`
- `bash scripts/record-check.sh -- python3 scripts/loop-health.py`

## Explicit Out-of-Scope

- Do not edit product app files during the readiness bead.
- Do not activate the difficulty-filter bead before explicit transition approval.
- Do not add maps, geolocation, persistence, accounts, APIs, deployment, or database work.

## Next Up

- Proposed next bead: `tasks/beads/B002-add-difficulty-filter.md`
- Requires explicit approval: `python3 scripts/bead-transition.py --approve`
