# PrecodeOS Candidate Queue
<!-- ANCHOR: candidate-queue -->

> AUTHORITY: User-maintained candidate intent queue for parked ideas, research leads, candidate ranking for review, promotion notes, and future-work visibility.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation priority, generated proof, project-board authority, or permission to code.
> LOAD_WHEN: A user wants to park ideas, review candidate intent, decide what needs research, prepare Local Source Intake, identify PRD candidates, or inspect candidate bead visibility before promotion.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-21

## Purpose

The Candidate Queue is a place for intents we have not lost, with enough evidence and status to decide what, if anything, deserves promotion.

It is upstream of PRDs and beads. It helps answer:

- What ideas have we parked?
- Which ones need research?
- Which ones are worth shaping?
- Which ones are blocked or stale?
- Which ones might become PRDs?
- Which approved PRDs have candidate beads?

It cannot answer:

- What is the active task?
- What should the agent build next?
- Is this PRD approved?
- Is this bead active?
- Is this ranked item authorized for implementation?

Use `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` before adding, reviewing, ranking, promoting, deferring, or killing queue entries.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Queue Rules

- Candidate ranking is review order only. It is not implementation priority.
- Candidate IDs use `CQ-###-short-name`, for example `CQ-001-owner-dashboard`.
- Candidate IDs do not reserve PRD IDs or bead IDs.
- Do not create `B###` bead IDs here. Bead IDs are assigned only when real bead files are created.
- Do not copy raw notes wholesale into this file. Link or name the source and summarize only the decision-relevant parts.
- Do not store secrets, credentials, dashboard values, billing details, or private raw transcripts here.
- Promote only reviewed conclusions through Local Source Intake, Product Discovery, PRDs, decisions, authority-file updates, decomposition review, defer, or kill decisions.

## Candidate States

Use one status per candidate:

- `idea`
- `research_needed`
- `ready_for_intake`
- `prd_candidate`
- `bead_candidate`
- `blocked`
- `stale`
- `deferred`
- `promoted`
- `superseded`
- `done`
- `killed`

## Review Queue

Keep this table short. Move detailed notes into each candidate entry.

| Rank | Candidate ID | Title | Status | Promotion target | Next review trigger |
|---:|---|---|---|---|---|
| 1 | `CQ-001-example` | Example candidate | `idea` | Local Source Intake | user review |

## Candidate Entry Template

Copy this section for each candidate.

### CQ-001-example -- Example Candidate

- Status: `idea`
- Reviewed rank: `1`
- User intent:
- Why this matters:
- Evidence or source pointers:
- Open questions:
- Evidence strength: `unknown | weak | medium | strong`
- Weakest assumption:
- Blocked or stale reason:
- Promotion target: `Local Source Intake | Product Discovery | PRD draft | PRD amendment | DECISIONS.md | authority-file update | decomposition review | defer | kill`
- Related PRDs:
- Candidate bead visibility:
- Next review trigger:
- Last reviewed: `YYYY-MM-DD`

Promotion notes:

- No promotion has been approved yet.
