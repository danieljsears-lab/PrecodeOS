---
prd_id: PRD-012
status: approved
owner: user
risk_level: medium
feature_link: Precode Doctor Dashboard
features_status: not compiled
related_prds: []
---

# PRD-012 -- Precode Doctor Dashboard
<!-- ANCHOR: prd-012-precode-doctor-dashboard -->

> AUTHORITY: Destination shard for the generated Precode Doctor Dashboard inside OS Health.
> NOT_AUTHORITY: Active memory, task selection, bead activation, transition approval, command approval, generated report truth, implementation acceptance, `precode doctor` command behavior, installable CLI behavior, wrapper behavior, external mutation, package-manager behavior, or release-channel behavior.
> LOAD_WHEN: Reviewing, implementing, or decomposing the generated diagnostic dashboard inside `OS-HEALTH.md` and `logs/os-health.json`.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-15

## State

- ID: `PRD-012`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-15`

## Feature Link

- Feature: `Precode Doctor Dashboard`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | generated health evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Precode Doctor Dashboard`
  - `scripts/os-health.py`
  - `scripts/os_compiler.py`
  - `scripts/next-step.py`
  - `scripts/loop-health.py`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Stable facts:
  - OS Health already compiles state, warning sources, generated sidecars, and human-readable health output.
  - `next-step.py` owns the generated next human decision.
  - Generated reports are evidence only and must not select tasks, approve transitions, or replace owner files.
- Assumptions:
  - "Full dashboard now" means a generated diagnostic summary inside health reporting, not a visual app dashboard or new command.
  - The first implementation should compose existing compiled state instead of re-running independent checks.
- Conflicts or stale inputs:
  - The maintainer roadmap previously ranked Doctor as P3 and deferred `precode doctor` until diagnostics were quiet enough. This PRD intentionally pulls forward the dashboard as a health extension while keeping the standalone command and CLI deferred.

## Problem

As Precode's advisory checks grow, users and agents can see many warnings without knowing which source owns each warning, what repair path is shortest, or whether the warning is competing with the canonical next-step router.

## User Moment

- Before: A builder reads OS Health or several generated reports and cannot tell which warning matters most or which command owns the repair path.
- After: OS Health includes a Doctor Dashboard that summarizes the highest-impact diagnostic sources and points back to the owner command and protocol.
- Why now: The main loop now has enough warning sources that a compact diagnostic dashboard can clarify health without adding a second router.

## Destination

- Destination statement: Precode Doctor Dashboard explains existing warning sources inside OS Health while preserving `next-step.py` as the next-decision owner.
- Definition of done:
  - `OS-HEALTH.md` includes a `Doctor Dashboard` section.
  - `logs/os-health.json` includes a `doctor_dashboard` payload.
  - Dashboard rows include source, status/severity, why it matters, owner command/protocol, shortest repair path, and `scripts/next-step.py` as decision owner.
  - Public docs, package inventory, Extension Protocol, generated docs/PRD surfaces, roadmap history, roadmap journal, and maintainer changelog are current.
- First useful vertical slice: generated health-report dashboard only.

## Users

- Primary user: Non-technical builder trying to understand why Precode is warning.
- Secondary user: Maintainer, support helper, or AI coding agent diagnosing package health without expanding authority.
- Excluded user: Automation expecting command approval, task selection, repair automation, a visual dashboard, installable CLI, `precode doctor`, external mutation, or package-manager behavior.

## Goals

- Goal 1: Explain which diagnostic source currently matters most.
- Goal 2: Make owner commands and protocols visible without duplicating all protocol rules.
- Goal 3: Preserve generated-evidence and router authority boundaries.

## Non-Goals

