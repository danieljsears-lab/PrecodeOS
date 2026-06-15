---
prd_id: PRD-014
status: approved
owner: user
risk_level: medium
feature_link: Authority Map For Package Surfaces
features_status: not compiled
related_prds: []
---

# PRD-014 -- Authority Map For Package Surfaces
<!-- ANCHOR: prd-014-authority-map-package-surfaces -->

> AUTHORITY: Destination shard for generated package-surface authority-map refinements.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, transition approval, implementation acceptance, generated evidence truth, private maintainer authority, package-manager behavior, install/update behavior, command-wrapper behavior, registry behavior, optional-pack behavior, or release approval.
> LOAD_WHEN: Reviewing, implementing, or decomposing generated authority-map behavior for public PrecodeOS package surfaces.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-15

## State

- ID: `PRD-014`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-06-15`

## Feature Link

- Feature: `Authority Map For Package Surfaces`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `none`

## Source Inputs

- Source type: `maintainer roadmap evidence | approved implementation plan | package inventory`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Authority Map For Package Surfaces`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `scripts/os_compiler.py`
  - `logs/authority-map.json`
  - `tasks/reference/SEMANTIC-CHANGE-PROPOSAL-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Stable facts:
  - Markdown owner files and protocols hold package meaning.
  - Generated JSON and reports are evidence only.
  - Public package docs must not depend on private `_maintainer/` material.
- Assumptions:
  - The first implementation should refine the existing authority-map compiler instead of adding a new command, checker gate, registry, or public authority document.
  - Surface-class grouping helps contributors and agents avoid mistaking shims, generated surfaces, scripts, and private maintainer files for the same authority class.

## Problem

Public docs, protocols, scripts, adapters, generated files, shims, and maintainer-private files can blur which package surface owns which facts.

## User Moment

- Before: A contributor or agent sees a file path or generated report and has to infer whether it is authority, evidence, compatibility guidance, or private maintainer material.
- After: The generated authority map keeps the existing per-document contract list and adds package-surface class metadata that explains each class's authority and non-authority boundaries.
- Why now: PrecodeOS now has more shims, generated review surfaces, protocols, diagnostics, and maintainer-local roadmap history. The package needs better orientation without adding enforcement.

## Destination

- Destination statement: `logs/authority-map.json` groups parsed authority contracts by package surface class and includes class-level boundaries for public package surfaces while excluding private maintainer detail.
- Definition of done:
  - `scripts/os_compiler.py` emits `surface_classes`, `docs_by_surface`, `generated_is_not_authority`, and `private_maintainer_surfaces_excluded` in `logs/authority-map.json`.
  - The existing flat `docs` list remains present for compatibility.
  - Public inventory and relevant protocols explain the refined map and generated-evidence boundary.
  - Roadmap history, roadmap journal, generated docs/roadmap HTML, and maintainer changelog are current.
- First useful vertical slice: generated authority-map grouping and public inventory/protocol explanation only.

## Users

- Primary user: Maintainer or contributor checking which package surface owns a fact.
- Secondary user: AI coding agent orienting before editing public PrecodeOS package files.
- Excluded user: Automation expecting approval, task selection, package installation, update behavior, registry behavior, or private maintainer material.

## Goals

- Goal 1: Make package surface classes and ownership boundaries easier to inspect.
- Goal 2: Preserve Markdown owner files and protocols as canonical.
- Goal 3: Keep generated authority-map output evidence-only and public-package scoped.

## Non-Goals

- Not doing: new active memory, new checker gate, new command, standalone authority-map tool, generated-output approval, PRD approval, bead activation, transition approval, registry, optional packs, command wrappers, install/update behavior, package-manager behavior, release behavior, external mutation, or public dependence on `_maintainer/`.
- Deferred: stricter file inventory enforcement, richer generated review UI, contribution packaging thresholds, optional pack metadata, and command-wrapper review paths.
- Explicitly out of scope: using the generated map to select tasks, rewrite source Markdown, approve changes, validate private maintainer files, or expose maintainer-private detail in public generated output.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-014-FR01` | `logs/authority-map.json` must include `surface_classes` with class-level authority and non-authority boundaries. | P0 | Covers active memory, owner/reference docs, protocols, PRDs, beads, templates, adapters, shims, generated public HTML, generated reports/sidecars, scripts, workflows, and maintainer-private surfaces. |
| `PRD-014-FR02` | `logs/authority-map.json` must include `docs_by_surface` grouped from parsed authority contracts. | P0 | Preserve current parsed-document source. |
| `PRD-014-FR03` | The existing flat `docs` array must remain available. | P0 | Avoid breaking current readers. |
| `PRD-014-FR04` | The generated map must state that generated output is not authority and that private maintainer surfaces are excluded from public generated detail. | P0 | Boundary flags are explicit. |
| `PRD-014-FR05` | Public inventory and relevant protocols must document the refined map without making it an approval surface. | P1 | Inventory owns public package orientation. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-014-SEC01` | Authority-map output must not expose private `_maintainer/` file detail. | P0 | Class metadata may name the private class, but public generated entries must not inventory private files. |
| `PRD-014-SEC02` | Authority-map output must not approve or perform file mutation, external mutation, package install/update behavior, transition approval, release approval, or package-manager behavior. | P0 | Evidence only. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-014-NFR01` | Authority-map generation must remain repo-local and network-free. | P0 | Existing compiler path only. |
| `PRD-014-NFR02` | Grouping must be concise enough for manual inspection. | P1 | Avoid duplicating the full package inventory. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-014-FR01` | `logs/authority-map.json` includes `surface_classes` with requested classes and boundaries. | `python3 scripts/os_compiler.py` | Inspect generated JSON. | current workspace | `logs/authority-map.json` |
| `PRD-014-FR02` | `docs_by_surface` groups parsed authority-contract documents. | `python3 scripts/os_compiler.py` | Inspect grouped paths. | current workspace | `logs/authority-map.json` |
| `PRD-014-FR03` | Existing `docs` list remains present. | `python3 scripts/os_compiler.py` | Confirm `docs` array exists. | current workspace | `logs/authority-map.json` |
| `PRD-014-FR04` | Boundary flags state generated output is not authority and private maintainer surfaces are excluded. | `python3 scripts/os_compiler.py` | Inspect top-level flags. | current workspace | `logs/authority-map.json` |
| `PRD-014-FR05` | Inventory and protocols describe the map and boundaries. | docs HTML and inventory checks | Boundary review. | Markdown docs | generated surfaces |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: unchanged.
- Authority model: clarified through generated evidence and public docs, not changed by generated output.
- Private maintainer material: named as a class boundary but not exposed as public generated detail.
- Generated evidence: remains evidence only.
- External systems: not touched.

### Human Approval Gates

- Approval required before any package-surface change is treated as accepted, any semantic change is implemented, any bead is activated, any transition occurs, any source Markdown is rewritten from generated output, any external system is touched, or any install/update/package-manager behavior is added.
- Stop if generated authority-map output is treated as task authority, approval evidence, a private maintainer inventory, or a source of package-manager behavior.

## Public Interface

- Existing generated sidecar extended:
  - `logs/authority-map.json["surface_classes"]`
  - `logs/authority-map.json["docs_by_surface"]`
  - `logs/authority-map.json["generated_is_not_authority"]`
  - `logs/authority-map.json["private_maintainer_surfaces_excluded"]`
- Existing generated sidecar preserved:
  - `logs/authority-map.json["docs"]`

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `scripts/os_compiler.py` | Adds authority-map surface-class metadata and grouped parsed contracts. | Generated evidence only. |
| `logs/authority-map.json` | Adds grouped and class-level fields. | Generated sidecar; not authority. |
| `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` | Explains the package surface authority map. | Public inventory remains curated Markdown. |
| Semantic Change Proposal Protocol | Names authority-map follow-through for trust-affecting changes. | Proposal evidence only. |
| Extension Protocol | Clarifies extension-generated surfaces should be classed without gaining approval authority. | Extension findings remain evidence until promoted. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/file-inventory.py --check`
- `python3 scripts/os_compiler.py`
- Inspect `logs/authority-map.json`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/docs-html.py` if stale
- `python3 _maintainer/scripts/roadmap-maintenance.py`
- `python3 _maintainer/scripts/roadmap-maintenance.py --apply` after the implemented-candidate entry is added
- `python3 _maintainer/scripts/roadmap-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py` if stale
