# PrecodeOS -- Local Source Intake Protocol
<!-- ANCHOR: local-source-intake-protocol -->

> AUTHORITY: Local source intake rules, source summary format, evidence boundaries, privacy exclusions, and promotion paths for turning local project material into Precode-owned planning artifacts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, active task selection, route structure, schema definitions, implementation plans, or generated progress state.
> LOAD_WHEN: Turning local notes, docs, screenshots, chat summaries, issue exports, research files, diagrams, manual drafts, client handoff artifacts, or existing codebases into PRD-ready source summaries.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.19
Last updated: 2026-07-22

## Purpose

Local Source Intake helps a solo builder turn messy project material into trusted Precode artifacts without treating the raw material as authority.

In the first-product spine, intake sits after the reviewed packet and before PRD shaping: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`. A Conviction Packet / Precode Ingestion Packet can feed intake. A reviewed Conviction Packet / Precode Ingestion Packet can feed intake after a compact readiness self-check, but intake output still requires user review before PRD shaping, owner-file promotion, decomposition, bead activation, or coding. The self-check is advisory only. It does not approve a PRD, owner-file edit, roadmap, backlog, bead, or coding.

The intake output is not the plan. It is a short, inspectable evidence summary that can feed:

- `PRODUCT.md`
- `tasks/prds/*.md`
- `FEATURES.md`
- `DECISIONS.md`
- `ARCHITECTURE.md`
- `API.md`
- `DATA-MODELS.md`
- `SECURITY.md`
- `ACCEPTANCE.md`
- `tasks/beads/*.md`

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Supported Local Sources

When a project keeps raw source material in the repo, the default location is root-level `project-evidence/`. That folder is project-owned evidence storage, not a Precode authority folder. Agents may inspect explicitly named `project-evidence/` files read-only during intake, but must not auto-treat the folder as active memory, implementation instructions, task approval, or permission to code.

Supported source types include:

- notes and markdown docs
- Candidate Queue entries from `CANDIDATE-QUEUE.md`, including reviewed shaping fields, product-value ratings, themes, and near-bead sketches
- text files and manual drafts
- screenshots, wireframes, design images, frontend design files, Figma exports, and design-system notes
- chat transcript summaries
- public GitHub feedback issues, package-bug issues, pull requests, Linear items, or issue-tracker exports
- research notes and PDFs summarized by the user or agent
- Reviewed Product Ideation Workbook Conviction Packets / Precode Ingestion Packets, including guided Precode Idea Coach outputs, builder lens notes, Challenge And Clarity findings, evidence-strength review, optional visible-iteration/MVE framing, Local Source Intake readiness self-check, and Candidate Goal Frames
- user-provided implementation packets that bundle an ingestion packet, design files, and PRD-like notes
- existing PRDs or product specs that need Precode review, amendment, or adaptation
- existing codebases, repository snapshots, route trees, package manifests, tests, CI configs, and README conventions inspected read-only
- client backend handover plans, Ember Handover Agent artifacts such as `Backend-dev-plan.md`, sprint plans, and implementation task lists
- customer quotes or feedback snippets
- existing feature, architecture, API, schema, security, or acceptance docs
- hand-written task lists or migration notes

Unsupported as durable source facts:

- secrets, tokens, credentials, or dashboard values
- raw private chat transcripts unless the user explicitly approves a short summary
- guesses about user intent that the user has not confirmed
- stale notes that conflict with active decisions
- generated summaries that have not been reviewed

## Evidence Rule

Source inputs are evidence, not authority.

Do not let local notes, screenshots, exports, or generated summaries drive active task selection directly. Promote only stable conclusions into the owning Precode file.

When source material may move toward an owner file, PRD, decision, Candidate Queue entry, reviewed memory card, protocol update, or bead proposal, run a Source-To-Promotion Hygiene Review before promotion. The review must name source refs, evidence strength, open conflicts, proposed owner, promotion action, approval required, and stop condition. This is a read-only review shape. It does not approve PRDs, promote owner-file facts, create beads, choose tasks, update `tasks/todo.md`, accept implementation, or make generated summaries authoritative.

When the source is a useful answer from chat, planning, review, discovery, source intake, memory recall, or maintainer analysis and its durable destination is unclear, run Question-To-Artifact Filing before promotion. It may recommend stay in chat, Local Source Intake, Candidate Queue update, Memory Promotion Review, PRD work, `DECISIONS.md`, owner-file update, decomposition review, defer, kill, or maintainer roadmap note. It does not file automatically, approve promotion, choose tasks, activate beads, update active memory, or make generated summaries authoritative.

Public GitHub feedback issues, package-bug issues, comments, labels, pull requests, reviews, checks, and project-board status are source evidence. They may inform intake, bug triage, PRD amendment, protocol updates, package docs, decisions, or candidate beads only after review. They must not choose roadmap direction, approve PRDs, activate beads, accept implementation, approve merge, approve package release, authorize GitHub mutation, or replace maintainer review.

If raw source material conflicts with `PRODUCT.md`, `DECISIONS.md`, an approved PRD, the active bead, or another owner file, current owner files win until the user reviews and approves an amendment.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when deciding whether source material should become intake evidence, PRD shaping, a challenge-planning bead, or a narrow execution bead.

Use `tasks/reference/EXISTING-REPO-INTAKE-PROTOCOL.md` before Local Source Intake when the source material is an app repository that already has code, docs, CI, product history, or active work and PrecodeOS has not yet been safely adapted into it.

Use `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` when source material comes from a client engagement, existing repo, external PRD, Ember/backend handoff, sprint plan, or repo-topology decision.

Examples:

- A product constitution fact belongs in `PRODUCT.md`.
- A product requirement belongs in a PRD shard and compiled `FEATURES.md`.
- A hard product or technical decision belongs in `DECISIONS.md`.
- A route or module-placement fact belongs in `ARCHITECTURE.md`.
- A field or relationship fact belongs in `DATA-MODELS.md`.
- An API contract belongs in `API.md`.
- A sensitive-surface or threat-model fact belongs in `SECURITY.md`.
- A completion criterion belongs in `ACCEPTANCE.md`.
- Work to execute belongs in a bead only after definition is ready.

## Intake Summary Format

Use this format inside a PRD shard `Source Inputs` section or a short planning note that is later distilled into a PRD.

```text
Source summary:
- Source type:
- Source reference:
- Date or recency:
- User-provided context:
- Stable facts:
- Assumptions:
- Conflicts or stale inputs:
- Privacy or secrets redactions:
- Open questions that could change implementation:
- Source refs:
- Open conflicts:
- Proposed owner:
- Promotion action:
- Approval required:
- Stop condition:
- Candidate requirements:
- Candidate non-goals:
- Candidate acceptance signals:
- Primary hypothesis / learning target:
- Hypothesis review status: `untested | tested | narrowed | killed | promoted | stale | not applicable`
- Learning outcome:
- Stale or untested signals:
- Evidence strength:
- Weakest assumption:
- What would change our mind:
- Smallest non-code learning step:
- Local Source Intake readiness self-check:
- Candidate Goal Frame:
- Candidate Queue ID:
- Candidate Queue status:
- Design inputs:
- Visual intent:
- Screens, states, and user flows:
- Interaction notes:
- Responsive expectations:
- Design-system constraints:
- Accessibility concerns:
- Unresolved design decisions:
- Existing codebase facts:
- Repo topology:
- External plan or sprint inputs:
- Authority files likely affected:
- Recommended next step:
```

Keep the summary short. If the material is large, summarize the decision-relevant parts and link or name the local source path instead of copying it wholesale.

Use the design fields only when the source includes design files, screenshots, wireframes, Figma exports, or UI references. If a design detail would change implementation, treat it as an open question until the user or owning PRD confirms it.

When source material includes a completed frontend and the user asks for backend-only work, summarize the frontend as existing evidence and an integration boundary. Capture routes, UI states, data needs, API expectations, auth/session assumptions, design-system constraints, and verification touchpoints, then mark frontend implementation as preserved unless a frontend touch is needed to connect, adapt, or verify backend behavior or the user explicitly approves a frontend scope change.

Use the existing-codebase and external-plan fields only when the source includes a repository, codebase snapshot, backend plan, sprint plan, or implementation task list. Inspect those sources read-only during intake and treat conflicts with current code, active memory, approved current PRDs, or owner files as open questions or amendment candidates.

Use `tasks/reference/HYPOTHESIS-REVIEW-PROTOCOL.md` when the intake question is specifically whether a hypothesis or learning target was tested, narrowed, killed, promoted, stale, or still untested. Hypothesis review status is evidence only; it does not approve product direction, approve PRDs, rank Candidate Queue entries, activate beads, choose tasks, require analytics, create a database, or promote findings automatically.

## Intake Workflow

1. Identify the source type and why it matters.
2. Remove secrets, credentials, and irrelevant private detail.
3. Extract stable facts, assumptions, conflicts, and open questions.
4. Name candidate requirements and non-goals only as candidates.
5. If a Candidate Goal Frame is present, summarize whether it is stable, conflicting, incomplete, stale, or too task-like.
6. If design files or completed frontend evidence are present, summarize visual intent, screens, states, flows, interaction notes, responsive expectations, design-system constraints, accessibility concerns, unresolved design decisions, and any backend integration touchpoints.
7. Identify affected authority files.
8. If an existing codebase or external plan is present, summarize repo topology, app directories, existing checks, implementation constraints, sprint-plan inputs, conflicts, and stale assumptions.
9. Name the primary hypothesis or learning target when source material includes a hunch, unproven assumption, discovery summary, Candidate Queue entry, or experiment claim.
10. When the source includes learning evidence, classify the hypothesis review status as `untested`, `tested`, `narrowed`, `killed`, `promoted`, `stale`, or `not applicable`, and summarize the learning outcome without treating it as authority.
11. Decide whether the next step is stay in chat, Question-To-Artifact Filing, Candidate Queue update, Memory Promotion Review, Goal Frame reaffirmation, Product Discovery Validation, PRFAQ-lite, PRD drafting, PRD amendment, design or architecture impact review, client engagement intake, decision logging, architecture/security/schema/API update, decomposition into candidate beads, a narrow unblocker, defer, kill, or no action.
12. Treat `scripts/candidate-queue.py --preview-import <path>` output as minimal queue capture only. It may park a title, source pointer, short summary, open questions, and privacy warning, but it does not replace Local Source Intake, approve promotion, or authorize coding.

Stop before PRD drafting if the source material lacks:

- a user problem
- a before/after user moment
- non-goals for broad work
- enough evidence to write observable requirements
- a testable hypothesis when worth-building uncertainty is material
- an owner file for architecture, API, schema, security, or acceptance changes

## Promotion Path

Promote stable conclusions only after user review.

| Intake finding | Destination |
|---|---|
| Useful chat, planning, review, discovery, memory, or maintainer answer whose destination is unclear | Question-To-Artifact Filing recommendation before any write |
| Parked intent that is not ready for source intake, PRD shaping, or decomposition | `CANDIDATE-QUEUE.md` |
| Product promise, users and jobs, strategy, non-goals, current bets, success signals, design or voice pointers | `PRODUCT.md` |
| Reviewed and reaffirmed product-level Goal Frame candidate | `PRODUCT.md` `## Goal Frame` section |
| Product problem, users, goals, non-goals, requirements | `tasks/prds/*.md` |
| Compiled feature or functional requirement | `FEATURES.md` |
| Hard decision or unresolved implementation-changing question | `DECISIONS.md` |
| Route, flow, module, or boundary fact | `ARCHITECTURE.md` |
| API contract or server boundary fact | `API.md` |
| Data field, relationship, or semantic fact | `DATA-MODELS.md` |
| Security, privacy, secret, or threat-model fact | `SECURITY.md` |
| Done check or acceptance criterion | `ACCEPTANCE.md` |
| Executable unit of work | `tasks/beads/*.md` after PRD readiness |

A workbook Candidate Goal Frame must not skip review. Promote it only after the intake summary and user reaffirmation, and keep it out of `tasks/todo.md`.

## Review Inputs

Screenshots, browser notes, AI critiques, design reviews, security notes, accessibility notes, and human QA notes are review inputs.

They become evidence only when:

- a command is run through `bash scripts/record-check.sh -- <command>`
- manual verification records what was checked and the outcome
- unresolved findings become follow-up beads, decisions, or authority-file updates

## User Prompts

```text
Use the Local Source Intake Protocol on these notes.
Do not write code.
Summarize stable facts, assumptions, conflicts, open questions, candidate requirements, and likely authority files.
```

```text
Use Local Source Intake on this Candidate Queue entry.
Treat it as parked intent and source evidence, not authority.
Tell me whether it should stay queued, move to Product Discovery, become a PRD draft or amendment, become a decision, update an authority file, route to decomposition review, defer, or be killed.
Treat product-value rating as product value only and near-bead sketches as sketches only.
Do not activate a bead or start coding.
```

```text
Use Local Source Intake on this Candidate Goal Frame. Tell me whether it is stable, conflicting, incomplete, stale, or too task-like. Do not update PRODUCT.md until I reaffirm it.
```

```text
Turn this local source summary into a PRD shard draft.
Keep source inputs as evidence, not authority.
List the questions that could change implementation.
```

```text
Review these screenshots and notes as local source inputs.
Do not create beads yet.
Tell me whether the Product Definition Gate is ready or what is missing.
```

```text
Use Local Source Intake on this user packet, frontend design, and optional existing PRD.
Treat every input as evidence, not authority.
Classify stable facts, conflicts, stale inputs, open questions, design implications, candidate requirements, candidate non-goals, candidate acceptance signals, affected owner files, and the next safe Precode action.
Do not update authority files, approve or amend a PRD, create or activate beads, or write code until I review the intake summary.
```

```text
Use Local Source Intake on this approved bootcamp PRD input and Student Experience Ingestion Packet.
Treat the packet as context for bead creation, not permission to code.
Summarize the target user, minimum value moment, core workflow spine, Core Spine Gate status, screens and states, reference artifacts, feedback gathered, feedback still needed, open questions, candidate acceptance checks, affected owner files, and the next safe Precode action.
If this is ready for implementation, propose one narrow core-spine bead and stop before activation or coding.
```
