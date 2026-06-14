---
prd_id: PRD-007
status: approved
owner: user
risk_level: medium
feature_link: Hybrid Spec Format v1 / HTML Review Surface
features_status: not compiled
related_prds: []
---

# PRD-007 -- Hybrid Spec Format v1 / HTML Review Surface
<!-- ANCHOR: prd-007-hybrid-spec-html-review-surface -->

> AUTHORITY: Destination shard for the static HTML PRD review surface in PrecodeOS.
> NOT_AUTHORITY: Active memory, PRD approval, task selection, bead activation, generated evidence truth, implementation acceptance, round-trip editing, or source-of-truth replacement.
> LOAD_WHEN: Reviewing, implementing, or maintaining the generated PRD HTML review surface.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-14

## State

- ID: `PRD-007`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-14`

## Feature Link

- Feature: `Hybrid Spec Format v1 / HTML Review Surface`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | existing PRD protocol`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Hybrid Spec Format v1 / HTML Review Surface`
  - `tasks/reference/PRD-PROTOCOL.md`
  - `tasks/prds/PRD-SHARD-SCHEMA.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Stable facts:
  - PRD Markdown shards in `tasks/prds/*.md` are canonical product destination documents.
  - Generated HTML may improve review, scanability, source navigation, and stakeholder inspection.
  - Generated HTML must remain subordinate to Markdown PRDs and cannot approve PRDs or activate beads.
- Assumptions:
  - V1 should render all non-template PRD shards, not only the latest PRD.
  - V1 output should live under `tasks/prds-html/` so it stays adjacent to PRD shards without mixing into `docs-html/`.
- Conflicts or stale inputs:
  - Interactive spec cockpit behavior belongs to the deferred v2 roadmap item, not this static v1 review surface.
- Privacy or secrets redactions:
  - PRD review pages must not expose secrets beyond what is already present in source Markdown. PRDs should not contain secrets.

## Problem

Long PRD shards are readable as Markdown, but they are hard for non-technical builders and reviewers to scan quickly when checking status, requirements, blockers, risks, context, bead proposals, and approval state.

Without a generated review surface, a reviewer may miss the next safe decision or confuse dense product-definition text with permission to start implementation.

## User Moment

- Before: The builder or reviewer opens a PRD Markdown file and must manually find stage, approval, requirements, blockers, risk gates, and bead proposals.
- After: The builder or reviewer opens a generated PRD HTML index or page that foregrounds those review cues while linking back to canonical Markdown.
- Why now: The roadmap has promoted static hybrid spec review as a P1 operating-loop improvement after PRD and generated-doc patterns are stable enough to reuse.

## Destination

- Destination statement: PrecodeOS provides a committed static HTML review surface for all non-template PRD shards while preserving Markdown PRDs as the only authority.
- Definition of done:
  - `scripts/prd-html.py` generates `tasks/prds-html/index.html` and one page per non-template PRD shard.
  - `scripts/prd-html.py --check` fails when committed PRD HTML is stale.
  - Generated pages visibly label HTML as review convenience and generated evidence only.
  - Generated pages link back to the source Markdown PRD.
  - Review pages foreground PRD state, approval status, unresolved blockers, forbidden premature actions, requirements, risk and permission model, agent context, bead proposals, and next safe review decision.
  - PRD protocol, PRD shard schema, package inventory, README, maintainer changelog, and roadmap history reflect the new surface.
  - Generated public docs HTML and maintainer roadmap HTML are refreshed when their Markdown sources change.
- First useful vertical slice: static generated HTML and documentation/reference integration only.

## Users

- Primary user: Non-technical builder or reviewer inspecting a PRD before approving, decomposing, or reviewing product scope.
- Secondary user: AI coding agent or support helper orienting to PRD status and constraints without loading unrelated context.
- Excluded user: Anyone expecting browser editing, round-trip promotion to Markdown, approval automation, bead activation, task selection, or cockpit behavior.

## Goals

- Goal 1: Make PRD review state and next safe decision easier to inspect.
- Goal 2: Preserve Markdown PRD authority and existing approval gates.
- Goal 3: Add a stale-output check so generated PRD HTML cannot quietly drift from source Markdown.

## Non-Goals

- Not doing: interactive editing, round-trip Markdown updates, approval buttons, task selection, bead activation, implementation acceptance, cockpit UI, external publishing, package-manager behavior, CLI wrapper installation, or new dependency adoption.
- Deferred: Hybrid Spec Format v2 / Interactive Spec Cockpit, rich visual editors, review lane integration, and spec-to-implementation matching.
- Explicitly out of scope: Any workflow that treats generated PRD HTML as authority, proof, approval, or source truth.

## Alternatives Considered

