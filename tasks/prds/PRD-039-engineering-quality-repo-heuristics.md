---
prd_id: PRD-039
status: approved
owner: Dan Sears / Recode
created: 2026-07-04
last_updated: 2026-07-04
risk_level: medium
feature_link: Engineering Quality Repo Heuristics
features_status: not compiled
related_prds:
  - PRD-038
---

# PRD-039 -- Engineering Quality Repo Heuristics
<!-- ANCHOR: prd-039-engineering-quality-repo-heuristics -->

> AUTHORITY: Public requirements for the optional Engineering Quality Repo Heuristics Preview on the advisory Engineering Quality Text-Contract Checker.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation approval, review acceptance, release approval, production-readiness certification, code-quality scoring, linter replacement, test execution, app-code parsing, generated proof, checker-gate behavior, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the explicit repo-shape preview for `scripts/engineering-quality-check.py`.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-04

## Summary

PrecodeOS needs a narrow repo-shape preview for cases where the quality-floor text sounds complete but the actual changed files suggest broader risk. This PRD adds the explicit `--repo-heuristics-preview` flag to `scripts/engineering-quality-check.py`.

The default checker remains the Engineering Quality Text-Contract Checker. Repo heuristics appear only when the preview flag is passed.

## Problem

Text-contract checks can confirm that a quality-floor answer names risk, shape, boundary, proof, stop conditions, and routing, but they cannot see whether changed files contradict the claimed scope. A task may say it is narrow while git status shows dependency, config, docs, protocol, script, generated-evidence, or broad cross-surface changes.

## Goals

- Add explicit, read-only repo-shape warnings to the existing checker.
- Compare changed-file summaries against active-bead primary authority, files in play, checks, and Stop If conditions.
- Preserve advisory-only behavior, no code-quality judgment, and no approval authority.
- Keep the first slice changed-file-only; do not add AST, language-aware, linter, or framework analysis.

## Non-Goals

- No default repo heuristics in `python3 scripts/engineering-quality-check.py --check`.
- No app-code parser, AST analysis, linter replacement, test execution, code-quality score, scorecard, production-readiness certification, security certification, or compliance claim.
- No checker gate, generated proof, implementation approval, review acceptance, release approval, task selection, PRD approval, bead activation, registry, optional pack, install/update behavior, release channel, package-manager behavior, or external mutation.
- No replacement for Engineering Quality Review Lane, Release Readiness, Verification Guardrail, Tool Execution, Architecture Shaping, or System Design Pattern.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-039-FR01` | `scripts/engineering-quality-check.py --check` must keep its current default text-contract behavior without repo heuristics. | P0 | Backward-compatible output unless existing contract terms change. |
| `PRD-039-FR02` | `--repo-heuristics-preview` must add an explicit advisory payload group for repo-shape warnings. | P0 | Output is additive and visibly preview-only. |
| `PRD-039-FR03` | The preview must inspect only active-bead metadata and read-only git changed-file summaries. | P0 | Primary authority, files in play, checks, Stop If, changed paths. |
| `PRD-039-FR04` | The preview must warn about undeclared changed files, broad cross-surface edits, config/dependency touches, docs/protocol/PRD touches, script touches, missing matching checks, generated-evidence gaps, and git-unavailable status. | P0 | Warnings are not blocking gates. |
| `PRD-039-FR05` | Public protocol, prompt, user docs, AI navigation, package inventory, clarity scenarios, generated docs/PRD surfaces, maintainer changelog, roadmap, and roadmap journal must be updated. | P1 | Maintainer follow-through for public package changes. |
| `PRD-039-FR06` | Deterministic checker self-test and clarity scenario coverage must protect the preview flag and no-authority boundaries. | P1 | Includes explicit git-unavailable behavior. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-039-FR01` | Running `python3 scripts/engineering-quality-check.py --check` does not include repo-preview details. | Source review and command output. |
| `PRD-039-FR02` | Running `python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview` includes a `repo_heuristics_preview` details group. | Command output. |
| `PRD-039-FR03` | Source uses active-bead metadata and read-only git status only. | Source review. |
| `PRD-039-FR04` | Self-test includes git-unavailable behavior and preview warning boundaries. | `python3 scripts/engineering-quality-check.py --self-test`. |
| `PRD-039-FR05` | Public docs, inventory, AI navigation, changelog, roadmap, and generated surfaces are fresh. | Validation commands. |
| `PRD-039-FR06` | Clarity scenario coverage requires the preview flag and advisory-only wording. | `python3 scripts/clarity-scenario-check.py`. |

## Required Validation

```bash
python3 scripts/engineering-quality-check.py --self-test
python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview
python3 scripts/clarity-scenario-check.py
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Boundaries

Engineering Quality Repo Heuristics Preview is advisory only. It can make changed-file risk visible before a builder trusts a quality-floor answer, but it does not decide whether work should continue, approve implementation, approve review, certify quality, certify production readiness, or replace human judgment.

If git metadata is unavailable, the preview must label that state directly and continue with declared Precode artifact signals only. That explicit warning is not a failure to be hidden.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B002-engineering-quality-repo-heuristics` | `PRD-039-FR01` through `PRD-039-FR06` | PRD shard, checker flag, protocol guidance, prompt guidance, docs/inventory/navigation, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-039-engineering-quality-repo-heuristics.md` | checker self-test, clarity scenario, package/docs/PRD/roadmap checks |
