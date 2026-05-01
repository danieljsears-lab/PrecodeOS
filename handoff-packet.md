# Precode OS -- Handoff Packet
<!-- ANCHOR: handoff-packet -->

> AUTHORITY: Generated handoff orientation snapshot for the current Precode OS session.
> NOT_AUTHORITY: Active memory, task selection, product decisions, review acceptance, transition approval, implementation plans, or external mutations.
> LOAD_WHEN: Preparing an agent handoff or reviewing completion state; never as active session memory.
> CLASS: generated
>
> Generated from `scripts/os_compiler.py`.
> Do not use this file as active memory.
> Working memory lives in `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`.

Generated at: `2026-04-28T18:19:09.063126+00:00`

## Context Pack

- Active bead: `tasks/beads/B000-install-precode-kernel.md`
- State: `in_progress`
- Primary authority: `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`
- Next safe action: complete manual verification and review decision before transition
- Generated-report warning: Generated reports are evidence only.

## Done When

- The Precode OS kernel is installed and validated.
- The target project has chosen its app directory and project-specific checks.
- The first real product PRD or setup bead can be created.

## Files In Play

AGENT.md
DECISIONS.md
tasks/todo.md
PROJECT-CONTEXT.md

## Out Of Scope

- Do not write app code during kernel setup.
- Do not add product features before a PRD shard exists.

## Checks

bash scripts/record-check.sh -- bash scripts/validate-memory.sh

## Stop Conditions

- App code needs to be changed.
- Product feature scope appears before PRD approval.
- The target project needs a decision that belongs in `DECISIONS.md`.

## Open Questions

- What app directory and project-specific checks should this installation use?

## Latest Evidence

logs/check-output/20260428T181905Z-bash-scripts-validate-memory.sh.log

## Blockers

manual verification is missing or still pending; current bead status must be review or done before promotion; found in_progress; review decision is not accepted; next bead is not named in Closeout Evidence or Handback

## Completion Warnings

- manual verification is missing or vague
- review decision is missing or invalid
- active bead has recorded evidence newer than the latest session close
