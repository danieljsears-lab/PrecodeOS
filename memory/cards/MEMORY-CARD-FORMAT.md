# PrecodeOS -- Memory Cards
<!-- ANCHOR: memory-cards -->

> AUTHORITY: Reviewed memory card format and field guidance.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Creating, editing, reviewing, or exporting Precode memory cards.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-07

Each memory card captures one reusable piece of reviewed knowledge.

Cards should be short. If a card becomes a decision, requirement, architecture rule, security rule, or task instruction, promote it to the correct owner file instead of letting memory become authority.

## Required Fields

- `category`: `lesson`, `user_preference`, `project_glossary`, `recurring_risk`, `tool_agent_note`, `unresolved_theme`, or `source_pointer`
- `confidence`: `high`, `medium`, or `low`
- `freshness`: `current`, `watch`, `stale`, or `superseded`
- `status`: `reviewed`, `needs_promotion`, `superseded`, or `archived`
- `source_pointers`: files, beads, PRDs, diary entries, checks, or approved notes that support the memory

## Project Glossary Guidance

Cards with `category: project_glossary` should include:

- domain terms with plain-English meanings
- aliases the builder or users may say
- avoid or confusing terms
- examples in UI, code, tests, docs, or user language
- authority owner if a term should be promoted

Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` for the full shared-language workflow.

## Review Rule

Do not create a memory card automatically from generated diary output. Propose the card, get user approval, then write the reviewed card.
