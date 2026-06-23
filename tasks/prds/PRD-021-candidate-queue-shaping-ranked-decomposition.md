---
prd_id: PRD-021
status: approved
owner: user
risk_level: medium
feature_link: Candidate Queue Shaping And Ranked Decomposition
features_status: not compiled
related_prds: []
---

# PRD-021 -- Candidate Queue Shaping And Ranked Decomposition
<!-- ANCHOR: prd-021-candidate-queue-shaping-ranked-decomposition -->

> AUTHORITY: Public requirements for Candidate Queue shaping, product-value ratings, themes, near-bead sketches, and approval-gated queue writeback.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation priority, generated authority, project-board authority, automatic product judgment, LLM/API behavior, or permission to code.
> LOAD_WHEN: Implementing or reviewing Candidate Queue shaping, ranked decomposition previews, raw-note queue import, or `scripts/candidate-queue.py`.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-021`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Candidate Queue Shaping And Ranked Decomposition`
- `FEATURES.md` status: `not compiled`
- Originating Candidate Queue ID: none; originating maintainer roadmap candidate `#6`

## Source Inputs

- Source type: `maintainer roadmap candidate | approved implementation plan | Candidate Queue protocol`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `#6`, `Candidate Queue Shaping And Ranked Decomposition`
  - `CANDIDATE-QUEUE.md`
  - `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md`
  - `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
- Stable facts:
  - The Candidate Queue is upstream of PRDs and beads.
  - Product-value ratings are product judgment only; they are not implementation priority, task selection, or authorization.
  - Near-bead sketches are candidate shaping notes; they do not reserve `B###` IDs and do not activate beads.
  - Raw-note import is minimal capture, not Local Source Intake replacement.
  - Script writeback must require explicit approved action IDs.
- Assumptions:
  - V1 uses agent-authored structured proposals plus deterministic validation.
  - V1 does not call an LLM, API, network, or external service.
  - Structured Markdown remains the canonical user-facing Candidate Queue format.
- Conflicts or stale inputs:
  - The term ranking can imply task priority. This PRD narrows P0/P1/P2/P3 to product value only.
- Privacy or secrets redactions:
  - Raw import must not copy private notes wholesale and must warn users not to store secrets, credentials, private transcripts, billing values, dashboard values, or sensitive raw data in the queue.

## Problem

Users want one place to park feature ideas and see early shaping: themes, rough product value, open questions, and possible decomposition shape. Without a reviewed queue surface, ideas either disappear, become premature PRDs, or leak into active-task language.

## User Moment

- Before: A user has raw feature ideas and wants a visible path toward PRDs or bead candidates, but the only safe answer is manual notes.
- After: The user can preview minimal queue capture from raw notes, review agent-authored shaping proposals, and apply only explicitly approved queue updates that preserve upstream boundaries.
- Why now: Candidate Queue already exists as public parked-intent guidance, and the next useful slice is reviewed shaping without implementation authority.

## Destination

- Destination statement: Candidate Queue can hold reviewed shaping fields, product-value ratings, themes, and near-bead sketches while staying upstream of PRDs and beads.
- Definition of done:
  - PRD-021 exists and owns the semantic boundary.
  - `CANDIDATE-QUEUE.md` and Candidate Queue Protocol define shaping fields, Global Theme Index, product-value rating boundaries, and sketch IDs.
  - `scripts/candidate-queue.py` previews raw-note import and shaping proposals, applies only approved action IDs, refuses forbidden bead IDs, and never mutates `tasks/todo.md`.
  - Related protocols and user docs expose the workflow and boundaries.
  - Clarity scenarios and script self-test cover rating, activation, preview, apply, import, and generated-authority limits.
  - Generated docs, PRD HTML, package inventory, maintainer changelog, and roadmap HTML are refreshed.
- First useful vertical slice: public docs, deterministic script, self-test, and text-contract scenarios only.

## Users

- Primary user: Builder or maintainer parking feature ideas before deciding whether they deserve intake, discovery, PRD shaping, decision, decomposition review, defer, or kill.
- Secondary user: AI agent drafting queue proposals for human review without creating task authority.
- Excluded user: Project manager expecting a sprint backlog, automation expecting automatic priority, or coding agent expecting permission to implement.

## Goals

- Goal 1: Capture raw feature ideas with minimal, privacy-aware queue entries.
- Goal 2: Let a human review product-value P0/P1/P2/P3 ratings, themes, and near-bead sketches.
- Goal 3: Preserve the Candidate Queue as evidence and visibility only, not work authorization.

## Non-Goals

