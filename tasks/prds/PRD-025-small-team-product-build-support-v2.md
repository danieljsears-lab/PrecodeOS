---
prd_id: PRD-025
status: approved
owner: user
risk_level: medium
feature_link: Small Team Product Build Support V2 Preview
features_status: not compiled
related_prds:
  - PRD-019
---

# PRD-025 -- Small Team Product Build Support V2 Preview
<!-- ANCHOR: prd-025-small-team-product-build-support-v2 -->

> AUTHORITY: Public requirements for the Small Team Collaboration Lane V2 read-only preview, scenario harness, team workspace state preview, owner-file conflict preview, merge/re-entry review packet, GitHub evidence aggregation preview, and team assignment prompts.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, merge approval, release approval, GitHub mutation, external mutation, project-management behavior, module behavior, registry behavior, runtime-toggle behavior, optional-pack behavior, installer behavior, update-channel behavior, package-manager behavior, or implementation status.
> LOAD_WHEN: Implementing or reviewing Small Team Product Build Support V2 Preview, `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`, or `scripts/team-collaboration-check.py`.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## State

- ID: `PRD-025`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-23`

## Feature Link

- Feature: `Small Team Product Build Support V2 Preview`
- `FEATURES.md` status: `not compiled`
- Originating maintainer roadmap candidate: `#6`

## Source Inputs

- Source type: `maintainer roadmap candidate | approved implementation plan | shipped Small Team Collaboration Lane v1`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `Small Team Product Build Support`
  - `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`
  - `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `scripts/team-collaboration-check.py`
- Stable facts:
  - Small Team Collaboration Lane v1 is built in but explicit, not default-active.
  - Team work still requires one active bead per checkout.
  - Branches, worktrees, pull requests, reviews, checks, teammate notes, and generated handoff packets are evidence until reviewed and promoted.
- Assumptions:
  - Full V2 Preview means read-only local and optional GitHub evidence previews, not merge automation or project management.
  - Deterministic scenario fixtures must ship in the same slice as broader preview support.
- Conflicts or stale inputs:
  - The roadmap recommended the scenario harness before script-level support. This PRD intentionally takes the broader V2 slice, so the harness is a required acceptance condition.
- Privacy or secrets redactions:
  - The preview must not require secrets, credentials, provider dashboards, production configuration, private issue content, or sensitive personal data.

## Problem

Small teams can coordinate Precode work only if teammate branches, worktrees, bead scope, owner-file impacts, checks, pull requests, and re-entry risks stay visible without becoming authority.

Without a read-only preview, coordinators may rely on chat history, PR status, generated reports, or teammate notes as if they can choose work, approve merge, or replace owner files.

## User Moment

- Before: A 2-5 person team has branches or worktrees in motion and cannot quickly tell whether a teammate can continue, re-enter, or merge safely.
- After: The coordinator can run a local preview, optionally add read-only GitHub evidence, and review a merge/re-entry packet without changing tasks, branches, GitHub, owner files, or active memory.
- Why now: The v1 lane, GitHub evidence boundaries, decomposition language, and review lanes are already documented enough to support advisory preview fixtures.

## Destination

- Destination statement: Precode provides a read-only Small Team Collaboration Lane V2 preview that helps coordinators inspect team state, owner-file conflicts, re-entry risk, and GitHub evidence while preserving one active bead per checkout and human review.
- Definition of done:
  - `scripts/team-collaboration-check.py` provides local preview, optional `--github`, `--integration-branch`, and `--self-test`.
  - `scripts/os_compiler.py` exposes a `team_collaboration` payload for OS Health sidecars without routing authority.
  - Scenario fixtures cover coordinator invocation, teammate startup, branch/worktree isolation, PR conflict review, stale branch re-entry, and GitHub evidence demotion.
  - Protocols, prompt patterns, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, generated docs, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: read-only preview script, compiler payload, fixtures, protocol/docs/prompt propagation, and generated reading surfaces.

## Goals

- Goal 1: Make branch/worktree, active bead, files in play, owner-file impact, and re-entry risks visible before coordinator decisions.
- Goal 2: Treat optional GitHub PR, review, and check status as evidence only.
- Goal 3: Standardize the coordinator's merge/re-entry review packet and teammate assignment packet.
- Goal 4: Preserve single-builder defaults and one active bead per checkout.

## Non-Goals

- Not doing: branch creation, worktree creation, push, rebase, merge, PR creation, PR approval, issue mutation, workflow rerun, deployment, release, task selection, PRD approval, bead activation, acceptance approval, owner-file rewrite, generated proof, project board, dashboard, module, optional pack, registry, runtime toggle, installer, update channel, package-manager behavior, or `precode team` facade.
- Deferred: validator enforcement, compiler warnings that block work, automatic merge readiness decisions, GitHub mutation support, multi-repo team orchestration, and project-management views.
- Explicitly out of scope: treating generated preview JSON, GitHub status, teammate notes, or handoff packets as authority.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-025-FR01` | Add `scripts/team-collaboration-check.py` as a read-only advisory preview script. | P0 | Default local preview writes nothing. |
| `PRD-025-FR02` | Script output must include current branch/worktree, integration branch, active bead, one-active-bead status, files in play, changed paths, owner-file impacts, re-entry risks, merge packet fields, assignment packet fields, forbidden uses, and generated-report warning. | P0 | JSON output. |
| `PRD-025-FR03` | Add `--github` optional read-only aggregation through `gh`; missing CLI/auth/network/config must be `not_configured` or `warning`, not guessed. | P0 | No GitHub mutation. |
| `PRD-025-FR04` | Add `--integration-branch <branch>` and otherwise detect origin HEAD or upstream when available. | P1 | Report unavailable comparisons visibly. |
| `PRD-025-FR05` | Add `--self-test` deterministic fixtures for coordinator invocation, teammate startup, isolated parallel bead, PR conflict review, stale branch re-entry, and GitHub evidence demotion. | P0 | Scenario harness must pass. |
| `PRD-025-FR06` | Expose a local `team_collaboration` payload from `scripts/os_compiler.py` and OS Health sidecars. | P1 | Advisory only; no `next-step.py` routing. |
| `PRD-025-FR07` | Update protocols, prompts, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, and generated surfaces. | P1 | Package follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-025-SEC01` | The preview must not mutate files, branches, worktrees, GitHub resources, workflows, releases, deployments, external systems, secrets, or dashboards. | P0 | Read-only by design. |
| `PRD-025-SEC02` | GitHub evidence must not include secrets, tokens, credentials, private dashboard data, or production configuration. | P0 | Use `gh` status metadata only. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-025-FR01` | Local preview prints advisory JSON and writes no files. | `python3 scripts/team-collaboration-check.py` | Inspect output. | Current repo | command output |
| `PRD-025-FR03` | GitHub preview is read-only and reports unavailable config visibly. | `python3 scripts/team-collaboration-check.py --github` when appropriate | Inspect output. | Optional `gh` auth | command output |
| `PRD-025-FR05` | Scenario fixtures protect six team contracts. | `python3 scripts/team-collaboration-check.py --self-test` | Review fixture failures if any. | Markdown source | command output |
| `PRD-025-FR06` | OS Health payload includes `team_collaboration`. | `python3 scripts/clarity-scenario-check.py` | Inspect OS Health after generation. | Compiler payload | generated sidecar |
| `PRD-025-FR07` | Docs, protocols, inventory, roadmap, changelog, and generated surfaces are current. | inventory/docs/PRD/roadmap checks | Read changed docs. | Markdown docs | generated surfaces |

