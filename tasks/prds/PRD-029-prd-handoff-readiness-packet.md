---
prd_id: PRD-029
status: approved
owner: user
risk_level: medium
feature_link: PRD Handoff Readiness Packet
features_status: not compiled
related_prds:
  - PRD-018
  - PRD-024
  - PRD-028
---

# PRD-029 -- PRD Handoff Readiness Packet
<!-- ANCHOR: prd-029-prd-handoff-readiness-packet -->

> AUTHORITY: Public requirements for advisory PRD handoff readiness packets, PRD-to-decomposition/design/engineering/review handoff cues, and generated-evidence boundaries.
> NOT_AUTHORITY: Active memory, PRD approval, bead activation, task selection, implementation acceptance, external mutation, export automation, MCP behavior, registry behavior, optional-pack behavior, package-manager behavior, generated proof, or implementation status.
> LOAD_WHEN: Planning, implementing, reviewing, or interpreting PRD handoff readiness, PRD review cues, decomposition readiness, design handoff, or engineering handoff.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-24

## State

- ID: `PRD-029`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-24`

## Feature Link

- Feature: `PRD Handoff Readiness Packet`
- `FEATURES.md` status: `not compiled`
- Originating maintainer roadmap candidate: `PRD Handoff Readiness Packet`
- Related PRDs: `PRD-018`, `PRD-024`, `PRD-028`

## Source Inputs

- Source type: `maintainer roadmap candidate | ChatPRD handoff pressure pattern | existing PRD review and handoff surfaces`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` candidate `PRD Handoff Readiness Packet`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
- Stable facts:
  - Markdown PRD shards remain canonical.
  - Generated PRD HTML is a static review convenience only.
  - Decomposition still needs the Decomposition Protocol and normal human-gated bead activation.
  - Requirement-to-proof and Acceptance Oracle guidance already exist.
- Assumptions:
  - The first useful slice should be a read-only advisory packet/checker plus static PRD HTML cue.
  - A packet should expose blockers and next safe action without becoming a second PRD approval gate.
- Conflicts or stale inputs:
  - "Handoff packet" can imply current-session handoff authority. This PRD narrows the feature to PRD readiness evidence before decomposition, design, engineering, or review handoff.
- Privacy or secrets redactions:
  - Packets must not require secrets, credentials, private dashboard values, sensitive customer data, or raw private transcripts.

## Problem

A PRD can be approved enough to discuss while still being weak for decomposition, design handoff, engineering handoff, or PRD review. The missing context is usually scattered: requirement IDs, acceptance coverage, open questions, candidate beads, risk gates, proof expectations, and owner protocols.

## User Moment

- Before: A builder or agent must manually inspect a PRD and infer whether it is ready to hand to decomposition, design, engineering, or review.
- After: A read-only packet names PRD handoff readiness, blockers, proof expectations, owner protocols, and next safe action while preserving Markdown PRD authority.
- Why now: PRD HTML review, Acceptance Oracle export, Review Lanes, requirement-to-proof guidance, and build attribution already make PRD and review evidence easier to inspect; the remaining gap is handoff readiness visibility.

## Destination

- Destination statement: PrecodeOS can show whether a PRD is ready for advisory handoff without approving the PRD, selecting work, activating beads, or replacing the Markdown shard.
- Definition of done:
  - PRD-029 exists as the public authority shard.
  - `scripts/prd-handoff-readiness.py` prints advisory JSON and writes nothing by default.
  - The script supports `--prd`, `--target general|decomposition|design|engineering|review`, and `--self-test`.
  - Generated PRD HTML includes a compact handoff readiness cue derived from Markdown PRD content.
  - PRD, Decomposition, Review Lanes, Session Completion/Handoff, and Prompt Patterns guidance expose the boundary.
  - User Guide, package inventory, and AI navigation expose discoverability.
  - Clarity scenario coverage pins advisory-only behavior and forbidden authority wording.
  - Maintainer changelog, roadmap implemented history, roadmap journal, public docs HTML, PRD HTML, and roadmap HTML are refreshed.
- First useful vertical slice: local checker, static HTML cue, text-contract fixtures, docs/protocol propagation, and maintainer history.

