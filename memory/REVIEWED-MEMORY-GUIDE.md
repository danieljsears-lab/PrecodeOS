# Precode OS -- Reviewed Memory
<!-- ANCHOR: reviewed-memory -->

> AUTHORITY: Reviewed memory directory guidance and filesystem memory card orientation.
> NOT_AUTHORITY: Active memory, task selection, product decisions, feature requirements, implementation plans, route structure, schema definitions, bead state, or generated progress state.
> LOAD_WHEN: Reviewing or creating filesystem memory cards for Precode OS.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-05-07

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

Use `tasks/reference/MEMORY-PROTOCOL.md` for the full rules.
