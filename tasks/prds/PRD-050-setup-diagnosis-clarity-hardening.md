---
prd_id: PRD-050
status: approved
owner: Dan Sears / Recode
created: 2026-08-04
last_updated: 2026-08-04
risk_level: medium
feature_link: Setup Diagnosis Clarity Hardening
features_status: not compiled
related_prds:
  - PRD-002
  - PRD-006
  - PRD-010
  - PRD-016
  - PRD-042
  - PRD-047
---

# PRD-050 -- Setup Diagnosis Clarity Hardening
<!-- ANCHOR: prd-050-setup-diagnosis-clarity-hardening -->

> AUTHORITY: Public requirements for clearer Bootstrap setup diagnosis, partial-setup routing, missing reusable setup support-file messaging, and validation-after-apply guidance.
> NOT_AUTHORITY: Active memory, target-project truth, setup mutation approval, repair approval, rollback approval, new setup command behavior, command facade expansion, support-only setup authority, prepared starter-target authority, package update permission, dirty-file overwrite, owner-file adaptation approval, package-manager behavior, generated-output authority, PRD approval, bead activation, review acceptance, or implementation acceptance.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting Bootstrap setup diagnosis, partial setup recovery, required reusable setup support-file repair, or source/target confusion.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-08-04

## Summary

Setup Diagnosis Clarity Hardening makes the existing Bootstrap Confidence output easier for a beginner or support helper to interpret when setup is partial or confusing.

The slice adds an explicit diagnosis object and plain-English diagnosis section to `scripts/bootstrap-check.py`. It clarifies source/target state, target kind, partial setup classification, missing reusable setup support files, recommended route, validation-after-apply, and forbidden next actions. It does not add a new command or change mutation authority.

## Problem

Incomplete setup can pass one check while still missing reusable support files, using the wrong source or target folder, or leaving the user unsure whether the next step is fresh setup, Existing Repo Intake, package-owned refresh, recovery guidance, first-session orientation, or product work.

That ambiguity is safer to solve through clearer existing output before adding a facade or stronger command behavior.

## Goals

- Add additive setup-diagnosis fields to Bootstrap plain and JSON output.
- Make partial setup states readable without asking support helpers to infer meaning from raw target-kind and warning fields.
- Clarify required reusable setup support-file recovery for `tasks/beads/BEAD-SCHEMA.md`, `tasks/prds/PRD-000-template.md`, and `tasks/prds/PRD-SHARD-SCHEMA.md`.
- Make validation-after-apply visible for fresh setup and package-owned refresh paths.
- Align setup, troubleshooting, support, protocol, inventory, AI navigation, generated docs, PRD HTML, and maintainer roadmap history.

## Non-Goals

- No new setup command, `precode doctor` behavior, npm subcommand, local facade expansion, broad installer, support-only hidden setup flow, prepared starter-target authority, blind branch clone path, package-manager behavior, executable release-channel behavior, registry lookup, dist-tag resolution, automatic update, dirty-file overwrite, owner-file adaptation approval, rollback automation, task selection, PRD approval, bead activation, review acceptance, generated proof, generated-output authority, app command, app-code edit, hook installation, CI mutation, or external mutation.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-050-FR01` | `scripts/bootstrap-check.py` must add an additive `setup_diagnosis` JSON object without removing existing output keys. | P0 | Source/target clarity, target state, partial setup classification, route, validation, forbidden actions. |
| `PRD-050-FR02` | Plain Bootstrap output must include a setup-diagnosis section that names the route before setup repair, package refresh, first-session orientation, or product work. | P0 | Beginner/support readable. |
| `PRD-050-FR03` | Existing Precode targets missing reusable setup support files must route to package-owned refresh and validation, not product work or package development PRD/bead copy. | P0 | Required template/schema files are not optional. |
| `PRD-050-FR04` | Recovery guidance must include setup diagnosis, validation-after-apply, and forbidden next actions without approving mutation. | P0 | No rollback or support-only authority. |
| `PRD-050-FR05` | Public setup, troubleshooting, support, protocol, inventory, command, and AI navigation surfaces must expose the diagnosis wording without adding a new route or command. | P1 | Discoverability without route inflation. |
| `PRD-050-FR06` | Bootstrap self-test and clarity scenario coverage must pin wrong source/target, existing project, existing Precode partial setup, missing support files, validation-after-apply, and no-mutation boundaries. | P1 | Deterministic package checks. |
| `PRD-050-FR07` | Generated PRD HTML, generated public docs HTML, maintainer changelog, roadmap implemented history, roadmap journal, and generated private roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-050-FR01` / `PRD-050-FR02` | Plain and JSON output include setup diagnosis, source/target clarity, target state, partial setup classification, recommended route, validation-after-apply, and forbidden next actions. | `python3 scripts/bootstrap-check.py --self-test` and representative `--json` command. |
| `PRD-050-FR03` | Missing `BEAD-SCHEMA.md`, `PRD-000-template.md`, and `PRD-SHARD-SCHEMA.md` classify as required support files missing and surface `review_package_copy_candidate` `UP-ID` actions when source files exist. | Bootstrap self-test. |
| `PRD-050-FR04` | `--recovery-guidance` carries setup diagnosis and forbids rollback, destructive cleanup, dirty overwrite, new setup command, support-only setup path, hooks, CI, and generated-output authority. | Bootstrap self-test and clarity scenario. |
| `PRD-050-FR05` | Docs and protocols route confusing setup to existing Bootstrap, Troubleshooting, Support Runbook, Existing Repo Intake, package-owned refresh, or first-session orientation as appropriate. | Source review and docs HTML freshness. |
| `PRD-050-FR06` | Fixtures fail if diagnosis output implies mutation approval, package-manager behavior, broad installer behavior, prepared starter-target authority, or a new command. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-050-FR07` | Roadmap, journal, changelog, generated docs, generated PRD HTML, and generated roadmap HTML are current with numeric shortstats. | Maintainer checks and rendered surface inspection. |

## Required Validation

```bash
python3 scripts/bootstrap-check.py --self-test
python3 scripts/clarity-scenario-check.py
python3 scripts/prd-html.py
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py
python3 _maintainer/scripts/docs-html.py --check
python3 scripts/file-inventory.py --check
python3 scripts/version-check.py
python3 scripts/public-repo-check.py
python3 _maintainer/scripts/roadmap-maintenance.py
python3 _maintainer/scripts/roadmap-html.py
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Boundaries

Setup diagnosis is generated evidence only. It can name the likely route and the first safe validation path, but it cannot approve copying, repair, rollback, setup/update mutation, product work, PRD approval, bead activation, review acceptance, command approval, or package-manager behavior.

The existing Python Bootstrap path remains the source of truth. Optional npm and local facades remain transparent delegation surfaces over existing commands.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B050-setup-diagnosis-clarity-hardening` | `PRD-050-FR01` through `PRD-050-FR07` | PRD shard, additive Bootstrap diagnosis output, recovery guidance, docs/protocol/inventory/navigation wording, clarity coverage, generated docs/PRD/roadmap HTML, maintainer changelog, and roadmap journal are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-050-setup-diagnosis-clarity-hardening.md` | bootstrap self-test, clarity scenario, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-08-04.
