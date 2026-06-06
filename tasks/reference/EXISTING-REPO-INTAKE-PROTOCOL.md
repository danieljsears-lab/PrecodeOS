# PrecodeOS -- Existing Repo Intake Protocol
<!-- ANCHOR: existing-repo-intake-protocol -->

> AUTHORITY: Read-only existing-repository intake workflow for choosing the existing-app adoption branch, preserving current project conventions, and producing setup/adaptation evidence before PrecodeOS files are copied or app work begins.
> NOT_AUTHORITY: Active memory, installer approval, target-project truth, product decisions, repo-topology decisions, PRD approval, bead activation, app diagnostics, generated evidence truth, or permission to mutate files.
> LOAD_WHEN: A user, support engineer, or agent is adopting PrecodeOS into a repository that already has app code, docs, CI, product history, or active work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-06

## Purpose

Existing Repo Intake helps a builder answer one question at the first adoption fork:

```text
What is already here, what must Precode respect, and what is the safe adaptation path?
```

Use Bootstrap Confidence first to confirm the PrecodeOS package source and target project folder. Then choose:

- Fresh install path for an empty or nearly empty target.
- Existing Repo Intake path for a target with app code, docs, CI, product history, or active work.

This protocol is intentionally read-only for v1. It summarizes repo shape, app boundaries, existing docs, likely checks, sensitive surfaces, conflicts, and owner-file adaptation needs before any setup mutation. It does not copy files, install hooks, run app commands, edit docs, create active memory, create beads, approve PRDs, change CI, or write app code.

## V1 Command

Use the helper from the PrecodeOS package checkout:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <existing-repo-root>
```

Optional modes:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <existing-repo-root> --json
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <existing-repo-root> --write-evidence
```

Default mode prints a plain-English report and writes nothing.

`--json` prints machine-readable output and writes nothing.

`--write-evidence` writes generated evidence only under the source Precode workspace:

- `logs/existing-repo-intake.json`
- `logs/existing-repo-intake.md`

The helper must not write to the target project.

## Required Output

Existing Repo Intake output should include:

- `status`: `pass`, `warning`, or `blocked`
- `warnings`
- `blockers`
- `source_root`
- `target_root`
- `target_kind`
- `repo_topology`
- `likely_app_dirs`
- `package_managers`
- `frameworks`
- `runtimes`
- `build_tools`
- `docs`
- `ci_deploy_hints`
- `generated_ignored_surfaces`
- `sensitive_path_patterns`
- `owner_file_gaps`
- `likely_checks`
- `conflicts`
- `recommended_next_step`
- `stop_conditions`

Plain output should remind the user that the report is generated evidence only and does not approve setup mutation, product decisions, or implementation.

## Intake Rules

Inspect only enough to preserve the existing project:

- repo topology and app directories
- package managers, frameworks, runtimes, and build tools
- existing docs, PRDs, architecture notes, and README conventions
- existing test, lint, build, typecheck, CI, and deploy hints
- route, API, schema, auth, security, and integration boundaries
- design-system or UI component conventions
- generated folders, caches, ignored files, and bulky local outputs
- secrets, env files, credentials, and dashboard-dependent setup that must not be copied into Precode docs
- conflicts between existing project material and Precode owner files

Do not run installers, formatters, migrations, dev servers, dependency updates, lint, test, build, typecheck, deployment, dashboard commands, destructive commands, or app-code edits during intake.

Likely checks may be reported as future verification hints only. They are not proof and must be run later only through an approved setup, unblocker, implementation, or verification bead.

## Adoption Fork

Use this branch after Bootstrap Confidence:

| Target state | Next path |
|---|---|
| Target is missing | Stop and identify or create the target folder. |
| Source and target are identical | Stop; do not treat the PrecodeOS package checkout as the app. |
| Target is empty or nearly empty | Fresh install path in `docs/PRECODE-GUIDED-SETUP.md`. |
| Target has app code, docs, CI, product history, or active work | Existing Repo Intake. |
| Target already has Precode active memory | Validate memory, then decide whether this is setup, repair, update, or source intake. |

## Promotion Path

Generated intake is evidence only. Stable conclusions require user review before promotion:

| Intake finding | Destination |
|---|---|
| App directory, stack, repo topology, checks, conventions, integrations, sensitive boundaries | `PROJECT-CONTEXT.md` |
| Layout, module, route, component, or generated-folder conventions | `CODEBASE-GUIDE.md` |
| Hard setup, topology, CI, deployment, or ownership decision | `DECISIONS.md` |
| Product facts, users, promise, non-goals, or success signals | `PRODUCT.md` after user confirmation |
| Architecture, API, schema, or security facts | `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, or `SECURITY.md` |
| Product requirements | `tasks/prds/*.md` after Local Source Intake or PRD shaping |
| Executable work | `tasks/beads/*.md` after definition and approval |

## Guardrails

- Existing Repo Intake output is generated evidence only.
- It must not approve mutation.
- It must not copy files.
- It must not overwrite existing docs, app code, package files, CI, env files, or generated outputs.
- It must not install Git hooks.
- It must not add or change GitHub Actions.
- It must not run app commands.
- It must not create active memory.
- It must not create or activate beads.
- It must not approve PRDs, acceptance, repo topology, product direction, or owner-file facts.
- It must not update `tasks/todo.md`.
- It must not read or print secret file contents.
- It must not treat likely checks as proof.

## Stop Conditions

Stop before setup mutation or implementation when:

- source and target are unclear
- source and target resolve to the same folder
- target is empty and should use the fresh install path instead
- existing project docs conflict with Precode owner files
- current app directory or repo topology is unclear
- secrets, credentials, env files, production access, auth, payments, deployment settings, or private dashboards are needed
- CI, Git hooks, package files, migrations, or external systems would need mutation
- existing active work is uncommitted or unclear
- generated intake output is being treated as authority or install permission

## Builder Prompt

```text
Run Existing Repo Intake after Bootstrap Confidence.
Use the PrecodeOS checkout as the package source and my existing app repo as the target.
Do not copy, edit, install hooks, change CI, run app commands, or write code.
Tell me the repo topology, likely app directories, stack, docs, likely checks, CI/deploy hints, generated and sensitive surfaces, conflicts, owner-file gaps, first safe next action, and stop conditions.
Treat the output as evidence only, not permission to mutate.
```