## Users

- Primary user: Non-technical builder asking whether an approved PRD is ready for the next handoff conversation.
- Secondary user: AI coding agent, reviewer, support helper, designer, or engineer preparing decomposition or review from a PRD.
- Excluded user: Deploy bot, project-management system, external design tool, MCP server, package manager, registry, or automation expecting mutation.

## Goals

- Goal 1: Make PRD status, requirement IDs, open questions, acceptance coverage, candidate bead/decomposition readiness, proof expectations, risks, owner protocols, blockers, and next safe action visible together.
- Goal 2: Keep the packet generated evidence only.
- Goal 3: Route unresolved blockers back to PRD amendment, Architecture Shaping, or unblocker planning before bead activation.
- Goal 4: Make generated PRD HTML more useful for review without adding write-back or browser persistence.

## Non-Goals

- Not doing: PRD approval, bead activation, task selection, implementation acceptance, external mutation, export automation, MCP behavior, registry behavior, optional-pack behavior, package-manager behavior, generated proof, generated PRD authority, source Markdown write-back, browser persistence, design-tool integration, GitHub mutation, or new active-memory file.
- Deferred: richer handoff templates, generated diff artifacts, provider-specific design or engineering exports, external integrations, and stricter decomposition enforcement.
- Explicitly out of scope: treating a readiness packet, PRD HTML cue, Acceptance Oracle export block, generated report, chat summary, or external status as current instructions or approval.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-029-FR01` | Add `scripts/prd-handoff-readiness.py` as a read-only advisory checker. | P0 | Default command writes nothing. |
| `PRD-029-FR02` | The script must require `--prd` unless `--self-test` is used. | P0 | PRD path points to canonical Markdown. |
| `PRD-029-FR03` | The script must support `--target general|decomposition|design|engineering|review`, defaulting to `general`. | P0 | Target changes recommendation language only. |
| `PRD-029-FR04` | Output must include `status`, `warnings`, `details.packet`, and `generated_report_warning`. | P0 | JSON stdout. |
| `PRD-029-FR05` | Packet fields must cover PRD status, requirement IDs, open questions, acceptance oracle coverage, candidate bead/decomposition readiness, proof expectations, risks/permissions, owner protocols, blockers, and recommended next safe action. | P0 | Generated evidence only. |
| `PRD-029-FR06` | `--self-test` must cover ready PRD, unapproved PRD, missing acceptance oracle, unresolved implementation-changing questions, missing proof expectations, and forbidden authority wording. | P0 | No external dependencies. |
| `PRD-029-FR07` | Generated PRD HTML must include a compact handoff readiness cue from existing Markdown PRD content. | P1 | Static review cue only. |
| `PRD-029-FR08` | Protocols, prompts, user docs, package inventory, AI navigation, maintainer changelog, roadmap, roadmap journal, and generated surfaces must be updated. | P1 | Maintainer follow-through. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-029-SEC01` | Packets must not require secrets, credentials, private dashboard values, sensitive customer data, raw private transcripts, or provider configuration. | P0 | Use source file references and safe summaries only. |
| `PRD-029-SEC02` | Checker and HTML cue must not mutate files, external systems, branches, worktrees, PRDs, beads, generated reports, browser state, GitHub, or design tools. | P0 | Generated HTML is written only by the existing PRD HTML generator. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-029-NFR01` | The packet must stay compact enough for a non-technical builder to read. | P0 | Avoid enterprise handoff ceremony. |
| `PRD-029-NFR02` | Warning language must remain advisory and explicitly preserve approval gates. | P0 | No hidden authority. |
| `PRD-029-NFR03` | The feature must stay independent of private maintainer files. | P0 | Public package completeness. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-029-FR01` / `PRD-029-FR04` | Default checker prints advisory JSON with `details.packet` and writes no files. | `python3 scripts/prd-handoff-readiness.py --prd tasks/prds/PRD-029-prd-handoff-readiness-packet.md` | Inspect JSON. | Current PRD shard | command output |
| `PRD-029-FR02` | Checker refuses normal runs without `--prd`. | `python3 scripts/prd-handoff-readiness.py --self-test` | Inspect argparse behavior if needed. | Synthetic fixtures | command output |
| `PRD-029-FR03` | Target values are accepted and only change advisory recommendation language. | `python3 scripts/prd-handoff-readiness.py --self-test` | Review target language. | Synthetic fixtures | command output |
| `PRD-029-FR05` | Packet exposes status, requirements, open questions, acceptance coverage, decomposition readiness, proof, risk, protocols, blockers, and next safe action. | `python3 scripts/prd-handoff-readiness.py --self-test` | Inspect JSON shape. | Synthetic fixtures | command output |
| `PRD-029-FR06` | Ready, unapproved, missing acceptance, unresolved questions, missing proof, and forbidden wording fixtures are covered. | `python3 scripts/prd-handoff-readiness.py --self-test` | Review fixture failures if any. | Synthetic PRDs | command output |
| `PRD-029-FR07` | PRD HTML renders a compact readiness cue without write-back behavior. | `python3 scripts/prd-html.py --check` | Inspect generated PRD HTML. | Markdown PRDs | `tasks/prds-html/*.html` |
| `PRD-029-FR08` | Docs, protocols, inventory, roadmap, changelog, and generated surfaces are current. | docs, inventory, PRD HTML, and roadmap checks | Boundary review. | Markdown docs | generated surfaces |
| `PRD-029-SEC01` / `PRD-029-SEC02` | Packet/checker behavior stays local, redacted, and non-mutating. | `python3 scripts/prd-handoff-readiness.py --self-test` | Review forbidden uses and source handling. | Synthetic fixtures | command output |
| `PRD-029-NFR01` / `PRD-029-NFR02` / `PRD-029-NFR03` | Output remains compact, advisory, and public-package complete. | `python3 scripts/clarity-scenario-check.py` | Review packet and docs wording. | Markdown docs and fixtures | check output |

