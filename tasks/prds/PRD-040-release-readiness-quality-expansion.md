---
prd_id: PRD-040
status: approved
owner: Dan Sears / Recode
created: 2026-07-11
last_updated: 2026-07-11
risk_level: high
feature_link: Release-Readiness Quality Expansion
features_status: not compiled
related_prds:
  - PRD-005
  - PRD-009
  - PRD-020
---

# PRD-040 -- Release-Readiness Quality Expansion
<!-- ANCHOR: prd-040-release-readiness-quality-expansion -->

> AUTHORITY: Public requirements for release-quality cue guidance and advisory completion-check warnings inside the existing Release Readiness lane.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, review acceptance, release approval, deployment approval, production-readiness certification, compliance certification, generated proof, provider checklist, release gate, GitHub mutation, external mutation, package release management, release-channel behavior, package-manager behavior, or a new checker surface.
> LOAD_WHEN: Planning, implementing, reviewing, or validating release-quality cue handling for release-relevant user-project work.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-11

## Summary

PrecodeOS should make release-adjacent quality concerns visible inside Release Readiness without turning them into production certification or a new command. This PRD adds a `Release quality cues` evidence block to existing release-readiness notes, Release Candidate Evidence Profiles, and Verification and Release Evidence.

The existing command path remains `scripts/completion-check.py` through `scripts/os_compiler.py`. Missing cue fields create advisory warnings only.

## Problem

Release evidence already names smoke paths, docs freshness, rollback or blocked escape, approvals, and decision state. It can still miss broader release-adjacent quality concerns such as CI/status checks, logs or observability, configuration/environment parity, performance expectations, data/privacy/security expectations, dependency freshness, or monitoring/support ownership.

Those concerns belong near release evidence, not the pre-coding Engineering Quality floor. They are evidence-preparation questions, not proof of production readiness.

## Goals

- Extend Release Readiness with compact, beginner-readable release-quality cues.
- Keep broader NFR concerns as evidence prompts and advisory warnings.
- Preserve the existing `completion-check.py` command interface.
- Keep `ready for human release decision` as evidence state only, not approval.

## Non-Goals

- No new public checker, release command, generated evidence report, provider-specific checklist, deploy automation, rollback automation, CI release gate, scorecard, production-readiness certification, compliance claim, GitHub mutation, dashboard mutation, provider mutation, package release management, release-channel behavior, package-manager behavior, registry behavior, or optional-pack behavior.
- No app-code parsing, AST analysis, linter replacement, performance testing, monitoring integration, dashboard inspection, or secret/config value inspection.
- No required cue set for ordinary non-release-relevant beads.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-040-FR01` | Release Readiness Protocol must define a `Release quality cues` block for release-readiness notes, Release Candidate Evidence Profiles, and Verification and Release Evidence. | P0 | Human-authored evidence fields only. |
| `PRD-040-FR02` | The cue block must cover CI/status checks, logs or observability signal, configuration/environment parity, performance or scalability expectation, data retention/privacy/security expectation, dependency/runtime freshness, and monitoring/support owner. | P0 | Each cue can cite evidence or say not applicable with a reason. |
| `PRD-040-FR03` | `scripts/os_compiler.py` must expose advisory missing-cue warnings through existing `details.release_evidence` output when release evidence/profile/readiness content is invoked. | P0 | No new command or report. |
| `PRD-040-FR04` | Prompt Patterns and public user guidance must ask for release-quality cues without implying approval, deployment, provider mutation, or certification. | P0 | Copyable prompts only. |
| `PRD-040-FR05` | Package inventory and AI navigation must list PRD-040 and the existing command boundary. | P1 | Discoverability without command sprawl. |
| `PRD-040-FR06` | Clarity scenarios must pin evidence-only cue behavior, not-applicable-with-reason handling, non-approval wording, review-input demotion, and forbidden release-gate/certification behavior. | P1 | Deterministic local regression. |
| `PRD-040-FR07` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs, generated PRD HTML, and generated roadmap HTML must be refreshed. | P1 | Maintainer follow-through for public package changes. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-040-FR01` / `PRD-040-FR02` | Release Readiness Protocol includes release-quality cue fields and says missing cues are advisory evidence gaps only. | Protocol source review and clarity scenario. |
| `PRD-040-FR03` | `release_evidence_quality` returns missing cue warnings for incomplete release evidence and passes when all cue fields are present or not applicable with reasons. | `python3 scripts/clarity-scenario-check.py` and `python3 scripts/completion-check.py`. |
| `PRD-040-FR04` | Prompt Patterns and public docs include cue prompts and forbidden action language. | Docs freshness checks and manual boundary review. |
| `PRD-040-FR05` | Inventory and AI navigation mention PRD-040 and no new command surface. | `python3 scripts/file-inventory.py --check`. |
| `PRD-040-FR07` | Roadmap, journal, changelog, and generated surfaces are current. | Maintainer docs/PRD/roadmap checks. |

