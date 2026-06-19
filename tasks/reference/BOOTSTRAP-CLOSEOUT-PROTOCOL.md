# PrecodeOS -- Bootstrap Closeout Protocol
<!-- ANCHOR: bootstrap-closeout-protocol -->

> AUTHORITY: Final staged closeout contract for PrecodeOS bootstrap adoption, existing-project adaptation planning, package upgrade preview, support-assisted recovery guidance, and narrowly approved missing-package-file copy actions.
> NOT_AUTHORITY: Active memory, target-project truth, broad installer behavior, owner-file adaptation approval, dirty package-file replacement, hook installation, CI mutation, app commands, app-code edits, release channels, package-manager behavior, rollback automation, task selection, PRD approval, bead activation, or generated evidence truth.
> LOAD_WHEN: A user, support engineer, maintainer, or agent needs the final P0 bootstrap lane behavior after Bootstrap Confidence, Existing Repo Intake, manifest preview, supervised setup plan, and supervised setup apply.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-19

## Purpose

The Bootstrap Closeout Protocol finishes the P0 Installer / Bootstrap Experience without creating a broad installer.

It answers four setup questions:

```text
How should an existing project plan owner-file adaptation?
What package upgrade state is visible before mutation?
What recovery guidance should support give when setup is partial or confusing?
Which missing package-owned files may be copied after explicit action approval?
```

All preview and guidance modes are non-mutating generated evidence. They do not approve setup mutation, owner-file adaptation, package updates, hook installation, CI changes, app commands, app-code edits, release channels, package-manager behavior, or rollback automation.

## Commands

Use these modes from the PrecodeOS package checkout after source and target are clear:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --existing-project-adaptation-plan
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --recovery-guidance
```

For existing Precode targets, missing package-owned files marked `review_package_copy_candidate` may be copied only by explicit action ID:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>
```

Structured output is available with `--json`. Generated evidence remains explicit and source-side only through `--write-evidence`; the helper must not write target files unless an apply mode is explicitly requested.

## Existing-Project Adaptation Plan

`--existing-project-adaptation-plan` applies to targets with app code, docs, CI, product history, or active work.

It must:

- route the target through Existing Repo Intake before any owner-file edit
- identify owner-file creation or adaptation candidates
- preserve existing project truth and conflicts
- defer package copying, hooks, CI, app commands, and app-code edits
- require explicit user approval for each owner-file adaptation

The plan is not copy approval or edit approval.

## Package Upgrade Preview

`--upgrade-preview` applies to targets that already contain Precode active memory.

It must classify package state as one of:

| Classification | Meaning |
|---|---|
| `clean` | No dirty package-owned files were detected; missing package-owned files may still need explicit copy approval. |
| `dirty_package_edits` | Package-owned files differ from the source package and require manual review before update mutation. |
| `dirty_project_or_owner_edits` | Owner or active-memory surfaces differ from package templates or are missing; preserve project truth and review manually. |
| `mixed_or_unknown` | Package-owned files and owner/project surfaces both need review, or path shape is unclear. |
| `blocked` | Source, target, or target kind prevents safe preview. |

Preview actions use stable IDs and categories:

| Category | Meaning |
|---|---|
| `current` | Target package-owned file matches the source package. |
| `review_package_copy_candidate` | Missing package-owned file may be copied after explicit approval. |
| `manual_package_review` | Existing package-owned path differs or has a path-type conflict; do not overwrite automatically. |
| `preserve_owner_edit` | Owner or active-memory surface differs from the package template; preserve and review manually. |
| `review_owner_creation_candidate` | Owner or active-memory surface is missing; create only from confirmed target truth. |
| `preserve_existing` | Existing target material should stay in place. |
| `deferred` | Hooks, CI, or other out-of-scope setup remains a separate approval path. |

## Upgrade Apply

`--apply-upgrade-preview` is deliberately narrow. It may copy only approved `review_package_copy_candidate` actions when all are true:

- target kind is `existing_precode`
- preview state is not `dirty_package_edits`, `mixed_or_unknown`, or `blocked`
- each approved ID exists in the current upgrade preview
- each approved action is for a missing package-owned file
- the source file exists and the target path does not exist

It must refuse dirty package states, unknown action IDs, non-copy actions, existing target paths, owner-file adaptation, overwrites, hooks, CI, app commands, app-code edits, release channels, package-manager behavior, and rollback automation.

The package keeps fixture coverage for these upgrade-apply refusals in `scripts/bootstrap-check.py --self-test`, including missing approval, unknown IDs, dirty or unknown package state, missing source files, and overwrite refusal. The fixtures are regression evidence only; they do not approve package updates or dirty-file replacement.

## Recovery Guidance

`--recovery-guidance` gives support-assisted next steps for partial or confusing setup states. It may recommend Git inspection, memory validation, file inventory checks, Existing Repo Intake, upgrade preview, or supervised setup planning.

It must not automate rollback, run destructive cleanup, overwrite dirty files, install hooks, change CI, or treat generated preview output as authority.

## Guardrails

- Preview output is generated evidence only.
- Existing projects must complete Existing Repo Intake before owner-file adaptation or package copy decisions.
- Dirty package-owned files require manual review; they are not safe update candidates.
- Owner and active-memory files preserve project truth and are never automatically adapted.
- Hooks and CI require separate explicit approval.
- No command in this protocol creates release channels, package-manager semantics, registry behavior, optional-pack installation, or rollback automation.

## Builder Prompt

```text
Close out PrecodeOS bootstrap safely.
Use the PrecodeOS checkout as the source and my project folder as the target.
Run the relevant non-mutating preview first: existing-project adaptation plan, upgrade preview, or recovery guidance.
Do not copy, edit, overwrite, install hooks, change CI, run app commands, adapt owner files, define release channels, provide package-manager behavior, or automate rollback.
If a missing package-owned file can be copied, show the action ID and wait for my explicit approval.
Treat all preview output as evidence only, not authority or permission to mutate.
```
