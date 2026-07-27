---
prd_id: PRD-032
status: approved
owner: Dan Sears / Recode
created: 2026-06-24
risk_level: medium
feature_link: GitHub Collaboration Hub
features_status: not compiled
related_prds:
  - PRD-025
  - PRD-028
last_updated: 2026-07-27
---

# PRD-032 -- GitHub Collaboration Hub
<!-- ANCHOR: prd-032-github-collaboration-hub -->

> AUTHORITY: Public requirements for GitHub feedback intake, package-bug intake, contribution routing, issue-template boundaries, and GitHub source-intake promotion rules for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, roadmap approval, PRD approval, bead activation, implementation acceptance, merge approval, package release approval, contributor governance, GitHub mutation, project-board authority, support-bot behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Opening, triaging, importing, or reviewing public GitHub feedback issues, package-bug issues, issue templates, or GitHub Collaboration Hub behavior.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-07-27

## State

- ID: `PRD-032`
- Status: `approved`
- Owner: Dan Sears / Recode
- Risk level: `medium`
- Last updated: `2026-07-27`

## Feature Link

- Feature: GitHub Collaboration Hub
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-025`, `PRD-028`

## Source Inputs

- Source type: maintainer roadmap evidence and public feedback/support friction
- Source references: GitHub issue-template needs, Local Source Intake, contribution and package-bug intake boundaries
- Stable facts: GitHub Issues, labels, comments, pull requests, reviews, checks, and boards are external evidence until reviewed and promoted.
- Assumptions: narrow public issue intake can expose adoption friction without creating issue-driven roadmap authority.
- Privacy or secrets redactions: issue templates must warn users not to include secrets, credentials, or private dashboard data.

## Alignment / Grilling Summary

- Alignment method: maintainer roadmap planning
- Shared design concept: open narrow GitHub intake while keeping Precode owner files and maintainer review authoritative.
- Key decisions reached: no GitHub automation, bot behavior, project-board authority, registry, or package-manager behavior.
- Remaining implementation-changing questions: none for the approved v1 slice.

## Domain Language

| Term | Status | Plain-English meaning | Aliases | Avoid/confusing terms | UI/code/test examples | Source pointer |
|---|---|---|---|---|---|---|
| GitHub Collaboration Hub | introduced | Public intake and routing surface for feedback and package bugs. | GitHub intake | project management system, support bot | issue templates | This PRD |
| Package bug | introduced | A bug or mismatch in PrecodeOS package docs, scripts, protocols, generated surfaces, setup helpers, CI, or GitHub helpers. | package issue | app bug | package-bug issue template | This PRD |

## PRFAQ-Lite

- Press-release claim: PrecodeOS can accept public feedback without turning GitHub into the operating system.
- Customer problem: adoption friction and package bugs need a narrow public intake path.
- Customer FAQ: Do issues choose work? No; they are source evidence until reviewed and promoted.
- Internal FAQ: Does this mutate GitHub automatically? No; external mutation requires explicit approval.
- Appetite: issue templates, source-intake guidance, and public boundary wording.
- Kill or pause criteria: stop if GitHub becomes roadmap authority, support-bot behavior, automatic mutation, or merge/release approval.

## Summary

PrecodeOS should accept public GitHub feedback and package-bug intake without letting GitHub become a second operating system.

The GitHub Collaboration Hub opens narrow intake for adoption friction and package bugs. Issues, labels, comments, pull requests, reviews, checks, and project boards remain external evidence until reviewed and promoted into the correct Precode owner file.

## Problem

PrecodeOS now has enough release evidence, package trust guidance, and read-only GitHub intake support to accept public feedback and package-bug reports. Keeping Issues closed or unavailable hides adoption friction, but opening broad collaboration too early can create issue-driven roadmap pressure, hidden task authority, and support expectations the package does not yet own.

## Goals

- Open a narrow GitHub issue intake path for adoption feedback and package bugs.
- Keep GitHub Issues, labels, comments, pull requests, reviews, checks, and boards as evidence only.
- Route reviewed findings through Local Source Intake, PRD amendment, `DECISIONS.md`, protocols, package docs, or candidate beads.
- Preserve maintainer authority, contribution boundaries, and explicit external-mutation approval gates.
- Avoid project-management, support-bot, registry, optional-pack, installer, update-channel, or package-manager behavior.

## Non-Goals

- No issue-driven roadmap authority.
- No project board as authority or active project-management surface.
- No automatic issue creation, labeling, assignment, commenting, closing, or synchronization.
- No GitHub workflow, bot, labeler, or project-board automation.
- No contributor governance, maintainer status, trademark permission, merge approval, package release approval, review acceptance, or implementation acceptance.
- No new active-memory file, command wrapper, registry, optional pack, module, runtime toggle, installer, update channel, or package-manager behavior.

## User Moment

- Before: users can have public package feedback but no narrow intake path.
- After: users can file feedback or package-bug evidence with clear redaction and promotion boundaries.
- Why now: PrecodeOS has enough public package surface to accept bounded feedback.

## Destination

- Destination statement: PrecodeOS provides narrow GitHub source-intake surfaces while preserving maintainer and owner-file authority.
- Definition of done: issue templates, protocol/docs/prompt routing, validation, generated surfaces, and maintainer history are updated.
- First useful vertical slice: feedback and package-bug issue templates plus evidence-only routing.

## Product Constitution Fit

- `PRODUCT.md` loaded: not needed
- Product promise fit: supports evidence-backed improvement without task drift.
- User and job fit: helps adopters report friction and package defects.
- Strategy and non-goal fit: avoids project-management, support-bot, registry, and package-manager behavior.
- Current bet or success signal affected: package feedback loop.
- Product constitution update needed: no

## Users

- Primary user: PrecodeOS adopter filing feedback or package-bug evidence.
- Secondary user: maintainer or contributor reviewing source evidence.
- Excluded user: anyone expecting issue-driven task selection, automatic support, GitHub automation, merge approval, or release approval.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-032-FR01` | Add public GitHub issue templates for feedback and package bugs. | P0 | Blank issues disabled. |
| `PRD-032-FR02` | Feedback intake must cover adoption friction, confusing docs, setup friction, and workflow questions. | P0 | Evidence only. |
| `PRD-032-FR03` | Package-bug intake must cover package docs, scripts, protocols, generated-surface expectations, setup/copy helpers, CI, and GitHub helper behavior. | P0 | Not app bug support. |
| `PRD-032-FR04` | Issue templates must ask for facts, context or reproduction, expected behavior, checks tried, and sensitive-data redaction. | P0 | No secrets or private dashboard data. |
| `PRD-032-FR05` | GitHub Integration, Local Source Intake, Tool Execution, Prompt Patterns, public docs, governance, contributing policy, and package inventory must route issues as source evidence only. | P0 | No hidden authority. |
| `PRD-032-FR06` | `scripts/import-github-sources.py --self-test` must cover feedback issue, package-bug issue, pull-request source intake, and evidence-only promotion wording. | P1 | Deterministic, no network. |
| `PRD-032-FR07` | `scripts/clarity-scenario-check.py` must guard collaboration-hub wording across templates, protocols, policy, and prompts. | P1 | Contract coverage. |
| `PRD-032-FR08` | Maintainer changelog, roadmap, roadmap journal, and generated reading surfaces must be refreshed after implementation. | P1 | Maintainer-history follow-through. |

