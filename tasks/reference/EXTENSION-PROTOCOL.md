# PrecodeOS -- Extension Protocol
<!-- ANCHOR: extension-protocol -->

> AUTHORITY: Extension rules, extension types, skill-playbook boundaries, authority boundaries, active-memory limits, generated-output boundaries, mutation boundaries, and extension review checklist for adding PrecodeOS capabilities.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, external mutation approval, generated progress state, or plugin registry.
> LOAD_WHEN: Adding or reviewing a Precode adapter, protocol, skill playbook, importer, audit, generated report, bead template, or external integration.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.12
Last updated: 2026-06-15

## Purpose

Extensions let PrecodeOS grow without turning into a giant prompt or a hidden automation system.

An extension may add a tool surface, workflow protocol, skill playbook, source importer, audit, generated report, bead template, or external integration. It must not add active-memory files or let generated evidence choose work.

Use `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` when an extension packages a named host-agent prompt playbook, docs-help invocation, beginner workflow invocation, maintainer package-review playbook, or extension-review playbook. Skill playbooks are read-only in v1 and must point back to their owner protocols or canonical docs.

Use the Skill / Extension Review Skill in `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` when the user wants a structured advisory review of a proposed skill or extension before implementation. The review output is input to this protocol; it does not approve the extension, install a skill, mutate files, add a registry, or create optional-pack behavior.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when an extension exposes commands, touches external systems, logs non-check tool runs, wraps existing commands, or needs tool-call approval boundaries.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when an extension introduces a new integration boundary, provider abstraction, workflow state, audit trail, or other reusable implementation shape.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Extension Types

| Type | Purpose | Usual owner |
|---|---|---|
| Adapter | Tool-specific guidance for a coding agent | `adapters/*.md` or a tool shim |
| Protocol | Workflow rules for a repeatable Precode process | `tasks/reference/*.md` |
| Skill playbook | Read-only host-agent invocation guidance for stable docs help, an existing Precode workflow, or extension review | `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` plus the owner protocol, canonical docs, or adapter |
| Importer | Reads source material or telemetry and normalizes evidence | `scripts/import-*.py` |
| Audit | Reads project or external status and reports findings | `scripts/*-audit.py` |
| Generated report | Human-readable or machine-readable evidence output | `logs/`, `OS-HEALTH.md`, or `PROGRESS.md` |
| Generated execution profile | Machine-readable run-contract export for a host or adapter | `logs/run-contract.json` and `logs/run-contract.yaml` |
| Bead template | Repeatable task shape with the standard bead contract | `tasks/beads/BEAD-SCHEMA.md` |
| Bounded attempt engine | Opt-in local loop that runs one explicit attempt command, validators, and generated attempt evidence for one active bead | `tasks/reference/RALPH-LOOP-PROTOCOL.md` plus `scripts/ralph-loop.py` |
| External integration | Read-only or approved interaction with outside systems | Integration protocol plus `PROJECT-CONTEXT.md` |
| Role contract | Compact mode card for bounded agent behavior | `modes/*.md` |

## Boundary Rules

Every extension must preserve these boundaries:

- Do not add a fourth active-memory file.
- Do not promote generated output into authority.
- Do not let external systems choose task selection, bead transitions, product decisions, or implementation plans.
- Do not mutate external systems unless the active bead explicitly allows it and the user approves the manual gate.
- Keep extension rules in one owning protocol or adapter.
- Keep skill playbooks read-only unless a later approved extension explicitly defines command-wrapper boundaries.
- Keep docs-help playbooks limited to stable documentation questions; they must cite canonical docs/protocols and stop before current-state diagnosis.
- Keep extension findings as evidence until promoted into a PRD, `DECISIONS.md`, an owning authority file, or an approved bead.
- Keep bounded engines subordinate to one active bead, explicit user approval gates, and generated-evidence demotion.

## Authority Contract Rules

Reference and generated markdown added by an extension must include:

- canonical anchor
- `AUTHORITY`
- `NOT_AUTHORITY`
- `LOAD_WHEN`
- `CLASS`

Use `CLASS: reference` for durable rules and `CLASS: generated` for reports.

Generated markdown must clearly say it is not active memory, not a task plan, and not an instruction source.

## Generated Output Rules

