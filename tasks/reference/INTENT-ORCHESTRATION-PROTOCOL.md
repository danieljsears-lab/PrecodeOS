# Precode OS -- Intent Orchestration Protocol
<!-- ANCHOR: intent-orchestration-protocol -->

> AUTHORITY: Intent lifecycle states, intent ownership by stage, promotion rules, mid-task intent-change handling, traceability expectations, and generated orchestration boundaries for Precode OS.
> NOT_AUTHORITY: Active memory expansion, product decisions, task selection, implementation plans, feature approval, generated progress state, or automatic bead transitions.
> LOAD_WHEN: Capturing rough intent, promoting source material into PRDs or decisions, changing direction mid-task, reviewing PRD-to-bead traceability, or auditing whether work is ready to proceed.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

Intent orchestration keeps a user's idea from becoming the wrong code.

Precode already separates ideas, source evidence, PRDs, decisions, beads, and recorded checks. This protocol names the lifecycle so agents and users can see where intent is stable, where it is still a candidate, and which file owns the next move.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Intent Lifecycle States

Use these states when explaining where an idea is in the Precode loop:

| State | Meaning | Typical owner |
|---|---|---|
| `raw` | A rough idea, note, issue, screenshot, or user request exists. | user/local source |
| `intake_summarized` | Source material has been summarized as evidence. | intake summary or PRD `Source Inputs` |
| `framed` | Problem, non-goals, before/after moment, risks, and verification path are understood enough to draft. | Idea-to-PRD workflow |
| `prd_draft` | A PRD shard exists but is not approved. | `tasks/prds/*.md` |
| `prd_approved` | Product definition is approved and can produce candidate beads. | approved PRD shard and `FEATURES.md` |
| `beads_proposed` | Candidate beads exist or are listed, but none is active by default. | PRD bead proposals or bead files |
| `bead_active` | One approved bead is the current execution contract. | `tasks/todo.md` and active bead |
| `evidence_recorded` | Checks, manual verification, or closeout evidence exists for the bead. | check logs and bead closeout |
| `accepted` | Review decision accepts the bead outcome. | bead closeout |
| `changed` | Intent changed after work started and needs owner-file handling. | PRD, `DECISIONS.md`, authority doc, or follow-up bead |
| `superseded` | Earlier intent is replaced by a newer approved decision or artifact. | owning authority file |
| `deferred` | Intent is intentionally not acted on now. | PRD notes, `DECISIONS.md`, or follow-up/backlog bead |

Generated reports may summarize these states. They do not own them.

## Ownership By Stage

| Intent stage | Owns | Does not own |
|---|---|---|
| Local/source material | raw evidence and user-provided context | approved requirements or active work |
| Intake summary | stable facts, assumptions, conflicts, open questions, candidates | product decisions or implementation plan |
| PRD shard | product problem, goals, non-goals, requirements, acceptance oracle, risks, approval | active task selection |
| `FEATURES.md` | compiled approved feature inventory | full PRD narrative or active execution state |
| `DECISIONS.md` | hard decisions and unresolved implementation-changing questions | task plans or generated summaries |
| Authority docs | architecture, API, schema, security, acceptance, deployment, or project rules | temporary source claims |
| Beads | one executable unit, files in play, checks, stop conditions, closeout | broad product definition |
| Check logs and closeout | evidence of what happened | future task selection |
| Generated reports | compiled snapshots and warnings | instructions, approvals, or owner-file mutation |

## Promotion Rules

Raw or imported intent becomes action only through one of these paths:

- source material -> reviewed intake -> PRD shard
- source material -> reviewed decision -> `DECISIONS.md`
- source material -> reviewed authority update -> owning reference doc
- approved PRD -> compiled feature inventory -> candidate beads
- candidate bead -> user-approved activation -> `tasks/todo.md`
- review finding -> accepted closeout, follow-up bead, decision, or authority update

Do not promote intent directly from generated reports, diary entries, audit output, GitHub issues, screenshots, chat summaries, or local notes into active work.

## Mid-Task Intent Change Pattern

When the user changes direction during a bead:

1. Stop implementation.
2. Name the change in plain English.
3. Identify the owner: PRD, `DECISIONS.md`, authority doc, active bead, follow-up bead, or defer note.
4. Decide whether the current bead still has one outcome.
5. If the change affects product definition, amend or revisit the PRD before continuing.
6. If it is a hard product or technical decision, record it in `DECISIONS.md`.
7. If it is separate work, create or name a follow-up bead instead of widening the active bead.
8. If it blocks current work, move the bead toward `needs_info` or `manual_testing` and record the escape path.

The active bead should not silently absorb changed intent.

## Traceability Expectations

For product-feature work, the intended trace is:

```text
source/input -> PRD requirement ID -> bead -> recorded checks/manual verification -> review decision
```

Older work may have partial traceability. New product-feature beads should cite a parent PRD and requirement IDs, and should record evidence strong enough for the requirement risk.

## Orchestration Boundaries

Generated orchestration maps, OS Health, scheduled audits, learning diary entries, and advisory checks are evidence only.

They may:

- show lifecycle position
- point to missing traceability
- warn about blocked or changed intent
- suggest human review prompts

They must not:

- choose the next task
- approve a PRD
- activate a bead
- rewrite `tasks/todo.md`
- mutate PRDs, `DECISIONS.md`, authority docs, or external systems

## Advisory Check

`scripts/orchestration-check.py` is advisory. It may warn about missing PRD traceability, PRDs without bead proposals, intent-looking `Next Up` entries, blocked work without an escape path, generated reports appearing to own active intent, or follow-up work that has no destination.

Warnings are generated evidence only. They do not choose tasks or approve transitions.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when intent state is clear but the next operating path is not.

Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when accepted, changed, superseded, deferred, or follow-up intent needs future-work visibility without task activation.
