---
prd_id: PRD-049
status: approved
owner: Dan Sears / Recode
created: 2026-08-04
last_updated: 2026-08-04
risk_level: medium
feature_link: Product Code Quality Snapshot
features_status: not compiled
related_prds:
  - PRD-038
  - PRD-039
  - PRD-040
---

# PRD-049 -- Product Code Quality Snapshot
<!-- ANCHOR: prd-049-product-code-quality-snapshot -->

> AUTHORITY: Public requirements for the advisory Product Code Quality Snapshot over active-bead code-change evidence and explicit whole-codebase changed-file health evidence.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, review approval, release approval, code-quality certification, production-readiness certification, security certification, compliance approval, generated proof, scorecard authority, checker gate, linter replacement, test execution, app-code parsing, AST analysis, framework-specific correctness claim, auto-fix behavior, command approval, command-wrapper behavior, GitHub mutation, external mutation, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the Product Code Quality Snapshot package capability.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-04

## Summary

Product Code Quality Snapshot gives a nontechnical builder one plain, local way to ask whether the AI coding agent's changed code appears bounded, maintainable, owner-file-aligned, and supported by proof before acceptance.

V1 is active-bead-first. It gathers evidence from the active bead, declared files in play, declared checks, changed files, undeclared changed files, repo-shape risk signals, and likely project-owned lint or check commands. A secondary whole-codebase mode can inspect changed-file health without choosing work or certifying the codebase.

The snapshot is evidence gathering, not code-quality judgment. It does not run linters or tests by default, parse app code, score quality, certify "decent code", approve acceptance, or replace Engineering Quality Review Lane.

## Problem

Engineering Quality floor, repo heuristics, and Engineering Quality Review Lane already help before and after implementation. The gap is evidence assembly. A builder can still ask, "did the AI write decent code?", while the agent has changed undeclared files, skipped project checks, touched configuration or dependencies, or produced proof that does not match the scope.

Builders need that evidence made legible without being asked to trust a score.

## Goals

- Add an active-bead-first snapshot that gathers code-change evidence for one current bead.
- Add a secondary whole-codebase mode for explicit changed-file health inspection.
- Discover likely project-owned lint and check commands without running them.
- Feed Engineering Quality Review Lane with a clearer evidence packet when human review is needed.
- Keep all output advisory and non-authoritative.

## Non-Goals

- No standalone `precode lint`, npm wrapper support, command wrapper, package-manager behavior, or release-channel behavior.
- No linter installation, lint-config mutation, auto-fix behavior, linter replacement, test replacement, or default command execution.
- No app-code parser, AST analysis, language-aware analysis, framework-specific correctness claim, quality score, scorecard, certification, generated proof, checker gate, implementation acceptance, review approval, release approval, follow-up task creation, owner-file rewrite authority, GitHub mutation, or external mutation.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-049-FR01` | `scripts/product-code-quality-snapshot.py --active-bead` must be the documented default user path for active-bead code-change evidence. | P0 | Active bead, authority, files in play, checks, changed files, undeclared changes, missing proof. |
| `PRD-049-FR02` | `scripts/product-code-quality-snapshot.py --whole-codebase` must be an explicit secondary mode for broad changed-file health evidence. | P0 | No task selection or certification. |
| `PRD-049-FR03` | The script must support `--json` and plain text output. | P0 | Stable inspection shape without generated authority. |
| `PRD-049-FR04` | The script must discover likely project-owned lint/check commands from package manifests and common config files, but must not run them. | P0 | Project Linter Evidence is discovery only. |
| `PRD-049-FR05` | Output must include snapshot mode, active bead path, primary authority, declared files in play, declared checks, changed files, undeclared changed files, repo-shape risk signals, likely lint/check commands, missing proof, review questions, recommended next action, advisory-only warning, and `does_not`. | P0 | Plain fields for nontechnical review. |
| `PRD-049-FR06` | Engineering Quality Standards Protocol and Review Lanes Protocol must route the snapshot between repo heuristics and Engineering Quality Review Lane. | P0 | Evidence packet before review lane. |
| `PRD-049-FR07` | Prompt Patterns, Daily Cockpit, User Guide, README, AI navigation, Tool Execution, Security, and Package File Inventory must expose the snapshot without making it a start route, required stage, score, gate, proof, or approval. | P1 | Discoverability without route inflation. |
| `PRD-049-FR08` | Clarity scenario coverage and script self-test must protect advisory-only boundaries, active-bead-first default, Project Linter Evidence wording, and no score/certification/gate language. | P1 | Deterministic package checks. |
| `PRD-049-FR09` | Generated PRD HTML, generated public docs HTML, maintainer changelog, roadmap implemented history, roadmap journal, and generated private roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-049-FR01` / `PRD-049-FR05` | Active-bead mode emits active bead, authority, declared files, declared checks, changed paths, undeclared paths, missing proof, review questions, recommended next action, and advisory warning. | `python3 scripts/product-code-quality-snapshot.py --active-bead --json` |
| `PRD-049-FR02` | Whole-codebase mode is explicit and does not depend on active bead approval or choose work. | `python3 scripts/product-code-quality-snapshot.py --whole-codebase --json` |
| `PRD-049-FR03` | Plain and JSON output both render without running lint or tests. | Source review and command output. |
| `PRD-049-FR04` | Likely lint/check command rows say discovery only and require separate approval before execution. | Self-test and source review. |
| `PRD-049-FR06` / `PRD-049-FR07` | Protocols, prompts, docs, AI navigation, security, tool execution, and inventory route the snapshot as advisory evidence only. | Clarity scenario and source review. |
| `PRD-049-FR08` | Self-test and clarity scenario checks fail if score/certification/gate language or command-running behavior appears. | `python3 scripts/product-code-quality-snapshot.py --self-test` and `python3 scripts/clarity-scenario-check.py` |
| `PRD-049-FR09` | Roadmap, journal, changelog, generated docs, generated PRD HTML, and generated roadmap HTML are current with numeric shortstats. | Maintainer checks and rendered surface inspection. |

## Required Validation

```bash
python3 scripts/product-code-quality-snapshot.py --self-test
python3 scripts/product-code-quality-snapshot.py --active-bead --json
python3 scripts/product-code-quality-snapshot.py --whole-codebase --json
python3 scripts/engineering-quality-check.py --self-test
python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview
python3 scripts/clarity-scenario-check.py
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/docs-html.py
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Boundaries

Product Code Quality Snapshot is a local advisory evidence packet. It can make scope drift, missing proof, changed-file breadth, and likely project-owned lint/check commands visible before acceptance. It cannot decide whether code is good, certify code quality, approve review, approve release, or replace human judgment.

Project Linter Evidence is discovery only. The snapshot may identify likely existing commands and explain their probable scope, but running those commands is a separate tool action under normal Tool Execution approval rules.

The script must not run lint, tests, typechecks, package managers, fixers, or app code.

If the snapshot finds new work, the promotion path is normal Precode review: Closeout Evidence, PRD amendment, owner-file update, candidate or approved bead after user review, Release Readiness, reviewed memory, or another Review Lane. The snapshot does not create or apply those changes automatically.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B049-product-code-quality-snapshot` | `PRD-049-FR01` through `PRD-049-FR09` | PRD shard, read-only snapshot script, protocol guidance, prompt guidance, docs/inventory/navigation, Tool Execution and Security boundaries, clarity coverage, maintainer changelog, roadmap history, roadmap journal, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-049-product-code-quality-snapshot.md` | snapshot self-test, clarity scenario, package/docs/PRD/roadmap checks |
