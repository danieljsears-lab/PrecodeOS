---
prd_id: PRD-038
status: approved
owner: Dan Sears / Recode
created: 2026-07-04
last_updated: 2026-07-04
risk_level: medium
feature_link: Engineering Quality Review Lane
features_status: not compiled
related_prds:
  - PRD-018
  - PRD-020
  - PRD-024
  - PRD-036
---

# PRD-038 -- Engineering Quality Review Lane
<!-- ANCHOR: prd-038-engineering-quality-review-lane -->

> AUTHORITY: Public requirements for the advisory Engineering Quality Review Lane for one completed or nearly completed active bead.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, review acceptance, implementation acceptance, release approval, production readiness certification, code-quality certification, generated proof, scorecard authority, checker gate, follow-up task creation, owner-file rewrite, app-code parsing, linter replacement, GitHub mutation, external mutation, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or a persona system.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the Engineering Quality Review Lane package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-04

## Summary

PrecodeOS already has a thin pre-coding Engineering Quality floor and an advisory text-contract checker. PRD-038 makes the post-implementation review lane durable by defining the narrow Review Lanes extension that checks whether completed or nearly completed work respected that floor.

This is a reconciliation-and-close slice for the roadmap candidate. It does not broaden the quality floor into repo heuristics, standards taxonomy, release readiness, language-aware analysis, app-code parsing, linting, scoring, or approval machinery.

## Problem

An implementation can sound complete while still hiding scope drift, needless abstraction, owner-file confusion, weak proof, skipped stop conditions, or unreviewed configuration, dependency, data, secret, or sensitive-surface risk.

The pre-coding quality floor helps before code changes begin. Builders also need a small post-implementation review lens that turns those same concerns into findings, missing proof, acceptance questions, and a recommendation without accepting the work.

## Goals

- Define the Engineering Quality Review Lane as advisory review input for one completed or nearly completed active bead.
- Keep the lane tied to the existing Review Lanes output contract.
- Keep the lane clearly separate from implementation acceptance, code-quality certification, production-readiness certification, checker authority, repo heuristics, and language-aware analysis.
- Make the public PRD, protocol, docs, prompt, checker, inventory, generated surfaces, and maintainer roadmap history agree.

## Non-Goals

- No app-code parser, linter replacement, test runner, repo-heuristics analyzer, language-aware analysis, standards taxonomy, production-readiness certification, code-quality score, generated review report, new command, checker gate, or scorecard.
- No implementation acceptance, review approval, PRD approval, bead activation, transition approval, release approval, follow-up task creation, owner-file rewrite, GitHub mutation, external mutation, registry, optional pack, install/update behavior, release-channel behavior, or package-manager behavior.
- No app-code parsing, no linter replacement, no code-quality score, and no checker gate.
- No change to Security Review Lane, Release / Docs Freshness Review Lane, Dependency Graph Review Lane, PRD Quality Review Lane, Verification Guardrail, Tool Execution, Architecture Shaping, System Design Pattern, or Release Readiness authority.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-038-FR01` | Review Lanes Protocol must define Engineering Quality Review Lane as optional advisory review for one completed or nearly completed active bead. | P0 | Owner protocol update. |
| `PRD-038-FR02` | Lane input guidance must include the active bead, primary authority, files in play or changed-file summary, recorded checks, manual verification when relevant, Closeout Evidence or current closeout draft, and the Engineering Quality Standards Protocol. | P0 | Keeps review grounded. |
| `PRD-038-FR03` | Lane output must use the existing Review Lanes fields and recommendation values. | P0 | Stable review shape. |
| `PRD-038-FR04` | Lane focus must include scope discipline, simplest acceptable implementation shape, owner-file and boundary integrity, proof quality, configuration or dependency handling, sensitive-surface routing, stop-condition observance, and approval-gate observance. | P0 | Review substance. |
| `PRD-038-FR05` | Engineering Quality Standards Protocol must keep the pre-coding floor distinct from post-implementation review. | P0 | Prevents ceremony creep. |
| `PRD-038-FR06` | Prompt Patterns, User Guide, Daily Cockpit, Bead Schema, package inventory, and AI navigation must expose the lane only as conditional review guidance. | P1 | Discoverability without daily-route inflation. |
| `PRD-038-FR07` | `scripts/clarity-scenario-check.py` must check PRD-038, lane focus, output fields, and forbidden authority claims. | P1 | Text-contract coverage only. |
| `PRD-038-FR08` | `scripts/engineering-quality-check.py` must verify the package text contract references post-implementation Engineering Quality Review Lane while remaining advisory only. | P1 | No review-output or app-code analysis. |
| `PRD-038-FR09` | Maintainer changelog, roadmap implemented history, roadmap journal, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-038-FR01` | Review Lanes Protocol defines Engineering Quality Review Lane as advisory review for completed or nearly completed active beads. | Source review and clarity scenario. |
| `PRD-038-FR02` | Required input guidance names active bead, primary authority, files or changed-file summary, checks, manual verification, closeout evidence, and Engineering Quality Standards Protocol. | Source review. |
| `PRD-038-FR03` | Lane output uses `Lane`, `Review target`, `Authority checked`, `Evidence reviewed`, `Findings`, `Missing proof`, `Acceptance questions`, `Recommendation`, `Approval still required`, and `Promotion path`. | Clarity scenario. |
| `PRD-038-FR04` | Lane focus covers scope, simplest shape, boundaries, proof, configuration/dependency handling, sensitive-surface routing, and stop conditions. | Clarity scenario. |
| `PRD-038-FR05` | Standards Protocol distinguishes pre-coding floor from post-implementation review and preserves deferred taxonomy. | Engineering quality checker and source review. |
| `PRD-038-FR06` | Prompt, docs, bead schema, inventory, and AI navigation mention the lane without making it a required gate. | Source review and generated docs HTML. |
| `PRD-038-FR07` | Clarity scenario catches required lane terms and forbidden authority drift. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-038-FR08` | Engineering quality checker self-test covers review-lane contract terms and still reports advisory-only output. | `python3 scripts/engineering-quality-check.py --self-test`. |
| `PRD-038-FR09` | Package inventory, maintainer changelog, roadmap, journal, and generated surfaces are fresh. | Validation commands. |

## Required Validation

```bash
python3 scripts/engineering-quality-check.py --self-test
python3 scripts/engineering-quality-check.py --check
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

The Engineering Quality Review Lane is a review conversation shape. It may recommend `accepted`, `revise`, `split`, `blocked`, or `stop`, but the recommendation is not acceptance.

If findings reveal new work, the promotion path is normal Precode review: Closeout Evidence, PRD amendment, owner-file update, candidate or approved bead after user review, Release Readiness, reviewed memory, or another Review Lane. The lane does not create or apply those changes automatically.

Repo-level heuristics, standards taxonomy, release-readiness quality expansion, and language-aware analysis remain separate deferred roadmap work.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B002-engineering-quality-review-lane` | `PRD-038-FR01` through `PRD-038-FR09` | PRD shard, protocol guidance, prompt guidance, docs/inventory/navigation, clarity coverage, engineering-quality checker text contract, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-038-engineering-quality-review-lane.md` | clarity scenario, engineering-quality checker, package/docs/PRD/roadmap checks |
