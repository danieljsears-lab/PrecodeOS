# PrecodeOS -- Install/Update Manifest Protocol
<!-- ANCHOR: install-update-manifest-protocol -->

> AUTHORITY: Non-mutating install/update manifest and dry-run preview workflow for explaining candidate PrecodeOS setup actions before any target-project mutation.
> NOT_AUTHORITY: Active memory, installer approval, target-project truth, release channels, package-manager semantics, rollback automation, copy permission, update permission, task selection, PRD approval, bead activation, or generated evidence truth.
> LOAD_WHEN: A user, support engineer, or agent needs to preview what PrecodeOS would consider copying, adapting, preserving, excluding, blocking, or deferring after Bootstrap Confidence and before any supervised setup mutation.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-14

## Purpose

The Install/Update Manifest Protocol gives PrecodeOS one more trust layer between read-only Bootstrap Confidence and any future mutating setup flow.

It answers:

```text
What would PrecodeOS consider doing, and what must stay stopped, before I approve setup changes?
```

This protocol is intentionally non-mutating. It produces a dry-run preview of setup action categories and keeps every result as generated evidence only. It does not copy files, adapt owner files, install hooks, change CI, create active memory, run app commands, write app code, define release channels, update packages, install a CLI, or provide rollback automation.

## Command

Use the preview from the PrecodeOS package checkout after Bootstrap Confidence:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest
```

Structured output is available with:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest --json
```

Generated evidence remains explicit and source-side only:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest --write-evidence
```

`--write-evidence` writes only the Bootstrap Confidence evidence files under the PrecodeOS package source:

- `logs/bootstrap-check.json`
- `logs/bootstrap-check.md`

The helper must not write to the target project.

After preview, use the supervised setup plan when the user needs a checklist before approving any manual setup work:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
```

The supervised setup plan is governed by `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`. It is still non-mutating generated evidence and does not approve copying, owner-file edits, overwrites, hooks, CI changes, active-memory edits, app commands, or app-code edits.

## Required Preview Shape

The preview output should include:

- `manifest_kind`: `install_update_dry_run_preview`
- `status`: `pass`, `warning`, or `blocked`
- `source_root`
- `target_root`
- `target_kind`
- `action_categories`
- `actions`
- `writes_by_default`: `false`
- `target_mutation_allowed`: `false`
- `generated_evidence_only`: `true`
- `not_authority_for`
- `next_setup_gate`

Each action should include:

- `category`
- `path`
- `reason`
- optional `group`

## Action Categories

| Category | Meaning |
|---|---|
| `copy_candidate` | A path may be copied later by a supervised setup plan after explicit user approval. |
| `adapt_candidate` | A path needs project-specific review or adaptation before use, especially owner files or conflicts. |
| `preserve_existing` | Existing target material should be preserved while the user decides whether this is setup, repair, or update work. |
| `exclude` | A path or pattern must stay out of setup copying. |
| `blocked` | Setup preview cannot proceed safely until source, target, or stop-condition issues are resolved. |
| `deferred` | A possible future action is deliberately outside this preview slice. |

## Branch Rules

| Target state | Preview behavior |
|---|---|
| Missing source, missing target, or same source/target | Mark setup actions as `blocked`. |
| Empty target | Show public file-group copy candidates and owner-file adaptation candidates after user approval. |
| Nearly empty target | Preserve or adapt existing minimal material such as `README.md`; show remaining supervised candidates. |
| Existing project | Defer copying and adaptation until Existing Repo Intake runs and conflicts are reviewed. |
| Existing Precode target | Preserve existing Precode material and validate memory before setup, repair, or update decisions. |

## Guardrails

- Manifest preview output is generated evidence only.
- It must not approve mutation.
- It must not copy files.
- It must not overwrite target material.
- It must not install Git hooks.
- It must not add or change GitHub Actions.
- It must not edit active memory.
- It must not run app commands.
- It must not write app code.
- It must not read or print secret file contents.
- It must not define release channels, pinned versions, package-manager updates, rollback automation, or an installable `precode` CLI.
- It must route existing projects through Existing Repo Intake before any copy or owner-file adaptation becomes actionable.

## Next Setup Layer

The next non-mutating layer is the supervised setup plan. It converts preview categories into action IDs, approval gates, exclusions, blockers, and validation steps without making any action executable or approved.

## Builder Prompt

```text
Run the PrecodeOS install/update manifest preview after Bootstrap Confidence.
Use the PrecodeOS checkout as the source and my project folder as the target.
Do not copy, edit, install hooks, change CI, run app commands, create active memory, or write app code.
Show copy candidates, adaptation candidates, preserved existing paths, exclusions, blockers, and deferred actions.
Treat the preview as evidence only, not permission to mutate.
```
