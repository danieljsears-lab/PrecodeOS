---
prd_id: PRD-041
status: approved
owner: Dan Sears / Recode
created: 2026-07-24
last_updated: 2026-07-24
risk_level: high
feature_link: npm Updater Evidence And Compatibility Policy
features_status: not compiled
related_prds:
  - PRD-013
  - PRD-016
---

# PRD-041 -- npm Updater Evidence And Compatibility Policy
<!-- ANCHOR: prd-041-npm-updater-evidence-and-compatibility-policy -->

> AUTHORITY: Public policy for interpreting npm-assisted PrecodeOS upgrade-preview evidence, compatibility thresholds, blocked-update cases, and support expectations before any richer npm updater behavior exists.
> NOT_AUTHORITY: Active memory, target-project truth, package update permission, npm registry freshness, dist-tag resolution, release-channel selection, npm apply behavior, postinstall mutation, dirty-file overwrite, owner-file adaptation approval, rollback automation, package-manager behavior, generated-output authority, PRD approval, bead activation, or implementation acceptance.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting existing-Precode refresh behavior where npm acquisition, package version, upgrade preview, compatibility, or updater language could be confused with update permission.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-24

## Summary

PrecodeOS now has an optional npm `precodeos` entry and upgrade preview may show advisory release-reference metadata from local `package.json`. That improves acquisition and support visibility, but it can also invite a dangerous assumption: that `latest`, npm acquisition, or a clean-looking preview means an active project can be overwritten.

This PRD defines the compatibility policy before any richer npm updater exists. The policy is intentionally conservative: upgrade preview evidence may explain package state, blocked cases, and safe manual review gates, but it does not create an updater, package-manager flow, executable release channel, or mutation authority.

## Problem

Existing Precode targets can contain local package edits, active-memory changes, owner-file truth, active PRDs, active beads, generated evidence, hooks, CI, support recovery state, and app-specific code. A package source can also be acquired through GitHub, local checkout, or npm.

Without a public compatibility policy, users and support helpers may treat npm acquisition, package version, `latest`, or upgrade-preview output as permission to overwrite project truth. That would collapse the staged npm pathway before the read-only update-plan preview and approved package-owned apply candidates have earned trust.

## Goals

- Define the evidence threshold before any existing-Precode refresh decision.
- Name compatible, blocked, dirty, identity-collision, and clone-first support states.
- Keep owner files, active memory, active PRDs/beads, app code, hooks, CI, and generated evidence protected.
- Make the policy inspectable through read-only upgrade-preview metadata and clarity fixtures.
- Preserve the staged roadmap path: policy first, read-only update-plan preview later, approved package-owned apply last.

## Non-Goals

- No npm registry lookup, dist-tag resolution, channel selection, package-manager update behavior, postinstall target mutation, new npm command, npm apply flag, automatic package update, dirty-file overwrite, owner-file adaptation approval, hook or CI mutation, app command, app-code edit, PRD/bead renumbering, rollback automation, support-only hidden shortcut, generated-output authority, task selection, PRD approval, bead activation, review acceptance, release approval, registry behavior, optional-pack behavior, or public promise that `latest` is safe to apply.

## Compatibility Policy

Before any existing-Precode refresh is considered, the user or support helper must have same-source evidence from upgrade preview:

- source package root and target root
- target kind
- package-state classification
- release-reference metadata, including registry lookup and dist-tag lookup status
- dirty package paths
- dirty owner or project paths
- missing package-owned paths
- identity collisions
- deferred package-development PRD or bead identities
- candidate `UP-ID` actions
- explicit non-authority warnings

Compatibility exists only when all of these are true:

- target kind is `existing_precode`
- package state is `clean` for any approved package-owned copy action
- the action is a missing package-owned `review_package_copy_candidate`
- the approved `UP-ID` exists in the current preview
- the source file exists and the target path does not exist
- target PRDs, beads, owner files, active memory, app code, hooks, CI, generated evidence, and private/local state are preserved

Anything else is review evidence, not compatibility.

## Target-State Taxonomy