## Risk And Permission Model

- Approval required before PRD approval, PRD amendment, bead creation, bead activation, implementation, review acceptance, transition approval, design-tool mutation, GitHub mutation, external mutation, generated-source promotion, or package-maintenance history claims.
- Stop if PRD status, requirement IDs, open questions, acceptance coverage, proof expectations, risk gates, owner protocols, or next safe action are unclear.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Generated reports added: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/prd-handoff-readiness.py` | Read-only advisory JSON packet for one Markdown PRD. | Warns and recommends next safe action; writes nothing. | Self-test, clarity scenarios, command run. | `tasks/prds/PRD-029-prd-handoff-readiness-packet.md` |
| `scripts/prd-html.py` | Static generated PRD review cue. | Derived from Markdown PRD content only; no write-back or approval. | PRD HTML freshness check. | `tasks/prds/PRD-029-prd-handoff-readiness-packet.md` |
| Protocol and prompt guidance | Copyable PRD handoff readiness review. | Routes blockers back to owner workflows without activating work. | Text-contract and docs review. | `tasks/prds/PRD-029-prd-handoff-readiness-packet.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-029-prd-handoff-readiness-packet.md`
- Owner protocol: `tasks/reference/PRD-PROTOCOL.md`
- Secondary reference files:
  - `tasks/reference/DECOMPOSITION-PROTOCOL.md`
  - `tasks/reference/REVIEW-LANES-PROTOCOL.md`
  - `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Files or folders likely in play:
  - listed above
  - `scripts/prd-handoff-readiness.py`
  - `scripts/prd-html.py`
  - `scripts/clarity-scenario-check.py`
  - `tasks/prds-html/`
  - `docs-html/`
  - `llms.txt`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`

## Bead Proposals

| Candidate bead | Purpose | Primary authority | Checks |
|---|---|---|---|
| `B-PRD-029-01` | Implement the read-only checker, HTML cue, protocols, docs, maintainer history, and generated surface refresh as one package-maintenance slice. | `tasks/prds/PRD-029-prd-handoff-readiness-packet.md` | `python3 scripts/prd-handoff-readiness.py --self-test`; `python3 scripts/clarity-scenario-check.py`; PRD/docs/roadmap checks |
