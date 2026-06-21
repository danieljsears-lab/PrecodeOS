# PrecodeOS -- Candidate Queue Protocol
<!-- ANCHOR: candidate-queue-protocol -->

> AUTHORITY: Candidate Queue rules, candidate states, queue entry fields, user-reviewed ranking boundaries, promotion paths, and forbidden uses for parked intent before PRDs or beads.
> NOT_AUTHORITY: Active memory, task selection, product approval, PRD approval, bead activation, implementation priority, generated progress state, generated proof, project-board authority, or permission to code.
> LOAD_WHEN: Capturing parked ideas, reviewing backlog-like requests, ranking candidates for review, deciding whether intent needs research, routing candidates to intake/discovery/PRD/decomposition, or checking candidate bead visibility.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-21

## Purpose

A Candidate Queue says: "Here are intents we have not lost, with enough evidence/status to decide what, if anything, deserves promotion."

The queue is upstream of PRDs and beads. It gives users a structured place to park ideas, research leads, possible future work, stale or blocked intent, and approved-PRD bead visibility without making those candidates active work.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## What The Queue Can And Cannot Answer

The Candidate Queue can help answer:

- what ideas are parked
- which ideas need research
- which ideas are worth shaping
- which ideas are blocked or stale
- which ideas might become PRDs
- which approved PRDs have candidate beads

The Candidate Queue cannot answer:

- what the active task is
- what the agent should build next
- whether a PRD is approved
- whether a bead is active
- whether a ranked candidate is authorized for implementation

## Candidate States

Use these states when reviewing queue entries:

| State | Meaning |
|---|---|
| `idea` | A parked intent exists, but evidence and owner path are unclear. |
| `research_needed` | The candidate needs Product Discovery, user evidence, source review, or a non-code learning step before shaping. |
| `ready_for_intake` | The candidate has enough source pointers for Local Source Intake. |
| `prd_candidate` | The candidate may become a PRD draft or PRD amendment after intake/review. |
| `bead_candidate` | The candidate references an approved PRD or non-product authority and may be decomposed into candidate beads. |
| `blocked` | A missing input, decision, manual setup, or external status blocks promotion. |
| `stale` | The candidate may conflict with current code, owner files, active PRD, active bead, or newer user intent. |
| `deferred` | The user intentionally postponed the candidate with an owner or revisit trigger when possible. |
| `promoted` | The candidate has moved into Local Source Intake, Product Discovery, a PRD, a decision, an authority update, or decomposition review. |
| `superseded` | A newer decision, PRD, candidate, or bead replaced this candidate. |
| `done` | The candidate's intended outcome was completed and retained as history or evidence. |
| `killed` | The user decided not to pursue the candidate. |

## Candidate Entry Fields

Every queue entry should include:

- Candidate ID: `CQ-###-short-name`
- Status
- Reviewed rank
- User intent
- Why this matters
- Evidence or source pointers
- Open questions
- Evidence strength
- Weakest assumption
- Blocked or stale reason when relevant
- Promotion target
- Related PRDs
- Candidate bead visibility when relevant
- Next review trigger
- Last reviewed date

Keep entries short. If the evidence is large, point to `project-evidence/`, a PRD `Source Inputs` section, or another local source path and summarize only stable, decision-relevant facts.

## Ranking Rules

Reviewed rank is a human review order. It is not implementation priority, sprint order, task selection, agent instruction, or permission to code.

Generated reports, agents, and scripts may surface candidate state or warn about missing promotion paths, but they must not automatically rank candidates, choose a candidate to build, approve a PRD, activate a bead, or mutate queue entries.

If ranking rationale is unclear, leave the rank blank or mark the candidate `research_needed`, `blocked`, `stale`, or `deferred` instead of inventing priority.

## Promotion Paths

Use the smallest promotion path that matches the candidate:

| Candidate condition | Next path |
|---|---|
| Raw idea, note, screenshot, issue, or research lead | Local Source Intake |
| Worth-building uncertainty is material | Product Discovery Validation |
| Durable orientation is needed but not a task | Goal Frame proposal or reaffirmation |
| Product behavior needs definition | PRD draft or PRD amendment |
| Hard product, technical, or operating decision is needed | `DECISIONS.md` |
| Architecture/API/data/security/acceptance fact is stable | owning authority-file update |
| Approved PRD or non-product authority is ready for execution planning | Decomposition Protocol |
| Work is not worth pursuing now | defer, supersede, or kill |

Promotion path:

```text
Candidate Queue -> Local Source Intake / Product Discovery / decision / PRD draft -> approved PRD -> candidate bead -> user-approved bead transition
```

Do not skip from a Candidate Queue entry directly to implementation unless the work is a tiny non-product maintenance fix that already has an owner file, clear verification path, and an approved bead route.

## Candidate IDs And Bead IDs

Candidate IDs are source IDs. Use `CQ-###-short-name` and keep them stable.

Do not reserve PRD IDs or bead IDs in the queue. PRD IDs are assigned when PRD shard files are created. Bead IDs are assigned only when actual bead files are created.

A PRD may cite an originating Candidate Queue ID in `Source Inputs`. A bead proposal may cite both the parent PRD and the originating Candidate Queue ID as source context, but the bead's authority still comes from the PRD or another primary authority file.

## Review Output

When reviewing the Candidate Queue, return:

- Current candidate:
- Status:
- Evidence used:
- Can help answer:
- Cannot answer:
- Recommended next path:
- Promotion target:
- User approval needed:
- Stop condition:
- Generated-report warning:

The review output is guidance only. It does not approve a PRD, activate a bead, choose next work, or update active memory.

## Forbidden Uses

The Candidate Queue must not:

- become active memory
- replace `tasks/todo.md`
- choose the active task
- approve PRDs
- activate beads
- reserve final bead IDs
- authorize implementation
- become a project board or sprint plan
- enable automatic ranking
- let generated reports rank or promote candidates
- store secrets or private raw evidence
- override current code, active memory, active bead, approved PRDs, owner files, or user approval

## Advisory Checks

Existing long-horizon, workflow, orchestration, decomposition, and completion checks may mention queue-related drift as generated evidence. Their warnings do not choose candidates, set priority, approve promotion, activate beads, or edit `CANDIDATE-QUEUE.md`.
