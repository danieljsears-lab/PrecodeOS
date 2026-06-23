# Memory Card Template
<!-- ANCHOR: memory-card-template -->

> AUTHORITY: Template for reviewed Precode filesystem memory cards.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Creating a new reviewed memory card.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-06-23

---
memory_id: MEMORY-000
category: lesson
confidence: medium
freshness: current
status: reviewed
memory_space: default
related_bead: none
related_prd: none
authority_owner_if_promoted: none
source_pointers:
  - none
topics:
  - none
---

## Summary

- Replace this with one reusable memory in plain English.

## Why It Matters

- Explain how this helps future users or agents avoid repeating work, confusion, or drift.

## Source Notes

- Cite the bead, PRD, diary entry, check, intake summary, or approved user note that supports this memory.

## Project Glossary

Use this section only when `category: project_glossary`; otherwise write `Not applicable`.

| Term | Plain-English meaning | Aliases | Avoid/confusing terms | Source pointers | Examples | Freshness | Authority owner if promoted |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | current | none |

## Promotion Review

- If this becomes a decision, requirement, architecture rule, security rule, acceptance rule, or task instruction, move it to the correct owner file after human review.
- If `status` is `needs_promotion`, replace `authority_owner_if_promoted: none` with the proposed owner file or protocol. Search results may warn about promotion need, but they must not perform the promotion.
- For `project_glossary`, use reviewed terms to orient future agents only. Do not override current code, active beads, approved PRDs, active memory, or owner files.
- Keep `memory_space` as a retrieval label only. It does not create authority, task selection, access control, or optional-pack behavior.
- If this card becomes stale, superseded, archived, or low-confidence, keep that state visible so memory search treats it as weak or historical context.
