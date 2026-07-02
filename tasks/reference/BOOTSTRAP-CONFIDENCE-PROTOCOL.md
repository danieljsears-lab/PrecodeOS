# PrecodeOS -- Bootstrap Confidence Protocol
<!-- ANCHOR: bootstrap-confidence-protocol -->

> AUTHORITY: Read-only first-run confidence workflow for inspecting a PrecodeOS package source and target project before setup mutation.
> NOT_AUTHORITY: Active memory, installer approval, target-project truth, mutating copy behavior, update channels, package-manager release semantics, generated evidence truth, task selection, PRD approval, or bead activation.
> LOAD_WHEN: A user, support engineer, or agent is preparing to adopt PrecodeOS into a new or existing project and needs to verify source, target, copy groups, exclusions, conflicts, dependencies, and first safe next action before editing.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.7
Last updated: 2026-07-02

## Purpose

Bootstrap Confidence helps a builder answer one question before setup work starts:

```text
Is it clear enough to proceed with a supervised PrecodeOS setup plan?
```

The protocol is intentionally read-only for v1. It inspects the package source and target project, names public file groups and exclusions, reports conflicts and missing dependencies, and gives the first safe next action. It does not copy files, install hooks, edit active memory, mutate CI, change package files, or write app code.

Use this protocol before guided setup, support-assisted setup, existing repo intake, or first-use troubleshooting when the source package, target project, or setup state is uncertain.

## V1 Command

Use the helper from the PrecodeOS package checkout:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

Optional modes:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --json
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --existing-project-adaptation-plan
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --recovery-guidance
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --write-evidence
```

Default mode prints a plain-English report and writes nothing.

`--json` prints machine-readable output and writes nothing.

`--preview-manifest` adds a non-mutating install/update dry-run preview with candidate setup action categories. It still writes nothing by default and does not approve setup mutation.

`--supervised-setup-plan` adds the manifest preview plus a non-mutating setup checklist with action IDs, approval gates, exclusions, blockers, and validation steps. It still writes nothing by default and does not approve setup mutation.

`--apply-supervised-setup` requires `--supervised-setup-plan` and one or more explicit `--approve-action <SP-ID>` flags. It copies only approved `review_copy_candidate` actions into empty or nearly empty targets. It is governed by `tasks/reference/SUPERVISED-SETUP-APPLY-PROTOCOL.md` and refuses owner-file adaptation, existing-repo mutation, overwrites, hooks, CI, app commands, app code, release channels, package-manager behavior, rollback automation, and CLI installation.

`--existing-project-adaptation-plan`, `--upgrade-preview`, `--apply-upgrade-preview`, and `--recovery-guidance` are governed by `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`. They close the P0 bootstrap lane with non-mutating existing-project adaptation planning, ID-aware package upgrade preview, support-assisted recovery guidance, and a narrow apply path for explicitly approved missing package-owned files only. Upgrade preview must report PRD/bead identity collisions instead of marking incoming package dev PRDs or beads copyable.

`--write-evidence` writes generated evidence only under the source Precode workspace:

- `logs/bootstrap-check.json`
- `logs/bootstrap-check.md`

The helper must not write to the target project.

## Required Output

Bootstrap Confidence output should include:

- `status`: `pass`, `warning`, or `blocked`
- `warnings`
- `blockers`
- `source_root`
- `target_root`
- `target_kind`
- `public_file_groups`
- `excluded_paths`
- `conflicts`
- `missing_dependencies`
- `recommended_next_step`
- `stop_conditions`

Plain output should also remind the user that the result is generated evidence only and does not approve mutation.

When `--preview-manifest` is used, output should also include an `install_update_preview` object with action categories and a next setup gate. The preview is governed by `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`.

When `--supervised-setup-plan` is used, output should also include a `supervised_setup_plan` object. The setup plan is governed by `tasks/reference/SUPERVISED-SETUP-PLAN-PROTOCOL.md`.

When `--upgrade-preview` is used, output should also include a `package_upgrade_preview` object with package-state classification, copy/action IDs, `identity_collisions`, `deferred_package_dev_identity_paths`, and the same non-authority warnings as Bootstrap Closeout. A `blocked_identity_collision` action is never copyable.

## Target Kinds

Use these labels:

| Target kind | Meaning |
|---|---|
| `missing` | The target path does not exist. |
| `same_as_source` | Source and target resolve to the same folder. |
| `empty` | Target exists and has no visible project files. |
| `nearly_empty` | Target has only minimal repository files such as `.git`, `.gitignore`, `README.md`, or `LICENSE`. |
| `existing_precode` | Target already has Precode active-memory files. |
| `existing_project` | Target has project material that needs conflict review before setup. |

## Thin Manifest

V1 uses a thin public package manifest to teach setup shape. It is not an update manifest, release channel, package-manager contract, or install permission.

Public file groups:

| File group | Include |
|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` |
| Candidate Queue | `CANDIDATE-QUEUE.md` |
| Product and project owner files | `PRODUCT.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` |
| Public orientation docs | `README.md`, `docs/`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `TRADEMARK.md`, `NOTICE`, `LICENSE` |
| Agent shims and adapters | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `adapters/` |
| Work structure | `tasks/beads/`, `tasks/prds/`, `tasks/reference/`, `tasks/templates/`, `modes/`, `memory/` |
| Scripts and checks | `scripts/`, `.githooks/`, `.github/workflows/` when approved |
| Public generated-log guide | `logs/LOG-EVIDENCE-TAXONOMY.md` |

