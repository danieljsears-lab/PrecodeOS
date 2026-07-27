---
prd_id: PRD-044
status: approved
owner: Dan Sears / Recode
created: 2026-07-26
last_updated: 2026-07-26
risk_level: medium
feature_link: Polish / Product-Taste Review Lane
features_status: not compiled
related_prds:
  - PRD-018
  - PRD-020
  - PRD-030
  - PRD-038
  - PRD-040
---

# PRD-044 -- Polish / Product-Taste Review Lane
<!-- ANCHOR: prd-044-polish-product-taste-review-lane -->

> AUTHORITY: Public requirements for the advisory Polish / Product-Taste Review Lane for one completed or nearly completed user-facing active bead.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, review acceptance, implementation acceptance, release approval, design certification, UX certification, product authority, generated proof, screenshot-as-proof shortcut, scorecard authority, checker gate, generated report, follow-up task creation, owner-file rewrite, professional UX research requirement, GitHub mutation, external mutation, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, command-wrapper behavior, or a persona system.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the Polish / Product-Taste Review Lane package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-26

## Summary

PrecodeOS has advisory review lanes for security, release/docs freshness, dependency relationships, engineering quality, PRD quality, and package cross-reference/staleness. PRD-044 adds a narrow post-implementation lane for one user-facing bead where the work technically runs but the visible experience may still be confusing, poorly worded, rough, or weak against the acceptance oracle.

This is a protocol-and-prompt slice. It does not add a checker, command, generated report, design scorecard, acceptance replacement, release gate, or professional UX research requirement.

## Problem

Non-technical builders can accept work that passes checks but still feels hard to understand, visibly rough, weakly connected to the target user, or unclear against the promised before/after moment.

Existing Engineering Quality, PRD Quality, Release / Docs Freshness, Verification Guardrail, and Acceptance surfaces cover important adjacent risks, but none provides a plain post-implementation lens for visible product feel while preserving human product judgment.

## Goals

- Define Polish / Product-Taste Review Lane as advisory review input for one completed or nearly completed user-facing active bead.
- Keep the lane tied to the existing Review Lanes output contract and recommendation values.
- Review visible user flow, screen behavior, copy clarity, target-user comprehension, acceptance-oracle fit, manual QA path, polish risks, and remaining human taste judgment.
- Keep reviewer taste subordinate to owner files, PRDs, acceptance criteria, recorded proof, and human approval.
- Make the public PRD, protocol, prompts, docs, package inventory, bead schema, AI navigation, clarity fixtures, generated surfaces, and maintainer roadmap history agree.

## Non-Goals

- No design certification, UX certification, taste score, scorecard, checker, command, generated report, required review gate, professional UX research requirement, app-code parser, linter replacement, or screenshot-as-proof shortcut.
- No implementation acceptance, review approval, PRD approval, bead activation, transition approval, release approval, follow-up task creation, owner-file rewrite, GitHub mutation, external mutation, registry, optional pack, install/update behavior, release-channel behavior, package-manager behavior, command-wrapper behavior, or persona system.
- No change to Acceptance, Verification Guardrail, Engineering Quality Review, PRD Quality Review, Release / Docs Freshness, Release Readiness, Requirements Gap And Conflict Review, Product Discovery Validation, or Product owner-file authority.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-044-FR01` | Review Lanes Protocol must define Polish / Product-Taste Review Lane as optional advisory review for one completed or nearly completed user-facing active bead. | P0 | Owner protocol update. |
| `PRD-044-FR02` | Lane input guidance must include the active bead, primary authority, files in play or changed-file summary, acceptance oracle, recorded checks, manual verification path, screenshots or browser notes only as evidence, and Closeout Evidence or current closeout draft. | P0 | Keeps review grounded. |
| `PRD-044-FR03` | Lane output must use the existing Review Lanes fields and recommendation values. | P0 | Stable review shape. |
| `PRD-044-FR04` | Lane focus must include visible user flow, screen behavior, copy clarity, target-user comprehension, acceptance-oracle fit, manual QA path, rough or polish risks, remaining human taste judgment, and target-user feedback needs. | P0 | Review substance. |
| `PRD-044-FR05` | Prompt Patterns, User Guide, Daily Cockpit, Bead Schema, package inventory, and AI navigation must expose the lane only as conditional review guidance. | P1 | Discoverability without daily-route inflation. |
| `PRD-044-FR06` | Fixture coverage must prove the lane remains advisory and does not certify design or UX quality, approve acceptance or release, make reviewer taste product authority, treat screenshots as proof, create follow-up tasks, create a generated report, create a checker gate, create a required gate, or create command-wrapper/package-manager behavior. | P1 | Use existing clarity scenario checks. |
| `PRD-044-FR07` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs/PRD surfaces, and generated roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-044-FR01` | Review Lanes Protocol defines Polish / Product-Taste Review Lane as advisory review for completed or nearly completed user-facing active beads. | Source review and clarity scenario. |
| `PRD-044-FR02` | Required input guidance names active bead, primary authority, files or changed-file summary, acceptance oracle, checks, manual verification path, screenshots or browser notes as evidence only, and Closeout Evidence. | Source review. |
| `PRD-044-FR03` | Lane output uses `Lane`, `Review target`, `Authority checked`, `Evidence reviewed`, `Findings`, `Missing proof`, `Acceptance questions`, `Recommendation`, `Approval still required`, and `Promotion path`. | Clarity scenario. |
| `PRD-044-FR04` | Lane focus covers visible flow, screen behavior, copy, target-user comprehension, acceptance-oracle fit, manual QA, polish risk, human taste judgment, and target-user feedback. | Clarity scenario. |
| `PRD-044-FR05` | Prompt, docs, bead schema, inventory, and AI navigation mention the lane without making it a required gate. | Source review and generated docs HTML. |
| `PRD-044-FR06` | Clarity scenario catches required lane terms and forbidden authority drift. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-044-FR07` | Roadmap, journal, changelog, PRD HTML, docs HTML, and roadmap HTML are current and rendered shortstats are numeric. | Maintainer checks and rendered roadmap inspection. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/docs-html.py
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Boundaries

The Polish / Product-Taste Review Lane is a review conversation shape. It may recommend `accepted`, `revise`, `split`, `blocked`, or `stop`, but the recommendation is not acceptance. It must not accept implementation, certify design quality, certify UX quality, or create product authority from reviewer taste.

Reviewer taste is not product authority. If findings imply new product direction, route through normal Precode review: Closeout Evidence, PRD amendment, owner-file update, Candidate Queue entry after user review, candidate or approved bead after user review, Release Readiness, reviewed memory after user review, target-user feedback, or another Review Lane.

Screenshots, browser notes, and AI critique are evidence only. They can help explain what was inspected, but they do not prove acceptance or design quality by themselves.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B044-polish-product-taste-review-lane` | `PRD-044-FR01` through `PRD-044-FR07` | PRD shard, protocol guidance, prompt guidance, docs/inventory/navigation, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-044-polish-product-taste-review-lane.md` | clarity scenario, package/docs/PRD/roadmap checks |
