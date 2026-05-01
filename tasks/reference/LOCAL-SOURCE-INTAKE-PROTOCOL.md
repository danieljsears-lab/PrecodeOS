# Precode OS -- Local Source Intake Protocol
<!-- ANCHOR: local-source-intake-protocol -->

> AUTHORITY: Local source intake rules, source summary format, evidence boundaries, privacy exclusions, and promotion paths for turning local project material into Precode-owned planning artifacts.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, active task selection, route structure, schema definitions, implementation plans, or generated progress state.
> LOAD_WHEN: Turning local notes, docs, screenshots, chat summaries, issue exports, research files, diagrams, or manual drafts into PRD-ready source summaries.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

Local Source Intake helps a solo builder turn messy project material into trusted Precode artifacts without treating the raw material as authority.

The intake output is not the plan. It is a short, inspectable evidence summary that can feed:

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

Supported source types include:

- notes and markdown docs
- text files and manual drafts
- screenshots, wireframes, and design images
- chat transcript summaries
- GitHub, Linear, or issue-tracker exports
- research notes and PDFs summarized by the user or agent
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

Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when deciding whether source material should become intake evidence, PRD shaping, a challenge-planning bead, or a narrow execution bead.

Examples:

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
- Authority files likely affected:
- Recommended next step:
```

Keep the summary short. If the material is large, summarize the decision-relevant parts and link or name the local source path instead of copying it wholesale.

## Intake Workflow

1. Identify the source type and why it matters.
2. Remove secrets, credentials, and irrelevant private detail.
3. Extract stable facts, assumptions, conflicts, and open questions.
4. Name candidate requirements and non-goals only as candidates.
5. Identify affected authority files.
6. Decide whether the next step is PRFAQ-lite, PRD drafting, decision logging, architecture/security/schema/API update, or no action.

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
| Product problem, users, goals, non-goals, requirements | `tasks/prds/*.md` |
| Compiled feature or functional requirement | `FEATURES.md` |
| Hard decision or unresolved implementation-changing question | `DECISIONS.md` |
| Route, flow, module, or boundary fact | `ARCHITECTURE.md` |
| API contract or server boundary fact | `API.md` |
| Data field, relationship, or semantic fact | `DATA-MODELS.md` |
| Security, privacy, secret, or threat-model fact | `SECURITY.md` |
| Done check or acceptance criterion | `ACCEPTANCE.md` |
| Executable unit of work | `tasks/beads/*.md` after PRD readiness |

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
Turn this local source summary into a PRD shard draft.
Keep source inputs as evidence, not authority.
List the questions that could change implementation.
```

```text
Review these screenshots and notes as local source inputs.
Do not create beads yet.
Tell me whether the Product Definition Gate is ready or what is missing.
```
