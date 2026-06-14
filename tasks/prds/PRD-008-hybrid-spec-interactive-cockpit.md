---
prd_id: PRD-008
status: approved
owner: user
risk_level: medium
feature_link: Hybrid Spec Format v2 / Interactive Spec Cockpit
features_status: not compiled
related_prds:
  - PRD-007
---

# PRD-008 -- Hybrid Spec Format v2 / Interactive Spec Cockpit
<!-- ANCHOR: prd-008-hybrid-spec-interactive-cockpit -->

> AUTHORITY: Destination shard for the static PRD HTML cockpit enhancement that exports proposed Acceptance Oracle Matrix Markdown.
> NOT_AUTHORITY: Active memory, PRD approval, task selection, bead activation, generated evidence truth, implementation acceptance, direct Markdown write-back, automatic source promotion, browser storage, external mutation, package-manager behavior, or CLI wrapper behavior.
> LOAD_WHEN: Reviewing, implementing, or maintaining the interactive PRD cockpit export surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-008`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Hybrid Spec Format v2 / Interactive Spec Cockpit`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-007`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | shipped PRD HTML v1`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Hybrid Spec Format v2 / Interactive Spec Cockpit`
  - `tasks/prds/PRD-007-hybrid-spec-html-review-surface.md`
  - `scripts/prd-html.py`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/prds/PRD-SHARD-SCHEMA.md`
- Stable facts:
  - PRD Markdown shards in `tasks/prds/*.md` remain canonical.
  - Static generated PRD HTML already improves review scanability without becoming authority.
  - V2 must preserve manual promotion back into Markdown and avoid browser write-back.
- Assumptions:
  - The first safe cockpit surface is the `Acceptance Oracle Matrix`.
  - Exporting a copyable Markdown replacement block is enough for the first v2 slice.
  - Inline JavaScript is acceptable for local browser interaction when the page remains readable without it.
- Conflicts or stale inputs:
  - Earlier v2 language suggested broad micro-editors, visual design intent, and intent-matching hooks. This slice deliberately narrows v2 to one export-only matrix editor.
- Privacy or secrets redactions:
  - PRDs should not contain secrets. The cockpit must not add network calls, browser storage, or external export behavior.

## Problem

Acceptance oracles are one of the hardest PRD sections for non-technical builders to review because each requirement needs expected behavior, automated proof, manual proof, fixture needs, and evidence location.

Static HTML makes the matrix easier to read, but a reviewer still has to edit Markdown tables by hand when an acceptance check is missing, confusing, or too technical.

## User Moment

- Before: A reviewer notices a weak acceptance oracle in the generated PRD HTML page, then must manually locate and edit the Markdown table.
- After: The reviewer edits the Acceptance Oracle Matrix in the generated page and exports a proposed Markdown replacement block, then manually applies that block to the canonical PRD source.
- Why now: PRD HTML v1 established a generated review surface; v2 can add bounded interaction without changing source authority.

## Destination

- Destination statement: Generated PRD pages provide an export-only Acceptance Oracle Matrix cockpit that helps reviewers propose Markdown changes without writing source files or bypassing approval gates.
- Definition of done:
  - `scripts/prd-html.py` renders an Acceptance Oracle Matrix cockpit on PRD pages when that section contains a Markdown table.
  - The cockpit lets a reviewer edit table cell text in-browser.
  - The cockpit exports a copyable Markdown replacement block headed `## Acceptance Oracle Matrix`.
  - The exported block is labeled as a proposal requiring manual application to `tasks/prds/*.md`.
  - Generated pages do not offer source write-back, approval buttons, task activation, bead activation, implementation acceptance, browser storage, or external export.
  - Existing `python3 scripts/prd-html.py` and `python3 scripts/prd-html.py --check` behavior is preserved.
  - PRD protocol, shard-schema guidance, package inventory, README, maintainer changelog, and roadmap history reflect the new surface.
  - Generated public docs HTML and maintainer roadmap HTML are refreshed when their Markdown sources change.
- First useful vertical slice: export-only Acceptance Oracle Matrix cockpit.

## Users

- Primary user: Builder or reviewer checking whether PRD requirements have clear proof paths.
- Secondary user: AI coding agent or support helper preparing a proposed PRD amendment for user review.
- Excluded user: Anyone expecting direct Markdown editing, approval automation, bead activation, browser-persisted state, external publishing, CLI wrapper behavior, package-manager behavior, or broad spec-to-implementation matching.

## Goals

- Goal 1: Make acceptance-oracle edits easier to propose.
- Goal 2: Preserve Markdown PRD shards as the only source authority.
- Goal 3: Keep v2 interaction narrow enough to validate before adding richer cockpit behavior.

## Non-Goals

