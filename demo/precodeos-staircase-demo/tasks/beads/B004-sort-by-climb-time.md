---
bead_id: B004
status: proposed
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B002
parent_prd: none
requirement_ids:
  - DEMO-SORT-001
files_in_play:
  - index.html
  - src/**
checks:
  - bash scripts/record-check.sh -- npm run check
verification_type:
  - app check
  - manual verification
---

# B004 — Sort Staircases By Climb Time

> AUTHORITY: Proposed later bead for sorting seeded staircase cards by estimated climb time.
> NOT_AUTHORITY: Active work until explicitly approved in a later session.
> LOAD_WHEN: Showing proposed backlog-derived beads without activating them.
> CLASS: candidate-task

## Objective

Let users sort seeded staircase cards by estimated climb time.

## Status

Proposed only. Do not activate during the beginner demo.
