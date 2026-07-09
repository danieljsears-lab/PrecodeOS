# PrecodeOS -- Extension Protocol
<!-- ANCHOR: extension-protocol -->

> AUTHORITY: Extension rules, extension types, skill-playbook boundaries, authority boundaries, active-memory limits, generated-output boundaries, mutation boundaries, and extension review checklist for adding PrecodeOS capabilities.
> NOT_AUTHORITY: Active memory, task selection, product decisions, implementation plans, external mutation approval, generated progress state, or plugin registry.
> LOAD_WHEN: Adding or reviewing a Precode adapter, protocol, skill playbook, importer, audit, generated report, bead template, or external integration.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.23
Last updated: 2026-07-08

## Purpose

Extensions let PrecodeOS grow without turning into a giant prompt or a hidden automation system.

An extension may add a tool surface, workflow protocol, skill playbook, source importer, audit, generated report, bead template, AI-readable navigation index, or external integration. It must not add active-memory files or let generated evidence choose work.

Use `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` when an extension packages a named host-agent prompt playbook, docs-help invocation, beginner workflow invocation, maintainer package-review playbook, or extension-review playbook. Skill playbooks are read-only in v1 and must point back to their owner protocols or canonical docs.

Use `.agents/README.md` when inspecting host-discoverable skill files under `.agents/skills/`. Those files are host skill contracts, not PrecodeOS skill playbooks, and they do not expand active memory, approve commands, create a package registry, or replace the Skill Playbook Protocol.

Use the Skill / Extension Review Skill in `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` when the user wants a structured advisory review of a proposed skill or extension before implementation. The review output is input to this protocol; it does not approve the extension, install a skill, mutate files, add a registry, or create optional-pack behavior.

