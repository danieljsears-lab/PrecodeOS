---
prd_id: PRD-045
status: approved
owner: user
risk_level: medium
feature_link: Authority Map Query CLI
features_status: not compiled
related_prds:
  - PRD-014
---

# PRD-045 -- Authority Map Query CLI
<!-- ANCHOR: prd-045-authority-map-query-cli -->

> AUTHORITY: Destination shard for the read-only Authority Map Query CLI over existing public PrecodeOS authority-map contracts.
> NOT_AUTHORITY: Active memory, task selection, command approval, PRD approval, bead activation, transition approval, implementation acceptance, owner-file replacement, runtime enforcement, private maintainer inventory, generated evidence truth, registry behavior, optional-pack behavior, install/update behavior, release-channel behavior, package-manager behavior, or release approval.
> LOAD_WHEN: Reviewing, implementing, or decomposing authority-map lookup behavior for maintainers, contributors, or AI assistants orienting before public package edits.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-27

## State

- ID: `PRD-045`
- Status: `approved`
- Owner: `user`
- Risk level: `medium`
- Last updated: `2026-07-27`

## Feature Link

- Feature: `Authority Map Query CLI`
- `FEATURES.md` status: `not compiled`
- Related PRDs: `PRD-014`

## Source Inputs

- Source type: `maintainer roadmap evidence | PRD-014 follow-up | package inventory`
- Source references:
  - `_maintainer/PRECODE-ROADMAP.md` ranked item, `Authority Map Query CLI`
  - `tasks/prds/PRD-014-authority-map-package-surfaces.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `scripts/precode_inventory.py`
  - `logs/authority-map.json`
- Stable facts:
  - Markdown owner files and protocols hold package meaning.
  - `logs/authority-map.json` is generated orientation evidence only.
  - PRD-014 intentionally shipped generated authority-map grouping without a command.
- Assumptions:
  - The query CLI should compile fresh authority-map data in memory instead of treating stale generated JSON as authority.
  - A transparent optional `precode authority-map` facade can improve discoverability when it prints the underlying script command and preserves the script boundary.

## Problem

Contributors and AI assistants can inspect the generated authority map, but finding the relevant owner file or surface class still requires opening a large JSON sidecar or broad-searching the repo.

## User Moment

- Before: A maintainer, contributor, or AI assistant has a term such as `PRD approval`, `active memory`, or `generated evidence` and must manually search multiple docs to find the right authority surface.
- After: They can run a read-only query that returns candidate authority contracts, surface classes, and load triggers before deciding which canonical Markdown owner file to read.
- Why now: Authority-map grouping exists, PRD cluster navigation has improved reader orientation, and the next architecture-health need is map-first lookup without adding enforcement.

## Destination

- Destination statement: `scripts/authority-map-query.py` provides a read-only lookup over freshly compiled authority-map data, with readable default output and `--json` output for agents.
- Definition of done:
  - The dedicated script supports text queries, exact path lookup, surface-class filtering, surface-class listing, JSON output, limits, and deterministic self-test coverage.
  - `scripts/precode_cli.py authority-map` transparently delegates to the script and keeps the wrapper boundary visible.
  - Public docs and protocols explain the CLI as navigation-only and evidence-only.
  - Roadmap history, roadmap journal, generated docs/PRD/roadmap HTML, and maintainer changelog are current.
- First useful vertical slice: lookup over parsed authority contracts and surface-class summaries only.

## Users

- Primary user: Maintainer or contributor checking which public package surface owns a fact.
- Secondary user: AI coding agent orienting before editing PrecodeOS package files.
- Excluded user: Automation expecting task selection, command approval, owner-file replacement, runtime enforcement, install/update behavior, package-manager behavior, or private maintainer inventory detail.

## Goals

- Goal 1: Make relevant authority contracts easier to find before full-file reads.
- Goal 2: Preserve Markdown owner files, PRDs, beads, protocols, and human approval as canonical.
- Goal 3: Keep authority-map query output read-only, repo-local, network-free, and public-package scoped.

## Non-Goals

- Not doing: active-memory expansion, task selection, command approval, owner-file replacement, PRD approval, bead activation, transition approval, implementation acceptance, generated-output approval, runtime enforcement, private maintainer inventory exposure, registry behavior, optional packs, install/update behavior, release-channel behavior, package-manager behavior, release approval, or external mutation.
- Deferred: richer ranking, semantic search, graph traversal, stale-claim judgment, package knowledge lint integration, CI enforcement, and generated HTML query UI.
- Explicitly out of scope: using query output to rewrite source Markdown, approve edits, choose current work, validate private maintainer files, or replace `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`.

## Requirements

### Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-045-FR01` | `scripts/authority-map-query.py` must compile fresh authority-map data in memory and not read `logs/authority-map.json` as authority. | P0 | Generated sidecar can be refreshed separately. |
| `PRD-045-FR02` | The script must support positional query text or `--query`, `--path`, `--surface-class`, `--list-surface-classes`, `--limit`, `--json`, and `--self-test`. | P0 | Query and filters may combine when useful. |
| `PRD-045-FR03` | Default text output must show path, title, surface class, authority, not-authority, and load trigger for each match. | P0 | Human-readable orientation. |
| `PRD-045-FR04` | JSON output must include `tool`, `query`, `match_count`, `matches`, `surface_classes` when relevant, a boundary warning, and forbidden uses. | P0 | Agent-readable output without authority promotion. |
| `PRD-045-FR05` | `scripts/precode_cli.py authority-map` must transparently delegate to the dedicated script and preserve underlying-command display. | P1 | Convenience facade only. |
| `PRD-045-FR06` | Public docs, protocols, and clarity scenario coverage must preserve navigation-only wording. | P1 | Prevents future authority drift. |

