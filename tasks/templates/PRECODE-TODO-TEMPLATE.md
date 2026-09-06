---
current_bead: tasks/beads/B###-short-name.md
current_state: in_progress
build_lane: setup and orientation
active_feature_window: first safe action
primary_authority: PRODUCT.md
---

# Project Active Work
<!-- ANCHOR: active-work -->

> AUTHORITY: Template for creating a project-specific `tasks/todo.md` that records the current task, done-when target, primary authority, files in play, checks, immediate next step, open questions, and noticed execution facts.
> NOT_AUTHORITY: Live active memory until copied to `tasks/todo.md` and adapted with user-approved project facts; resolved decisions, feature requirements, generated progress, or long-range roadmap commitments.
> LOAD_WHEN: Creating fresh project active-work state during approved setup; never as a substitute for the target project's `tasks/todo.md`.
> CLASS: reference template

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-09-06

## Current Bead

- `tasks/beads/B###-short-name.md`
- State: `in_progress`
- Build lane: setup and orientation
- Active feature window: first safe action

## Done When

- Replace this line with the approved, observable setup or orientation outcome.
- The target project has exactly one `in_progress` bead.
- The target validates before product implementation begins.

## Primary Authority File

- `PRODUCT.md`

Replace this placeholder with the owner file or protocol that governs the current bead.

## Files In Play

- `tasks/todo.md`
- `tasks/beads/B###-short-name.md`

List only files approved for the current bead.

## Checks To Run

- `bash scripts/validate-memory.sh`
- `python3 scripts/file-inventory.py --check`

Add project-specific checks only after an owner file or approved bead names them.

## Explicit Out-of-Scope

- Product implementation before setup validation and a separate product-work approval.
- Unapproved owner-file, hook, CI, app-code, secret, or existing-file mutation.

## Next Up

- Complete setup validation, open the First Session Card or Daily Cockpit, and identify the next safe action.

## Open Questions

- Which project fact, owner, or approval is still missing?

## Noticed

- Record execution facts here without expanding the current bead.

## Closeout Evidence

- Status: pending
- Changed: pending
- Checks: pending
- Manual verification: pending
- Review: pending
- Parked follow-ups: pending
- Work digest: pending
- Suggested commit message: pending
- Next safe action: pending