| State | Meaning | Policy |
|---|---|---|
| `clean` | Package-owned files match the source except possible missing package-owned candidates. | Only missing package-owned `review_package_copy_candidate` actions may be considered after explicit `UP-ID` approval. |
| `dirty_package_edits` | Existing package-owned files differ from the source package. | Block automatic update/apply; review manually. |
| `dirty_project_or_owner_edits` | Owner, active-memory, or project-truth surfaces differ from package templates or need review. | Preserve target truth; do not adapt or overwrite through upgrade preview. |
| `mixed_or_unknown` | Package-owned and owner/project surfaces both need review, or path shape is unclear. | Block automatic update/apply; use support review or recovery guidance. |
| `blocked` | Source, target, target kind, or stop condition prevents safe preview. | Resolve blockers and rerun preview before considering any action. |
| `blocked_identity_collision` | Incoming PRD/bead ID exists at another target path. | Do not copy or renumber; preserve target identity. |
| clone-first support case | Important active work, known local Precode changes, or unclear recovery state. | Preserve the current environment and run preview against a fresh clone before any approved copy action. |

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-041-FR01` | Bootstrap Closeout and Install/Update Manifest must name this compatibility policy before any richer npm updater behavior. | P0 | Policy owns interpretation, not command behavior. |
| `PRD-041-FR02` | Upgrade-preview output must expose read-only policy metadata naming evidence threshold, compatible-only cases, blocked cases, clone-first support, and non-authority limits. | P0 | Existing command only; no new flags. |
| `PRD-041-FR03` | Public setup, support, troubleshooting, user, package-inventory, and AI-readable navigation surfaces must frame npm refresh as compatibility evidence, not update permission. | P0 | Keeps support language consistent. |
| `PRD-041-FR04` | Clarity fixtures must reject wording drift that implies npm updater permission, package-manager behavior, registry lookup, dist-tag resolution, or `latest` overwrite permission. | P0 | Text-contract and payload regression only. |
| `PRD-041-FR05` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs/PRD surfaces, and generated roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-041-FR01` | Bootstrap Closeout and Install/Update Manifest point to this policy and keep npm update-plan/apply deferred. | Protocol source review. |
| `PRD-041-FR02` | `bootstrap-check.py --upgrade-preview --json` includes `updater_compatibility_policy` and `--self-test` checks the policy fields. | `python3 scripts/bootstrap-check.py --self-test`. |
| `PRD-041-FR03` | User/support docs and package inventory describe compatibility evidence without saying npm updates the target. | Docs review and docs HTML freshness. |
| `PRD-041-FR04` | Clarity scenarios pin no registry lookup, no dist-tag lookup, blocked cases, compatible-only cases, and non-authority warnings. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-041-FR05` | Roadmap, journal, changelog, PRD HTML, docs HTML, and roadmap HTML are current and rendered shortstats are numeric. | Maintainer checks and rendered roadmap inspection. |

## Risk And Permission Model

- Stop if source package root, target root, target kind, package-state classification, release-reference status, dirty paths, identity collisions, deferred identities, or candidate action IDs are unclear.
- Stop if the target has important active work, known local Precode changes, unclear support history, or recovery risk and no clone-first preview has been run.
- Stop if a user asks npm to overwrite, adapt owner files, renumber PRDs/beads, install hooks, change CI, run app commands, edit app code, query registry freshness, resolve dist-tags, select a channel, or roll back.
- Approval for a specific `UP-ID` is still only approval to copy an eligible missing package-owned file through the existing Python closeout path; it is not approval to update the project, overwrite dirty files, adapt owner truth, or accept generated output as proof.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/bootstrap-check.py` | Existing `--upgrade-preview` JSON/plain output. | Adds read-only `updater_compatibility_policy` metadata; no new command behavior. | Self-test and manual JSON/plain review. | `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md` |
| `bin/precodeos.mjs` | Existing npm `setup-preview` and `upgrade-preview` facade. | Still exposes no apply flags and delegates visibly to Bootstrap Confidence. | Clarity scenario no-apply fixture. | `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md` |
| Bootstrap/setup protocols | Policy references and support wording. | Explain compatibility evidence before update-plan or apply candidates. | Source review and docs checks. | `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md`
- Parent PRDs:
  - `tasks/prds/PRD-013-installable-precode-cli-wrapper.md`
  - `tasks/prds/PRD-016-installer-bootstrap-closeout.md`
- Owner protocols:
  - `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Files or folders likely in play:
  - `scripts/bootstrap-check.py`
  - `scripts/clarity-scenario-check.py`
  - `bin/precodeos.mjs`
  - `README.md`
  - `docs/PRECODE-GUIDED-SETUP.md`
  - `docs/PRECODE-SUPPORT-RUNBOOK.md`
  - `docs/PRECODE-TROUBLESHOOTING.md`
  - `docs/PRECODE-USER-GUIDE.md`
  - `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
  - `llms.txt`
  - `tasks/reference/PROMPT-PATTERNS.md`
  - `tasks/prds-html/`
  - `docs-html/`
  - `_maintainer/CHANGELOG.md`
  - `_maintainer/PRECODE-ROADMAP.md`
  - `_maintainer/PRECODE-ROADMAP-JOURNAL.md`
  - `_maintainer/PRECODE-ROADMAP.html`
- Files or folders out of scope:
  - target app code
  - package-manager mutation
  - npm registry integration
  - release-channel metadata
  - hooks and CI mutation
  - dirty package-file overwrite
  - automatic owner-file adaptation
  - rollback automation
  - new npm commands or apply flags

## Required Validation

```bash
python3 scripts/bootstrap-check.py --self-test
python3 scripts/clarity-scenario-check.py
python3 scripts/file-inventory.py --check
python3 scripts/version-check.py
python3 scripts/prd-html.py --check
python3 _maintainer/scripts/docs-html.py --check
python3 _maintainer/scripts/roadmap-html.py --check
git diff --check
```

## Anti-Shallow Checks

- If implementation adds a new npm command, npm apply flag, registry lookup, dist-tag resolution, channel selection, postinstall mutation, or package-manager behavior, it violates this PRD.
- If `latest` or package version is treated as overwrite permission, it violates this PRD.
- If dirty package files, owner files, active memory, PRDs, beads, hooks, CI, app code, or generated evidence are updated automatically, it violates this PRD.
- If generated preview output is treated as target-project truth, compatibility proof, or implementation acceptance, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B041-npm-updater-evidence-and-compatibility-policy` | `PRD-041-FR01` through `PRD-041-FR05` | PRD policy, read-only upgrade-preview metadata, protocol/docs/navigation wording, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md` | bootstrap self-test, clarity scenario, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-07-24.
