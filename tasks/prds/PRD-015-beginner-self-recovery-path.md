---
prd_id: PRD-015
status: approved
owner: user
risk_level: medium
feature_link: Beginner Self-Recovery Path
features_status: not compiled
related_prds:
  - PRD-012
---

# PRD-015 -- Beginner Self-Recovery Path
<!-- ANCHOR: prd-015-beginner-self-recovery-path -->

> AUTHORITY: Destination shard for the exact beginner stuck-trigger recovery path.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, implementation acceptance, destructive repair approval, generated evidence truth, automatic rollback policy, setup/update mutation, command-wrapper behavior, package-manager behavior, or support-bot authority.
> LOAD_WHEN: Reviewing, implementing, or decomposing beginner stuck-trigger recovery guidance across active memory, public docs, and recovery protocols.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-15

## State

- ID: `PRD-015`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-15`

## Feature Link

- Feature: `Beginner Self-Recovery Path`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-012`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | user clarification`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Beginner Self-Recovery Path`
  - `AGENT.md`
  - `docs/PRECODE-DAILY-COCKPIT.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `tasks/reference/RECOVERY-PROTOCOL.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `tasks/prds/PRD-012-precode-doctor-dashboard.md`
- Stable facts:
  - PrecodeOS already has recovery protocols, troubleshooting docs, next-step recovery prompts, and Doctor Dashboard diagnostics.
  - Beginners still need the exact phrase `I am stuck, help me` to produce prescriptive guidance rather than a generic documentation pointer.
  - Generated reports and diagnostics are evidence only.
- Assumptions:
  - The first implementation should be active-agent guidance plus public docs/protocols, not a new command, chatbot, checker gate, or auto-repair flow.
  - Prescriptive guidance means clear next steps and stop conditions, not mutation permission.

## Problem

Unsupported beginners may say "I am stuck, help me" before they can classify whether the issue is active state, generated reports, missing proof, scope drift, setup confusion, or approval confusion.

## User Moment

- Before: A user asks for help while stuck and may receive a link, a broad troubleshooting suggestion, or premature repair.
- After: The loaded agent and public docs require a prescriptive recovery response with the symptom, first safe move, likely owner surface, up to three read-only checks, next safe action, and forbidden actions.
- Why now: The package has strong recovery pieces, but beginner recovery should work from natural stuck language.

## Destination

- Destination statement: Saying `I am stuck, help me` triggers a visible recovery response contract before edits or repair.
- Definition of done:
  - `AGENT.md` contains the active-agent stuck trigger and response shape.
  - Daily Cockpit, Troubleshooting, Recovery Protocol, Support Runbook, and Prompt Patterns expose the same phrase and contract.
  - Deterministic clarity scenario coverage verifies the phrase and required response elements.
  - Package inventory, generated docs/PRD/roadmap surfaces, roadmap history, roadmap journal, and maintainer changelog are current.
- First useful vertical slice: active-memory trigger plus public docs/protocol prompt contract only.

## Users

- Primary user: Beginner or non-technical builder who cannot classify why Precode feels stuck.
- Secondary user: Support engineer or AI coding agent helping diagnose the stuck state.
- Excluded user: Automation expecting permission to repair, roll back, transition, set up, update, or mutate files from the stuck phrase alone.

## Goals

- Goal 1: Make the exact phrase `I am stuck, help me` useful and prescriptive.
- Goal 2: Keep diagnosis before repair.
- Goal 3: Preserve Recovery Protocol and generated-evidence boundaries.

## Non-Goals