## Risk And Permission Model

- Approval required before any file edit, owner-file promotion, PRD amendment, bead creation or activation, branch/worktree mutation, GitHub mutation, merge, review acceptance, release, deployment, external mutation, or sensitive-surface action.
- Stop if the coordinator or product decision owner is missing, team agreement is absent from shared authority, active bead state is unclear, multiple active beads are requested in one checkout, owner-file conflicts lack a plan, GitHub status is treated as authority, or the work requires mutation.
- Network needs: none by default; optional `--github` may read GitHub through authenticated `gh`.
- Dependency changes: none.
- Generated reports added: `logs/team-collaboration-preview.json` through OS Health sidecar generation.

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-025-small-team-product-build-support-v2.md`
- Owner protocol: `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-OS-README.md`
  - `docs/PRECODE-ARCHITECTURE-OVERVIEW.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/team-collaboration-check.py`
  - `scripts/os_compiler.py`
  - `scripts/os-health.py`
  - `scripts/precode_outputs.py`
  - `scripts/clarity-scenario-check.py`
  - `tasks/prds-html/`
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - `AGENT.md`
  - `DECISIONS.md`
  - `tasks/todo.md`
  - target app code
  - `scripts/precode_cli.py`
  - branch/worktree mutation
  - GitHub mutation
  - external systems
- Required checks:
  - `python3 scripts/team-collaboration-check.py --self-test`
  - `python3 scripts/clarity-scenario-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/public-repo-check.py`
  - `python3 scripts/prd-html.py --check`
  - `python3 scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
  - `bash scripts/validate-memory.sh`
