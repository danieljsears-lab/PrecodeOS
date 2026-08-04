---
prd_id: PRD-042
status: approved
owner: Dan Sears / Recode
created: 2026-07-24
last_updated: 2026-07-24
risk_level: high
feature_link: npm Update Plan Preview
features_status: not compiled
related_prds:
  - PRD-013
  - PRD-016
  - PRD-041
---

# PRD-042 -- npm Update Plan Preview
<!-- ANCHOR: prd-042-npm-update-plan-preview -->

> AUTHORITY: Public requirements for the read-only npm-facing update-plan preview over existing Precode package-refresh evidence.
> NOT_AUTHORITY: Active memory, target-project truth, package update permission, copy approval, npm apply behavior, npm registry freshness, dist-tag resolution, release-channel selection, postinstall mutation, dirty-file overwrite, owner-file adaptation approval, rollback automation, package-manager behavior, generated-output authority, PRD approval, bead activation, or implementation acceptance.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting existing-Precode refresh behavior where a user needs a grouped update plan before any separately approved package-owned copy action.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-24

## Summary

PrecodeOS already has a read-only npm `precodeos` entry, local release-reference metadata, and the npm Updater Evidence And Compatibility Policy. Existing users still need a clearer way to inspect candidate refresh actions without treating npm as an updater.

This PRD adds a read-only update-plan preview. It groups the existing upgrade-preview evidence into candidate package-copy IDs, manual-review IDs, blocked IDs, deferred IDs, same-session freshness requirements, validation prompts, and explicit non-authority warnings. It does not itself approve or perform copying; the later PRD-047 `apply-package-owned` delegation is separate.

## Problem

Upgrade preview exposes the raw package-state comparison and `UP-ID` actions. That is useful, but it can be too low-level for a support helper or returning user deciding whether a refresh is safe enough to discuss.

Without a grouped update-plan preview, users may either skip blocker review or overinterpret a clean-looking preview as update permission. The package needs one more read-only planning layer before any approved package-owned apply path is considered.

## Goals

- Add a read-only `npm_update_plan_preview` object to `scripts/bootstrap-check.py`.
- Expose the plan through `--update-plan-preview` and the optional npm `precodeos update-plan-preview` command.
- Reuse upgrade-preview evidence and PRD-041 compatibility policy metadata instead of creating a separate updater subsystem.
- Group current `UP-ID` actions into candidate package-copy, manual-review, blocked, and deferred buckets.
- Name same-session freshness, clone-first support, validation prompts, optional registry metadata status, and non-authority limits.
- Keep copy approval and mutation behavior out of update-plan preview.

## Non-Goals

- No target mutation, copy approval from update-plan preview, postinstall behavior, npm registry lookup, dist-tag resolution, channel selection, package-manager update behavior, automatic package update, dirty-file overwrite, owner-file adaptation approval, hook or CI mutation, app command, app-code edit, PRD/bead renumbering, rollback automation, support-only hidden shortcut, generated-output authority, task selection, PRD approval, bead activation, review acceptance, release approval, registry behavior, optional-pack behavior, or public promise that `latest` is safe to apply.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-042-FR01` | `scripts/bootstrap-check.py --update-plan-preview` must include `package_upgrade_preview` evidence and a separate `npm_update_plan_preview` object. | P0 | The plan summarizes, not replaces, upgrade preview. |
| `PRD-042-FR02` | The plan must expose action summary counts, grouped current `UP-ID` lists, same-session freshness requirements, validation prompts, optional registry metadata status, and non-authority limits. | P0 | Action IDs remain advisory evidence. |
| `PRD-042-FR03` | `bin/precodeos.mjs` and `scripts/precode_cli.py` may expose read-only `update-plan-preview` delegation to Bootstrap Confidence. | P0 | No npm apply flags or approval IDs. |
| `PRD-042-FR04` | Public setup, support, troubleshooting, user, package-inventory, protocol, and AI-readable navigation surfaces must frame update-plan preview as generated evidence only. | P0 | Prevents package-manager drift. |
| `PRD-042-FR05` | Bootstrap self-test and clarity fixtures must cover update-plan JSON/plain shape, facade delegation, no registry lookup, no dist-tag resolution, no copy approval from update-plan preview, and no mutation authority. | P0 | Text-contract and payload regression only. |
| `PRD-042-FR06` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs/PRD surfaces, and generated roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-042-FR01` | `--update-plan-preview --json` includes both `package_upgrade_preview` and `npm_update_plan_preview`. | `python3 scripts/bootstrap-check.py --self-test`. |
| `PRD-042-FR02` | The plan reports grouped `UP-ID` buckets, counts, `same_session_requirement`, `validation_prompts`, `optional_registry_metadata`, and non-authority warnings. | Bootstrap self-test and manual JSON review. |
| `PRD-042-FR03` | `precodeos update-plan-preview --target <existing-precode-root>` and `python3 scripts/precode_cli.py update-plan-preview --target <existing-precode-root>` print/delegate to `--update-plan-preview`; update-plan preview still exposes no approval flags. | `python3 scripts/clarity-scenario-check.py`. |
| `PRD-042-FR04` | Public docs/protocols/navigation describe update-plan preview without implying update permission. | Docs review and docs HTML freshness. |
| `PRD-042-FR05` | Fixtures fail if registry/dist-tag lookup, npm apply exposure, package-manager behavior, or generated-output authority appears. | Clarity scenario and bootstrap self-test. |
| `PRD-042-FR06` | Roadmap, journal, changelog, PRD HTML, docs HTML, and roadmap HTML are current and rendered shortstats are numeric. | Maintainer checks and rendered roadmap inspection. |

