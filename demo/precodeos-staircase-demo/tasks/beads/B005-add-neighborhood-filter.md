---
bead_id: B005
status: proposed
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B002
parent_prd: none
requirement_ids:
  - DEMO-NEIGHBORHOOD-001
files_in_play:
  - index.html
  - src/**
checks:
  - bash scripts/record-check.sh -- npm run check
verification_type:
  - app check
  - manual verification
---

# B005 — Add Neighborhood Filter

> AUTHORITY: Proposed later bead for filtering seeded staircase cards by neighborhood.
> NOT_AUTHORITY: Active work until explicitly approved in a later session.
> LOAD_WHEN: Showing proposed backlog-derived beads without activating them.
> CLASS: candidate-task

## Objective

Let users filter seeded staircase cards by neighborhood.

## Status

Proposed only. Do not activate during the beginner demo.