## Risk And Permission Model

- Approval remains required before deployment, promotion, rollback, merge, migration, dashboard update, provider mutation, secret change, GitHub mutation, external-service mutation, production configuration change, or package release action.
- Stop if the release target, cue evidence, recorded source, smoke path, docs/support freshness, rollback or blocked escape, approval owner, decision state, or remaining uncertainty is unclear.
- Release-quality cue warnings are advisory. They may recommend `needs evidence`, but they do not block, approve, certify, or mutate anything.
- Evidence must not expose secrets, tokens, credentials, personal data samples, private dashboard values, production config values, or sensitive provider details.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | `Release quality cues` block. | Frames release-adjacent NFR evidence without certification. | Source review and clarity scenario. | `tasks/prds/PRD-040-release-readiness-quality-expansion.md` |
| `scripts/completion-check.py` via `scripts/os_compiler.py` | Existing advisory `details.release_evidence` payload. | Adds missing-cue warnings only when release evidence is invoked. | Clarity scenario and command run. | `tasks/prds/PRD-040-release-readiness-quality-expansion.md` |
| Prompt and user docs | Copyable prompts for cue evidence. | Ask for evidence and not-applicable reasons without release action. | Docs freshness and manual boundary review. | `tasks/prds/PRD-040-release-readiness-quality-expansion.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-040-release-readiness-quality-expansion.md`
- Parent PRDs:
  - `tasks/prds/PRD-005-release-readiness-lane.md`
  - `tasks/prds/PRD-009-release-candidate-evidence-lane.md`
  - `tasks/prds/PRD-020-verification-release-evidence.md`
- Owner protocol: `tasks/reference/RELEASE-READINESS-PROTOCOL.md`
- Files or folders likely in play:
  - `scripts/os_compiler.py`
  - `scripts/clarity-scenario-check.py`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `llms.txt`
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
  - provider configuration
  - dashboards
  - secrets or environment files
  - GitHub mutation
  - deployment scripts
  - new release-quality checker scripts

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/completion-check.py
PYTHONPYCACHEPREFIX=/private/tmp/precode-pycache python3 -m py_compile scripts/os_compiler.py scripts/completion-check.py scripts/clarity-scenario-check.py
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Anti-Shallow Checks

- If release-quality cues are treated as production-readiness certification, the implementation violates this PRD.
- If missing cue warnings block or approve release by themselves, the implementation violates this PRD.
- If a new command or checker is added for this slice, the implementation violates this PRD.
- If logs, dashboards, screenshots, GitHub status, generated reports, or cue text are treated as proof without recorded evidence, the implementation violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B040-release-readiness-quality-expansion` | `PRD-040-FR01` through `PRD-040-FR07` | PRD shard, Release Readiness cue block, existing completion-check advisory warnings, prompt/user guidance, package inventory, AI navigation, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-040-release-readiness-quality-expansion.md` | clarity scenario, completion-check, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-07-11.
