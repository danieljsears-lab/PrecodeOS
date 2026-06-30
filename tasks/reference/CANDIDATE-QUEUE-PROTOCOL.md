# PrecodeOS -- Candidate Queue Protocol
<!-- ANCHOR: candidate-queue-protocol -->

> AUTHORITY: Candidate Queue rules, candidate states, queue entry fields, product-value ratings, themes, near-bead sketch rules, user-reviewed ranking boundaries, promotion paths, script preview/apply gates, and forbidden uses for parked intent before PRDs or beads.
> NOT_AUTHORITY: Active memory, task selection, product approval, PRD approval, bead activation, implementation priority, generated progress state, generated proof, project-board authority, or permission to code.
> LOAD_WHEN: Capturing parked ideas, reviewing backlog-like requests, ranking candidates for review, deciding whether intent needs research, routing candidates to intake/discovery/PRD/decomposition, or checking candidate bead visibility.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-06-30

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
- which reviewed candidates have product-value ratings, themes, or near-bead sketches

The Candidate Queue cannot answer:

- what the active task is
- what the agent should build next
- whether a PRD is approved
- whether a bead is active
- whether a ranked candidate is authorized for implementation

## Shaping Scope

Candidate Queue shaping may add reviewed metadata that helps a user decide what deserves promotion:

- shaping status
- product-value rating
- product-value rationale
- themes
- raw source pointer
- near-bead sketches
- sketch status
- dependencies
- likely authority
- likely verification
- weakest assumption

This shaping is not product approval. It does not approve a PRD, activate a bead, reserve a bead ID, choose the next task, mutate `tasks/todo.md`, or authorize implementation.

Use Plan Mode before developing a Candidate Queue entry from an idea, feature angle, not-yet item, or rough implementation thought. In Codex, use `/plan`; in Claude Code, use Plan Mode; in other agents, use an equivalent read-only planning mode. If the user later selects a candidate for implementation planning, use Plan Mode again before drafting the implementation plan. The resulting Plan Packet, queue entry, or implementation plan is evidence only and must still move through Local Source Intake, Product Discovery, PRD work, decisions, owner-file updates, Architecture Shaping, Decomposition, defer, kill, or stop.

## Product-Value Ratings

Use `P0`, `P1`, `P2`, `P3`, or `unrated` only as reviewed product-value ratings.

| Rating | Meaning | Forbidden interpretation |
|---|---|---|
| `P0` | Highest product value if evidence and authority path hold. | Build next, active task, sprint priority, or implementation permission. |
| `P1` | Strong product value worth shaping after open questions are addressed. | Active-work priority. |
| `P2` | Possible product value that needs more evidence or narrower framing. | A task or approved PRD. |
| `P3` | Low or speculative product value, likely defer, kill, or revisit later. | Automatic rejection or done state. |
| `unrated` | No reviewed product-value rating exists yet. | Hidden priority. |

Product-value ratings are separate from reviewed rank. Reviewed rank is queue review order only. Product-value rating is product judgment only. Neither field can select work.

## Global Theme Index

`CANDIDATE-QUEUE.md` may include a Global Theme Index to group related candidates by user-visible theme.

Themes are scan aids. They must not become categories for automatic ranking, sprint planning, task selection, PRD approval, bead activation, or implementation authorization.

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
- Shaping status
- Product-value rating
- Product-value rationale
- Themes
- User intent
- Why this matters
- Raw source pointer
- Evidence or source pointers
- Open questions
- Primary hypothesis / learning target
- Hypothesis review status
- Learning outcome
- Stale or untested signals
- Evidence strength
- Weakest assumption
- Blocked or stale reason when relevant
- Promotion target
- Related PRDs
- Candidate bead visibility when relevant
- Near-bead sketches when relevant
- Sketch status when relevant
- Dependencies when relevant
- Likely authority when relevant
- Likely verification when relevant
- Next review trigger
- Last reviewed date

Keep entries short. If the evidence is large, point to `project-evidence/`, a PRD `Source Inputs` section, or another local source path and summarize only stable, decision-relevant facts.

Use the shared hypothesis vocabulary from Product Discovery:

- `hunch`: early belief worth preserving.
- `assumption`: unproven dependency.
- `hypothesis`: testable belief with user or situation, pain or current workaround, expected behavior, supporting evidence, weakest assumption, and falsifier.
- `experiment hypothesis`: metric-backed rollout bet for the Planning Protocol.