### Security And Privacy Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-045-SEC01` | Query output must not expose private `_maintainer/` file inventory detail. | P0 | Surface-class summary may retain the private boundary. |
| `PRD-045-SEC02` | Query behavior must not mutate files, touch external systems, approve commands, or create package-manager/update behavior. | P0 | Read-only local inspection. |

### Non-Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---|---|
| `PRD-045-NFR01` | The CLI must remain dependency-free, repo-local, and network-free. | P0 | Standard-library implementation. |
| `PRD-045-NFR02` | Text output must be concise enough to scan before loading owner files. | P1 | Default limit should prevent noisy output. |

## Acceptance Oracle Matrix

| Requirement ID | Expected behavior | Automated check | Manual check | Fixture or data needed | Evidence location |
|---|---|---|---|---|---|
| `PRD-045-FR01` | Query payload comes from in-memory compiler output. | `python3 scripts/authority-map-query.py --self-test` | Inspect implementation imports and no generated-sidecar read path. | temp fixture and current workspace | stdout JSON/text |
| `PRD-045-FR02` | Supported flags parse and return expected statuses. | `python3 scripts/authority-map-query.py --self-test` | Run representative commands. | temp fixture and current workspace | stdout |
| `PRD-045-FR03` | Text output includes path, title, surface class, authority, not-authority, and load trigger. | `python3 scripts/authority-map-query.py --query "PRD approval"` | Inspect printed output. | current workspace | stdout |
| `PRD-045-FR04` | JSON output includes stable top-level fields and boundary warning. | `python3 scripts/authority-map-query.py --path tasks/prds/PRD-014-authority-map-package-surfaces.md --json` | Inspect payload. | current workspace | stdout JSON |
| `PRD-045-FR05` | Optional facade prints and runs the underlying script command. | `python3 scripts/precode_cli.py authority-map --query "active memory" --dry-run` | Confirm wrapper boundary note. | current workspace | stdout |
| `PRD-045-FR06` | Docs/protocol wording keeps query navigation-only. | `python3 scripts/clarity-scenario-check.py` | Boundary review. | canonical Markdown | check output |

## Risk And Permission Model

### Sensitive Surfaces

- Active memory: unchanged.
- Authority model: easier to inspect, not changed by query output.
- Private maintainer material: remains excluded from public generated detail and query matches.
- Generated evidence: remains evidence only.
- External systems: not touched.

### Human Approval Gates

- Approval required before any package-surface change is treated as accepted, any source Markdown is rewritten from query output, any task is selected, any command is approved, any PRD or bead is approved, any transition occurs, any external system is touched, or any install/update/package-manager behavior is added.
- Stop if authority-map query output is treated as task authority, command approval, generated proof, owner-file replacement, private maintainer inventory, runtime enforcement, or package-manager behavior.

## Public Interface

- New direct command:
  - `python3 scripts/authority-map-query.py --query "active memory"`
  - `python3 scripts/authority-map-query.py --path tasks/prds/PRD-014-authority-map-package-surfaces.md --json`
  - `python3 scripts/authority-map-query.py --list-surface-classes`
- New optional facade command:
  - `python3 scripts/precode_cli.py authority-map --query "active memory"`

## Affected Surfaces

| Surface | Change | Authority boundary |
|---|---|---|
| `scripts/authority-map-query.py` | Adds read-only lookup over compiled authority-map contracts. | Navigation evidence only. |
| `scripts/precode_cli.py` | Adds transparent `authority-map` convenience facade. | Wrapper does not approve work or hide the underlying script. |
| `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` | Explains the query CLI and facade. | Inventory remains curated Markdown authority. |
| `tasks/reference/EXTENSION-PROTOCOL.md` | Clarifies query surfaces are navigation-only. | Extension findings remain evidence until promoted. |
| `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` | Clarifies command-surface triage for the lookup CLI. | No command approval or enforcement. |
| Maintainer roadmap, journal, and changelog | Record implemented candidate. | Maintainer-local history only. |

## Validation Plan

- `python3 scripts/authority-map-query.py --self-test`
- `python3 scripts/authority-map-query.py --query "PRD approval"`
- `python3 scripts/authority-map-query.py --path tasks/prds/PRD-014-authority-map-package-surfaces.md --json`
- `python3 scripts/precode_cli.py authority-map --query "active memory" --dry-run`
- `python3 scripts/precode_cli.py authority-map --query "active memory"`
- `python3 scripts/clarity-scenario-check.py`
- `python3 scripts/version-check.py`
- `python3 scripts/file-inventory.py --check`
- `python3 scripts/package-knowledge-lint.py --check`
- `python3 scripts/extension-check.py`
- `python3 scripts/public-repo-check.py`
- `python3 scripts/prd-html.py --check`
- `python3 _maintainer/scripts/docs-html.py --check`
- `python3 _maintainer/scripts/roadmap-html.py --check`
