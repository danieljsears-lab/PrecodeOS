---
prd_id: PRD-013
status: approved
owner: user
risk_level: high
feature_link: Installable precode CLI Wrapper
features_status: not compiled
related_prds: ["PRD-002", "PRD-004", "PRD-006", "PRD-010", "PRD-012"]
---

# PRD-013 -- Installable `precode` CLI Wrapper
<!-- ANCHOR: prd-013-installable-precode-cli-wrapper -->

> AUTHORITY: Destination shard for the local `precode` command facade over trusted PrecodeOS repo commands.
> NOT_AUTHORITY: Active memory, task selection, bead activation, transition approval, command approval, generated report truth, implementation acceptance, setup approval, package publishing, package updates, release-channel behavior, broad installer behavior, registry behavior, external mutation, or a second Precode operating model.
> LOAD_WHEN: Reviewing, implementing, or decomposing the local installable `precode` CLI wrapper.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-15

## State

- ID: `PRD-013`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-15`

## Feature Link

- Feature: `Installable precode CLI Wrapper`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-002`, `PRD-004`, `PRD-006`, `PRD-010`, `PRD-012`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Installable precode CLI Wrapper`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Stable facts:
  - Existing repo-local commands already own session start, next-step routing, health generation, validation, and bootstrap inspection.
  - Current setup and health docs repeatedly exclude CLI, package-manager, release-channel, updater, and broad installer semantics.
  - The wrapper must compose trusted commands rather than discover a new operating model.
- Assumptions:
  - "Installable" means local editable console entrypoint or direct script use, not publishing to PyPI, Homebrew, npm, or another package channel.
  - The first slice should expose only curated aliases and print the exact underlying command before running it.
- Conflicts or stale inputs:
  - Earlier docs deferred any installable CLI until router, session-start, bootstrap, and generated evidence behavior proved stable. This PRD implements a constrained wrapper after those surfaces shipped while preserving the deferred package-manager and release-channel boundaries.

## Problem

Precode has many useful commands, but beginners and support helpers still have to remember script paths and command families. A small local CLI can improve command discovery if it stays a facade over trusted commands.

## User Moment

- Before: A user asks which Precode command to run and may copy the wrong script path or treat a generated report as the decision owner.
- After: The user can run a small set of `precode` aliases that print and execute the underlying canonical command.
- Why now: Bootstrap, next-step, OS Health, supervised setup, and generated-evidence boundaries are stable enough for a conservative wrapper slice.

## Destination

- Destination statement: `precode` is a local command facade over existing PrecodeOS scripts.
- Definition of done:
  - `scripts/precode_cli.py` exposes only curated aliases for trusted commands.
  - `pyproject.toml` defines a local `precode` console entrypoint without runtime dependencies.
  - CLI help and docs state that Markdown owner files and underlying scripts remain authoritative.
  - Public docs, package inventory, Extension Protocol, Tool Execution Protocol, generated docs/PRD surfaces, roadmap history, roadmap journal, and maintainer changelog are current.
- First useful vertical slice: local wrapper for start, next, health, validate, package check, and bootstrap-check inspection/apply passthrough with existing approval gate.

## Users

- Primary user: Non-technical builder or support helper who wants a shorter way to invoke common Precode commands.
- Secondary user: Maintainer or AI coding agent checking package health without memorizing script paths.
- Excluded user: Automation expecting package publishing, update channels, package-manager behavior, release management, task approval, setup approval, or external mutation.

## Goals

- Goal 1: Make stable Precode commands easier to discover and invoke.
- Goal 2: Preserve exact underlying command visibility and exit codes.
- Goal 3: Keep all authority and approval boundaries in existing Markdown protocols and scripts.

## Non-Goals

- Not doing: PyPI/Homebrew/npm publishing, package update behavior, release channels, broad installer behavior, registry behavior, optional packs, external mutation, hidden command approval, hook installation, CI setup, owner-file adaptation, automatic rollback, task selection, transition approval, review acceptance, generated-evidence authority, or active-memory changes.
- Deferred: broader setup mutation, existing-repo adaptation, standalone `precode doctor`, provider integrations, command-wrapper skill behavior, optional packs, and release-channel semantics.
- Explicitly out of scope: Any workflow where `precode` replaces canonical scripts, approves commands, hides file mutation, or becomes required for normal repo-local use.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-013-FR01` | The CLI must expose `start`, `next`, `health`, `validate`, `check`, and `bootstrap-check` aliases. | P0 | Curated facade only. |
| `PRD-013-FR02` | Every alias must print the exact underlying command before running it. | P0 | No hidden command path. |
| `PRD-013-FR03` | The CLI must detect a PrecodeOS repo root or fail clearly. | P0 | Requires active-memory files and `scripts/next-step.py`. |
| `PRD-013-FR04` | The CLI must preserve underlying command exit codes. | P0 | Useful for local scripts and CI-like checks. |
| `PRD-013-FR05` | `bootstrap-check` passthrough must expose only curated setup flags and require `--approve-action` for `--apply-supervised-setup`. | P0 | Preserves existing setup apply gate. |
| `PRD-013-FR06` | Local packaging must define a `precode` console entrypoint without adding runtime dependencies. | P1 | Local editable install only. |
| `PRD-013-FR07` | Public docs, package inventory, Extension Protocol, Tool Execution Protocol, roadmap, roadmap journal, generated docs/PRD/roadmap surfaces, and maintainer changelog must be updated. | P1 | Required maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-013-SEC01` | The CLI must not handle secrets, credentials, provider dashboards, private customer data, or external systems. | P0 | Repo-local commands only. |
| `PRD-013-SEC02` | The CLI must not approve or perform task selection, transition approval, review acceptance, release approval, package updates, registry behavior, release-channel behavior, rollback automation, hook installation, CI changes, or external mutation. | P0 | Existing commands retain their own gates. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-013-NFR01` | The wrapper must use only the Python standard library. | P0 | No new runtime dependencies. |
| `PRD-013-NFR02` | Direct script use must work without installation. | P0 | `python3 scripts/precode_cli.py ...` remains valid. |
| `PRD-013-NFR03` | Existing canonical command paths must remain documented and usable. | P0 | CLI is optional. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-013-FR01` | Help shows only curated aliases. | `python3 scripts/precode_cli.py --help` | Confirm no broad command runner is exposed. | current workspace | command output |
| `PRD-013-FR02` | Dry run prints the exact underlying command. | `python3 scripts/precode_cli.py --dry-run next` | Confirm the output names `python3 scripts/next-step.py`. | current workspace | command output |
| `PRD-013-FR03` | CLI runs from a PrecodeOS repo and fails outside one. | source inspection plus command checks | Confirm root detection uses required Precode files. | current workspace | source review |
| `PRD-013-FR04` | Underlying exit codes are preserved. | run a successful alias and inspect exit code | Confirm no exception swallows failures. | current workspace | command output |
| `PRD-013-FR05` | Setup apply refuses missing approval IDs. | `python3 scripts/precode_cli.py bootstrap-check --source . --target /tmp --apply-supervised-setup` | Confirm parser refuses without `--approve-action`. | current workspace | command output |
| `PRD-013-FR06` | Local console script entrypoint exists with no runtime dependencies. | source inspection of `pyproject.toml` | Confirm no publish/update language. | package metadata | source review |
| `PRD-013-FR07` | Docs, generated surfaces, roadmap, and changelog are current. | docs, PRD HTML, roadmap HTML, and roadmap maintenance checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: unchanged.
- Command execution: wrapper prints and delegates to existing commands.
- Setup mutation: only existing supervised setup apply may mutate, and only with explicit `--approve-action` IDs.
- Generated evidence: remains evidence only.
- External systems: not touched.

### Human Approval Gates

- Approval required before setup apply, transition approval, cleanup, repair mutation, external mutation, release action, rollback, package update, hook installation, CI changes, or owner-file adaptation.
- Stop if wrapper output is treated as authority, task selection, implementation acceptance, or approval.

## Public Interface

- New direct command:
  - `python3 scripts/precode_cli.py --help`
- New local console script entrypoint after editable install:
  - `precode --help`
- Curated aliases:
  - `precode start`
  - `precode next`
  - `precode health`
  - `precode validate`
  - `precode check`
  - `precode bootstrap-check --source <precode-package-root> --target <target-project-root> [--preview-manifest] [--supervised-setup-plan] [--apply-supervised-setup --approve-action <SP-ID>]`

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `scripts/precode_cli.py` | Adds local wrapper over trusted commands. | Facade only; not command authority. |
| `pyproject.toml` | Adds local console script metadata. | No publishing, dependencies, update, or release-channel behavior. |
| Public docs and package inventory | Describe optional CLI and boundaries. | Canonical scripts and Markdown remain authoritative. |
| Extension and Tool Execution protocols | Record command-wrapper boundary. | No hidden approval, external mutation, or package-manager behavior. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/precode_cli.py --help`
- `python3 scripts/precode_cli.py --dry-run next`
- `python3 scripts/precode_cli.py health`
- `python3 scripts/precode_cli.py bootstrap-check --source . --target /tmp --apply-supervised-setup`
- `bash scripts/validate-memory.sh`
- `python3 scripts/version-check.py`
- `python3 scripts/file-inventory.py --check`
- `python3 scripts/public-repo-check.py`
- `python3 scripts/prd-html.py --check`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-maintenance.py`
- `python3 _maintainer/scripts/roadmap-maintenance.py --apply`
- `python3 _maintainer/scripts/roadmap-html.py --check`

## Open Questions

- None for this slice.
