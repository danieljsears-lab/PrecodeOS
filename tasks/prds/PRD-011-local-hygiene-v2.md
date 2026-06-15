---
prd_id: PRD-011
status: approved
owner: user
risk_level: medium
feature_link: Local Hygiene v2
features_status: not compiled
related_prds: []
---

# PRD-011 -- Local Hygiene v2 Preview Hardening
<!-- ANCHOR: prd-011-local-hygiene-v2 -->

> AUTHORITY: Destination shard for Local Hygiene v2 preview classification, protected generated evidence handling, and explicit no-mutation cleanup boundaries.
> NOT_AUTHORITY: Active memory, task selection, bead activation, cleanup approval, archive approval, delete approval, file mutation, evidence rewrite approval, generated report truth, implementation acceptance, or future cleanup-apply permission.
> LOAD_WHEN: Reviewing, implementing, or decomposing Local Hygiene preview hardening before any cleanup mutation is proposed.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-011`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Local Hygiene v2`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped local hygiene evidence`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Local Hygiene v2`
  - `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md`
  - `scripts/local-hygiene-check.py`
  - `scripts/local-hygiene-dry-run.py`
  - `scripts/os_compiler.py`
- Stable facts:
  - Local Hygiene v1 is advisory and non-mutating.
  - Current local hygiene output reports `logs/os-checkpoints/*` as unexpected even though OS checkpoints are generated evidence.
  - Cleanup is risky because truth, evidence, generated reports, caches, and clutter can look similar.
- Assumptions:
  - V2 should harden preview and protection rules before adding any mutating cleanup path.
- Candidate requirements:
  - Stable preview row classifications.
  - Protected generated evidence handling for OS checkpoints.
  - Deterministic self-test coverage.
  - Public docs, inventory, roadmap, and maintainer changelog follow-through.
- Candidate non-goals:
  - No delete, archive, move, compact, or rewrite behavior.
  - No cleanup approval command.
  - No package-manager, CLI wrapper, or doctor dashboard behavior.

## Problem

Local clutter, bulky logs, caches, and generated outputs can confuse builders and agents. The current Local Hygiene preview is non-destructive, but its classifications are too coarse and can mislabel newer generated evidence families such as OS checkpoints as generic unexpected clutter.

## User Moment

- Before: A builder or agent sees generated files under `logs/` and cannot tell whether they are cleanup candidates, protected evidence, or review-only surprises.
- After: Local Hygiene reports stable preview classifications and protects known generated evidence families without mutating files.
- Why now: OS checkpoints expanded generated evidence under `logs/`, exposing a concrete classification gap.

## Destination

- Destination statement: Local Hygiene v2 gives users a safer, clearer preview of local clutter without granting cleanup mutation.
- Definition of done: Preview rows distinguish candidates, protected evidence, unexpected review items, and not-candidates; `logs/os-checkpoints/*` is protected generated evidence; docs and roadmap history are current.
- First useful vertical slice: Preview hardening only.

## Users

- Primary user: Non-technical builder or support helper trying to understand local clutter.
- Secondary user: Maintainer or coding agent reviewing generated evidence and cache/build output.
- Excluded user: Automation expecting Local Hygiene to delete, archive, compact, rewrite, or approve cleanup.

## Goals

- Goal 1: Prevent generated evidence from being mistaken for cleanup clutter.
- Goal 2: Make Local Hygiene preview rows stable enough for human review and future approval-gated cleanup planning.
- Goal 3: Preserve the non-mutating cleanup boundary.

## Non-Goals

- Not doing: delete command, archive command, compact command, cleanup apply mode, generated-evidence rewrite, approval automation, OS checkpoint cleanup, package-manager semantics, `precode doctor`, or installable CLI behavior.
- Deferred: A separate cleanup-apply PRD or semantic-change proposal may define explicit approval, rollback, archive location, and recovery semantics after preview hardening proves trustworthy.
- Explicitly out of scope: External mutation, tool/session cache clearing, auth/session state cleanup, private maintainer file cleanup, and app-runtime cleanup.

## Alternatives Considered

