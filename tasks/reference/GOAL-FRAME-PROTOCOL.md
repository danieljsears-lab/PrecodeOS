# Precode OS -- Goal Frame Protocol
<!-- ANCHOR: goal-frame-protocol -->

> AUTHORITY: Goal Frame purpose, allowed locations, advisory workflow use, reaffirmation rules, auto-suggestion boundaries, and stale-goal guardrails for Precode OS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, implementation plans, backlog, roadmap, or generated progress state.
> LOAD_WHEN: A user wants to persist a durable goal, workflow arc, north-star outcome, or broad intent without creating active work or when `next-step.py` reports Goal Frame warnings.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-08

## Purpose

A Goal Frame is reviewed orientation for a workflow arc.

It helps a builder and agent remember what current work is in service of before choosing a workflow. It does not choose tasks, approve work, replace PRDs, activate beads, or expand active memory.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Allowed Locations

Store Goal Frames only inside existing owner files:

| Location | Use for |
|---|---|
| `PRODUCT.md` | product-level direction or current product arc |
| `tasks/prds/*.md` | feature-level outcome or PRD arc |
| `tasks/beads/*.md` | execution-specific orientation for one bead |
| `DECISIONS.md` | a durable goal tied to a hard product, technical, or operating decision |

Do not create a `goals/` directory or a fourth active-memory file.

## Goal Frame Format

Use this section when a durable goal needs to guide workflow selection:

```md
## Goal Frame

- Status: `draft | active | reaffirm_needed | retired`
- Last reaffirmed: `YYYY-MM-DD`
- Owner file: `PRODUCT.md | tasks/prds/... | tasks/beads/... | DECISIONS.md`
- Horizon: `session | feature | product`
- Workflow guidance: `intake | PRD | decomposition | implementation | review | repair | long-horizon`
- Goal:
- Why now:
- Success signal:
- Out of scope:
- Approval gates:
- Reaffirmation trigger:
```

Keep the fields plain-English and short. If a Goal Frame needs many steps, it is becoming a plan and should be moved through PRD, bead, decision, or long-horizon ownership instead.

## Lifecycle

| State | Meaning |
|---|---|
| `draft` | Candidate text exists but should not guide workflow yet. |
| `active` | The user has reviewed and reaffirmed the frame. It may guide workflow selection as advisory context. |
| `reaffirm_needed` | The frame may be stale, changed, or incomplete. Ask the user before using it. |
| `retired` | Historical orientation only. Do not use it to guide workflow. |

## Auto-Suggestion Rules

Agents and generated helpers may suggest a Goal Frame when:

- broad user intent sounds durable
- a Product Ideation Workbook becomes a Precode Ingestion Packet
- Local Source Intake finds stable intent
- a PRD draft lacks a clear outcome
- a bead proposal needs an execution-level orientation
- review accepts, splits, blocks, defers, or changes the work

Auto-suggestion means "draft a Goal Frame for review." It never means silently creating an active frame.

## Workbook Candidate Flow

The Product Ideation Workbook may produce a `Candidate Goal Frame For Precode Review` inside its Precode Ingestion Packet.

That candidate is local source evidence only. It is not a persisted Goal Frame until Local Source Intake summarizes it, the user reviews it, and the user reaffirms whether it should be promoted into the `## Goal Frame` section of `PRODUCT.md` or another allowed owner file.

Use this path:

```text
Initial Direction -> workbook refinement -> Candidate Goal Frame -> Local Source Intake -> user reaffirmation -> PRODUCT.md Goal Frame
```

If the candidate is conflicting, incomplete, stale, too task-like, or broader than the product constitution can own, keep it as intake evidence and ask the user whether to revise, retire, split, or route it to a PRD, bead, or `DECISIONS.md`.

## Reaffirmation Rules

Reaffirmation is required before a Goal Frame guides future workflow when:

- the frame is marked `reaffirm_needed`
- the active PRD or active bead changes
- a bead is accepted, split, blocked, deferred, or moved to manual testing
- the frame starts implying new work not already approved
- generated reports or `next-step.py` reference it after meaningful state change
- the builder is unsure whether the goal still applies

If the frame is stale, ask the user to reaffirm, revise, retire, or split it before using it.

## Boundaries

Goal Frames may:

- orient workflow selection
- help explain whether intake, PRD, decomposition, implementation, review, repair, or long-horizon review is the right next workflow
- appear in generated `next-step.py`, OS Health, and advisory checks
- remind a builder what outcome they previously reaffirmed

Goal Frames must not:

- choose the next task
- approve PRDs
- activate beads
- approve bead transitions
- rewrite `tasks/todo.md`
- become a backlog, roadmap, or task list
- replace PRDs, `DECISIONS.md`, beads, or authority docs
- override active memory, the active bead, or user approval

## Script Support

`scripts/goal-frame-check.py` is advisory. It may warn about missing reaffirmation, task-list-like Goal Frames, missing fields, conflicts with active state, or generated output treating a Goal Frame as authority.

`scripts/next-step.py` may read Goal Frames as advisory context. It may recommend reaffirmation before workflow guidance. It must not treat Goal Frames as task authority.