- Not doing: product backlog, roadmap authority, sprint planning, generated priority, deterministic product judgment, LLM/API integration, direct task selection, PRD approval, bead activation, `B###` reservation, `tasks/todo.md` mutation, external mutation, package-manager behavior, or project-board behavior.
- Deferred: richer thematic analytics, queue reports, visual queue UI, cross-repo queue import, and automatic stale-candidate detection.
- Explicitly out of scope: treating P0 as "build next" or treating `CQ-001-S01` as a real bead ID.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-021-FR01` | Candidate Queue must define a Global Theme Index and reviewed shaping fields. | P0 | Public Markdown remains canonical. |
| `PRD-021-FR02` | Queue entries must support shaping status, product-value rating, product-value rationale, themes, raw source pointer, near-bead sketches, sketch status, dependencies, likely authority, likely verification, and weakest assumption. | P0 | Fields may be blank until reviewed. |
| `PRD-021-FR03` | Product-value ratings `P0`/`P1`/`P2`/`P3` must mean product value only. | P0 | Not review order, task priority, sprint order, or implementation permission. |
| `PRD-021-FR04` | Near-bead sketches must use IDs like `CQ-001-S01` and never `B###`. | P0 | Final bead IDs are assigned only when bead files are created. |
| `PRD-021-FR05` | `scripts/candidate-queue.py --preview-import <path>` must produce minimal queue-entry actions with IDs like `CQA-001`. | P0 | Title, source pointer, short summary, open questions, privacy warning only. |
| `PRD-021-FR06` | `scripts/candidate-queue.py --preview-shaping <path>` must validate agent-authored proposal JSON containing candidate ID, themes, product-value rating, rationale, and near-bead sketches. | P0 | The script validates; it does not invent product judgment. |
| `PRD-021-FR07` | `--apply --approve-action <ID>` must be required for writeback and must apply only approved action IDs to `CANDIDATE-QUEUE.md`. | P0 | No direct writeback. |
| `PRD-021-FR08` | Script output must support `--json` and clearly state `mutates_now: false`, generated preview is not authority, apply requires `--approve-action`, ratings are not implementation priority, and sketches are not bead files. | P0 | Plain and JSON output. |
| `PRD-021-FR09` | Self-test must cover parser, preview, apply refusal without approval, approved writeback, invalid P-ranks, forbidden `B###` IDs, unknown candidate IDs, and no `tasks/todo.md` mutation. | P0 | No network or external mutation. |
| `PRD-021-FR10` | Related protocols, user docs, package inventory, `llms.txt`, generated docs, maintainer changelog, and roadmap surfaces must be updated. | P1 | Public package follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-021-SEC01` | Raw import must summarize and point to source files instead of copying raw notes wholesale. | P0 | Avoid secret or private transcript spill. |
| `PRD-021-SEC02` | The script must not use network access, LLM/API calls, external systems, hidden model dependencies, or files outside the queue writeback target. | P0 | Stdlib-only local behavior. |
| `PRD-021-SEC03` | Apply must refuse unknown actions, missing approvals, duplicate candidate IDs, malformed entries, and any action containing `B###`. | P0 | Stops false authority and ID leakage. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-021-NFR01` | User-facing language must stay beginner-readable and explicit about authority boundaries. | P0 | Avoid backlog/sprint ambiguity. |
| `PRD-021-NFR02` | Script behavior must be deterministic, testable, and package-local. | P0 | No dependencies beyond Python stdlib. |
| `PRD-021-NFR03` | Existing queue content must be preserved. | P0 | Append/update targeted structured blocks only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-021-FR01` | Queue and protocol define shaping fields and Global Theme Index. | `python3 scripts/clarity-scenario-check.py` | Read Markdown. | Markdown source | check output |
| `PRD-021-FR05` | Raw-note preview proposes minimal capture and does not mutate. | `python3 scripts/candidate-queue.py --self-test` | Inspect preview output. | Synthetic raw note | command output |
| `PRD-021-FR06` | Shaping proposal validates candidate IDs, ratings, themes, and sketch IDs. | `python3 scripts/candidate-queue.py --self-test` | Inspect JSON proposal shape. | Synthetic proposal | command output |
| `PRD-021-FR07` | Apply refuses missing or unknown approved action IDs and writes only the queue when approved. | `python3 scripts/candidate-queue.py --self-test` | Review script behavior. | Temporary queue fixture | command output |
| `PRD-021-FR09` | Invalid P-ranks, `B###`, unknown candidates, and `tasks/todo.md` mutation are blocked. | `python3 scripts/candidate-queue.py --self-test` and `python3 scripts/clarity-scenario-check.py` | Boundary review. | Synthetic fixtures | check output |
| `PRD-021-FR10` | Docs and generated surfaces are current. | inventory, docs HTML, PRD HTML, roadmap HTML checks | Read docs. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before queue writeback, PRD creation or approval, bead creation or activation, active-memory edits, `tasks/todo.md` edits, implementation, external mutation, deployment, release, or package-manager behavior.
- Stop if source notes contain secrets or private raw material, if the candidate ID is unknown, if a proposal contains `B###`, if product-value rationale is missing, if likely authority is unclear, or if the next path would skip Local Source Intake, Product Discovery, PRD, decision, owner-file, or Decomposition Protocol gates.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `CANDIDATE-QUEUE.md` | Human-maintained queue entries and shaping fields. | Stores parked intent, product-value ratings, themes, and near-bead sketches as guidance only. | Clarity scenario and manual review. | `tasks/prds/PRD-021-candidate-queue-shaping-ranked-decomposition.md` |
| `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` | Queue rules and promotion boundaries. | Defines ratings, sketch IDs, preview/apply gates, and forbidden uses. | Clarity scenario. | `tasks/prds/PRD-021-candidate-queue-shaping-ranked-decomposition.md` |
| `scripts/candidate-queue.py` | Preview/import/shaping/apply command. | Deterministic validation and approval-gated writeback to `CANDIDATE-QUEUE.md` only. | `--self-test`. | `tasks/prds/PRD-021-candidate-queue-shaping-ranked-decomposition.md` |
| User docs and prompt patterns | Copyable user prompts. | Teach queue shaping without task authority. | Docs and clarity checks. | `tasks/prds/PRD-021-candidate-queue-shaping-ranked-decomposition.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-021-candidate-queue-shaping-ranked-decomposition.md`
- Owner protocol:
  - `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md`
- Secondary reference files:
  - `CANDIDATE-QUEUE.md`
  - `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`
  - `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/candidate-queue.py`
  - `scripts/clarity-scenario-check.py`
  - `docs-html/`
  - `tasks/prds-html/`
