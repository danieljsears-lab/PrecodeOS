# PrecodeOS Candidate Queue
<!-- ANCHOR: candidate-queue -->

> AUTHORITY: User-maintained candidate intent queue for parked ideas, research leads, review ranking, product-value ratings, themes, near-bead sketches, promotion notes, and future-work visibility.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation priority, generated proof, project-board authority, or permission to code.
> LOAD_WHEN: A user wants to park ideas, review candidate intent, decide what needs research, prepare Local Source Intake, identify PRD candidates, or inspect candidate bead visibility before promotion.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-23

## Purpose

The Candidate Queue is a place for intents we have not lost, with enough evidence and status to decide what, if anything, deserves promotion.

It is upstream of PRDs and beads. It helps answer:

- What ideas have we parked?
- Which ones need research?
- Which ones are worth shaping?
- Which ones are blocked or stale?
- Which ones might become PRDs?
- Which approved PRDs have candidate beads?
- Which reviewed candidates have product-value ratings, themes, or near-bead sketches?

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
- Product-value ratings `P0`, `P1`, `P2`, and `P3` are product value only. They are not review order, implementation priority, sprint priority, task selection, or permission to code.
- Candidate IDs use `CQ-###-short-name`, for example `CQ-001-owner-dashboard`.
- Candidate IDs do not reserve PRD IDs or bead IDs.
- Do not create `B###` bead IDs here. Bead IDs are assigned only when real bead files are created.
- Near-bead sketch IDs use `CQ-###-short-name-S##`, for example `CQ-001-owner-dashboard-S01`. They are sketches only, not bead files.
- Do not copy raw notes wholesale into this file. Link or name the source and summarize only the decision-relevant parts.
- Do not store secrets, credentials, dashboard values, billing details, or private raw transcripts here.
- Use Question-To-Artifact Filing first when a useful answer from chat, planning, review, discovery, source intake, memory recall, or maintainer analysis might belong here but its destination is unclear. The recommendation does not file automatically, approve promotion, choose tasks, approve PRDs, activate beads, or update active memory.
- Promote only reviewed conclusions through Local Source Intake, Product Discovery, PRDs, decisions, authority-file updates, decomposition review, defer, or kill decisions.

## Product-Value Ratings

Use product-value ratings only after review:

| Rating | Meaning | Boundary |
|---|---|---|
| `P0` | Highest product value if the evidence and authority path hold. | Does not mean build now. |
| `P1` | Strong product value, likely worth shaping after open questions are addressed. | Does not outrank active work. |
| `P2` | Possible product value, needs more evidence or narrower framing. | Does not create a task. |
| `P3` | Low or speculative product value, likely defer, kill, or revisit later. | Does not close the candidate by itself. |
| `unrated` | No reviewed product-value rating yet. | Default for raw capture. |

## Global Theme Index

Use themes to help scan related parked intent. Themes do not rank candidates or choose work.

| Theme | Candidate IDs | Notes |
|---|---|---|
| Example theme | `CQ-001-example` | Replace or remove when real candidates are reviewed. |

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

## Candidate Entries

Reviewed queue entries live here. Keep templates below this section.

## Candidate Entry Template

Copy this section for each candidate.

### CQ-001-example -- Example Candidate

- Status: `idea`
- Reviewed rank: `1`
- Shaping status: `unshaped | proposed | reviewed | needs_research | blocked | stale | deferred`
- Product-value rating: `unrated | P0 | P1 | P2 | P3`
- Product-value rationale:
- Themes:
- User intent:
- Why this matters:
- Raw source pointer:
- Evidence or source pointers:
- Open questions:
- Primary hypothesis / learning target:
- Hypothesis review status: `untested | tested | narrowed | killed | promoted | stale | not applicable`
- Learning outcome:
- Stale or untested signals:
- Evidence strength: `unknown | weak | medium | strong`
- Weakest assumption:
- Blocked or stale reason:
- Promotion target: `Local Source Intake | Product Discovery | PRD draft | PRD amendment | DECISIONS.md | authority-file update | decomposition review | defer | kill`
- Related PRDs:
- Candidate bead visibility:
- Near-bead sketches:
  - `CQ-001-example-S01` -- Sketch title; likely authority; likely verification; dependencies; sketch status.
- Next review trigger:
- Last reviewed: `YYYY-MM-DD`

Shaping review:

- Rating boundary: Product value only; not review order, implementation priority, task selection, or permission to code.
- Sketch boundary: Near-bead sketches are not bead files, do not reserve `B###` IDs, and do not activate beads.
- Learning boundary: Hypothesis review status is evidence only; it does not approve product direction, rank candidates, promote entries, activate beads, choose tasks, require analytics, or create an experiment database.

Promotion notes:

- No promotion has been approved yet.

## Script-Assisted Review

`python3 scripts/candidate-queue.py --preview-import <path>` may preview minimal raw-note capture. The preview includes only a title, source pointer, short summary, open questions, and privacy warning.

`python3 scripts/candidate-queue.py --preview-shaping <path>` may validate an agent-authored JSON shaping proposal with candidate ID, product-value rating, rationale, themes, and near-bead sketches.

Script output is preview evidence only:

- `mutates_now: false`
- generated preview is not authority
- apply requires explicit `--apply --approve-action <ID>`
- product-value rating is not implementation priority
- near-bead sketches are not bead files

Apply may write only approved action IDs to `CANDIDATE-QUEUE.md`. It must not mutate `tasks/todo.md`, approve PRDs, activate beads, reserve `B###` IDs, or authorize implementation.
