# PrecodeOS -- Local Source Intake Protocol
<!-- ANCHOR: local-source-intake-protocol -->

> AUTHORITY: Local source intake rules, source summary format, evidence boundaries, privacy exclusions, and promotion paths for turning local project material into Precode-owned planning artifacts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, active task selection, route structure, schema definitions, implementation plans, or generated progress state.
> LOAD_WHEN: Turning local notes, docs, screenshots, chat summaries, issue exports, research files, diagrams, manual drafts, client handoff artifacts, or existing codebases into PRD-ready source summaries.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-05-30

## Purpose

Local Source Intake helps a solo builder turn messy project material into trusted Precode artifacts without treating the raw material as authority.

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
- text files and manual drafts
- screenshots, wireframes, design images, frontend design files, Figma exports, and design-system notes
- chat transcript summaries
- GitHub, Linear, or issue-tracker exports
- research notes and PDFs summarized by the user or agent
- Product Ideation Workbook Precode Ingestion Packets, including Candidate Goal Frames
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

If raw source material conflicts with `PRODUCT.md`, `DECISIONS.md`, an approved PRD, the active bead, or another owner file, current owner files win until the user reviews and approves an amendment.

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when deciding whether source material should become intake evidence, PRD shaping, a challenge-planning bead, or a narrow execution bead.

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
- Candidate requirements:
- Candidate non-goals:
- Candidate acceptance signals:
- Candidate Goal Frame:
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

Use the existing-codebase and external-plan fields only when the source includes a repository, codebase snapshot, backend plan, sprint plan, or implementation task list. Inspect those sources read-only during intake and treat conflicts with current code, active memory, approved current PRDs, or owner files as open questions or amendment candidates.

## Intake Workflow

1. Identify the source type and why it matters.
2. Remove secrets, credentials, and irrelevant private detail.
3. Extract stable facts, assumptions, conflicts, and open questions.
4. Name candidate requirements and non-goals only as candidates.
5. If a Candidate Goal Frame is present, summarize whether it is stable, conflicting, incomplete, stale, or too task-like.
6. If design files are present, summarize visual intent, screens, states, flows, interaction notes, responsive expectations, design-system constraints, accessibility concerns, and unresolved design decisions.
7. Identify affected authority files.
8. If an existing codebase or external plan is present, summarize repo topology, app directories, existing checks, implementation constraints, sprint-plan inputs, conflicts, and stale assumptions.
9. Decide whether the next step is Goal Frame reaffirmation, PRFAQ-lite, PRD drafting, PRD amendment, design or architecture impact review, client engagement intake, decision logging, architecture/security/schema/API update, decomposition into candidate beads, a narrow unblocker, or no action.

Stop before PRD drafting if the source material lacks:

- a user problem
- a before/after user moment
- non-goals for broad work
- enough evidence to write observable requirements
- an owner file for architecture, API, schema, security, or acceptance changes

## Promotion Path

Promote stable conclusions only after user review.

| Intake finding | Destination |
|---|---|
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
Summarize the target user, minimum value moment, core workflow spine, screens and states, reference artifacts, feedback gathered, open questions, candidate acceptance checks, affected owner files, and the next safe Precode action.
If this is ready for implementation, propose one narrow core-spine bead and stop before activation or coding.
```
