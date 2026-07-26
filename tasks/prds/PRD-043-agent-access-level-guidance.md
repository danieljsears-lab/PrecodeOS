---
prd_id: PRD-043
status: approved
owner: Dan Sears / Recode
created: 2026-07-26
last_updated: 2026-07-26
risk_level: medium
feature_link: Agent Access Level Guidance
features_status: not compiled
related_prds:
  - PRD-035
  - PRD-037
---

# PRD-043 -- Agent Access Level Guidance
<!-- ANCHOR: prd-043-agent-access-level-guidance -->

> AUTHORITY: Public requirements for plain-language agent access level guidance across Tool Execution, Run Contracts, routing, prompts, and user docs.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, command approval, runtime permission enforcement, sandbox behavior, package-manager behavior, host-plugin dependency, generated-output authority, external mutation approval, or schema-backed access metadata.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting PrecodeOS permission, access, command-risk, Run Contract, sensitive-surface, external-mutation, destructive-action, delegation, or re-entry guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-26

## Summary

PrecodeOS already has tool-call classes, bead autonomy metadata, files in play, Run Contracts, and approval gates. Builders still need a plain answer to "what can the agent do right now?" before commands, sensitive work, external systems, or long-running delegated work begin.

This PRD adds guidance-only access levels that translate existing command and risk rules into beginner-readable language. The levels do not enforce permissions, approve commands, add sandbox behavior, or create schema-backed access metadata.

## Problem

Agent-native tools often make capability feel like permission. A model or coding agent may be able to inspect files, edit code, read external state, push branches, touch secrets, or deploy, but PrecodeOS needs the repository to say which of those actions are appropriate for the active bead and which require explicit human approval.

Without a shared access vocabulary, Tool Execution classes, Run Contracts, approval gates, autonomy levels, and re-entry evidence can feel like separate rules. That increases permission drift and makes sensitive or external work harder for a non-technical builder to supervise.

## Goals

- Define a compact access ladder in plain English.
- Map the ladder to existing tool-call classes, `files_in_play`, Run Contracts, approval gates, and bead autonomy metadata.
- Keep `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` as the primary owner for command/access classification.
- Refresh routing, bead schema, system-design, prompt, reader-doc, inventory, and AI-index surfaces so they use the same language.
- Add deterministic clarity fixture coverage for the guidance-only boundary.

## Non-Goals

