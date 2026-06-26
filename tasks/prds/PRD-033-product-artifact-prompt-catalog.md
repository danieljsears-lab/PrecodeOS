---
prd_id: PRD-033
status: approved
owner: Dan Sears / Recode
created: 2026-06-26
last_updated: 2026-06-26
feature_link: Product Artifact Template / Prompt Catalog
features_status: not compiled
related_prds:
  - PRD-031
  - PRD-029
  - PRD-030
---

# PRD-033 -- Product Artifact Template / Prompt Catalog
<!-- ANCHOR: prd-033-product-artifact-prompt-catalog -->

> AUTHORITY: Public requirements for the PrecodeOS Artifact Chooser and prompt-catalog routing guidance.
> NOT_AUTHORITY: Active memory, task selection, roadmap approval, PRD approval, bead activation, implementation acceptance, review acceptance, release approval, template registry behavior, optional-pack behavior, automatic artifact generation, generated prompt-output authority, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Choosing which PrecodeOS artifact, prompt, or workflow surface to use before asking an agent to continue.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-26

## Summary

PrecodeOS should help builders choose the right artifact or prompt without turning artifact selection into a hidden task selector.

The Product Artifact Template / Prompt Catalog adds a compact Artifact Chooser to existing prompt and user-guide surfaces. It maps common user moments to the next Precode artifact, owner source, and stop condition while preserving Workflow Selection for current-state decisions.

## Problem

PrecodeOS now has many useful artifact paths: product ideation, Local Source Intake, PRD shaping, Candidate Queue, bugfix specs, Review Lanes, PRD handoff readiness, release evidence, team coordination, and recovery. A beginner may know that Precode has a prompt for the moment but not know which one to paste first.

A catalog can improve discoverability, but the wrong implementation would create a template registry, marketplace, optional pack, automatic artifact generator, or another authority layer.

## Goals

- Add a compact chooser that maps user moments to existing artifacts and prompts.
- Keep artifact selection subordinate to active memory, owner files, owner protocols, and user approval.
- Route uncertain or current-state-dependent cases to Workflow Selection instead of guessing.
- Preserve evidence-only treatment for generated reports, source notes, imported issues, handoffs, journals, ledgers, and previews.
- Keep the implementation in existing docs, prompt patterns, protocol boundary notes, package inventory, and deterministic text-contract coverage.

## Non-Goals

- No template registry, marketplace, optional-pack system, or package-manager behavior.
- No automatic artifact generation, prompt-output authority, task selection, PRD approval, bead activation, review acceptance, transition approval, release approval, or implementation permission.
- No new command, checker command, generated catalog sidecar, hosted workspace, plugin registry, or external integration.
- No new active-memory file and no private maintainer-file dependency in public docs.

## Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-033-FR01` | `tasks/reference/PROMPT-PATTERNS.md` must include an Artifact Chooser that maps common moments to the artifact or prompt to use first. | P0 | Prompt-catalog surface. |
| `PRD-033-FR02` | The chooser must cover rough idea, workflow choice, Local Source Intake, PRD shaping, Candidate Queue, bugfix spec, Review Lanes, PRD handoff readiness, release evidence, team coordination, and recovery. | P0 | Existing artifact families only. |
| `PRD-033-FR03` | User-facing docs must expose a short chooser or prompt so beginners can find the right artifact without browsing every protocol. | P0 | Daily Cockpit and User Guide. |
| `PRD-033-FR04` | Skill Playbook and Extension Protocol guidance must state that the chooser is an index/prompt aid, not a skill, registry, optional pack, command wrapper, task selector, or artifact generator. | P1 | Boundary hardening. |
| `PRD-033-FR05` | Package inventory must describe the new PRD and updated prompt/protocol surfaces accurately. | P1 | Public reference follow-through. |
| `PRD-033-FR06` | `scripts/clarity-scenario-check.py` must enforce the chooser's artifact coverage and anti-registry/anti-generator wording. | P1 | Deterministic text contract. |
| `PRD-033-FR07` | Maintainer changelog, roadmap, roadmap journal, and generated reading surfaces must be refreshed after implementation. | P1 | Maintainer-history follow-through. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-033-FR01` / `PRD-033-FR02` | Prompt Patterns includes the Artifact Chooser with all required artifact families and owner-source routing. | Source review and clarity scenario coverage. |
| `PRD-033-FR03` | Daily Cockpit and User Guide expose concise artifact-selection guidance without crowding the main loops. | Source review. |
| `PRD-033-FR04` | Skill Playbook and Extension Protocol preserve prompt/index-only boundaries. | Source review and clarity scenario coverage. |
| `PRD-033-FR05` | Package inventory includes PRD-033 and updated prompt/protocol descriptions. | Source review. |
| `PRD-033-FR06` | `python3 scripts/clarity-scenario-check.py` passes. | Command output. |
| `PRD-033-FR07` | Roadmap, changelog, journal, PRD HTML, docs HTML, and roadmap HTML are current. | Validation commands. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/docs-html.py --check
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
python3 scripts/version-check.py
git diff --check
```

## Boundaries

The Artifact Chooser is a navigation aid over existing PrecodeOS workflows. It does not decide the next task, approve work, create artifacts automatically, replace Workflow Selection, or change the authority of templates, prompts, generated reports, owner files, PRDs, beads, Review Lanes, release evidence, or recovery guidance.

When the next step depends on active memory, the active bead, generated evidence, local errors, current repo state, or what work should happen next, the chooser must route to Workflow Selection or the owning protocol instead of selecting work by itself.
