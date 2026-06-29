---
prd_id: PRD-034
status: approved
owner: Dan Sears / Recode
created: 2026-06-29
last_updated: 2026-06-29
risk_level: low
feature_link: Many-Bead Operating Rhythm
features_status: not compiled
related_prds:
  - PRD-031
  - PRD-033
---

# PRD-034 -- Many-Bead Operating Rhythm
<!-- ANCHOR: prd-034-many-bead-operating-rhythm -->

> AUTHORITY: Public requirements for the beginner-facing Many-Bead Operating Rhythm guidance.
> NOT_AUTHORITY: Active memory, task selection, Candidate Queue ranking, PRD approval, bead activation, review acceptance, transition approval, implementation acceptance, generated proof, generated report authority, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the repeated bead-work rhythm after the first PrecodeOS product slice.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-29

## Summary

PrecodeOS should make repeated work across many beads feel like one small daily rhythm instead of a tour through every report, prompt, review path, and queue.

The Many-Bead Operating Rhythm adds a beginner-facing orientation checklist: `Active -> Changed -> Proven -> Parked -> Approval -> Next`. It points to existing sources and approval gates. It does not create a new workflow, report, command, script behavior, or authority layer.

## Problem

The first-product spine is now visible: `Idea -> Brief -> Packet -> Intake -> PRD -> Bead -> Proof -> Review -> Close`. After a builder completes the first bead, the repeated loop can still feel larger than it is because active work, changed files, proof, parked intent, review, approval, closeout, and next-step guidance live across several surfaces.

A compact rhythm can help a beginner ask the same evidence-backed questions every time without letting an agent choose work or activate the next bead.

## Goals

- Add a compact repeated bead-work rhythm for beginner builders.
- Map each rhythm word to existing PrecodeOS sources and gates.
- Preserve the separation between active work, proof, parked intent, review, transition approval, and next guidance.
- Keep implementation in existing docs, prompt patterns, workflow guidance, completion/handoff guidance, package inventory, and text-contract validation.
- Avoid creating a new public protocol file, command, checker command, generated rhythm report, workflow authority, or runtime behavior.

## Non-Goals

- No task selection, Candidate Queue ranking, PRD approval, bead activation, review acceptance, transition approval, or implementation acceptance.
- No replacement for `next-step.py`, Workflow Selection, Work Graph, Daily Cockpit, closeout, or Session Completion/Handoff Protocol.
- No new script, generated report, command wrapper, CLI alias, public protocol file, active-memory field, schema requirement, registry, optional pack, install/update behavior, release-channel behavior, or package-manager behavior.
- No support-specific doc expansion in v1 unless core-surface validation reveals a direct contradiction.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-034-FR01` | Daily Cockpit must expose the every-bead rhythm `Active -> Changed -> Proven -> Parked -> Approval -> Next` near the beginner path and daily loop. | P0 | Primary beginner surface. |
| `PRD-034-FR02` | User Guide must explain how the rhythm supports repeated work, done review, approval, and copyable prompts without becoming a workflow. | P0 | Deeper manual. |
| `PRD-034-FR03` | Prompt Patterns must add a compact `Rhythm` alias or prompt that asks for the six fields without activating anything. | P0 | Copyable invocation. |
| `PRD-034-FR04` | Workflow Selection Protocol must state that after the first product spine, repeated work can orient through the rhythm before choosing the next workflow. | P1 | Protocol alignment. |
| `PRD-034-FR05` | Session Completion/Handoff Protocol must map changed, proven, parked, approval, and next fields to existing closeout, queue, review, transition, and handoff evidence. | P1 | Completion/handoff alignment. |
| `PRD-034-FR06` | Package inventory must describe PRD-034 and the updated affected surfaces. | P1 | Public reference follow-through. |
| `PRD-034-FR07` | `scripts/clarity-scenario-check.py` must enforce rhythm wording and forbidden-action boundaries as a text contract only. | P1 | No new user command. |
| `PRD-034-FR08` | Maintainer changelog, roadmap, roadmap journal, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer follow-through. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-034-FR01` / `PRD-034-FR02` | Daily Cockpit and User Guide expose the rhythm and map it to active bead, changed files, proof, Candidate Queue, approval, and next guidance. | Source review and generated docs HTML. |
| `PRD-034-FR03` | Prompt Patterns includes a `Rhythm` alias or copyable prompt with explicit no-activation wording. | Source review. |
| `PRD-034-FR04` / `PRD-034-FR05` | Workflow Selection and Session Completion/Handoff preserve existing authority and approval gates while naming the rhythm. | Source review. |
| `PRD-034-FR06` | Package inventory lists PRD-034 and updated affected surfaces. | Source review. |
| `PRD-034-FR07` | Clarity scenario coverage fails if rhythm wording or forbidden-action boundaries disappear. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-034-FR08` | Roadmap, changelog, journal, PRD HTML, docs HTML, and roadmap HTML are current. | Validation commands. |

## Required Validation

```bash
bash scripts/validate-memory.sh
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/clarity-scenario-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
python3 _maintainer/scripts/roadmap-maintenance.py
git diff --check
```

## Boundaries

The rhythm is an orientation checklist over existing PrecodeOS surfaces:

- Active: `tasks/todo.md`, active bead, and primary authority file.
- Changed: changed-file summary and Closeout Evidence.
- Proven: recorded checks, manual verification, proof traces, and review evidence.
- Parked: Candidate Queue or explicit defer/kill destination for future intent.
- Approval: review decision, transition proposal, and user approval still required.
- Next: session start, Workflow Selection, `next-step.py`, or transition proposal guidance.

`Parked` must not imply Candidate Queue chooses work. `Next` must not imply transition approval. The rhythm must not accept implementation, approve review, approve PRDs, activate beads, choose tasks, rank candidates, mutate owner files, or treat generated output as authority.
