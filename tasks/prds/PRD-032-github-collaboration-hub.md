---
prd_id: PRD-032
status: approved
owner: Dan Sears / Recode
created: 2026-06-24
last_updated: 2026-06-24
feature_link: GitHub Collaboration Hub
features_status: not compiled
related_prds:
  - PRD-025
  - PRD-028
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
Document version: v0.1.0
Last updated: 2026-06-24

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

## Functional Requirements

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

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-032-FR01` / `PRD-032-FR04` | Issue templates collect facts, reproduction/context, expected behavior, checks tried, and redaction warnings. | Manual review and clarity scenario coverage. |
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

## Boundaries

GitHub Collaboration Hub is an intake and routing surface only. It does not choose tasks, approve PRDs, activate beads, approve roadmap changes, accept implementation, approve merge, approve package release, mutate GitHub, replace maintainer review, or make generated intake output authoritative.

Enabling repository Issues, creating labels, changing issue settings, assigning issues, commenting, closing issues, adding project boards, or changing repository settings is external mutation and requires explicit maintainer approval outside this package implementation.
