# PrecodeOS — Logs
<!-- ANCHOR: logs -->

> AUTHORITY: Generated log directory description and evidence-file taxonomy.
> NOT_AUTHORITY: Active memory, task selection, product decisions, or implementation plans.
> LOAD_WHEN: Auditing generated evidence or OS health outputs.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.15
Last updated: 2026-07-26

Generated logs live here.

- `check-results.jsonl`
- `check-output/`
- `tool-runs.jsonl`
- `loop-runs.jsonl`
- `handoffs.jsonl`
- `bead-transitions.jsonl`
- `os-health.json`
- `agent-spend.jsonl`
- `bead-build-journal.jsonl`
- `bead-build-journal.md`
- `build-attribution-ledger.json`
- `build-attribution-ledger.md`
- `ralph-attempts.jsonl`
- `ralph-summary.md`
- `learning-diary.jsonl`
- `learning-diary.md`
- `memory-index.json`
- `memory-index.md`
- `scheduled-audit.json`
- `scheduled-audit.md`
- `orchestration-map.json`
- `workflow-map.json`
- `goal-frame.json`
- `long-horizon-map.json`
- `next-step.json`
- `handoff-packet.json`
- `handoff-packet.md`
- `pattern-guidance.json`
- `file-inventory.json`
- `package-knowledge-lint.json`
- `local-hygiene-preview.json`
- `local-hygiene-preview.md`
- `os-checkpoints/`
- `github-source-intake.jsonl`
- `github-source-intake.md`

## Local Hygiene

Use `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` before treating anything in `logs/` as cleanup material.

Truth is not cleanup; evidence is preserved; caches are disposable only when ignored and regeneratable.

Local Hygiene v1 is advisory only:

- `logs/check-output/*` and `logs/scheduled-audit-output/*` may be future archive candidates when old and unprotected.
- `logs/*.jsonl` ledgers are append-only evidence and are never compacted or deleted by v1.
- generated reports and sidecars may be regenerated, but they are not active memory.
- Ralph attempt logs are generated evidence for bounded retry review; they are not acceptance, command approval, or transition approval.
- dry-run manifests are generated evidence and do not authorize cleanup.
- OS checkpoints are explicit scoped source snapshots for PrecodeOS-owned integrity recovery. They live under ignored `logs/os-checkpoints/`, do not make generated evidence authoritative, and must not roll back append-only proof ledgers.

## Implemented Bead Reversal

Reversal work preserves evidence history.

- `logs/bead-build-journal.md/jsonl` may show closeout work digests, advisory commit-message suggestions, reversal provenance, or supersession provenance when a bead records them.
- `logs/build-attribution-ledger.md/json` may show reviewed human contributor, contributor role, agent/tool surface, reviewer, uncertainty, Git author hints, and missing-attribution warnings by bead.
- Existing journal entries, check ledgers, loop events, handoffs, and transition logs remain historical evidence.
- Advisory commit-message suggestions in generated logs do not stage files, commit, push, accept review, approve transition, or activate work.
- Generated reversal warnings from `completion-check.py` are advisory evidence only.
- Do not delete evidence, rewrite transition logs, reopen `done` beads, or treat Git revert as proof from generated output.

## Extension Output Rules

Generated extension evidence belongs under `logs/` unless an existing Precode generated report already owns the surface.

Generated markdown must include an authority contract and `CLASS: generated`.

Generated JSON and JSONL files are evidence only. They must not be treated as active memory, task selection, product decisions, implementation plans, or bead state.

Package Knowledge Lint JSON may include reviewed-intentional dispositions, `review_required` counts, and plain backtick path-reference counts. Those fields help maintainers separate new review-required drift from intentional inventory or protocol references; they do not approve edits, promote sources, rewrite docs, or create a checker gate.

If Package Knowledge Lint reports stale generated sidecars, refresh the owning generated evidence through its source command and rerun the lint. Do not hand-edit generated JSON as authority, treat the stale-sidecar cue as cleanup approval, or convert advisory lint output into CI enforcement without a separate maintainer decision.

Build attribution generated output must not be treated as acceptance, merge approval, release approval, blame, contributor scoring, telemetry, GitHub mutation, registry behavior, optional-pack behavior, or package-manager behavior.

## Versioning

This `LOG-EVIDENCE-TAXONOMY.md` file is a reference file and carries document version metadata.

Generated outputs under `logs/` are not manually versioned. They use generated timestamps, append-only evidence rows, and authority demotion instead.