## Acceptance Oracle Matrix

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-032-FR01` / `PRD-032-FR04` | Issue templates collect facts, reproduction/context, expected behavior, checks tried, and redaction warnings. | Manual review and clarity scenario coverage. |
| `PRD-032-FR02` | Feedback intake covers adoption friction, confusing docs, setup friction, and workflow questions as evidence only. | Source review and template review. |
| `PRD-032-FR03` | Package-bug intake covers package docs, scripts, protocols, generated-surface expectations, setup/copy helpers, CI, and GitHub helper behavior without becoming app support. | Source review and template review. |
| `PRD-032-FR05` | Public docs and protocols state issues, labels, comments, PRs, and boards are evidence only until promoted. | Source review. |
| `PRD-032-FR06` | `python3 scripts/import-github-sources.py --self-test` passes. | Command output. |
| `PRD-032-FR07` | `python3 scripts/clarity-scenario-check.py` passes. | Command output. |
| `PRD-032-FR08` | Roadmap, changelog, journal, package inventory, and generated surfaces are current. | Validation commands. |

## Required Validation

```bash
python3 scripts/import-github-sources.py --self-test
python3 scripts/clarity-scenario-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
bash scripts/validate-memory.sh
```

## Risk And Permission Model

GitHub Collaboration Hub is an intake and routing surface only. It does not choose tasks, approve PRDs, activate beads, approve roadmap changes, accept implementation, approve merge, approve package release, mutate GitHub, replace maintainer review, or make generated intake output authoritative.

Enabling repository Issues, creating labels, changing issue settings, assigning issues, commenting, closing issues, adding project boards, or changing repository settings is external mutation and requires explicit maintainer approval outside this package implementation.

## Architecture / Project Context Impact

- `PROJECT-CONTEXT.md` impact: none.
- Architecture impact: issue templates and source-intake routing only.
- Data model impact: none.
- Security/privacy impact: templates and docs must warn against secrets and sensitive data.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| GitHub issue templates | `.github/ISSUE_TEMPLATE/*.yml` | Collect source evidence without approving tasks or mutating GitHub automatically. | source review and clarity scenario | This PRD |
| GitHub source importer | `scripts/import-github-sources.py --self-test` | Read-only source-intake support. | deterministic self-test | This PRD |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-032-github-collaboration-hub.md`
- Owner surfaces likely in play: GitHub issue templates, GitHub Integration guidance, Local Source Intake, Tool Execution, Prompt Patterns, public docs, governance, contributing policy, and package inventory.
- Forbidden assumptions: do not mutate GitHub, choose work, approve PRDs, activate beads, approve roadmap changes, accept implementation, approve merge, or approve release.

## Anti-Shallow Checks

- Do templates request facts, context or reproduction, expected behavior, checks tried, and redaction?
- Do public surfaces keep GitHub evidence subordinate to owner-file and maintainer review?
- Does any GitHub mutation require explicit maintainer approval?

## Bead Proposals

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B032-github-collaboration-hub` | `PRD-032-FR01` through `PRD-032-FR08` | Issue templates, source-intake routing, docs/protocols, validation, generated surfaces, and maintainer history are updated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | This PRD | importer self-test and clarity scenario |

## Compilation Notes

- Feature entry: GitHub Collaboration Hub
- Functional requirements to compile: `PRD-032-FR01` through `PRD-032-FR08`
- Acceptance updates needed: GitHub remains source evidence only.

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should future GitHub feedback use richer source-intake summaries? | Follow-up scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-24
- Approval notes: Approved as narrow public GitHub evidence intake with no GitHub mutation, issue-driven roadmap authority, merge approval, release approval, support-bot behavior, registry behavior, or package-manager behavior.