- Not doing: standalone `precode doctor` command, shell wrapper, installable `precode` CLI, visual dashboard app, task selection, transition approval, command approval, repair automation, cleanup mutation, external status integration, package-manager behavior, release-channel behavior, or new active-memory file.
- Deferred: standalone doctor command, CLI wrapper, richer visual review surface, external diagnostic integrations, and strict router JSON-shape contracts.
- Explicitly out of scope: Any workflow that treats Doctor Dashboard output as proof of done, approval to mutate, or authority over Markdown PRDs, active beads, owner files, or human review.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-012-FR01` | OS Health must include a Doctor Dashboard section. | P0 | Human-readable generated report. |
| `PRD-012-FR02` | `logs/os-health.json` must include `doctor_dashboard`. | P0 | Machine-readable generated evidence. |
| `PRD-012-FR03` | Dashboard rows must include source, status/severity, why it matters, owner command/protocol, shortest repair path, warnings, and `scripts/next-step.py` as decision owner. | P0 | Do not create a second router. |
| `PRD-012-FR04` | Dashboard input must compose existing compiled state only. | P0 | No independent app runtime, external calls, or mutating checks. |
| `PRD-012-FR05` | Deterministic scenario coverage must verify dashboard severity and generated-evidence boundaries. | P1 | Use existing clarity harness unless a separate self-test is needed. |
| `PRD-012-FR06` | Public docs, package inventory, Extension Protocol, roadmap, roadmap journal, generated docs/PRD/roadmap surfaces, and maintainer changelog must be updated. | P1 | Required maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-012-SEC01` | Doctor Dashboard must not read secrets, credentials, provider dashboards, private customer data, or external systems. | P0 | Existing compiled local state only. |
| `PRD-012-SEC02` | Doctor Dashboard must not approve or perform file mutation, command execution, external mutation, transition approval, release approval, rollback, cleanup, or package update behavior. | P0 | Generated evidence only. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-012-NFR01` | Dashboard generation must run as part of `python3 scripts/os-health.py` without network access. | P0 | Repo-local only. |
| `PRD-012-NFR02` | Dashboard output must be concise enough to scan before the detailed OS Health sections. | P1 | Top summary plus table rows. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-012-FR01` | `OS-HEALTH.md` contains `## Doctor Dashboard`. | `python3 scripts/os-health.py` | Inspect generated report. | current workspace | `OS-HEALTH.md` |
| `PRD-012-FR02` | `logs/os-health.json` has `doctor_dashboard`. | `python3 scripts/os-health.py` | Inspect JSON shape. | current workspace | `logs/os-health.json` |
| `PRD-012-FR03` | Dashboard rows expose source, severity, owner, repair path, and next-step owner. | `python3 scripts/clarity-scenario-check.py` | Inspect one generated row. | synthetic clarity scenarios | check output |
| `PRD-012-FR04` | Dashboard composes compiled state and adds no public command. | `python3 scripts/version-check.py` | Confirm no `precode doctor` script or CLI wrapper was added. | current workspace | command output |
| `PRD-012-FR05` | Clear, scope-drift, and transition-review scenarios classify deterministically. | `python3 scripts/clarity-scenario-check.py` | Boundary review. | in-memory fixtures | check output |
| `PRD-012-FR06` | Docs, generated surfaces, roadmap, and changelog are current. | docs, PRD HTML, roadmap HTML, and roadmap maintenance checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: unchanged.
- Generated evidence: dashboard remains evidence only.
- Router authority: `scripts/next-step.py` remains the next-decision owner.
- External systems: not touched.
- File mutation: not performed by dashboard output.

### Human Approval Gates

- Approval required before any transition, cleanup, repair mutation, external mutation, release action, rollback, package update, or standalone command-wrapper work.
- Stop if dashboard output is treated as a task selector, acceptance decision, or approval surface.

## Public Interface

- Existing command preserved: `python3 scripts/os-health.py`
- Generated Markdown extended:
  - `OS-HEALTH.md#doctor-dashboard`
- Generated JSON extended:
  - `logs/os-health.json["doctor_dashboard"]`

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `scripts/precode_doctor.py` | Internal dashboard payload and Markdown helpers. | Imported by health reporting; no standalone command. |
| `scripts/os_compiler.py` | Adds `doctor_dashboard` to compiled state. | Generated evidence only. |
| `scripts/os-health.py` | Renders Doctor Dashboard in OS Health. | Does not choose tasks or approve work. |
| `scripts/clarity-scenario-check.py` | Adds deterministic dashboard classification fixtures. | Regression check only. |
| Public docs and package inventory | Describe the dashboard and boundaries. | Markdown remains canonical. |
| Extension Protocol | Reclassifies dashboard as a generated report extension while preserving deferred wrapper rule. | No CLI or wrapper authority. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/clarity-scenario-check.py`
- `python3 scripts/os-health.py`
- `python3 scripts/loop-health.py --json`
- `python3 scripts/version-check.py`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`
- `python3 _maintainer/scripts/roadmap-maintenance.py`
- `python3 _maintainer/scripts/roadmap-maintenance.py --apply` after implemented-candidate entry is added.

## Open Questions

- None for this slice.
