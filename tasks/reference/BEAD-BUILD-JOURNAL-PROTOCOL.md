# PrecodeOS -- Bead Build Journal Protocol
<!-- ANCHOR: bead-build-journal-protocol -->

> AUTHORITY: Bead build journal purpose, evidence sources, generated report shape, Daily Cockpit surfacing rule, and conservative uncertainty handling.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, PRD approval, bead activation, implementation acceptance, generated progress state, or Git history truth by itself.
> LOAD_WHEN: Creating, reviewing, or changing the generated bead build journal, bead-level build snapshot, code-change report, or related Daily Cockpit status surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-09

## Purpose

The bead build journal helps a builder understand what code or implementation-relevant work changed during a bead, what evidence supports the current build state, and what remains uncertain.

It is a generated narrative build journal with traceability support. It is not active memory, not review acceptance, and not permission to continue from generated output alone.

The journal should answer:

- What bead did this session affect?
- What implementation-relevant files appear to have changed for the bead?
- What generated evidence was produced?
- What checks or manual verification support the current state?
- What still needs review, proof, acceptance, or user approval?

## Source Inputs

Use durable Precode and Git evidence:

- active bead metadata and Closeout Evidence
- `tasks/todo.md` current-bead pointer
- `logs/check-results.jsonl`
- `logs/tool-runs.jsonl`
- `logs/loop-runs.jsonl`
- `logs/os-health.json`
- Git bead/session baseline metadata when available
- Git status or diff summaries when baseline metadata is incomplete

Do not use chat history as a journal source unless the user explicitly asks to preserve a short, sanitized note.

## Generated Outputs

Journal output belongs under `logs/` and must identify itself as generated.

Recommended files:

- `logs/bead-build-journal.jsonl` for append-only structured session-close entries
- `logs/bead-build-journal.md` for the human-readable builder view grouped by bead

The markdown file must include an authority contract with:

- `CLASS: generated`
- `NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead activation, implementation acceptance, or generated progress state.`

## Entry Shape

Each entry should be short, plain-English, and evidence-backed.

Capture:

- timestamp
- bead path, ID, title, and status
- build lane and active feature window when available
- Git branch and baseline/end metadata when available
- changed-path summary
- implementation changes, separated from generated evidence changes
- latest recorded checks and result
- manual verification state
- build-readiness state based on evidence, not confidence
- blockers, remaining uncertainty, and approval still needed
- unverified possible related changes only when hard delta evidence is incomplete

Do not provide percentage completion by default. Use evidence-based wording such as `ready for review`, `evidence incomplete`, `checks failing`, `blocked`, or `accepted in closeout`.

## Daily Cockpit Surfacing Rule

The Daily Cockpit is the primary daily reader surface for this journal.

When the bead build journal exists, Daily Cockpit report guidance should include it where a builder is trying to understand what changed or validate build status:

- Learn: read the bead build journal alongside the learning diary when the question is "what code changed?"
- Close: session close should update or point to the latest bead build journal entry after closeout evidence refresh.
- Runnable reports: list the generated journal command or file once implemented.
- Done/evidence prompts: ask the agent to summarize the latest journal entry without treating it as active memory.

Daily Cockpit should depend only on the generated evidence contract, not on journal content as authority. If the journal is missing, stale, or incomplete, repair source evidence and regenerate it instead of hand-editing generated output.

## Uncertainty Handling

If Git baseline evidence is missing or incomplete, generate the journal entry anyway but mark the delta as incomplete.

Use conservative language:

- state what evidence is known
- name exactly which anchor is missing
- avoid claiming exact bead attribution when it cannot be proven
- include possible related changes only under an explicitly unverified recovery-help section

Never let an inferred journal entry accept a bead, approve a transition, or override Closeout Evidence.

## Session Close Behavior

Session close may update the bead build journal after checks, closeout evidence, and health reports have been refreshed.

The journal update should:

- read existing evidence
- append one structured entry per close event when appropriate
- regenerate the human-readable Markdown view
- avoid changing active memory
- avoid changing bead state
- avoid proposing or activating the next task

## Relationship To Other Reports

`logs/learning-diary.md` teaches what happened and what the builder should learn. The bead build journal explains what changed in the build and how that change is evidenced.

`OS-HEALTH.md` and `PROGRESS.md` may summarize the latest journal state or point to it, but should not duplicate the full journal.

The Daily Cockpit should point builders to the bead build journal when they need a plain-English build-status snapshot for the current bead.
