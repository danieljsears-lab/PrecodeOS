# PrecodeOS -- Supervised Setup Plan Protocol
<!-- ANCHOR: supervised-setup-plan-protocol -->

> AUTHORITY: Non-mutating supervised setup-plan workflow for turning Bootstrap Confidence and manifest preview evidence into a visible setup checklist before any target-project mutation.
> NOT_AUTHORITY: Active memory, installer approval, target-project truth, copy permission, update permission, release channels, package-manager semantics, rollback automation, task selection, PRD approval, bead activation, or generated evidence truth.
> LOAD_WHEN: A user, support engineer, or agent needs a setup checklist after Bootstrap Confidence and manifest preview but before any copying, owner-file adaptation, hook installation, CI change, app command, or app-code edit.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-14

## Purpose

The Supervised Setup Plan Protocol gives PrecodeOS a final non-mutating planning layer before any future setup mutation.

It answers:

```text
What exact setup checklist should I review before I approve any manual changes?
```

This protocol is intentionally non-mutating. It produces setup-plan evidence only. It does not copy files, adapt owner files, install hooks, change CI, create active memory, run app commands, write app code, define release channels, update packages, install a CLI, or provide rollback automation.

## Command

Use the setup plan from the PrecodeOS package checkout after Bootstrap Confidence:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
```

Structured output is available with:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --json
```

Generated evidence remains explicit and source-side only:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --write-evidence
```

`--supervised-setup-plan` includes the install/update manifest preview because setup-plan actions must be traceable to preview categories.

`--write-evidence` writes only Bootstrap Confidence evidence files under the PrecodeOS package source:

- `logs/bootstrap-check.json`
- `logs/bootstrap-check.md`

The helper must not write to the target project.

After the setup plan is reviewed, a separate apply mode may copy explicitly approved `review_copy_candidate` actions into empty or nearly empty targets:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>
```

That apply mode is governed by `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md`. The plan itself remains evidence only and does not approve the apply step.

## Required Plan Shape

The setup-plan output should include:

- `plan_kind`: `supervised_setup_plan`
- `status`: `pass`, `warning`, or `blocked`
- `source_root`
- `target_root`
- `target_kind`
- `actions`
- `approval_gates`
- `excluded_paths`
- `blockers`
- `validation_steps`
- `target_mutation_allowed`: `false`
- `generated_evidence_only`: `true`
- `not_authority_for`
- `next_manual_gate`

Each action should include:

- `id`
- `category`
- `path`
- `reason`
- `requires_user_approval`
- optional `group`

## Action Categories

| Category | Meaning |
|---|---|
| `review_copy_candidate` | A path may be copied manually later after explicit user approval. |
| `review_adaptation_candidate` | A path needs project-specific review or adaptation before use. |
| `preserve_existing` | Existing target material should be preserved while the user decides whether this is setup, repair, or update work. |
| `exclude` | A path or pattern must stay out of setup copying. |
| `blocked` | Setup planning cannot proceed safely until source, target, or stop-condition issues are resolved. |
| `deferred` | A possible future action is deliberately outside this setup-plan slice. |

## Branch Rules

| Target state | Setup-plan behavior |
|---|---|
| Missing source, missing target, or same source/target | Mark setup plan as `blocked`. |
| Empty target | Show public file-group setup candidates, owner-file adaptation candidates, exclusions, approval gates, and validation steps. |
| Nearly empty target | Preserve or adapt existing minimal material such as `README.md`; show remaining supervised candidates. |
| Existing project | Stop at Existing Repo Intake before copying or owner-file adaptation becomes actionable. |
| Existing Precode target | Preserve existing Precode material and validate memory before setup, repair, or update decisions. |

## Approval Gates

The setup plan should name these gates before mutation:

- user confirms the source package checkout and target project folder
- user reviews excluded paths and secret boundaries
- user approves each file group before manual copying
- user approves each owner-file adaptation before editing
- user separately approves Git hooks or CI changes if those are ever needed
- user validates active memory before first implementation work

## Validation Steps

For fresh or nearly empty targets, the plan should recommend validation after approved manual setup:

- inspect target Git status
- run `bash scripts/validate-memory.sh` from the target after Precode files exist
- run `python3 scripts/file-inventory.py --check` from the target when package files are present
- run target-specific project checks only after owner files name them

These steps are validation suggestions, not proof that setup occurred.

## Guardrails

- Setup-plan output is generated evidence only.
- It must not approve mutation.
- It must not copy files.
- It must not provide bulk overwrite commands.
- It must not overwrite target material.
- It must not install Git hooks.
- It must not add or change GitHub Actions.
- It must not edit active memory.
- It must not run app commands.
- It must not write app code.
- It must not read or print secret file contents.
- It must not define release channels, pinned versions, package-manager updates, rollback automation, or an installable `precode` CLI.
- It must route existing projects through Existing Repo Intake before any copy or owner-file adaptation becomes actionable.
- It must not imply that `--apply-supervised-setup` can adapt owner files, overwrite target material, install hooks, change CI, mutate existing projects, run app commands, write app code, install a CLI, provide package-manager behavior, define release channels, or automate rollback.

## Builder Prompt

```text
Run the PrecodeOS supervised setup plan after Bootstrap Confidence and manifest preview.
Use the PrecodeOS checkout as the source and my project folder as the target.
Do not copy, edit, install hooks, change CI, run app commands, create active memory, or write app code.
Show the setup checklist, approval gates, exclusions, blockers, and validation steps.
Treat the setup plan as evidence only, not permission to mutate.
```
