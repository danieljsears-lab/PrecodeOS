---
bead_id: B002
status: in_progress
execution_mode: builder
bead_kind: feature
primary_authority: tasks/reference/DEMO-WORKFLOW.md
depends_on:
  - B001
parent_prd: none
requirement_ids:
  - DEMO-FILTER-001
files_in_play:
  - index.html
  - src/**
  - FEATURES.md
checks:
  - bash scripts/record-check.sh -- npm run check
  - bash scripts/record-check.sh -- npm run check:future
  - bash scripts/record-check.sh -- python3 scripts/loop-health.py
verification_type:
  - app check
  - manual verification
---

# B002 — Add Difficulty Filter

> AUTHORITY: First visible product bead for the staircase discovery demo app.
> NOT_AUTHORITY: Maps, geolocation, persistence, accounts, APIs, database work, deployment, or unrelated redesign.
> LOAD_WHEN: After B001 is accepted and `python3 scripts/bead-transition.py --approve` has activated this bead.
> CLASS: active-task

## Objective

Add a local difficulty filter to the existing seeded staircase cards.

## Done When

- The app shows a difficulty control with `All`, `Easy`, `Moderate`, and `Hard`.
- Selecting a difficulty shows only matching staircase cards.
- Selecting `All` restores the full seeded list.
- The implementation uses local static data only.
- Future ideas may be captured in `FEATURES.md` only if they remain clearly inactive.
- App checks pass.
- Future-work capture check passes if `FEATURES.md` is updated.
- Manual verification steps are clear enough for a beginner to follow.

## Files In Play

- `index.html`
- `src/**`
- `FEATURES.md` only for inactive future candidate notes

## Checks

- `bash scripts/record-check.sh -- npm run check`
- `bash scripts/record-check.sh -- npm run check:future`
- `bash scripts/record-check.sh -- python3 scripts/loop-health.py`

## Explicit Out-of-Scope

- Maps
- Geolocation
- Saved preferences
- Accounts
- APIs
- Database work
- Deployment
- Visual redesign
- Unrelated docs except inactive future candidate capture in `FEATURES.md`

## Stop If

- Claude proposes maps or geolocation.
- Claude introduces persistence, accounts, APIs, or a database.
- Claude changes files outside `index.html`, `src/**`, and inactive `FEATURES.md` capture.
- Claude activates or starts building an item from `FEATURES.md`.
- Claude says the bead is done without checks or manual verification.

## Closeout Evidence

- Checks run: not yet recorded
- Result: pending
- Manual verification: pending
- Review decision: pending
- Next bead candidate: `tasks/beads/B003-mark-staircase-visited.md`