- No runtime access enforcement, sandbox behavior, command approval layer, host-plugin dependency, new checker, new command, new router, registry, optional pack, package-manager behavior, release-channel behavior, install/update semantics, automatic external mutation approval, or generated-output authority.
- No new `autonomy_level` values.
- No schema-backed access metadata in this slice.
- No claim that an agent receives full developer parity by default.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-043-FR01` | Tool Execution must define guidance-only agent access levels for read-only inspection, verification, scoped local mutation, sensitive or secret-bearing work, external mutation, and destructive or irreversible action. | P0 | Existing tool-call classes remain canonical. |
| `PRD-043-FR02` | Run Contract and Agent Routing guidance must map access levels to allowed actions, proof needed, approval required before risky actions, stop conditions, and re-entry evidence. | P0 | No new enforcement layer. |
| `PRD-043-FR03` | Bead Schema and System Design guidance must keep `autonomy_level` unchanged while explaining when access risk requires human-only handling or a Run Contract. | P0 | Schema-backed metadata is deferred. |
| `PRD-043-FR04` | Prompt and reader surfaces must give builders a copyable way to ask what access level applies before work or risky commands. | P0 | Beginner docs should stay compact. |
| `PRD-043-FR05` | Script fixture coverage must prove access-level wording remains advisory and does not approve commands, enforce permissions, add schema requirements, or create package-manager behavior. | P0 | Use existing clarity scenario checks. |
| `PRD-043-FR06` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs/PRD surfaces, and generated roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Access Level Ladder

| Level | Plain meaning | Existing Precode mapping | Human gate |
|---|---|---|---|
| `inspect` | The agent may read local or external information without changing it. | `read_only`; active memory, owner files, source evidence, generated reports as evidence only. | Ask if the source may contain secrets or private data. |
| `verify` | The agent may run checks intended to prove behavior or package integrity. | `verification`; recorded through `record-check.sh` when used as proof. | Ask if the check is expensive, external, secret-bearing, or mutating. |
| `local-change` | The agent may change local files inside the approved bead boundary. | `local_mutation`; `files_in_play`; active bead scope. | Ask before dependency installs, generated authority-like rewrites, scope widening, or sensitive surfaces. |
| `sensitive` | The agent may prepare or inspect sensitive work only after the risk and proof path are explicit. | `secret_bearing` or sensitive-surface local mutation; `SECURITY.md`; Run Contract when needed. | Explicit approval before secrets, credentials, auth, private data, payments, security config, or dashboard values. |
| `external-change` | The agent may change a hosted service, GitHub, CI, deployment, dashboard, issue tracker, release, or shared branch only after approval. | `external_mutation`; Tool Execution external mutation rules; Run Contract when needed. | Explicit approval naming action, affected system, recovery path, and evidence. |
| `destructive` | The agent must stop before irreversible or hard-to-reverse work. | `destructive`; deletion, reset, drop, force-push, destructive migration, rollback. | Stop until the user explicitly approves the exact command, expected effect, rollback or blocked escape, and evidence plan. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-043-FR01` | Tool Execution contains the ladder and says access levels are guidance over existing tool-call classes. | Source review and clarity scenario. |
| `PRD-043-FR02` | Run Contract and routing language name allowed actions, proof needed, approval required before, stop conditions, re-entry evidence, and non-enforcement limits. | Source review and `python3 scripts/clarity-scenario-check.py`. |
| `PRD-043-FR03` | Bead Schema still lists only `supervised`, `bounded-afk`, and `human-only`; schema-backed access metadata is named as deferred. | Source review and clarity scenario. |
| `PRD-043-FR04` | Daily Cockpit, User Guide, Prompt Patterns, README, and `llms.txt` expose compact access-level routing without making it a new workflow. | Docs review and docs HTML freshness. |
| `PRD-043-FR05` | Existing command classification reports guidance-only access-level metadata and fixture checks fail if it becomes command approval, enforcement, schema requirement, or package-manager behavior. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-043-FR06` | Roadmap, journal, changelog, PRD HTML, docs HTML, and roadmap HTML are current and rendered shortstats are numeric. | Maintainer checks and rendered roadmap inspection. |

## Risk And Permission Model

- Stop if an agent treats access levels as permission grants, sandbox policy, command approval, or runtime enforcement.
- Stop if sensitive, external, destructive, dependency, deployment, migration, release, shared-branch, secret, auth, private-data, payment, or dashboard work lacks explicit approval and a proof path.
- Stop if the change adds new `autonomy_level` values or schema-backed access metadata in this slice.
- Stop if generated reports, command facades, checkers, adapters, or host tools are treated as access authority.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| Tool Execution Protocol | Access ladder plus command class mapping. | Guidance only; classes remain canonical. | Source review and clarity fixture. | `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` |
| Run Contract guidance | Allowed actions, proof needed, approval gates, stop conditions, re-entry evidence. | Advisory contract state, not enforcement. | `python3 scripts/run-contract-check.py` via compiler and clarity scenario. | `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` |
| Command classification metadata | Existing `command_classification` payload may include access-level explanation. | Advisory generated evidence only. | `python3 scripts/clarity-scenario-check.py`. | `scripts/os_compiler.py` |
| Prompt and reader docs | Copyable "what access level applies?" prompt. | Routing help only; no task or command approval. | Docs HTML and source review. | `tasks/reference/PROMPT-PATTERNS.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-043-agent-access-level-guidance.md`
- Owner protocols:
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/AGENT-ROUTING-PROTOCOL.md`
  - `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md`
- Files or folders likely in play:
  - `scripts/os_compiler.py`
  - `scripts/clarity-scenario-check.py`
  - `tasks/beads/BEAD-SCHEMA.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `README.md`
  - `llms.txt`
  - `tasks/prds-html/`
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - active memory
  - target app code
  - host-plugin configuration
  - access enforcement or sandbox integration
  - new commands or new checkers
  - schema-backed access metadata
  - package-manager behavior

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/file-inventory.py --check
python3 scripts/version-check.py
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Anti-Shallow Checks

- If implementation treats access levels as approval, enforcement, or sandbox policy, it violates this PRD.
- If implementation adds new `autonomy_level` values or a required access schema, it violates this PRD.
- If implementation adds a command, checker, registry, optional pack, host-plugin dependency, install/update behavior, release-channel behavior, package-manager behavior, or generated-output authority, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B043-agent-access-level-guidance` | `PRD-043-FR01` through `PRD-043-FR06` | Access ladder guidance, protocol/docs/navigation wording, clarity coverage, generated docs/PRD surfaces, maintainer changelog, roadmap history, and generated roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-043-agent-access-level-guidance.md` | clarity scenario, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-07-26.
