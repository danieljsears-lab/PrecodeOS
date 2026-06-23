---
prd_id: PRD-028
status: approved
owner: Dan Sears / Recode
created: 2026-06-23
last_updated: 2026-06-23
feature_link: Build Attribution Ledger
---

# PRD-028 -- Build Attribution Ledger
<!-- ANCHOR: prd-028-build-attribution-ledger -->

> AUTHORITY: Public requirements for generated Build Attribution Ledger evidence, reviewed human contributor and agent/tool attribution fields, confidence states, and accountability boundaries.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, merge approval, release approval, contributor scoring, blame assignment, telemetry, GitHub mutation, package registry, optional-pack behavior, install/update behavior, or package-manager behavior.
> LOAD_WHEN: Planning, implementing, reviewing, or validating build attribution, contributor accountability, agent/tool traceability, or the generated Build Attribution Ledger.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-23

## Summary

PrecodeOS should help a builder answer "who built what?" without turning attribution into task authority, blame, scoring, telemetry, or a package registry.

The Build Attribution Ledger compiles reviewed attribution evidence from beads and supporting Git/journal hints. Closeout-reviewed attribution is the strongest source. Git authorship, generated journal entries, branch names, tool logs, and teammate notes are evidence hints only until reviewed into bead Closeout Evidence.

## Problem

Existing Precode surfaces show what bead changed, what evidence exists, and what branch/worktree context may matter. They do not preserve a compact shared view of human contributor, contributor role, agent/tool surface, reviewer, and attribution uncertainty by bead.

That gap matters more once Small Team Collaboration Lane, handoffs, fresh-context review, and generated build journal evidence are used together. A future reviewer should be able to trace who contributed the work and which agent/tool surface helped, without relying on chat memory.

## Goals

- Add reviewed build attribution fields to bead closeout.
- Add generated ledger JSON and Markdown views for attribution by bead.
- Preserve human contributor and agent/tool surface separately.
- Label missing, partial, reviewed, and Git-hint-only attribution clearly.
- Keep the ledger generated evidence only.
- Record the shipped feature in maintainer roadmap history as an implemented candidate.

## Non-Goals

- No task assignment or task selection.
- No PRD approval, bead activation, implementation acceptance, merge approval, or release approval.
- No contributor scoring, blame assignment, productivity ranking, telemetry, analytics, dashboard backend, or external tracking system.
- No GitHub mutation, PR approval, label/comment mutation, workflow mutation, or project-board behavior.
- No package registry, plugin registry, optional-pack behavior, install/update behavior, release channel, command wrapper, or package-manager behavior.
- No new active-memory file.

## Functional Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-028-FR01` | Add closeout fields for human contributor, contributor role, agent/tool surface, attribution reviewer, and attribution uncertainty. | P0 | Existing reviewed values must be preserved by closeout refresh. |
| `PRD-028-FR02` | Add `scripts/build-attribution-ledger.py` as a read-only checker that prints JSON by default. | P0 | Default command writes no files. |
| `PRD-028-FR03` | Add `--self-test` deterministic fixtures for reviewed closeout, partial closeout, missing attribution, generated warning, and forbidden uses. | P0 | No network or external dependency. |
| `PRD-028-FR04` | Expose `build_attribution` in compiled state and generated OS Health sidecars. | P1 | Sidecars are generated evidence only. |
| `PRD-028-FR05` | Generate `logs/build-attribution-ledger.json` and `logs/build-attribution-ledger.md`. | P1 | Markdown must carry generated authority demotion. |
| `PRD-028-FR06` | Ledger entries must include bead identity, status, primary authority, human contributor, role, agent/tool surface, reviewer, uncertainty, source, confidence, Git author hint, journal timestamp, changed-path hints, and warnings. | P1 | Git hints must not become contributor identity. |
| `PRD-028-FR07` | Protocols, prompts, user docs, package inventory, maintainer changelog, roadmap, roadmap journal, and generated surfaces must be updated. | P1 | Maintainer-history follow-through is part of done. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-028-FR01` | `scripts/update-bead-closeout.py` preserves attribution fields and fills explicit missing values. | Code review and closeout refresh behavior. |
| `PRD-028-FR02` | `python3 scripts/build-attribution-ledger.py` prints JSON and writes no files. | Command output. |
| `PRD-028-FR03` | `python3 scripts/build-attribution-ledger.py --self-test` passes. | Command output. |
| `PRD-028-FR04` / `PRD-028-FR05` | `python3 scripts/os-health.py` refreshes attribution sidecars. | `logs/build-attribution-ledger.json/md`. |
| `PRD-028-FR07` | Scenario, inventory, docs, PRD HTML, roadmap HTML, memory, and version checks pass. | Validation commands. |

## Required Validation

```bash
python3 scripts/build-attribution-ledger.py --self-test
python3 scripts/clarity-scenario-check.py
python3 scripts/file-inventory.py --check
python3 scripts/public-repo-check.py
python3 scripts/prd-html.py --check
python3 scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
bash scripts/validate-memory.sh
python3 scripts/version-check.py
PYTHONPYCACHEPREFIX=/private/tmp/precode-pycache python3 -m py_compile scripts/build-attribution-ledger.py scripts/os_compiler.py scripts/os-health.py scripts/precode_outputs.py scripts/update-bead-closeout.py scripts/clarity-scenario-check.py
```

## Boundaries

The ledger answers attribution questions only as evidence. It must route any durable correction back to bead Closeout Evidence, owner files, recorded checks, coordinator review, or maintainer history. It must not become a second tracker, task registry, people registry, plugin registry, package registry, or authority surface.
