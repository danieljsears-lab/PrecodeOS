---
prd_id: PRD-046
status: approved
owner: user
risk_level: medium
feature_link: Reviewed Memory Citation Ergonomics
features_status: not compiled
related_prds:
  - PRD-014
---

# PRD-046 -- Reviewed Memory Citation Ergonomics
<!-- ANCHOR: prd-046-reviewed-memory-citation-ergonomics -->

> AUTHORITY: Destination shard for improving reviewed-memory citation, demotion, and filing guidance on existing filesystem memory search commands.
> NOT_AUTHORITY: Active memory, task selection, product decisions, owner-file promotion, memory-card creation, PRD approval, bead activation, transition approval, implementation acceptance, semantic search approval, shared backend approval, generated-index authority, command wrapper behavior, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or release approval.
> LOAD_WHEN: Reviewing, implementing, or decomposing reviewed-memory citation ergonomics for `scripts/memory-check.py`, memory indexes, Memory Protocol, or reviewed-memory user guidance.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-31

## State

- ID: `PRD-046`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-07-31`

## Feature Link

- Feature: `Reviewed Memory Citation Ergonomics`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-014`

## Source Inputs

- Source type: `maintainer roadmap evidence | memory protocol follow-up | reviewed-memory command output`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Reviewed Memory Citation Ergonomics`
  - `tasks/reference/MEMORY-PROTOCOL.md`
  - `scripts/memory-check.py`
  - `scripts/precode_outputs.py`
  - `memory/REVIEWED-MEMORY-GUIDE.md`
- Stable facts:
  - Reviewed memory is evidence, not authority.
  - `scripts/memory-check.py --recall` already provides filesystem-first exact-match snippets.
  - `scripts/memory-check.py --retrieval-review` already gates optional retrieval discussion behind hygiene and Extension Review.
  - Memory Promotion Review is manual and does not create cards or promote owner files.
- Assumptions:
  - Better field names and prompts can reduce citation and filing confusion without adding a new command or flag.
  - JSON output can become more readable for agents while preserving existing top-level fields.

## Problem

Reviewed memory search exists, but agents and users can still struggle to turn results into concise cited recall, demotion decisions, and destination recommendations without loading too much context or over-promoting memory.

## User Moment

- Before: A user asks an agent to search memory, and the result may include useful snippets but still requires the agent to infer the citation, demotion, and destination decision.
- After: Existing memory-check output names compact citations, demotion decisions, and filing recommendations while keeping weak matches as leads only.
- Why now: Filesystem-first recall, retrieval-readiness review, and Memory Promotion Review already exist; the remaining gap is ergonomics and consistency, not infrastructure.

## Destination

- Destination statement: Existing reviewed-memory commands provide clearer cited snippets, demotion decisions, no-match handling, and filing recommendations without changing command surface or authority boundaries.
- Definition of done:
  - `scripts/memory-check.py --recall` keeps existing fields and adds compact citation, demotion decision, and filing recommendation fields.
  - Weak-match and no-match output says weak matches are search leads only and does not force recall into context.
  - Generated memory-index wording teaches compact citation, manual promotion, and demotion before use.
  - Memory Protocol, Prompt Patterns, user docs, package inventory, PRD HTML, docs HTML, maintainer changelog, roadmap, roadmap journal, and private roadmap HTML are current.
- First useful vertical slice: additive JSON fields and text-contract coverage on existing `memory-check.py` behavior.

## Users

- Primary user: AI agent or maintainer searching reviewed memory before acting.
- Secondary user: Builder asking what should survive a session or whether a memory claim should become owner-file truth.
- Excluded user: Automation expecting memory search to create cards, promote owner files, choose tasks, approve PRDs, activate beads, or install retrieval infrastructure.

## Goals

- Goal 1: Make memory search results easier to cite without loading whole cards.
- Goal 2: Make stale, superseded, archived, low-confidence, and promotion-needed results visibly demoted.
- Goal 3: Make destination recommendations explicit while preserving human approval gates.

## Non-Goals

- Not doing: new `memory-check.py` command, new CLI flag, command facade, semantic search, hybrid backend, shared memory service, MCP server, dashboard, registry behavior, optional-pack behavior, automatic memory-card creation, owner-file auto-promotion, active-memory expansion, task selection, PRD approval, bead activation, review acceptance, transition approval, install/update behavior, release-channel behavior, package-manager behavior, or external mutation.
- Deferred: human-readable summary mode, semantic search, shared backend retrieval, richer ranking, and generated HTML memory browser.
- Explicitly out of scope: treating generated memory indexes, memory-check JSON, weak-match examples, or filing recommendations as authority.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-046-FR01` | Existing `scripts/memory-check.py --recall` output must keep current fields and add compact citation, demotion decision, and filing recommendation fields. | P0 | Additive JSON only. |
| `PRD-046-FR02` | Recall snippets must remain exact-match only, and no-match output must explicitly demote weak matches to search leads. | P0 | No weak recall. |
| `PRD-046-FR03` | Filing recommendations must use existing destinations: stay reviewed memory, proposed memory card, `DECISIONS.md`, PRD, protocol, approved bead, another owner file, or defer. | P0 | No automatic filing. |
| `PRD-046-FR04` | Promotion-needed cards must name the proposed owner when present and require Memory Promotion Review before any edit. | P0 | Manual promotion only. |
| `PRD-046-FR05` | Generated memory-index wording and public docs must explain citation, demotion, no-match, and filing guidance consistently. | P1 | Markdown remains canonical. |
| `PRD-046-FR06` | Text-contract and script self-test coverage must preserve the existing-command boundary. | P1 | Prevents later command drift. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-046-SEC01` | Memory search must remain read-only, repo-local, dependency-free, and network-free. | P0 | Existing script posture. |
| `PRD-046-SEC02` | Output must not expose secrets, raw transcripts, or unapproved private notes beyond existing reviewed card source pointers. | P0 | Reviewed memory remains curated. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-046-NFR01` | Additive fields must be concise and stable enough for agents to consume. | P0 | Avoid whole-card loading. |
| `PRD-046-NFR02` | Existing command invocations must continue to work without new flags. | P0 | No CLI expansion. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-046-FR01` | Recall output includes `compact_citation`, `demotion_decision`, and `filing_recommendation`. | `python3 scripts/memory-check.py --self-test` | Inspect `--recall` JSON. | deterministic fixture and current workspace | stdout JSON |
| `PRD-046-FR02` | No-match output keeps weak matches as leads only. | `python3 scripts/memory-check.py --self-test` | Inspect a no-match query. | deterministic fixture | stdout JSON |
| `PRD-046-FR03` | Filing recommendations use existing destinations and say no automatic filing. | `python3 scripts/memory-check.py --self-test` | Inspect promotion-needed fixture. | deterministic fixture | stdout JSON |
| `PRD-046-FR04` | Promotion-needed cards name proposed owner and approval requirement. | `python3 scripts/memory-check.py --self-test` | Inspect output for `status: needs_promotion`. | deterministic fixture | stdout JSON |
| `PRD-046-FR05` | Docs/protocols explain citation, demotion, and filing boundaries. | `python3 scripts/clarity-scenario-check.py` | Boundary review. | canonical Markdown | check output |
| `PRD-046-FR06` | Generated PRD/docs/roadmap surfaces are fresh. | `python3 scripts/prd-html.py --check`; `python3 scripts/docs-html.py --check`; `python3 _maintainer/scripts/roadmap-html.py --check` | Open generated surfaces if needed. | current workspace | stdout |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: unchanged.
- Reviewed memory cards: not created, edited, archived, or promoted by search output.
- Owner files: not edited from memory output without separate approval.
- Generated indexes and JSON: evidence only.
- Retrieval infrastructure: not added.
- External systems: not touched.

### Human Approval Gates

- Approval required before any memory-card write, owner-file edit, PRD amendment, protocol update, bead change, active-memory change, card promotion, generated evidence acceptance, or external mutation.
- Stop if memory output is treated as a decision, requirement, task selector, card write approval, owner-file promotion approval, PRD approval, bead activation, implementation acceptance, backend approval, command approval, or package-manager behavior.

## Public Interface

- Existing command only:
  - `python3 scripts/memory-check.py --query "topic words" --recall`
  - `python3 scripts/memory-check.py --query "topic words" --retrieval-review`
  - `python3 scripts/memory-check.py --needs-promotion`
- No new command, flag, facade, generated report, backend, service, or wrapper.

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `scripts/memory-check.py` | Adds compact citation, demotion decision, filing recommendation, and clearer no-match fields. | Advisory JSON only. |
| `scripts/precode_outputs.py` | Makes generated memory-index wording more scanable. | Generated evidence only. |
| `tasks/reference/MEMORY-PROTOCOL.md` | Explains refined output fields and boundaries. | Memory behavior owner protocol. |
| `tasks/reference/PROMPT-PATTERNS.md` | Updates copyable memory prompts. | Prompt catalog, not approval. |
| Public docs and package inventory | Align user guidance and command descriptions. | Markdown docs remain reference surfaces. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate history. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/memory-check.py --self-test`
- `python3 scripts/memory-check.py --query "selective recall" --recall --limit 3`
- `python3 scripts/memory-check.py --query "semantic backend" --retrieval-review --limit 3`
- `python3 scripts/clarity-scenario-check.py`
- `bash scripts/validate-memory.sh`
- `python3 scripts/file-inventory.py --check`
- `python3 scripts/public-repo-check.py`
- `python3 scripts/prd-html.py --check`
- `python3 scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`
