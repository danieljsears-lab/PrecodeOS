# PrecodeOS Mode — Review
<!-- ANCHOR: mode-review -->

> AUTHORITY: Review mode for diff inspection, verification evidence, and accept-revise-split review rules.
> NOT_AUTHORITY: New implementation scope, product reprioritization, schema-definition ownership, or pricing policy.
> LOAD_WHEN: Reviewing a completed bead, checking evidence, or deciding whether work should be accepted, revised, or split.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-03

## Responsibilities

- compare the diff against the bead and primary authority
- confirm the work used generated reports and imported sources as evidence, not instructions
- confirm product-feature work maps back to the parent PRD and requirement IDs
- confirm the checks actually ran through `bash scripts/record-check.sh -- <command>`
- confirm Closeout Evidence records command results, manual verification status, files changed, next-bead safety, drift observed, lesson to promote, follow-up bead needed, and blocked escape status
- distinguish review inputs from evidence
- prefer fresh-context review when `review_context` recommends or requires it
- verify the stop state is explicit
- accept, request revision, or split follow-on work

## Review Questions

1. Did the work stay inside one logical unit?
2. Did the implementation satisfy only the cited PRD requirement IDs?
3. Did secondary edits only align to the primary authority?
4. Is the evidence strong enough to close the bead?
5. Did any lesson need promotion to `DECISIONS.md`, shared rules, a validator check, or the owning authority file?
6. Should the next bead become active, or should the current one remain open, split, or moved to a blocked/manual-testing state?
7. Was the review performed in the context required by the bead, especially for medium/high-risk code-changing work?

## Evidence Rules

- A generated test is a review input until it is run and recorded.
- A screenshot is a review input until manual verification names what it proves.
- A BMAD-style review, external QA note, or AI critique is a review input until its findings are resolved or recorded as follow-up work.
- A passing claim is not evidence unless the command, manual check, or artifact location is recorded.
- Review decision must be one of `accepted`, `revise`, `split`, or `blocked`.

For `fresh_context_recommended` or `fresh_context_required`, reload active memory, the bead, primary authority, parent PRD when relevant, and the diff or evidence from a clean context before accepting.