Generated evidence should live under `logs/` unless a legacy Precode report already owns the surface.

Generated JSON and JSONL files must be treated as evidence only. They may feed summaries, audits, or human review, but they must not directly rewrite active memory, bead state, PRDs, decisions, or product authority files.

Generated reports, sidecars, and public generated HTML added by an extension should be represented in `logs/authority-map.json` surface classes when the generated map is refreshed. That classification is orientation evidence only; it does not approve the extension, make generated output authoritative, or replace the owning protocol, adapter, PRD, decision, authority file, or approved bead.

`logs/run-contract.json` and `logs/run-contract.yaml` are generated execution profiles compiled from the active bead. They may help a future host adapter enforce allowed actions and proof needed, but they are not authority and do not approve commands.

`logs/next-step.json` may include generated router fields such as `load_plan`, `single_next_protocol`, and `context_footprint`. These fields are advisory evidence for context loading and user decisions, not command approval, bead activation, or active memory.

`logs/work-graph.json` and `logs/work-graph.md` may expose bead, PRD, owner-file, check, blocker, follow-up, and transition relationships compiled from existing Precode surfaces. They are inspection evidence only; they must not become a second task tracker, choose work, approve transitions, rewrite beads, or replace markdown authority.

The Doctor Dashboard inside `OS-HEALTH.md` and `logs/os-health.json` is a generated report extension. It may summarize warning sources, plain-English triage labels, safe asks, do-not-approve warnings, owner commands, owner protocols, severity, and shortest repair paths from existing compiled state. It must not become a standalone router, approve transitions, approve commands, approve repair, approve cleanup, select tasks, mutate files, or replace `scripts/next-step.py`.

ZYAL-like export belongs in an adapter or extension that maps the generic Precode run-contract profile to that host. The generic Precode profile must prove useful before any host-specific contract becomes a maintained surface.

## Mutation Rules

External integrations start read-only.

Mutation requires all of these:

- a user-approved bead names the external system in scope
- the bead lists the exact allowed mutation
- secret handling is documented without storing secrets
- checks and rollback or escape path are named
- the user performs or explicitly approves the manual gate

Scheduled audits, importers, generated reports, and source-intake helpers must remain read-only unless a separate approved execution bead explicitly says otherwise.

Bounded local engines such as Ralph may run explicit local attempt commands only inside the active bead boundary. They must stop before approval-required, destructive, secret-bearing, or external mutation actions unless the active bead and user approval gate allow the exact action.

## Promotion Path

Extension findings become action only after user review:

| Finding type | Promotion destination |
|---|---|
| Product requirement | `tasks/prds/*.md` and compiled `FEATURES.md` |
| Product or technical decision | `DECISIONS.md` |
| Architecture, API, data, security, or acceptance fact | Owning authority file |
| Work to perform | Proposed or approved bead |
| Repeated process lesson | Relevant protocol, adapter, or agent rule |
| Generated report gap | Follow-up bead or validator/audit improvement |

## Command Wrapper Rule

The Doctor Dashboard health extension is allowed as generated OS Health evidence. The local `precode` CLI wrapper is allowed only as a facade over trusted commands that prints the exact underlying command, preserves exit codes, and keeps canonical scripts and Markdown owner files authoritative.

Do not introduce broad command runners, package-manager behavior, release channels, registries, optional-pack installation, hidden setup approval, standalone `precode doctor` behavior, or external mutation through a wrapper. Wrappers should compose trusted commands, not become the place where Precode discovers its operating model.

## Extension Checklist

Use this checklist before adding or accepting an extension:

```text
Extension name:
Extension type:
Capability being added:
Owning protocol or adapter:
Script, command, or surface exposed:
Generated evidence written:
Active-memory files unchanged:
Authority files affected:
External systems touched:
Read-only by default:
User approval gates:
Secrets or privacy exclusions:
Validation command:
Promotion path for findings:
Rollback or removal note:
```

## Current Example

GitHub is the first concrete example of this pattern.

`tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md` owns the rules. `scripts/github-audit.py` and `scripts/import-github-sources.py` read GitHub status or source material and write generated evidence. GitHub issues, pull requests, checks, and Actions remain external evidence until a user promotes conclusions into Precode-owned files.
