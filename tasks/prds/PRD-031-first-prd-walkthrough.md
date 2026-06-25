---
prd_id: PRD-031
status: approved
owner: Dan Sears / Recode
created: 2026-06-24
last_updated: 2026-06-24
feature_link: First PRD Walkthrough
---

# PRD-031 -- First PRD Walkthrough
<!-- ANCHOR: prd-031-first-prd-walkthrough -->

> AUTHORITY: Public requirements for the First PRD Walkthrough guidance path from rough idea to PRD readiness.
> NOT_AUTHORITY: Active memory, task selection, automatic PRD drafting, PRD approval, bead activation, implementation permission, roadmap or backlog authority, generated progress, external integrations, hosted workspace behavior, command-wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating the beginner-facing First PRD Walkthrough guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-24

## Summary

PrecodeOS should give first-time non-technical builders one visible path from a rough idea to PRD readiness without pretending the path approves a PRD or authorizes coding.

The First PRD Walkthrough packages existing Product Ideation Workbook, Precode Idea Coach, Product Brief, Challenge And Clarity, Conviction Packet, Local Source Intake, and gentle PRD ramp guidance into a named walkthrough across current public docs and protocols.

## Problem

PrecodeOS already has strong product-definition pieces, but a new builder can miss the shortest safe sequence. That creates two opposite risks: the builder may stall before PRD shaping, or the agent may jump from excitement, research, or workbook evidence directly into requirements or code.

## Goals

- Make the rough-idea-to-PRD-readiness path easy to find from daily and onboarding surfaces.
- Name "First PRD Walkthrough" as a beginner-facing request that routes through existing protocols.
- Preserve Product Brief, Conviction Packet, research notes, and workbook output as evidence only.
- Keep Local Source Intake before PRD shaping when a Conviction Packet or source material is used.
- Keep human PRD approval before feature compilation, decomposition, bead proposal activation, or coding.
- Add narrow text-contract coverage so future edits do not turn the walkthrough into hidden authority.

## Non-Goals

- No new public protocol file.
- No new command, checker command, readiness score, or generated report.
- No automatic PRD drafting or approval.
- No generated PRD authoring surface, export hub, hosted workspace, MCP mutation, SaaS runtime, or external integration.
- No PRD approval shortcut, bead activation path, task selection, roadmap or backlog creation, owner-file mutation, or implementation permission.
- No command-wrapper, registry, optional-pack, install/update, release-channel, or package-manager behavior.
- No edits to active memory or normal task state.

## Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-031-FR01` | Public user and daily guide surfaces must include a named First PRD Walkthrough entrypoint. | P0 | The path must be visible without reading the whole PRD protocol first. |
| `PRD-031-FR02` | Idea-to-PRD, PRD, Workflow Selection, and Prompt Patterns surfaces must route the walkthrough through the existing evidence-first sequence. | P0 | No new protocol file for v1. |
| `PRD-031-FR03` | The walkthrough must state that Product Briefs, Conviction Packets, workbook output, and research are evidence only. | P0 | These artifacts do not approve requirements or implementation. |
| `PRD-031-FR04` | The walkthrough must require Local Source Intake before PRD shaping when the builder brings a Conviction Packet, workbook output, notes, research, screenshots, or similar source material. | P0 | Prevents direct packet-to-requirements promotion. |
| `PRD-031-FR05` | The walkthrough must preserve human PRD approval before feature compilation, decomposition, bead activation, or coding. | P0 | PRD approval remains a separate human gate. |
| `PRD-031-FR06` | `scripts/clarity-scenario-check.py` must include text-contract coverage for the walkthrough's authority boundaries. | P1 | Existing checker only; no new command. |
| `PRD-031-FR07` | Package inventory, maintainer changelog, roadmap, roadmap journal, and generated docs/PRD/roadmap surfaces must be updated. | P1 | Maintainer-history follow-through is part of done. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-031-FR01` / `PRD-031-FR02` | User Guide, Daily Cockpit, How-To guide, Idea-to-PRD, PRD Protocol, Workflow Selection, and Prompt Patterns include the named walkthrough and route it through existing surfaces. | Static review and generated docs. |
| `PRD-031-FR03` / `PRD-031-FR04` / `PRD-031-FR05` | The text-contract fixture fails if required boundary language disappears from owner surfaces. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-031-FR06` | The walkthrough fixture is part of the existing clarity scenario check and adds no standalone command. | Code review and command output. |
| `PRD-031-FR07` | PRD HTML, docs HTML, maintainer roadmap HTML, changelog, and roadmap journal reflect the shipped slice. | Generated surface checks. |

## Required Validation

```bash
python3 scripts/clarity-scenario-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
```

## Boundaries

The First PRD Walkthrough is a discoverability and guidance layer over existing PrecodeOS workflows. It can help a builder ask for the right next artifact, but it cannot decide the product, approve a PRD, create or activate beads, mutate owner files, select tasks, or authorize implementation.

