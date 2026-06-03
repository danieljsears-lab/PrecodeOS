---
bead_id: B007
status: proposed
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B002
parent_prd: none
requirement_ids:
  - DEMO-SHARE-001
files_in_play:
  - index.html
  - src/**
checks:
  - bash scripts/record-check.sh -- npm run check
verification_type:
  - app check
  - manual verification
---

# B007 — Share A Staircase Route

> AUTHORITY: Proposed later bead for sharing a seeded staircase route idea.
> NOT_AUTHORITY: Active work until explicitly approved in a later session.
> LOAD_WHEN: Showing proposed backlog-derived beads without activating them.
> CLASS: candidate-task

## Objective

Let users copy or share a simple staircase route recommendation.

## Status

Proposed only. Do not activate during the beginner demo.
