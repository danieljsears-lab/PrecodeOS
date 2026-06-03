---
bead_id: B006
status: proposed
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B002
parent_prd: none
requirement_ids:
  - DEMO-DETAIL-001
files_in_play:
  - index.html
  - src/**
checks:
  - bash scripts/record-check.sh -- npm run check
verification_type:
  - app check
  - manual verification
---

# B006 — Add Staircase Detail View

> AUTHORITY: Proposed later bead for showing additional context for a seeded staircase.
> NOT_AUTHORITY: Active work until explicitly approved in a later session.
> LOAD_WHEN: Showing proposed backlog-derived beads without activating them.
> CLASS: candidate-task

## Objective

Let users open a simple detail view for a seeded staircase card.

## Status

Proposed only. Do not activate during the beginner demo.
