---
bead_id: B003
status: proposed
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B002
parent_prd: none
requirement_ids:
  - DEMO-VISITED-001
files_in_play:
  - index.html
  - src/**
checks:
  - bash scripts/record-check.sh -- npm run check
verification_type:
  - app check
  - manual verification
---

# B003 — Mark Staircase Cards As Visited

> AUTHORITY: Proposed next bead shown at the end of the demo.
> NOT_AUTHORITY: Active work until explicitly approved in a later session.
> LOAD_WHEN: Showing the next-bead gate without activating it.
> CLASS: candidate-task

## Objective

Let a user mark seeded staircase cards as visited.

## Status

Proposed only. Do not activate during the beginner demo.
