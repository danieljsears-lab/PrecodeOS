# Precode OS -- Learning Diary Protocol
<!-- ANCHOR: learning-diary-protocol -->

> AUTHORITY: Learning-diary capture rules, privacy boundaries, generated diary shape, and lesson-promotion path for Precode OS.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, or generated progress state.
> LOAD_WHEN: Creating, reviewing, or changing learner-facing session diary behavior.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-04-27

## Purpose

The learning diary helps a solo builder understand what happened during a Precode session without forcing them to read logs, command output, or chat history.

It is a teaching layer and memory-candidate source. It is not reviewed filesystem memory or project authority.

The diary should answer:

- What task or bead did we work on?
- What changed or was checked?
- What did the session teach the user about the project or the OS?
- What remains unclear?
- What should the user ask or inspect next time?

## Source Inputs

Use durable Precode evidence only:

- active bead metadata
- active bead Closeout Evidence
- `logs/check-results.jsonl`
- `logs/loop-runs.jsonl`
- `logs/os-health.json`
- generated sidecars from `scripts/os-health.py`

Do not use chat history as a diary source unless the user has explicitly asked to preserve a short, sanitized note.

## Generated Outputs

Diary output belongs under `logs/` and must identify itself as generated.

Recommended files:

- `logs/learning-diary.jsonl` for structured session entries
- `logs/learning-diary.md` for the human-readable learner view

The markdown file must include an authority contract with:

- `CLASS: generated`
- `NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, or generated progress state.`

## Entry Shape

Each session entry should be short and plain-English.

Capture:

- timestamp
- current bead
- bead status
- primary authority
- checks run and latest result
- known token and cost spend for the current bead
- cumulative known token and cost spend across all beads
- per-agent spend rollup
- unknown or incomplete spend telemetry counts
- manual verification state
- drift observed
- lesson to promote
- follow-up bead signal
- one learner takeaway
- one next question

If evidence is missing, say it is missing. Do not invent a lesson.

## Exclusions

Never store:

- raw chat transcripts
- secrets, API tokens, credentials, or dashboard values
- speculative implementation plans
- private user notes that were not explicitly approved for capture
- full command output
- instructions for the next active task
- product decisions that have not been promoted to `DECISIONS.md`

## Promotion Path

The diary may surface learning candidates, but it does not own them.

Promote durable facts to the owning file:

- product or technical decisions -> `DECISIONS.md`
- product requirements -> `tasks/prds/*.md` and compiled `FEATURES.md`
- acceptance criteria -> `ACCEPTANCE.md`
- architecture or route facts -> `ARCHITECTURE.md`
- data model facts -> `DATA-MODELS.md`
- API facts -> `API.md`
- security facts -> `SECURITY.md`
- repeated OS/process lessons -> the relevant reference protocol or agent rule

If a lesson is not promoted, it remains a diary note only.

When a lesson should remain reusable evidence without becoming authority, propose a reviewed memory card under `memory/cards/` using `tasks/reference/MEMORY-PROTOCOL.md`. Do not auto-create memory cards from diary output.

## Session Close Behavior

Session close may update the learning diary after checks and closeout evidence have been refreshed.

The diary update should:

- read existing evidence
- import or summarize spend telemetry when available
- append or regenerate generated diary output
- avoid changing active memory
- avoid changing bead state
- avoid proposing or activating the next task

## Spend Accounting Rule

Token and cost accounting is generated evidence.

Prefer automatic import through `python3 scripts/import-agent-spend.py` when an agent exposes reliable telemetry. Use `bash scripts/log-agent-spend.sh` as a fallback when a tool only exposes advisory or manual usage totals.

The diary must label incomplete telemetry as unknown. Missing spend is not zero spend.

## User Reading Rule

The user may read the diary to learn what happened, but should not ask an agent to continue work from the diary alone.

To continue work, start from:

1. `AGENT.md`
2. `DECISIONS.md`
3. `tasks/todo.md`
4. the active bead
5. the bead's primary authority file
