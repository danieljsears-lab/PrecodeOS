# PrecodeOS -- Reviewed Memory
<!-- ANCHOR: reviewed-memory -->

> AUTHORITY: Reviewed memory directory guidance and filesystem memory card orientation.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Reviewing or creating filesystem memory cards for PrecodeOS.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.5
Last updated: 2026-07-11

This directory stores reviewed Precode memory as plain files.

Memory is evidence, not authority. It helps users and agents remember useful lessons, preferences, project-glossary terms, recurring risks, and source pointers across sessions without adding another active-memory file.

Use `tasks/reference/UBIQUITOUS-LANGUAGE-PROTOCOL.md` when a memory card captures shared domain vocabulary, aliases, avoid terms, UI/code/test examples, or stale terminology.

Before acting on memory, return to:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`
- the active bead
- the bead's primary authority file

## Files

- `cards/` -- reviewed memory cards
- `cards/MEMORY-CARD-template.md` -- starter template for new memory cards

Generated memory indexes live in `logs/` and can be refreshed with:

```bash
python3 scripts/update-memory-index.py
```

Search reviewed memory without mutating state:

```bash
python3 scripts/memory-check.py --query "topic words"
```

Optional filters include `--category`, `--freshness`, `--status`, and `--needs-promotion`.

Use selective recall when whole-card loading would waste context:

```bash
python3 scripts/memory-check.py --query "topic words" --recall
```

Selective recall returns snippets only when every query term matches the reviewed card search text. If there is no exact match, weak-match examples are leads only; do not load them as memory or treat them as recall.

Use retrieval-readiness review before discussing any optional semantic or shared memory backend:

```bash
python3 scripts/memory-check.py --retrieval-review --query "topic words"
```

Search results and generated indexes are evidence only. Cite the card path, title, category, freshness, status, source pointers, and promotion owner before using a result. Demote stale, superseded, archived, or low-confidence cards, then return to active memory, the active bead, and the owner file before recommending action.

Retrieval-readiness review may recommend staying filesystem-first, splitting/promoting cards first, or running Extension Review. `extension_review_required` means repeated no-match or weak-match evidence after card cleanup may justify a separate review; it does not approve semantic search, a shared backend, card creation, owner-file promotion, task selection, or active-memory changes.

Use `tasks/reference/MEMORY-PROTOCOL.md` for the full rules.