## Risk And Permission Model

- Stop if source package root, target root, target kind, package-state classification, release-reference status, dirty paths, identity collisions, deferred identities, or candidate action IDs are unclear.
- Stop if a user asks npm to apply, overwrite, adapt owner files, renumber PRDs/beads, install hooks, change CI, run app commands, edit app code, query registry freshness, resolve dist-tags, select a channel, or roll back.
- For important active work, known local Precode changes, or unclear recovery state, use clone-first support review before any package refresh discussion.
- The same-session preview requirement means old `UP-ID` values are not reusable approval tokens.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `scripts/bootstrap-check.py` | `--update-plan-preview` plain and JSON output. | Adds read-only update-plan summary over upgrade preview; no mutation. | Self-test and manual JSON/plain review. | `tasks/prds/PRD-042-npm-update-plan-preview.md` |
| `bin/precodeos.mjs` | `precodeos update-plan-preview --target <existing-precode-root> [--json]`. | Delegates to Bootstrap Confidence and exposes no apply flags. | Clarity scenario no-apply fixture. | `tasks/prds/PRD-042-npm-update-plan-preview.md` |
| `scripts/precode_cli.py` | `python3 scripts/precode_cli.py update-plan-preview --target <existing-precode-root> [--json]`. | Local facade prints the delegated Python command. | Clarity scenario delegation fixture. | `tasks/prds/PRD-042-npm-update-plan-preview.md` |
| Bootstrap/setup protocols | Protocol and support wording. | Explain update-plan preview as planning evidence before any separate copy decision. | Source review and docs checks. | `tasks/prds/PRD-042-npm-update-plan-preview.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-042-npm-update-plan-preview.md`
- Parent PRDs:
  - `tasks/prds/PRD-013-installable-precode-cli-wrapper.md`
  - `tasks/prds/PRD-016-installer-bootstrap-closeout.md`
  - `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md`
- Owner protocols:
  - `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Files or folders likely in play:
  - `scripts/bootstrap-check.py`
  - `scripts/precode_cli.py`
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
  - npm apply flags

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

- If implementation adds copy approval to update-plan preview, registry lookup, dist-tag resolution, channel selection, postinstall mutation, or package-manager behavior, it violates this PRD.
- If the update-plan preview is treated as copy permission or generated authority, it violates this PRD.
- If dirty package files, owner files, active memory, PRDs, beads, hooks, CI, app code, or generated evidence are updated automatically, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B042-npm-update-plan-preview` | `PRD-042-FR01` through `PRD-042-FR06` | Read-only update-plan preview, npm/local facade delegation, protocol/docs/navigation wording, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-042-npm-update-plan-preview.md` | bootstrap self-test, clarity scenario, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-07-24.