- Not doing: direct write-back, auto-applied patches, approval buttons, PRD status editing, requirement editing, Open Questions editing, bead activation, task selection, implementation acceptance, visual design editor, local server, external storage, package-manager behavior, CLI wrapper behavior, registry behavior, or new dependency adoption.
- Deferred: Requirements editor, Open Questions editor, spec-to-implementation matching, visual mockup review, generated diff artifacts, review-lane integration, and direct Markdown promotion workflow.
- Explicitly out of scope: Any workflow that treats generated HTML, exported Markdown, or browser state as authority.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-008-FR01` | Add an export-only Acceptance Oracle Matrix cockpit to generated PRD pages. | P0 | Only when the section has a parseable Markdown table. |
| `PRD-008-FR02` | Allow browser editing of Acceptance Oracle Matrix cell text. | P0 | Local page state only; no persistence. |
| `PRD-008-FR03` | Export a copyable Markdown replacement block for `## Acceptance Oracle Matrix`. | P0 | Manual application required. |
| `PRD-008-FR04` | Preserve existing `scripts/prd-html.py` generate and `--check` interfaces. | P0 | No new required command. |
| `PRD-008-FR05` | Keep Requirements, Open Questions, approval state, PRD status, and bead proposals read-only. | P0 | First v2 slice stays narrow. |
| `PRD-008-FR06` | Update public protocol, schema, inventory, README, changelog, roadmap, journal, and generated HTML surfaces. | P0 | Markdown remains canonical. |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-008-UX01` | Cockpit copy clearly says exported Markdown is a proposal, not source truth. | P0 | Visible before export. |
| `PRD-008-UX02` | The canonical Markdown source link remains visible near the cockpit. | P0 | User must know where manual application happens. |
| `PRD-008-UX03` | Pages remain readable without JavaScript. | P0 | Export controls require JavaScript, but source review does not. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-008-FR01` | Generated PRD pages with an Acceptance Oracle Matrix show an export-only cockpit. | `python3 scripts/prd-html.py --check` after regeneration | Inspect one generated PRD page and confirm the cockpit appears near review cues. | Existing PRD shard with an Acceptance Oracle Matrix | generated PRD HTML |
| `PRD-008-FR03` | The cockpit exports a Markdown block headed `## Acceptance Oracle Matrix`. | static generated output comparison | Edit a cell locally, export, and confirm the block is copyable and labeled as a proposal. | Browser with local generated HTML page | manual boundary review |
| `PRD-008-FR05` | No other PRD state or planning surface becomes editable. | source inspection | Confirm Requirements, Open Questions, approval, status, and bead proposal surfaces remain read-only. | Generated PRD page | manual boundary review |

## Risk And Permission Model

- Approval required before editing canonical Markdown, approving a PRD, changing PRD status, compiling `FEATURES.md`, creating or activating beads, accepting implementation, or promoting exported text into authority.
- Stop if generated HTML is treated as source truth, exported Markdown is treated as approval, a reviewer asks for direct write-back, or cockpit output is used to start implementation without canonical Markdown review.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.
- Browser storage: none.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/prd-html.py` | Existing `python3 scripts/prd-html.py` and `python3 scripts/prd-html.py --check` | Generate/check static PRD HTML with export-only Acceptance Oracle Matrix cockpit. | Stale-output check and manual cockpit review. | `tasks/prds/PRD-008-hybrid-spec-interactive-cockpit.md` |
| `tasks/prds-html/*.html` | Generated review pages with local export controls. | Review convenience and proposal export only; Markdown PRDs remain canonical. | Regenerated by `scripts/prd-html.py`. | `tasks/prds/*.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-008-hybrid-spec-interactive-cockpit.md`
- Secondary reference files:
  - `tasks/prds/PRD-007-hybrid-spec-html-review-surface.md`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/prds/PRD-SHARD-SCHEMA.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `README.md`
- Files or folders likely in play:
  - `scripts/prd-html.py`
  - `tasks/prds-html/`
  - `tasks/prds/*.md`
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - `AGENT.md`
  - `DECISIONS.md`
  - `tasks/todo.md`
  - target app code
  - external systems
  - generated evidence except generated PRD/docs/roadmap HTML
- Required checks:
  - `python3 scripts/prd-html.py --check`
  - `python3 scripts/file-inventory.py --check`
  - `python3 scripts/version-check.py`
  - `bash scripts/validate-memory.sh`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Open or inspect one generated PRD page with an Acceptance Oracle Matrix. Confirm the cockpit labels exported Markdown as a proposal, requires manual source editing, and never offers approval, write-back, task activation, or bead activation.
- Forbidden assumptions:
  - Exported Markdown is source truth.
  - Generated PRD HTML approves PRD changes.
  - The cockpit writes source files.
  - V2 includes broad spec editing or implementation matching.

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B008-hybrid-spec-interactive-cockpit` | `PRD-008-FR01` through `PRD-008-FR06`, `PRD-008-UX01` through `PRD-008-UX03` | PRD shard, generator cockpit, generated PRD HTML, public docs, inventory, changelog, roadmap history, generated docs HTML, and generated roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-008-hybrid-spec-interactive-cockpit.md` | `scripts/prd-html.py --check` plus package validation and manual cockpit boundary review |

## Open Questions

| Question | Affects | Blocking? |
|---|---|---|
| Should a future v2+ surface export a generated diff instead of a replacement block? | Follow-up cockpit scope | no |
| Should Requirements or Open Questions become separate export-only editors after this proves useful? | Follow-up cockpit scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of Hybrid Spec Format v2 as an export-only Acceptance Oracle Matrix cockpit, explicitly excluding direct write-back, generated diff artifacts for this slice, approval behavior, bead activation, task selection, implementation acceptance, browser storage, external mutation, CLI wrapper behavior, package-manager semantics, and active-memory changes.