Use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` when an extension exposes commands, touches external systems, logs non-check tool runs, wraps existing commands, or needs tool-call approval boundaries.

Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when an extension introduces a new integration boundary, provider abstraction, workflow state, audit trail, or other reusable implementation shape.

PrecodeOS's existing owner files, protocols, scripts, generated sidecars, recorded checks, adapters, and transparent command facades form an advisory repo-native harness contract. Treat harness hardening as boundary and contract work, not as permission to add a Harness Protocol, agent runtime, sandbox, command approval layer, registry, optional pack, package manager, install/update system, or enforcement layer.

Use `llms.txt` only as a compact navigation index for stable canonical PrecodeOS documentation. It is not active memory, a generated evidence report, a runtime integration contract, a package registry, or permission to compress, proxy, wrap, install, update, or mutate tools.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Use the Context Layer Matrix in `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` when an extension touches adapters, shims, skill playbooks, generated reports, reviewed memory, source evidence, or maintainer-local context. Extensions may add or improve one layer, but they must not let that layer become active memory, task authority, approval, or a hidden operating model.

Future host shims and native rule-directory surfaces must start as advisory compatibility notes in `adapters/ADAPTER-INDEX.md` or a specific adapter, then pass extension review before they become shipped Precode surfaces. Do not add broad host support promises from speculative model, IDE, agent, pricing, quota, or cloud-runner behavior.

Future host-facing contract consumption may become stricter only after advisory run contracts, command classification, and wrapper boundaries prove stable in real use. Any stricter host adapter must remain subordinate to owner files, active beads, recorded proof, user approval gates, and the Tool Execution Protocol; it must not silently become runtime enforcement or command approval.

Future optional packs are governed by this protocol before any pack distribution exists. A pack boundary spec may describe what a future pack is allowed to contain, but it must not create pack installation, registry, marketplace, update, release-channel, or package-manager behavior.

The Artifact Chooser in `tasks/reference/PROMPT-PATTERNS.md` is an index over existing prompts and artifacts, not an extension type. Do not treat it as a template registry, marketplace, optional pack, package manager, hidden task selector, automatic artifact generator, skill playbook, command wrapper, or approval surface. If artifact selection depends on active state, route through Workflow Selection or the owning protocol.

Future retrieval-backed memory is governed by this protocol before any database, MCP server, shared backend, dashboard, REST API, vector index, embedding layer, or cross-machine memory surface becomes a public package feature. Reviewed filesystem memory remains the default source of durable learning; retrieval backends may accelerate recall, but they must not become active memory, task selection, owner-file authority, promotion approval, external mutation, automatic write access, registry behavior, optional-pack installation, or package-manager behavior. `memory-check.py --retrieval-review` is a readiness review only: it may show token pressure, card hygiene, and query miss evidence, but it does not approve a backend.

## Extension Types

| Type | Purpose | Usual owner |
|---|---|---|
| Adapter | Tool-specific guidance for a coding agent | `adapters/*.md` or a tool shim |
| Protocol | Workflow rules for a repeatable Precode process | `tasks/reference/*.md` |
| Skill playbook | Read-only host-agent invocation guidance for stable docs help, an existing Precode workflow, or extension review | `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` plus the owner protocol, canonical docs, or adapter |
| Importer | Reads source material or telemetry and normalizes evidence | `scripts/import-*.py` |
| Approval-gated local queue helper | Previews Candidate Queue import or shaping actions and applies only explicit approved action IDs | `tasks/reference/CANDIDATE-QUEUE-PROTOCOL.md` plus `scripts/candidate-queue.py` |
| Audit | Reads project or external status and reports findings | `scripts/*-audit.py` or read-only preview scripts such as `scripts/team-collaboration-check.py` and `scripts/session-friction-check.py` |
| Generated report | Human-readable or machine-readable evidence output | `logs/`, `OS-HEALTH.md`, or `PROGRESS.md` |
| Generated execution profile | Machine-readable run-contract export for a host or adapter | `logs/run-contract.json` and `logs/run-contract.yaml` |
| AI-readable navigation index | Compact stable-docs index for AI assistants and documentation tools | `llms.txt` plus canonical Markdown owner files |
| Future retrieval-backed memory | Deferred optional retrieval layer for reviewed memory cards or approved memory exports | `tasks/reference/MEMORY-PROTOCOL.md`, this protocol, and a future extension review |
| Bead template | Repeatable task shape with the standard bead contract | `tasks/beads/BEAD-SCHEMA.md` |
| Bounded attempt engine | Opt-in local loop that runs one explicit attempt command, validators, and generated attempt evidence for one active bead | `tasks/reference/RALPH-LOOP-PROTOCOL.md` plus `scripts/ralph-loop.py` |
| External integration | Read-only or approved interaction with outside systems | Integration protocol plus `PROJECT-CONTEXT.md` |
| Role contract | Compact mode card for bounded agent behavior | `modes/*.md` |
| Future optional pack | Deferred package of related PrecodeOS reference surfaces, examples, or checks that must pass extension review before distribution | `tasks/reference/EXTENSION-PROTOCOL.md` plus the specific owning protocols or adapters |

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
- Keep context layers distinct: adapters translate, skill playbooks invoke, generated reports summarize, reviewed memory or raw evidence informs, and maintainer-local files guide package maintenance only.
- Keep host compatibility advisory-first until a repeated, validated gap warrants a shipped adapter or shim.
- Keep future optional packs explicit, reviewable, and non-installable until separate approved package work defines distribution behavior.
- Keep AI-readable navigation indexes as indexes only: they may point to canonical docs and protocols, but they must not summarize away source evidence, select work, approve commands, define runtime integration behavior, or replace owner files.
- Keep retrieval-backed memory optional and reviewed: no required Postgres, pgvector, Docker, MCP server, REST API, dashboard, shared backend, semantic index, embedding layer, automatic agent write access, external mutation, or cross-machine memory dependency may be added without a separate approved extension after readiness evidence shows plain-file recall is insufficient.

## Future Pack Boundary Spec

Optional packs are deferred. This section defines boundary rules for discussing or reviewing future packs before PrecodeOS ships any pack distribution surface.

A future pack may contain related reference protocols, templates, examples, scripts or checks, adapter notes, generated-evidence profile definitions, and documentation. Each included surface must keep its normal owner file, authority contract, validation path, and promotion path.

A future pack must not:

- add or replace active-memory files
- hide authority in generated output, host registries, examples, or metadata
- choose tasks, approve PRDs, approve beads, approve reviews, approve releases, approve setup, or approve commands
- require root shims, native rule directories, adapter files, hooks, CI, package managers, or host plugins
- create auto-update, release-channel, install/update, package-manager, registry, marketplace, or optional-pack installation behavior
- mutate external systems or target projects unless a separate approved bead and user gate allow the exact mutation
- make maintainer-local files public package authority

Illustrative non-installable metadata shape:

```yaml
pack:
  id: example-readiness-pack
  status: illustrative-only
  owner_protocol: tasks/reference/EXTENSION-PROTOCOL.md
  included_surfaces:
    - tasks/reference/EXAMPLE-PROTOCOL.md
    - tasks/templates/EXAMPLE-TEMPLATE.md
  generated_evidence: none
  active_memory_changes: none
  external_mutation: none
  validation:
    - python3 scripts/extension-check.py
  forbidden_effects:
    - task approval
    - command approval
    - installation
    - registry behavior
    - package-manager behavior
```

The example above is a review shape only. It is not a shipped pack, install manifest, registry record, package index, or permission to distribute optional packs.

## Authority Contract Rules

Reference and generated markdown added by an extension must include:

- canonical anchor
- `AUTHORITY`
- `NOT_AUTHORITY`
- `LOAD_WHEN`
- `CLASS`

Use `CLASS: reference` for durable rules and `CLASS: generated` for reports.

AI-readable text indexes should carry the same authority, non-authority, load trigger, and class metadata even when they are not Markdown documents.

Generated markdown must clearly say it is not active memory, not a task plan, and not an instruction source.

## Generated Output Rules

Generated evidence should live under `logs/` unless a legacy Precode report already owns the surface.

Generated JSON and JSONL files must be treated as evidence only. They may feed summaries, audits, or human review, but they must not directly rewrite active memory, bead state, PRDs, decisions, or product authority files.

Generated reports, sidecars, and public generated HTML added by an extension should be represented in `logs/authority-map.json` surface classes when the generated map is refreshed. That classification is orientation evidence only; it does not approve the extension, make generated output authoritative, or replace the owning protocol, adapter, PRD, decision, authority file, or approved bead.

`logs/run-contract.json` and `logs/run-contract.yaml` are generated execution profiles compiled from the active bead. They may help a future host adapter enforce allowed actions and proof needed, but they are not authority and do not approve commands.

`logs/next-step.json` may include generated router fields such as `load_plan`, `single_next_protocol`, `context_footprint`, recovery prompt fields, stable-fix eligibility, and advisory-only flags. These fields are advisory evidence for context loading and user decisions, not command approval, bead activation, or active memory. `scripts/clarity-scenario-check.py` protects key presence and category shape so future wrappers can rely on the generated interface without treating it as authority.

`logs/work-graph.json` and `logs/work-graph.md` may expose bead, PRD, owner-file, check, blocker, follow-up, and transition relationships compiled from existing Precode surfaces. They are inspection evidence only; they must not become a second task tracker, choose work, approve transitions, rewrite beads, or replace markdown authority.

`logs/build-attribution-ledger.json` and `logs/build-attribution-ledger.md` may expose reviewed human contributor, contributor role, agent/tool surface, attribution reviewer, uncertainty, Git author hints, and bead-level attribution gaps compiled from closeout and generated journal evidence. They are inspection evidence only; they must not choose work, accept implementation, approve merge, approve release, assign blame, score contributors, create telemetry, mutate GitHub, create a command wrapper, or create registry, optional-pack, install/update, or package-manager behavior.

`logs/team-collaboration-preview.json` may expose Small Team Collaboration Lane branch/worktree state, active bead scope, owner-file impact candidates, re-entry risks, and optional GitHub evidence compiled from local repo state and read-only `gh` calls. It is inspection evidence only; it must not choose work, activate beads, approve merge, mutate GitHub, create a project-management layer, create a command wrapper, or create module, registry, runtime-toggle, optional-pack, installer, update-channel, or package-manager behavior.

`logs/session-friction-review.json` may expose Session Friction Review findings compiled from tool-run, check, loop, completion/handoff, and reviewed-memory summary evidence. It is a read-only audit and generated evidence only; it must not choose work, approve commands, promote memory, edit owner files, accept review, mutate generated reports directly, create telemetry, create runtime compression, add a command wrapper, create a registry, create optional-pack behavior, or create package-manager behavior.

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

Candidate Queue helpers are a narrow exception only when their owning protocol defines preview/apply behavior. `scripts/candidate-queue.py` may write only approved action IDs to `CANDIDATE-QUEUE.md`; preview output remains non-authority and must not approve PRDs, activate beads, mutate `tasks/todo.md`, reserve `B###` IDs, choose work, or authorize implementation.

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
