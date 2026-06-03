---
bead_id: B001
status: accepted
execution_mode: builder
bead_kind: setup
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on: []
parent_prd: none
requirement_ids: []
files_in_play:
  - AGENT.md
  - DECISIONS.md
  - tasks/**
  - scripts/**
  - DEMO-NARRATION.md
checks:
  - bash scripts/record-check.sh -- bash scripts/validate-memory.sh
  - bash scripts/record-check.sh -- npm run check:docs
  - bash scripts/record-check.sh -- python3 scripts/next-step.py
  - bash scripts/record-check.sh -- python3 scripts/loop-health.py
verification_type:
  - doc validation
  - workflow validation
---

# B001 — Validate Precode Readiness

> AUTHORITY: First demo bead for proving the PrecodeOS control loop is ready in this VSCode + Claude Code project.
> NOT_AUTHORITY: Product app implementation, visual redesign, or external setup.
> LOAD_WHEN: Starting the beginner demo.
> CLASS: active-task

## Objective

Validate that Claude Code can orient from active memory, identify the current bead, run the beginner workflow commands, and prepare for the first product bead without activating it prematurely.

## Done When

- `bash scripts/session-start.sh` runs and explains the active context.
- `bash scripts/validate-memory.sh` passes.
- `npm run check:docs` confirms local PrecodeOS reference docs are present.
- `python3 scripts/next-step.py` identifies the next human decision.
- `python3 scripts/loop-health.py` reports a usable health signal.
- The difficulty-filter bead is visible as next up but remains inactive until transition approval.

## Files In Play

- `AGENT.md`
- `DECISIONS.md`
- `tasks/**`
- `scripts/**`
- `DEMO-NARRATION.md`

## Checks

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- npm run check:docs`
- `bash scripts/record-check.sh -- python3 scripts/next-step.py`
- `bash scripts/record-check.sh -- python3 scripts/loop-health.py`

## Stop If

- Claude tries to edit product app files during this readiness bead.
- Claude cannot name the active bead or primary authority.
- Claude treats generated next-step guidance as approval.
- Claude tries to activate the next bead without explicit approval.

## Closeout Evidence

- Checks run: not yet recorded
- Result: pending
- Manual verification: pending
- Review decision: pending
- Next bead: `tasks/beads/B002-add-difficulty-filter.md`
