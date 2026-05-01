# Precode OS -- Memory Cards
<!-- ANCHOR: memory-cards -->

> AUTHORITY: Reviewed memory card format and field guidance.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Creating, editing, reviewing, or exporting Precode memory cards.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-27

Each memory card captures one reusable piece of reviewed knowledge.

Cards should be short. If a card becomes a decision, requirement, architecture rule, security rule, or task instruction, promote it to the correct owner file instead of letting memory become authority.

## Required Fields

- `category`: `lesson`, `user_preference`, `project_glossary`, `recurring_risk`, `tool_agent_note`, `unresolved_theme`, or `source_pointer`
- `confidence`: `high`, `medium`, or `low`
- `freshness`: `current`, `watch`, `stale`, or `superseded`
- `status`: `reviewed`, `needs_promotion`, `superseded`, or `archived`
- `source_pointers`: files, beads, PRDs, diary entries, checks, or approved notes that support the memory

## Review Rule

Do not create a memory card automatically from generated diary output. Propose the card, get user approval, then write the reviewed card.