Excluded paths:

- private local planning material
- `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`
- generated `logs/*.json`, `logs/*.jsonl`, `logs/*.yaml`, and generated `logs/*.md`
- `logs/check-output/`, `logs/scheduled-audit-output/`
- `.agent-state/`, `.claude/`, `.codex/`, `.cursor/`, `.vscode/`, `.idea/`
- `.env`, `.env.*`, `secrets/`, `credentials/`, key files, and certificate files
- `__pycache__/`, test caches, coverage output, and local virtual environments

Keep `logs/LOG-EVIDENCE-TAXONOMY.md` when present.

## Recommended Next Step Rules

Use plain recommendations:

| Condition | Recommendation |
|---|---|
| Source or target is missing | Stop and identify the correct folders before setup. |
| Source and target are identical | Stop; do not treat the package checkout as the target app. |
| Source is not a plausible PrecodeOS package | Stop and use a clean PrecodeOS checkout. |
| Target is empty or nearly empty | Proceed to guided setup for a new project after user approval. |
| Target has existing project material | Run Existing Repo Intake, then review conflicts and owner-file adaptations before copying anything. |
| Target already has Precode active memory | Validate memory before deciding whether this is setup, repair, or update work. |

## Guardrails

- Bootstrap Confidence output is generated evidence only.
- It must not approve mutation.
- It must not copy files.
- It must not install Git hooks.
- It must not add or change GitHub Actions.
- It must not edit app code.
- It must not create or activate beads.
- It must not update `tasks/todo.md`.
- It must not read or print secret file contents.
- It must not treat a thin manifest as update, channel, package-manager, or release metadata.
- It must not treat manifest preview output as copy, update, or install approval.
- It must not treat supervised setup-plan output as copy, update, install, or owner-file adaptation approval.
- It must not treat supervised setup apply as a broad installer, owner-file adaptation engine, update flow, rollback flow, hook installer, CI installer, package manager, release channel, or CLI.
- It must not treat existing-project adaptation planning, upgrade preview, or recovery guidance as owner-file edit approval, package update permission, dirty-file overwrite approval, rollback approval, release-channel metadata, or package-manager behavior.
- It must not treat upgrade apply as permission to replace dirty package files, adapt owner files, install hooks, change CI, automate rollback, or update through a package manager.
- It must not make an installable `precode` CLI a prerequisite for normal repo-local use.

## Builder Prompt

```text
Run Bootstrap Confidence before setup.
Use the PrecodeOS checkout as the package source and my project folder as the target.
Do not copy, edit, install hooks, change CI, or write app code.
Tell me the source, target, target kind, public file groups, excluded files, conflicts, missing dependencies, first safe next action, and stop conditions.
Treat the output as evidence only, not permission to mutate.
```

To see the next non-mutating setup preview, ask:

```text
Add the install/update manifest dry-run preview.
Show candidate copy, adaptation, preserve, exclusion, blocked, and deferred actions.
Do not copy, edit, install hooks, change CI, create active memory, run app commands, or write app code.
```

To see the next non-mutating setup checklist, ask:

```text
Add the supervised setup plan.
Show action IDs, approval gates, exclusions, blockers, and validation steps.
Do not copy, edit, install hooks, change CI, create active memory, run app commands, adapt owner files, or write app code.
```

To apply a reviewed fresh-project copy action, ask:

```text
Apply only the supervised setup action IDs I explicitly approve.
Use the PrecodeOS checkout as the source and my empty or nearly empty project folder as the target.
Do not adapt owner files, overwrite files, install hooks, change CI, run app commands, write app code, install a CLI, provide package-manager behavior, define release channels, or automate rollback.
Show copied, skipped, blocked, and validation next steps.
```