- Not doing: auto-repair, destructive cleanup, rollback automation, standalone CLI, support-bot authority, new active-memory file, new generated report, setup/update mutation, package-manager behavior, command-wrapper behavior, registry, optional pack, or external mutation.
- Deferred: richer recovery scenario harness, no-engineer fallback prompt pack, Doctor Dashboard v2 plain-English row labels, and router JSON shape contracts.
- Explicitly out of scope: using `I am stuck, help me` to approve edits, transition beads, accept implementation, regenerate reports, overwrite user files, roll back work, or bypass active memory.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-015-FR01` | `AGENT.md` must treat `I am stuck`, `I am stuck, help me`, and equivalent stuck/confused/help-me phrases as a stop-and-diagnose trigger. | P0 | Active agent behavior. |
| `PRD-015-FR02` | The required response must restate the symptom, name stop-and-diagnose as the first safe move, name the likely owner surface or unknown owner, include up to three read-only/advisory checks, give the next safe prompt/action, and list forbidden actions. | P0 | Prescriptive guidance. |
| `PRD-015-FR03` | Daily Cockpit, Troubleshooting, Recovery Protocol, Support Runbook, and Prompt Patterns must expose the same exact phrase and response contract. | P0 | Public guidance consistency. |
| `PRD-015-FR04` | OS Health, Doctor Dashboard, `next-step.py`, and stable-fix eligibility must remain diagnostic only and must not approve repair. | P0 | No second router or auto-repair. |
| `PRD-015-FR05` | Clarity scenario coverage must verify the stuck phrase and response contract in the owner surfaces. | P1 | Existing harness only. |
| `PRD-015-FR06` | Package inventory, roadmap, roadmap journal, generated docs/PRD/roadmap surfaces, and maintainer changelog must be updated. | P1 | Required maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-015-SEC01` | Stuck guidance must not approve destructive commands, overwrites, deletes, rollback, setup/update mutation, transition approval, acceptance, generated-report regeneration, external mutation, or secret handling. | P0 | Explicit approval required. |
| `PRD-015-SEC02` | Stuck guidance must not require private maintainer files or expose private support operations. | P0 | Public package complete on its own. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-015-NFR01` | The path must be understandable without engineering vocabulary. | P0 | Beginner value. |
| `PRD-015-NFR02` | The path must stay concise enough to use in a live chat. | P1 | Avoid ceremony. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-015-FR01` | `AGENT.md` includes exact stuck trigger language. | `python3 scripts/clarity-scenario-check.py` | Read active-memory trigger. | current workspace | check output |
| `PRD-015-FR02` | Required response shape includes symptom, first safe move, owner surface, checks, next action, and forbidden actions. | `python3 scripts/clarity-scenario-check.py` | Review docs wording. | current workspace | check output |
| `PRD-015-FR03` | Public docs/protocol surfaces expose the same phrase and contract. | `python3 scripts/clarity-scenario-check.py`; docs HTML check | Review rendered docs if needed. | Markdown docs | generated docs HTML |
| `PRD-015-FR04` | Diagnostic surfaces remain advisory only. | `python3 scripts/clarity-scenario-check.py`; `python3 scripts/os-health.py` when health output changes | Boundary review. | current workspace | check output and OS Health |
| `PRD-015-FR06` | Inventory, roadmap, journal, changelog, and generated surfaces are current. | inventory, docs, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: changed narrowly to add the stuck trigger.
- Public docs and protocols: changed to expose the same user phrase and response contract.
- Generated evidence: remains evidence only.
- Doctor Dashboard: diagnostic only; not a repair authority.
- External systems: not touched.

### Human Approval Gates

- Approval required before any file deletion, overwrite, generated-report regeneration, rollback, transition approval, setup/update mutation, destructive command, external mutation, or implementation acceptance.
- Stop if the stuck phrase is treated as repair approval, task selection, transition approval, or permission to bypass active memory.

## Public Interface

- Exact user phrase:
  - `I am stuck, help me.`
- Required agent response shape:
  - symptom
  - first safe move
  - likely owner surface or unknown owner
  - up to three read-only/advisory checks
  - next safe prompt/action
  - forbidden actions

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `AGENT.md` | Adds active-agent stuck trigger. | Active-memory guidance only; no repair approval. |
| `tasks/reference/RECOVERY-PROTOCOL.md` | Owns the stuck-trigger response contract. | Diagnosis before repair. |
| Daily Cockpit, Troubleshooting, Support Runbook, Prompt Patterns | Expose copyable phrase and consistent response shape. | Public guidance only. |
| `scripts/clarity-scenario-check.py` | Adds deterministic text contract coverage. | Existing advisory check; no runtime repair behavior. |
| Package inventory, maintainer roadmap, roadmap journal, changelog | Record ownership and shipped scope. | Inventory and maintainer history only. |

## Validation Plan

- `python3 scripts/clarity-scenario-check.py`
- `python3 scripts/version-check.py`
- `python3 scripts/file-inventory.py --check`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`
- `python3 _maintainer/scripts/roadmap-maintenance.py`
