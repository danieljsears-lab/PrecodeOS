# Precode OS — Logs
<!-- ANCHOR: logs -->

> AUTHORITY: Generated log directory description and evidence-file taxonomy.
> NOT_AUTHORITY: Active memory, task selection, product decisions, or implementation plans.
> LOAD_WHEN: Auditing generated evidence or OS health outputs.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.2
Last updated: 2026-04-27

Generated logs live here.

- `check-results.jsonl`
- `check-output/`
- `tool-runs.jsonl`
- `loop-runs.jsonl`
- `handoffs.jsonl`
- `bead-transitions.jsonl`
- `os-health.json`
- `agent-spend.jsonl`
- `learning-diary.jsonl`
- `learning-diary.md`
- `memory-index.json`
- `memory-index.md`
- `scheduled-audit.json`
- `scheduled-audit.md`
- `orchestration-map.json`
- `workflow-map.json`
- `long-horizon-map.json`
- `handoff-packet.json`
- `handoff-packet.md`
- `pattern-guidance.json`
- `file-inventory.json`
- `github-source-intake.jsonl`
- `github-source-intake.md`

## Extension Output Rules

Generated extension evidence belongs under `logs/` unless an existing Precode generated report already owns the surface.

Generated markdown must include an authority contract and `CLASS: generated`.

Generated JSON and JSONL files are evidence only. They must not be treated as active memory, task selection, product decisions, implementation plans, or bead state.

## Versioning

This `README.md` is a reference file and carries document version metadata.

Generated outputs under `logs/` are not manually versioned. They use generated timestamps, append-only evidence rows, and authority demotion instead.
