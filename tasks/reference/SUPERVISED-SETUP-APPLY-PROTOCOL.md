# PrecodeOS -- Supervised Setup Apply Protocol
<!-- ANCHOR: supervised-setup-apply-protocol -->

> AUTHORITY: Approval-gated setup mutation workflow for copying explicitly approved PrecodeOS setup-plan paths into empty or nearly empty target projects.
> NOT_AUTHORITY: Active memory, target-project truth, owner-file adaptation approval, existing-repo mutation, hook installation, CI mutation, app commands, app-code edits, release channels, package-manager behavior, rollback automation, task selection, PRD approval, bead activation, or generated evidence truth.
> LOAD_WHEN: A user, support engineer, or agent has reviewed a supervised setup plan and needs to apply specific safe copy actions into an empty or nearly empty target.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-15

## Purpose

Supervised Setup Apply is the first intentionally mutating setup layer in PrecodeOS.

It answers:

```text
Which already-reviewed setup-plan copy actions may be copied into this fresh target now?
```

This protocol is deliberately narrow. It applies only to empty or nearly empty target projects, and only to setup-plan actions marked `review_copy_candidate` and explicitly approved by action ID. It does not adapt owner files, overwrite target material, install hooks, change CI, run app commands, write app code, define release channels, update packages, install a CLI, or provide rollback automation.

## Command

Run the command from the PrecodeOS package checkout after reviewing the supervised setup plan:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>
```

Approve multiple setup-plan copy actions by repeating `--approve-action`:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action SP-001 --approve-action SP-002
```

Structured output is available with:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID> --json
```

`--apply-supervised-setup` requires `--supervised-setup-plan`. The setup plan remains visible in output so the copied, skipped, and blocked apply results can be traced to reviewed action IDs.

Package upgrade preview and upgrade apply are separate closeout behavior governed by `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`. Supervised Setup Apply remains limited to fresh or nearly empty targets.

## Required Apply Shape

Apply output should include a `supervised_setup_apply` object with:

- `apply_kind`: `supervised_setup_apply`
- `status`: `applied` or `blocked`
- `source_root`
- `target_root`
- `target_kind`
- `approved_actions`
- `copied`
- `skipped`
- `blocked`
- `validation_next_step`
- `target_mutation_allowed`
- `not_authority_for`

Each copied, skipped, or blocked item should include:

- `path`
- `reason`

## Allowed Scope

Apply mode may copy only when all of these are true:

- the target kind is `empty` or `nearly_empty`
- Bootstrap Confidence and the supervised setup plan have no blockers
- the user supplied at least one `--approve-action`
- each approved action ID exists in the current supervised setup plan
- each approved action is `review_copy_candidate`
- the source path exists in the PrecodeOS package checkout
- the target path does not already exist

## Refusals

Apply mode must refuse:

- missing source or target paths
- source and target resolving to the same folder
- existing project targets
- existing Precode targets
- setup-plan blockers
- unknown action IDs
- unapproved actions
- `review_adaptation_candidate`, `preserve_existing`, `exclude`, `blocked`, or `deferred` actions
- owner-file adaptation
- existing target paths or overwrites
- Git hook installation
- GitHub Actions or CI mutation
- app commands
- app-code edits
- generated reports or generated logs
- local agent, editor, cache, virtualenv, environment, secret, credential, key, or certificate paths
- release channels, pinned versions, package-manager updates, rollback automation, registry behavior, optional packs, or an installable `precode` CLI

No refusal should fall back to a broader copy command. Blocked output should name the shortest safe next action.

## Validation After Apply

After an applied setup copy:

- inspect target Git status
- run `bash scripts/validate-memory.sh` from the target after copied files are present
- run `python3 scripts/file-inventory.py --check` from the target when package files are present
- adapt owner files manually before product implementation starts
- run target-specific checks only after owner files name them

These checks validate setup state. They do not prove product correctness or approve implementation.

## Rollback Limits

Apply mode does not provide rollback automation. If copied files are wrong, use normal Git inspection, `git diff`, and explicit human review to remove or adjust copied files. Do not run destructive cleanup commands unless the user approves them after seeing the target paths.

## Guardrails

- Supervised Setup Apply is a narrow setup copier, not a package installer.
- It must not approve mutation beyond the explicitly approved copy actions.
- It must not adapt owner files.
- It must not overwrite target material.
- It must not install Git hooks.
- It must not add or change GitHub Actions.
- It must not run app commands.
- It must not write app code.
- It must not read or print secret file contents.
- It must not define release channels, pinned versions, package-manager updates, rollback automation, or an installable `precode` CLI.
- It must route existing projects through Existing Repo Intake before any copy or owner-file adaptation becomes actionable.
- It must not replace package upgrade preview, dirty package-file review, support-assisted recovery guidance, or existing-project adaptation planning.

## Builder Prompt

```text
Apply only the supervised setup actions I explicitly approve.
Use the PrecodeOS checkout as the source and my empty or nearly empty project folder as the target.
Run the supervised setup plan first, then apply only the approved review_copy_candidate action IDs I name.
Do not adapt owner files, overwrite files, install hooks, change CI, run app commands, write app code, create release-channel behavior, install a CLI, provide package-manager behavior, or automate rollback.
After copying, show copied, skipped, blocked, and validation next steps.
```