| Option | Why rejected or deferred | Decision owner |
|---|---|---|
| Generate one requested PRD only | Less useful for package review and stale-surface validation. | user |
| Put PRD HTML under `docs-html/` | Mixes user docs and product-definition shards; `tasks/prds-html/` keeps the generated surface adjacent to PRDs. | user |
| Keep the surface maintainer-only | Weakens the user-facing PRD review value and conflicts with the selected public generated surface. | user |
| Add browser editing in v1 | Belongs to the deferred v2 cockpit candidate because promotion and authority boundaries need separate design. | user |

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-007-FR01` | Add a PRD HTML generator script. | P0 | Default output is `tasks/prds-html/`. |
| `PRD-007-FR02` | Render all non-template PRD shards into committed HTML. | P0 | Excludes `PRD-000-template.md` and `PRD-SHARD-SCHEMA.md`. |
| `PRD-007-FR03` | Add an index page summarizing PRD status, risk, feature link, and source file. | P0 | Index links to generated pages and Markdown sources. |
| `PRD-007-FR04` | Each PRD page foregrounds review cues before the full rendered PRD body. | P0 | Include status, approval, blockers, requirements, risks, context, bead proposals, and next safe decision. |
| `PRD-007-FR05` | Add `--check` mode that compares generated output to committed files. | P0 | Check must fail when output is stale, missing, or extra. |
| `PRD-007-FR06` | Update public PRD protocol, PRD shard schema, package inventory, and README discoverability. | P0 | Markdown remains canonical. |
| `PRD-007-FR07` | Complete maintainer changelog and roadmap history follow-through. | P0 | Includes roadmap implemented-candidate entry, journal card, maintenance cleanup, and generated roadmap HTML. |

### UX Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-007-UX01` | Generated pages make non-authority status visible without requiring scrolling. | P0 | Use a prominent notice near the top. |
| `PRD-007-UX02` | Generated pages provide source pointers to canonical Markdown. | P0 | Source links should be visible on the index and page header. |
| `PRD-007-UX03` | Generated pages are static and readable without JavaScript. | P0 | No runtime app surface. |

## Risk And Permission Model

- Approval required before treating any rendered PRD as approved, activating a bead, starting implementation, changing source Markdown, or promoting generated review notes into authority.
- Stop if a reviewer asks to edit PRD content through HTML, approve from HTML, start a bead from HTML alone, or treat generated output as proof.
- Network needs: none.
- Dependency changes: none.
- External systems touched: none.

## Architecture / Project Context Impact

- Project context impact: `minor`
- `PROJECT-CONTEXT.md` loaded: `not needed`
- Architecture Shaping: `skipped`
- Architecture Brief evidence: `none`
- Architecture Shaping skip reason: Static generator and documentation surface only; no app architecture, external service, schema, auth, or runtime behavior.
- Architecture authority updates needed: `none`
- Route/API authority updates needed: `none`
- Schema authority updates needed: `none`
- Security authority updates needed: `none`
- Decision log updates needed: `none`

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/prd-html.py` | `python3 scripts/prd-html.py` and `python3 scripts/prd-html.py --check` | Generate/check static PRD HTML from Markdown; no state authority or approval behavior. | Stale-output check and validation commands. | `tasks/prds/PRD-007-hybrid-spec-html-review-surface.md` |
| `tasks/prds-html/*.html` | Static generated review pages. | Review convenience only; Markdown PRDs remain canonical. | Regenerated by `scripts/prd-html.py`. | `tasks/prds/*.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-007-hybrid-spec-html-review-surface.md`
- Secondary reference files:
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
  - `bash scripts/validate-memory.sh`
  - `python3 scripts/version-check.py`
  - `python3 scripts/file-inventory.py --check`
  - `python3 _maintainer/scripts/docs-html.py --check`
  - `python3 _maintainer/scripts/roadmap-html.py --check`
- Manual verification:
  - Open or inspect `tasks/prds-html/index.html` and one generated PRD page to confirm source links, status, blockers, forbidden actions, requirements, risks, and next safe review decision are visible without implying authority.
- Forbidden assumptions:
  - HTML review output approves PRDs.
  - HTML review output activates beads.
  - HTML review output replaces Markdown PRDs.
  - HTML review output can edit or promote PRD changes.
  - Static PRD HTML is the v2 interactive cockpit.

## Anti-Shallow Checks

- User problem named: `yes`
- Non-goals named: `yes`
- Before/after user moment clear: `yes`
- Requirements observable: `yes`
- Sensitive surfaces identified: `yes`
- Authority files identified: `yes`
- First bead can be one logical unit: `yes`
- Generated text reviewed by user: `yes`

## Bead Proposals

These are proposals only. Do not activate a bead until the user approves the transition.

| Proposed bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Verification |
|---|---|---|---|---|---|---|---|
| `B007-hybrid-spec-html-review-surface` | `PRD-007-FR01` through `PRD-007-FR07`, `PRD-007-UX01` through `PRD-007-UX03` | Generator, generated PRD HTML, public docs, inventory, changelog, roadmap history, generated docs HTML, and generated roadmap HTML are implemented and validated. | `human_in_loop` | `static_only` | `same_session_ok` | `tasks/prds/PRD-007-hybrid-spec-html-review-surface.md` | `scripts/prd-html.py --check` plus package validation and manual HTML review |

## Compilation Notes

- Feature entry: `Hybrid Spec Format v1 / HTML Review Surface`
- Functional requirements to add or amend: not compiled in this slice
- MVP slice notes: static PRD HTML review only
- Acceptance updates needed: none

## Open Questions

Only include blockers that can change implementation.

| Question | Affects | Blocking? |
|---|---|---|
| Should a future v2 cockpit support browser edits with explicit promotion back to Markdown? | Follow-up roadmap scope | no |
| Should future review lanes integrate PRD HTML with acceptance review prompts? | Follow-up roadmap scope | no |

## Approval

- Approved by: Dan Sears / Recode
- Approved on: 2026-06-14
- Approval notes: User approved implementation of the decision-complete Hybrid Spec Format v1 plan, explicitly selecting all non-template PRDs under `tasks/prds-html/` and excluding editing, round-trip promotion, approval, bead activation, task selection, cockpit behavior, external mutation, CLI wrapper behavior, package-manager semantics, and active-memory changes.
