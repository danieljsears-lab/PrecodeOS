# PrecodeOS -- Ubiquitous Language Protocol
<!-- ANCHOR: ubiquitous-language-protocol -->

> AUTHORITY: Shared domain-language workflow, project-glossary card expectations, terminology freshness rules, and PRD/bead language guidance for PrecodeOS.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, implementation plans, route structure, schema definitions, generated progress state, or code naming decisions without owner-file approval.
> LOAD_WHEN: A feature, PRD, bead, review, source intake, or memory card depends on domain vocabulary, confusing terms, user language, module/interface names, or stale terminology.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-05-11

## Purpose

Precode uses shared language to keep a non-technical builder, an AI agent, the product docs, the UI, the tests, and the code from silently talking past each other.

Use this protocol when terms matter. The goal is not a dictionary for its own sake. The goal is to make the builder's intent legible enough that an agent can plan, name, test, and review work without inventing vocabulary.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Glossary material is reviewed evidence unless promoted into the correct owner file.

## When To Use

Load this protocol when:

- alignment/grilling reveals confusing words, aliases, or overloaded terms
- a PRD introduces domain concepts a first-time builder keeps explaining in plain language
- a feature is domain-heavy, such as bookings, payments, learning, healthcare, legal workflows, logistics, or creator tools
- UI labels, code symbols, test names, or module/interface names need to match user language
- a reviewer sees terms drift between the PRD, bead, UI, tests, and code
- old PRDs, closed issues, imported notes, or generated summaries use stale vocabulary
- a memory card category is `project_glossary`

Do not use this as ceremony for a tiny copy edit unless the wording reveals a real product or code meaning.

## Source Inputs

Shared language may come from:

- the builder's exact phrases
- domain expert notes or meeting summaries
- PRD alignment/grilling output
- product docs and source-intake summaries
- UI labels, onboarding copy, and support language
- code symbols, route names, database concepts, tests, and fixtures
- GitHub issues or local issue imports
- reviewed memory cards

Sources are evidence. If a term becomes a durable product, technical, security, or acceptance decision, promote it to the owner file named by the relevant protocol.

## Term Record Shape

When recording terms in a PRD, glossary card, or review note, prefer this shape:

| Field | Meaning |
|---|---|
| Term | The word or phrase to use. |
| Plain-English meaning | What the builder means by it. |
| Aliases | Other words people may use for the same concept. |
| Avoid or confusing terms | Similar words that should not be used, or overloaded words that need care. |
| Domain owner | User, team, product area, source, or owner file that can clarify the term. |
| Source pointers | PRD, bead, note, issue, code file, UI screen, or memory card supporting the meaning. |
| Freshness | `current`, `watch`, `stale`, or `superseded`. |
| Examples | UI label, code symbol, test name, fixture, or sentence that shows correct use. |
| Authority owner if promoted | Where the term belongs if it becomes durable truth. |

Keep the meaning short enough that a non-technical builder can correct it.

## PRD Usage

PRDs should include a `Domain Language` section when terms affect requirements, UI, architecture, tests, or module boundaries.

The PRD should name:

- terms introduced by the feature
- existing terms reused from product docs, code, or memory
- rejected or confusing terms to avoid
- module/interface names that should match domain language
- glossary-card candidates that need human review later

The PRD remains the destination document. Domain language in the PRD helps define the destination, but it does not activate work.

## Bead Usage

Beads may reference domain terms when language affects execution.

For code-changing beads, the agent should use shared terms in:

- UI labels and visible text
- test names and fixture names
- module/interface names where the project convention allows it
- manual verification language
- closeout evidence

If a bead discovers vocabulary drift, stop or checkpoint before renaming broadly. Create a follow-up bead, PRD amendment, memory-card proposal, or owner-file update as appropriate.

## Project Glossary Cards

Use `memory/cards/` category `project_glossary` for reviewed but non-authoritative shared language.

A project-glossary card should include:

- domain terms
- aliases
- avoid/confusing terms
- examples in UI, code, tests, or docs
- source pointers
- freshness
- authority owner if promoted

Glossary cards can orient future agents. They must not override active memory, current code, the active bead, an approved current PRD, or owner files.

## Stale Vocabulary

Vocabulary can rot just like requirements.

Treat completed PRDs, archived beads, closed issues, imported notes, old transcripts, generated summaries, and stale memory cards as historical evidence. If they conflict with current code, active memory, the active bead, an approved current PRD, or owner files, current authority wins.

Record stale vocabulary as one of:

- stale input in a PRD
- rejected term in `Domain Language`
- glossary card marked `stale` or `superseded`
- owner-file update if durable truth changed
- follow-up bead if renaming or migration work is needed

## Review Checklist

When reviewing shared language, answer:

- What terms did the user introduce?
- What did each term mean in plain English?
- Which aliases should the agent understand?
- Which words should be avoided because they confuse product, UI, code, or tests?
- Which source proves the current meaning?
- Which module/interface names should use the same domain language?
- Is any term stale, superseded, or only historical evidence?
- Does any term need promotion to `PRODUCT.md`, `DECISIONS.md`, a PRD, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, or another owner file?

## Output Shape

Use this compact output when a user asks for a shared-language pass:

- Terms introduced:
- Terms reused:
- Aliases to recognize:
- Terms to avoid:
- Source pointers:
- UI/code/test examples:
- Stale or superseded vocabulary:
- Promotion needed:
