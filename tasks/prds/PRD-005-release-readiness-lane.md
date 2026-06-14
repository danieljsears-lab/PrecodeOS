---
prd_id: PRD-005
status: approved
owner: user
risk_level: high
feature_link: Release Readiness / Shipping Lane
features_status: not compiled
related_prds: []
---

# PRD-005 -- Release Readiness / Shipping Lane
<!-- ANCHOR: prd-005-release-readiness-lane -->

> AUTHORITY: Destination shard for user-project release readiness guidance in PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, bead activation, deployment approval, release approval, provider configuration, external mutation, rollback execution, implementation acceptance, or generated evidence truth.
> LOAD_WHEN: Reviewing, implementing, or decomposing the user-project release-readiness lane for shipping, smoke evidence, rollback notes, and post-release review.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-005`
- Status: `approved`
- Owner: `user`
- Risk level: `high`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Release Readiness / Shipping Lane`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | existing verification protocols`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item 5, `Release Readiness / Shipping Lane`
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
- Stable facts:
  - Precode already requires recorded checks, manual verification when needed, explicit approval gates, and rollback or blocked escape notes for sensitive work.
  - Deployment, promotion, rollback, secret changes, migrations, dashboards, billing, auth, payments, and private data are sensitive surfaces.
  - GitHub status, browser notes, screenshots, and generated reports are review input until recorded, accepted, or promoted through the existing evidence path.
  - GitHub Releases remain a PrecodeOS package checkpoint path, not user-project release authority.
- Assumptions:
  - V1 should serve user projects first, not PrecodeOS package release management.
  - Protocol and template guidance are enough for V1.
- Conflicts or stale inputs:
  - Generic "ship" language can imply deployment automation; this PRD narrows the first lane to release-readiness evidence and approval gates only.
- Privacy or secrets redactions:
  - Release notes and evidence must not include secrets, tokens, private dashboard values, personal data samples, or production credentials.

## Problem

Precode is strong at planning, scoped implementation, checks, and review, but users still need a clearer stop-and-check lane before local confidence turns into user-facing risk. Without release-readiness guidance, an agent can treat "works locally" as "safe to ship" before deployment steps, rollback, smoke evidence, browser/manual checks, docs freshness, and post-release follow-up are visible.

## Destination

- Destination statement: PrecodeOS gives users a release-readiness lane that names the evidence, approvals, rollback or blocked escape, and follow-up needed before shipping user-project work.
- Definition of done:
  - Release Readiness Protocol exists.
  - Bead schema guidance names release-relevant beads and closeout expectations.
  - Verification and completion protocols point deployment and release-relevant work to the release-readiness lane.
  - GitHub protocol distinguishes PrecodeOS package release checkpoints from user-project release readiness.
  - User-facing docs provide copyable prompts for release readiness without authorizing deployment.
  - Package inventory lists the new protocol.
  - Generated public docs HTML is refreshed.
- First useful vertical slice: docs, protocol, PRD, and bead guidance only.

## Users

- Primary user: Non-technical builder deciding whether a completed project slice is safe enough to ship.
- Secondary user: AI coding agent or support helper preparing release evidence without mutating external systems.
- Excluded user: Maintainer or deploy bot expecting provider-specific deployment automation, release channels, rollback automation, dashboard mutation, or package-manager semantics.

## Goals

- Goal 1: Make shipping risk explicit before deployment or external mutation.
- Goal 2: Require smoke evidence, manual/browser verification, known uncertainty, and rollback or blocked escape before release approval.
- Goal 3: Preserve the user's authority over deployment, release, rollback, dashboards, secrets, and post-release decisions.

## Non-Goals

- Not doing: provider-specific deployment automation, release execution, rollback execution, dashboard updates, CI release gates, CLI commands, package-manager or release-channel semantics, GitHub mutation, new skill playbooks, or generated approval.
- Deferred: Release Readiness Skill, release-candidate evidence automation, provider-specific checklists, richer release evidence reports, and verification-evidence tooling.
- Explicitly out of scope: Any workflow that treats release-readiness output as permission to deploy, promote, roll back, merge, change secrets, migrate data, or mutate external systems.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-005-FR01` | Add a Release Readiness Protocol for user-project shipping decisions. | P0 | Protocol owns scope, evidence, approvals, and forbidden actions. |
| `PRD-005-FR02` | Define when a bead is release-relevant. | P0 | Includes deployment, production config, user-visible behavior, data/security/auth/payment risk, browser-facing flows, docs required for use, or external-service impact. |
| `PRD-005-FR03` | Define required release-readiness notes. | P0 | Changed behavior, affected users, checks, smoke test, browser/manual evidence, rollback or blocked escape, known uncertainty, docs freshness, post-release follow-up. |
| `PRD-005-FR04` | Add release-relevant bead guidance to the bead schema. | P0 | Keep one primary authority and existing closeout/review rules. |
| `PRD-005-FR05` | Point verification and completion protocols to release readiness without weakening sensitive-surface gates. | P0 | Deployment still requires explicit approval. |
| `PRD-005-FR06` | Clarify GitHub Releases are PrecodeOS package checkpoints, not user-project release authority. | P0 | Avoids accidental GitHub mutation or package-release confusion. |
| `PRD-005-FR07` | Add user-facing prompts in beginner docs. | P0 | Prompts prepare evidence and approval questions only. |
| `PRD-005-FR08` | Update package inventory and generated public docs. | P0 | Markdown remains canonical; HTML is generated reading surface. |

## Risk And Permission Model

- Approval required before deployment, promotion, rollback, merge, migration, dashboard update, secret change, billing/auth/payment/private-data change, external-service mutation, or production configuration change.
- Stop if release target, affected users, smoke path, manual/browser verification, rollback or blocked escape, approval owner, or post-release follow-up is unclear.
- Network needs: none for V1 docs/protocol work.
- Dependency changes: none.
- External systems touched: none.

## Module / Interface Candidates

- `tasks/reference/RELEASE-READINESS-PROTOCOL.md` owns the release-readiness lane.
- `tasks/beads/BEAD-SCHEMA.md` owns release-relevant bead guidance.
- User docs own copyable prompts for asking an agent to prepare release readiness.

## Agent Context Contract

- Primary authority file: `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
- Files or folders out of scope:
  - target app code
  - provider configuration
  - dashboards
  - secrets or environment files
  - GitHub mutation
  - deployment scripts
  - generated evidence except generated docs HTML
- Required checks:
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Confirm release-readiness language prepares evidence and approvals only, and does not authorize deployment, rollback, dashboard mutation, secret changes, GitHub mutation, or release-channel behavior.
- Forbidden assumptions:
  - Release readiness is release approval.
  - A smoke test replaces manual approval.
  - Browser notes, screenshots, GitHub status, or generated reports are proof unless recorded through existing evidence paths.
  - PrecodeOS package GitHub Releases define user-project release behavior.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B005-release-readiness-lane` | `PRD-005-FR01` through `PRD-005-FR08` | Release-readiness PRD/protocol, bead guidance, user prompts, inventory, changelog, roadmap cleanup, and generated docs are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | static validation plus manual boundary review |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a future release-candidate evidence helper compile release-readiness notes from closeout? | Follow-up roadmap scope | no |
| Should provider-specific release checklists exist after V1? | Follow-up automation scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of roadmap rank #5 as a user-project shipping-readiness lane, explicitly excluding provider-specific automation, deployment, promotion, rollback, dashboard mutation, CI release gates, CLI commands, package-manager semantics, release-channel semantics, and Release Readiness Skill behavior.
