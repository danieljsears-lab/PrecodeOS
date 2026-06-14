# PrecodeOS -- OS Integrity Protocol
<!-- ANCHOR: os-integrity-protocol -->

> AUTHORITY: PrecodeOS-owned surface classes, protected-source checkpoint expectations, OS-integrity check behavior, scoped restore limits, and generated-evidence boundaries.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, target-application file integrity, command approval, automatic repair, generated progress state, or package-manager behavior.
> LOAD_WHEN: Changing PrecodeOS-owned operating files, reviewing protected-source edits, creating an OS checkpoint, restoring from a checkpoint, or diagnosing OS-integrity warnings.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## Purpose

PrecodeOS integrity checks protect the operating layer itself: active memory, execution state, protocols, maintained scripts, hooks, adapters, package docs, and public/private boundary files.

This protocol is about PrecodeOS-owned package surfaces. It is not a target-application file guardrail. Normal bead execution scope belongs to `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`, `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`, and `scripts/files-in-play-check.py`.

## Surface Classes

| Class | Examples | Integrity posture |
|---|---|---|
| `active_memory` | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` | Protected source; checkpoint before intentional OS-layer mutation. |
| `execution_state` | `tasks/beads/*.md`, `tasks/prds/*.md`, `tasks/beads/BEAD-SCHEMA.md` | Protected when changing schema, active state, or approved work contracts. |
| `protocols_templates` | `tasks/reference/*.md`, `tasks/templates/*.md` | Protected source; checkpoint before protocol or template mutation. |
| `validation_hooks_scripts` | `scripts/*.py`, `scripts/*.sh`, `.githooks/*`, `.github/workflows/*.yml` | Protected source; checkpoint before validation, hook, compiler, or script mutation. |
| `adapters_shims` | `adapters/*.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` | Protected source; checkpoint before compatibility behavior changes. |
| `package_docs_surface` | `README.md`, `docs/*.md`, `docs-html/*.html`, root package reference docs | Protected when public package meaning, setup guidance, or authority boundaries change. |
| `public_private_boundary` | `.gitignore`, `.github/PULL_REQUEST_TEMPLATE.md`, public repo boundary docs | Protected source; checkpoint before public/private or contribution-boundary changes. |
| `generated_evidence` | `OS-HEALTH.md`, `PROGRESS.md`, `logs/*.json`, `logs/*.jsonl`, generated Markdown under `logs/` | Evidence only; usually preserve or regenerate, do not restore as source truth. |

## Checkpoint Expectations

Use `scripts/os-checkpoint.py` before intentional protected-source mutation:

```text
python3 scripts/os-checkpoint.py create --scope validation --reason "before validation hook change" --paths scripts/pre-commit-validate.sh scripts/write-guard.sh
```

Checkpoint scope should be narrow. Create checkpoints for the files or surface class being changed, not the whole repository by default.

Recommended scopes:

- `active-memory`
- `execution-state`
- `protocols`
- `validation`
- `adapters`
- `package-surface`
- `boundary`

The checkpoint helper refuses dirty covered paths by default so the checkpoint represents the pre-mutation state. A checkpoint is valid for strict integrity checking only when it includes the changed protected paths and was created from the same git `HEAD`.

For guardrail bootstrap or recovery of already-dirty tracked source files, maintainers may use `--from-head` to checkpoint the clean `HEAD` version explicitly:

```text
python3 scripts/os-checkpoint.py create --scope validation --reason "before committing OS-integrity bootstrap" --from-head --paths scripts/write-guard.sh
```

This is still an explicit checkpoint action. It does not make dirty working-tree content authoritative.

## Integrity Check Behavior

`scripts/os-integrity-check.py` classifies changed or staged paths and reports protected-source risk.

Use:

```text
python3 scripts/os-integrity-check.py --json
python3 scripts/os-integrity-check.py --staged --json
```

Hook usage is stricter:

```text
python3 scripts/os-integrity-check.py --staged --strict
```

Strict mode blocks high-risk protected-source commits that lack a valid scoped checkpoint. Outside strict mode, findings are advisory evidence only.

The checker does not:

- approve work
- choose tasks
- activate beads
- replace review
- infer product authority
- inspect private maintainer files
- mutate files
- install hooks
- create package-manager or release-channel behavior

## Restore Limits

Use restore as an explicit recovery action, starting with dry-run:

```text
python3 scripts/os-checkpoint.py restore --id <checkpoint-id> --dry-run
python3 scripts/os-checkpoint.py restore --id <checkpoint-id> --apply
```

Restore must stay scoped to the checkpoint manifest. It must not restore generated reports or append-only proof ledgers as source truth.

Generated evidence should usually be regenerated or preserved:

- `OS-HEALTH.md`, `PROGRESS.md`, and generated Markdown reports may be regenerated.
- `logs/*.json` and `logs/*.yaml` sidecars may be regenerated when their source commands own them.
- `logs/*.jsonl`, `logs/check-output/`, and other proof ledgers are append-only evidence and must not be rolled back by OS checkpoint restore.

If recovery requires deleting, compacting, or rewriting evidence, use the Recovery Protocol and ask for explicit human approval.

## Relationship To Other Guardrails

Use this protocol when the PrecodeOS operating layer may be damaged.

Use `scripts/files-in-play-check.py` when normal implementation work touches files outside the active bead's `files_in_play`.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when a command is destructive, external, secret-bearing, approval-sensitive, or needs non-check tool-run logging.

Use `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` before treating generated evidence, caches, bulky logs, or local clutter as cleanup material.

Warnings from OS-integrity tools are generated evidence. They do not become authority until a human promotes a conclusion into the relevant owner file, PRD, decision, or approved bead.