| Option | Why rejected or deferred | Decision owner |
|---|---|---|
| Add delete/archive now | Too much destructive-action risk before preview classifications are trustworthy. | maintainer |
| Keep v1 unchanged | Leaves OS checkpoints mislabeled as unexpected clutter and keeps preview rows too coarse. | maintainer |
| Add a broader doctor dashboard | Roadmap defers doctor aggregation until existing warnings are quiet and useful. | maintainer |

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-011-FR01` | Local Hygiene must classify preview rows as `candidate`, `protected`, `unexpected_review`, or `not_candidate`. | P0 | Stable JSON fields required. |
| `PRD-011-FR02` | Preview rows must include `candidate_id`, `classification`, `action`, `path`, `mutates_now: false`, `approval_required`, reason fields, and rollback notes. | P0 | Generated evidence only. |
| `PRD-011-FR03` | `logs/os-checkpoints/*` must be treated as protected generated evidence, not unexpected clutter. | P0 | OS checkpoints remain evidence. |
| `PRD-011-FR04` | Local Hygiene commands must keep stable public names and remain non-mutating. | P0 | No cleanup/apply flag in this slice. |
| `PRD-011-FR05` | `scripts/local-hygiene-dry-run.py --self-test` must cover representative v2 classifications. | P1 | Fast deterministic check. |
| `PRD-011-FR06` | Public docs, package inventory, roadmap, roadmap journal, generated surfaces, and maintainer changelog must be updated. | P1 | Required maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-011-SEC01` | Local Hygiene must not clear tool/session state, secrets, credentials, auth caches, or private local state. | P0 | Preserve existing protection rule. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-011-NFR01` | The self-test must run without network access, external services, or destructive filesystem mutation. | P0 | Temporary fixtures only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-011-FR01` | Preview rows expose the four v2 classifications. | `python3 scripts/local-hygiene-dry-run.py --self-test` | Inspect generated preview JSON shape. | Synthetic fixture summary | check output |
| `PRD-011-FR02` | Preview rows include stable fields and no mutation. | `python3 scripts/local-hygiene-dry-run.py --self-test` | Inspect `logs/local-hygiene-preview.md`. | Synthetic fixture summary | generated preview |
| `PRD-011-FR03` | OS checkpoint files are protected and not unexpected. | `python3 scripts/local-hygiene-dry-run.py --self-test` and `python3 scripts/local-hygiene-check.py` | Confirm current repo no longer reports checkpoint files as unexpected clutter. | temp `logs/os-checkpoints` fixture | check output |
| `PRD-011-FR04` | Public command names stay stable and non-mutating. | `python3 scripts/local-hygiene-check.py` and `python3 scripts/local-hygiene-dry-run.py` | Confirm no cleanup/apply flag was added. | current workspace | command output |
| `PRD-011-FR06` | Docs and generated reading surfaces are fresh. | docs, PRD HTML, roadmap HTML, inventory, and version checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Destructive actions: explicitly out of scope.
- Generated evidence: protected from cleanup mutation.
- Tool/session state: never cleared by Local Hygiene.
- Private local state: not a cleanup target.

### Human Approval Gates

- Approval required before any future delete, archive, move, compact, or rewrite behavior.
- Stop if a proposed cleanup path cannot name protected evidence, rollback or archive location, validation, and approval requirements.
- Escalate when cleanup would affect active memory, PRDs, beads, owner files, reviewed memory, append-only ledgers, current/unaccepted bead evidence, secrets, auth/session state, or private local material.

## Public Interface

- Existing command preserved: `python3 scripts/local-hygiene-check.py`
- Existing command preserved: `python3 scripts/local-hygiene-dry-run.py`
- Test command added: `python3 scripts/local-hygiene-dry-run.py --self-test`
- Generated preview files preserved:
  - `logs/local-hygiene-preview.json`
  - `logs/local-hygiene-preview.md`

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` | Update v2 preview classification and protection rules. | Protocol owns behavior. |
| `scripts/os_compiler.py` | Classify OS checkpoints as protected generated evidence and emit v2 preview rows. | Generated evidence only. |
| `scripts/local-hygiene-dry-run.py` | Add deterministic self-test. | No cleanup mutation. |
| Public docs and package inventory | Update v1-only wording and command descriptions. | Markdown remains authority over generated HTML. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/local-hygiene-dry-run.py --self-test`
- `python3 scripts/local-hygiene-check.py`
- `python3 scripts/local-hygiene-dry-run.py`
- `python3 scripts/version-check.py`
- `python3 scripts/file-inventory.py --check`
- `python3 scripts/prd-html.py --check`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`

## Rollback Or Reversal Path

Revert PRD-011, restore Local Hygiene protocol v1 wording, remove `--self-test`, remove v2 preview fields and checkpoint-family classification from `scripts/os_compiler.py`, regenerate docs/PRD/roadmap HTML, and record reversal in the maintainer changelog. Do not delete existing generated evidence during rollback.

## Bead Proposal

| Bead ID | Requirement IDs | Scope | Delegation mode | Test strategy | Review context | Primary authority | Checks |
|---|---|---|---|---|---|---|---|
| `B011-local-hygiene-v2-preview-hardening` | `PRD-011-FR01` through `PRD-011-FR06`, `PRD-011-SEC01`, `PRD-011-NFR01` | PRD shard, protocol, compiler classification, dry-run self-test, docs/inventory updates, changelog, roadmap history, generated PRD/docs/roadmap HTML, and validation. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/LOCAL-HYGIENE-PROTOCOL.md` | Local hygiene self-test plus package validation and manual boundary review |

## Approval Notes

- Approval notes: User approved implementation of Local Hygiene v2 Preview Hardening as a non-mutating preview/protection hardening slice, explicitly excluding cleanup apply, delete, archive, move, compact, rewrite, package-manager behavior, CLI wrapper behavior, doctor dashboard behavior, external mutation, and generated-evidence authority.
