# Release Readiness Curated Pack Exemplar
<!-- ANCHOR: release-readiness-curated-pack-exemplar -->

> AUTHORITY: Official non-installable curated pack exemplar review shape for grouping existing PrecodeOS release-readiness surfaces.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, review acceptance, release approval, deployment approval, command approval, generated evidence truth, skill installation, package registry, optional-pack installation, release-channel behavior, package-manager behavior, or target-project mutation.
> LOAD_WHEN: Reviewing how an official curated pack-shaped PrecodeOS capability should declare owner surfaces, validation, forbidden effects, active-memory impact, and removal notes before any pack distribution exists.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-06

## Purpose

Pack status: exemplar-review-shape

This exemplar shows how a future curated PrecodeOS pack-shaped review artifact can group related existing surfaces without becoming an installable pack, package manifest, registry entry, marketplace listing, command wrapper, host-plugin dependency, update path, release channel, package-manager behavior, or target-project mutation path.

Use it as review evidence when a maintainer or contributor needs to inspect whether a pack-shaped proposal has named its owners, validation, approval gates, forbidden effects, active-memory impact, and removal path clearly enough for Extension Protocol review.

This exemplar does not create optional-pack distribution. It does not approve release, deploy, activate work, install skills, mutate GitHub or providers, write generated proof, or make generated metadata authoritative.

## Exemplar Metadata

```yaml
pack:
  id: release-readiness-review-pack
  status: exemplar-review-shape
  owner_protocol: tasks/reference/EXTENSION-PROTOCOL.md
  capability_being_grouped: release-readiness evidence and approval-question review
  included_surfaces:
    - tasks/reference/RELEASE-READINESS-PROTOCOL.md
    - tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md
    - tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md
    - tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md
    - tasks/reference/PROMPT-PATTERNS.md
    - .agents/README.md
    - .agents/skills/release-readiness/SKILL.md
  pack_categories:
    - release-readiness
    - verification
    - human-approval-review
  authority_files_affected:
    - tasks/reference/EXTENSION-PROTOCOL.md
    - tasks/reference/RELEASE-READINESS-PROTOCOL.md
    - tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md
  generated_evidence: none
  active_memory_changes: none
  external_systems_touched: none
  read_only_by_default: true
  user_approval_gates:
    - release approval
    - deployment approval
    - merge approval
    - rollback approval
    - migration approval
    - dashboard or provider mutation approval
    - GitHub mutation approval
    - external mutation approval
  validation:
    - python3 scripts/clarity-scenario-check.py
    - python3 scripts/extension-check.py
    - python3 scripts/file-inventory.py --check
  forbidden_effects:
    - active-memory expansion
    - task selection
    - PRD approval
    - bead activation
    - review acceptance
    - release approval
    - deployment approval
    - command approval
    - generated proof
    - generated metadata authority
    - host skill installation
    - command-wrapper behavior
    - registry behavior
    - marketplace behavior
    - optional-pack installation
    - install/update behavior
    - release-channel behavior
    - package-manager behavior
    - target-project mutation
  removal_note: remove this exemplar by deleting this template and its explicit references; no installed assets, registries, package metadata, target files, or external state need rollback.
  distribution_behavior: none
  registry_or_marketplace_behavior: none
  install_update_package_manager_behavior: none
```

## Included Surface Roles

| Surface | Role in exemplar | Boundary |
|---|---|---|
| `tasks/reference/RELEASE-READINESS-PROTOCOL.md` | Owns release-readiness evidence fields, decision states, rollback or blocked escape, and approval questions. | Does not approve release, deploy, mutate providers, or replace human approval. |
| `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` | Owns proof tiers, manual verification shape, sensitive gates, and evidence-quality expectations. | Does not create proof by itself or certify production readiness. |
| `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` | Owns Closeout Evidence, review return, and transition boundaries. | Does not accept implementation or approve transition from release evidence alone. |
| `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md` | Owns Release Readiness Skill as a read-only invocation playbook. | Does not install skills, add command wrappers, or create optional packs. |
| `tasks/reference/PROMPT-PATTERNS.md` | Provides copyable release-readiness and release-candidate review prompts. | Teaching and invocation aid only; not active memory or approval authority. |
| `.agents/README.md` and `.agents/skills/release-readiness/SKILL.md` | Provide host-discoverable packaging for compatible agent tools. | Host packaging only; not a Precode skill catalog, registry, marketplace, or package manager. |

## Review Checklist

Before copying this shape for another future curated pack proposal, confirm:

- the grouped capability already has stable owner protocols or docs
- each included surface keeps its existing authority contract
- validation commands are named and local
- generated evidence, if any, is demoted and owned elsewhere
- active memory remains exactly `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- no host skill, example, metadata block, generated report, or template becomes authority
- no install/update, registry, marketplace, release-channel, package-manager, or target-project mutation behavior is introduced
- removal is documentation-only unless a separate approved package change explicitly adds maintained assets

## Stop Conditions

Stop review and return to the Extension Protocol if a proposed pack-shaped change:

- requires a pack manifest, registry listing, marketplace entry, installer, package manager, or host-plugin installation
- adds active-memory files or hidden owner surfaces
- lets generated metadata choose work, approve commands, approve release, accept implementation, or replace owner protocols
- mutates target projects, GitHub, providers, dashboards, secrets, deployment state, or external systems without a separate approved bead and explicit user gate
- uses this exemplar as permission to distribute optional packs
