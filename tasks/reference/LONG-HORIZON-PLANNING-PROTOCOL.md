# PrecodeOS -- Long-Horizon Planning Protocol
<!-- ANCHOR: long-horizon-planning-protocol -->

> AUTHORITY: Long-horizon task visibility, future-work ownership, deferred and blocked work review, and promotion rules for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, generated progress state, bead activation, priority ordering, or project-board authority.
> LOAD_WHEN: Reviewing future work, deferred ideas, blocked beads, follow-up candidates, PRD-approved but unscheduled work, dependency chains, or long-range planning health.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-11

## Purpose

Long-horizon planning gives future work a visible but demoted place in Precode.

It helps a solo builder see what is approved, blocked, deferred, proposed, or ready for human review without turning the future into active memory.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Long-Horizon Work States

Use these terms when reviewing future work:

| State | Meaning |
|---|---|
| `idea` | A raw user idea or note that has not been shaped |
| `source_intake` | Local or external material summarized as evidence |
| `prd_draft` | Product definition exists but is not approved |
| `prd_approved` | Product direction is approved and can propose beads |
| `bead_proposed` | A candidate bead exists in a PRD or planning output |
| `ready` | A bead file is ready but not active |
| `blocked` | Work is waiting on information, manual setup, external status, or another bead |
| `deferred` | Work is intentionally postponed with an owner or revisit trigger when possible |
| `follow_up_candidate` | Closeout mentions future work that has not yet become an owned bead, PRD amendment, decision, or explicit defer note |
| `superseded` | Work was replaced by a newer decision, PRD, bead, or scope |
| `done` | Work is completed and retained as history or evidence |

## Ownership Rules

- PRDs own product intent, approved requirements, and proposed product beads.
- Bead files own executable work and durable task contracts.
- `DECISIONS.md` owns hard product, technical, or operating-system decisions.
- Bead closeout owns immediate follow-up signals from the just-finished or blocked work.
- Reference docs own repeatable process rules.
- Generated long-horizon maps summarize state only.

`tasks/todo.md` remains current execution only. It must not become a backlog, roadmap, milestone tracker, project board, or parking lot for future work.

## Promotion Path

Future work becomes active only through the normal Precode path:

```text
source evidence or idea -> PRD, decision, or authority-file update -> candidate bead -> readiness and decomposition check -> user-approved bead transition
```

Generated maps, health reports, diary entries, and audit warnings may point at future work, but they must not activate it, rank it, rewrite owner files, or bypass approval.

## Revisit Guidance

Deferred or blocked work should name, when possible:

- owner file or bead
- reason for deferral or block
- dependency or missing input
- revisit trigger
- whether an unblocker bead is needed

Examples of revisit triggers:

- after a named PRD is approved
- after a manual dashboard setup is complete
- after a dependency bead is done
- after a user decision is recorded
- after external status changes

If the owner or revisit trigger is unknown, record that uncertainty in the correct owner file instead of hiding it in `tasks/todo.md`.

## Advisory Check

`scripts/long-horizon-check.py` is advisory. It may warn about roadmap language leaking into active memory, approved PRDs without bead proposals, ready or proposed beads missing readiness fields, blocked beads without escape paths, follow-up candidates without destinations, deferred or superseded work without owner or revisit trigger, dependency gaps, or generated reports appearing to drive active task selection.

Warnings are generated evidence only. They do not choose work, set priority, approve PRDs, activate beads, change bead state, or edit active memory.