For `idea` and `research_needed` entries, the primary hypothesis may be a learning target rather than a polished statement. For `prd_candidate` entries, it should name what PRD shaping must preserve or test. Candidate Queue hypotheses are evidence and review mechanics only; they do not approve PRDs, rank work, activate beads, select tasks, or authorize implementation.

Use `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` when reviewing whether a queue entry's hypothesis or learning target is `untested`, `tested`, `narrowed`, `killed`, `promoted`, `stale`, or `not applicable`. These labels are learning review status only; they do not rank candidates, approve promotion, choose work, create tasks, activate beads, require analytics, or create an experiment database.

## Ranking Rules

Reviewed rank is a human review order. It is not implementation priority, sprint order, task selection, agent instruction, or permission to code.

Generated reports, agents, and scripts may surface candidate state or warn about missing promotion paths, but they must not automatically rank candidates, choose a candidate to build, approve a PRD, activate a bead, or mutate queue entries.

If ranking rationale is unclear, leave the rank blank or mark the candidate `research_needed`, `blocked`, `stale`, or `deferred` instead of inventing priority.

## Near-Bead Sketch Rules

Near-bead sketches are early decomposition notes attached to a queue entry. They may name likely outcomes, dependencies, likely authority, likely verification, and sketch status.

Use sketch IDs like `CQ-001-short-name-S01`.

Do not use `B###` IDs in the queue. Do not reserve final bead IDs. Do not create bead files from queue sketches without the normal authority path: Local Source Intake or Product Discovery when needed, approved PRD or owner-file authority, Decomposition Protocol review, and user-approved bead transition.

Near-bead sketches may inform decomposition only after readiness and owner-file review. They do not replace the parent PRD, `DECISIONS.md`, an authority file, or the Bead Decomposition Test.

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

## Script-Assisted Queue Review

`scripts/candidate-queue.py` is a public, local, deterministic helper for queue preview and approved writeback.

Supported modes:

- `python3 scripts/candidate-queue.py --preview-import <path>` reads a named raw notes file and proposes minimal queue-entry actions with IDs like `CQA-001`.
- `python3 scripts/candidate-queue.py --preview-shaping <path>` validates agent-authored JSON proposal input for candidate ID, themes, product-value rating, rationale, and near-bead sketches.
- `python3 scripts/candidate-queue.py --apply --approve-action <ID>` applies only explicitly approved action IDs to `CANDIDATE-QUEUE.md`.
- `python3 scripts/candidate-queue.py --json` prints structured preview or apply output.

Preview output must say:

- `mutates_now: false`
- generated preview is not authority
- apply requires explicit `--approve-action`
- product-value rating is not implementation priority
- near-bead sketches are not bead files

Raw-note import is minimal capture only: title, source pointer, short summary, open questions, and privacy warning. It is not a Local Source Intake replacement.

The script must not call an LLM/API, use the network, mutate external systems, create generated authority, write directly without approved action IDs, edit files other than `CANDIDATE-QUEUE.md`, mutate `tasks/todo.md`, approve PRDs, activate beads, or authorize implementation.

Apply must refuse missing approvals, unknown action IDs, malformed queue entries, duplicate candidate IDs, unknown candidate IDs, forbidden `B###` IDs, and any target file other than `CANDIDATE-QUEUE.md`.

## Candidate IDs And Bead IDs

Candidate IDs are source IDs. Use `CQ-###-short-name` and keep them stable.

Do not reserve PRD IDs or bead IDs in the queue. PRD IDs are assigned when PRD shard files are created. Bead IDs are assigned only when actual bead files are created.

A PRD may cite an originating Candidate Queue ID in `Source Inputs`. A bead proposal may cite both the parent PRD and the originating Candidate Queue ID as source context, but the bead's authority still comes from the PRD or another primary authority file.

## Review Output

When reviewing the Candidate Queue, return:

- Current candidate:
- Status:
- Evidence used:
- Primary hypothesis / learning target:
- Hypothesis review status:
- Learning outcome:
- Stale or untested signals:
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
- enable automatic ranking or automatic product judgment
- let generated reports rank or promote candidates
- treat P0/P1/P2/P3 as implementation priority
- treat near-bead sketches as bead files
- allow script preview to mutate files
- store secrets or private raw evidence
- override current code, active memory, active bead, approved PRDs, owner files, or user approval

## Advisory Checks

Existing long-horizon, workflow, orchestration, decomposition, and completion checks may mention queue-related drift as generated evidence. Their warnings do not choose candidates, set priority, approve promotion, activate beads, or edit `CANDIDATE-QUEUE.md`.
