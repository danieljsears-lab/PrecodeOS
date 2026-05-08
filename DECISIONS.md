# Precode OS — Decision Log & Open Questions
<!-- ANCHOR: decisions -->

> AUTHORITY: Hard decisions currently in force, unresolved open questions, and superseded or historical decision context for this Precode OS scaffold.
> NOT_AUTHORITY: Detailed route structure, schema field definitions, generated progress state, or active task selection.
> LOAD_WHEN: Making or revisiting any architectural, product, or operating-system decision.
> CLASS: active-memory

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears
Document version: v0.1.2
Last updated: 2026-05-06

## Hard Decisions In Force Now

| Date | Decision | Rationale |
|---|---|---|
| 2026-04-26 | Active memory is limited to `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`. | Keeps agent context small and inspectable. |
| 2026-04-26 | Product features must pass the Product Definition Gate before implementation beads. | Prevents vague ideas from becoming code. |
| 2026-04-26 | Only one bead may be `in_progress`. | Keeps execution bounded and reviewable. |
| 2026-05-03 | Precode OS uses the repository root (`.`) as its app/workspace directory. | This repo is the OS itself, not a nested app scaffold. |
| 2026-05-03 | B000 project-specific checks are memory validation, version metadata advisory review, file-inventory advisory review, and completion/handoff advisory review. | Kernel setup changes docs and operating contracts, so review evidence should prove active-memory validity and surface doc-system warnings without requiring app runtime tests. |

## Open Questions

| # | Question | Affects | Status |
|---|---|---|---|
| OQ-1 | What app directory and project checks should this scaffold use after installation? | Verification | Resolved 2026-05-03 by hard decisions above. |

## Superseded / Historical Decisions

Historical context only. Do not implement from this section when it conflicts with active decisions above.

| Date | Decision | Superseded By |
|---|---|---|
|  |  |  |
