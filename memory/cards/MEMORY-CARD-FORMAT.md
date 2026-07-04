# PrecodeOS -- Memory Cards
<!-- ANCHOR: memory-cards -->

> AUTHORITY: Reviewed memory card format and field guidance.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Creating, editing, reviewing, or exporting Precode memory cards.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-07-04

Each memory card captures one reusable piece of reviewed knowledge.

Cards should be short. If a card becomes a decision, requirement, architecture rule, security rule, or task instruction, promote it to the correct owner file instead of letting memory become authority.

## Required Fields

- `category`: `lesson`, `user_preference`, `project_glossary`, `recurring_risk`, `tool_agent_note`, `unresolved_theme`, or `source_pointer`
- `confidence`: `high`, `medium`, or `low`
- `freshness`: `current`, `watch`, `stale`, or `superseded`
- `status`: `reviewed`, `needs_promotion`, `superseded`, or `archived`
- `source_pointers`: files, beads, PRDs, diary entries, checks, or approved notes that support the memory
- `authority_owner_if_promoted`: owner file or protocol if this memory should become authority; required when `status` is `needs_promotion`
- `topics`: search terms that help `scripts/memory-check.py --query` find the card
- optional `memory_space`: retrieval grouping such as `default`, a project name, or a domain; not an authority boundary

## Project Glossary Guidance

Cards with `category: project_glossary` should include:

- domain terms with plain-English meanings
- aliases the builder, users, support, or teammates may say
- avoid or confusing terms, including stale or overloaded vocabulary
- source pointers for each useful term group
- examples in UI, code, tests, docs, support language, or user language
- freshness for terms that may drift
- authority owner if a term should be promoted

Use this table shape for `Project Glossary` when possible:

| Term | Plain-English meaning | Aliases | Avoid/confusing terms | Source pointers | Examples | Freshness | Authority owner if promoted |
|---|---|---|---|---|---|---|---|

Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` for the full shared-language workflow.

## Review Rule

Do not create a memory card automatically from generated diary output. Propose the card, get user approval, then write the reviewed card.

## Search And Promotion Rule

Memory cards may be searched and exported through generated indexes, but search results are evidence only. Stale, superseded, archived, and low-confidence cards must be treated as weak or historical context. A `needs_promotion` card names the owner file to review; it does not update that owner file or become authority by itself.

Before a memory item becomes project truth, run a manual promotion review. Name the memory claim, source pointers, current status, proposed owner, promotion action, approval required, and stop condition. The answer should say whether the item should stay reviewed memory, become a proposed memory card, be promoted to `DECISIONS.md`, a PRD, a protocol, an approved bead, or another owner file.

Promotion review must not create cards, edit owner files, approve PRDs, activate beads, choose tasks, accept implementation, or change active memory without explicit approval.

For `project_glossary` cards, search and recall may surface term excerpts and demotion warnings. The agent must still verify the term against current active memory, active bead, approved PRD, code, and owner files before using it to name UI, modules, routes, tests, or docs.

Prefer short cards with focused summaries. If a card grows large enough that loading it would waste context, use selective recall through `scripts/memory-check.py --query "<topic>" --recall`, split the card, or promote durable truth into the correct owner file.

Use `scripts/memory-check.py --retrieval-review` before considering any optional retrieval backend. The review may expose oversized cards, token pressure, stale or low-confidence cards, promotion-needed cards, memory spaces, and query misses, but it remains generated evidence only. It does not approve semantic search, shared storage, new dependencies, card creation, owner-file promotion, task selection, or active-memory expansion.
