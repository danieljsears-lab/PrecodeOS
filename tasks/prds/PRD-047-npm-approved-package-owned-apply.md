---
prd_id: PRD-047
status: approved
owner: Dan Sears / Recode
created: 2026-07-31
last_updated: 2026-07-31
risk_level: high
feature_link: npm Approved Package-Owned Apply
features_status: not compiled
related_prds:
  - PRD-013
  - PRD-016
  - PRD-041
  - PRD-042
---

# PRD-047 -- npm Approved Package-Owned Apply
<!-- ANCHOR: prd-047-npm-approved-package-owned-apply -->

> AUTHORITY: Public requirements for the optional npm and local facade command that delegates explicitly approved missing package-owned `UP-ID` copy actions to the existing Python upgrade-apply source of truth.
> NOT_AUTHORITY: Active memory, target-project truth, broad npm updater behavior, package update permission, npm registry freshness, dist-tag resolution, release-channel selection, postinstall mutation, dirty-file overwrite, owner-file adaptation approval, rollback automation, package-manager behavior, generated-output authority, PRD approval, bead activation, review acceptance, or implementation acceptance.
> LOAD_WHEN: Planning, implementing, reviewing, or supporting existing-Precode refresh behavior where a current update-plan preview has named missing package-owned `UP-ID` copy candidates and the user explicitly approves those IDs.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-07-31

## Summary

PrecodeOS already has a Python upgrade-apply path for existing Precode targets:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>
```

That path copies only approved missing package-owned files marked `review_package_copy_candidate`. PRD-041 and PRD-042 intentionally kept npm read-only until policy and update-plan evidence proved trustworthy.

This PRD adds the narrow npm-facing apply slice. The npm and local facades may expose `apply-package-owned`, but only as transparent delegation to the existing Python command. Node must not implement copy logic.

## Problem

Existing users can inspect safe missing package-owned `UP-ID` candidates through upgrade preview and update-plan preview, but the public npm surface still stops before the same approved copy action the Python path already supports.

Without a single visible facade command, support helpers may either ask users to switch mental models from npm preview to Python apply, or invent unsafe "update" language. The package needs one explicit command name for approved package-owned copy actions while still refusing broad updater behavior.

## Goals

- Add `precodeos apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--json]`.
- Add matching `python3 scripts/precode_cli.py apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--json]`.
- Delegate to `scripts/bootstrap-check.py --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>`.
- Require at least one explicit `--approve-action <UP-ID>`.
- Preserve the Python implementation as the only mutation engine.
- Keep the same-session preview requirement from PRD-042 and the compatibility policy from PRD-041.

## Non-Goals

- No postinstall behavior, npm registry lookup, dist-tag resolution, channel selection, package-manager update behavior, automatic package update, dirty-file overwrite, owner-file adaptation approval, hook or CI mutation, app command, app-code edit, PRD/bead renumbering, rollback automation, support-only hidden shortcut, generated-output authority, task selection, PRD approval, bead activation, review acceptance, release approval, registry behavior, optional-pack behavior, or public promise that `latest` is safe to apply.
- No JavaScript copy engine. `bin/precodeos.mjs` only parses the facade command, prints the delegated Python command, and preserves the Python exit status.

## Requirements

| ID | Requirement | Priority | Notes |
|---|---|---:|---|
| `PRD-047-FR01` | `bin/precodeos.mjs` must expose `apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--json]`. | P0 | Repeatable `--approve-action` is allowed. |
| `PRD-047-FR02` | The npm command must delegate to `scripts/bootstrap-check.py --upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>` from the package source. | P0 | No Node copy logic. |
| `PRD-047-FR03` | `scripts/precode_cli.py` must expose the same local facade delegation. | P0 | Keeps local and npm command surfaces aligned. |
| `PRD-047-FR04` | Facades must require at least one approved `UP-ID` and reject `--approve-action` on preview-only commands. | P0 | Prevents accidental approval-shaped preview calls. |
| `PRD-047-FR05` | Public setup, support, troubleshooting, user, package-inventory, protocol, and AI-readable navigation surfaces must frame the command as approved package-owned copy delegation, not npm update. | P0 | Supersedes only the previous no-npm-apply wording for this narrow command. |
| `PRD-047-FR06` | Bootstrap self-test and clarity fixtures must cover facade delegation, missing approval refusal, preserved no-registry/no-dist-tag boundaries, and no package-manager behavior. | P0 | Regression and text-contract coverage only. |
| `PRD-047-FR07` | Maintainer changelog, roadmap implemented history, roadmap journal, generated docs/PRD surfaces, and generated roadmap HTML must be refreshed with numeric shortstats. | P1 | Maintainer closeout. |

## Acceptance Criteria

| Requirement | Acceptance check | Evidence |
|---|---|---|
| `PRD-047-FR01` | `precodeos apply-package-owned --target <existing-precode-root> --approve-action <UP-ID>` is accepted by the npm facade. | Clarity scenario fixture. |
| `PRD-047-FR02` | The printed underlying command includes `--upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>`. | Clarity scenario fixture and manual command review. |
| `PRD-047-FR03` | `python3 scripts/precode_cli.py apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> --dry-run` prints the same delegated Python apply path. | Clarity scenario fixture. |
| `PRD-047-FR04` | Missing approval fails before delegation, and preview commands still reject approval IDs. | Facade argument tests and clarity scenario. |
| `PRD-047-FR05` | Public docs/protocols/navigation describe approved package-owned copy delegation without implying update permission. | Docs review and docs HTML freshness. |
| `PRD-047-FR06` | Existing Python refusal fixtures still cover dirty states, identity collisions, unknown IDs, missing approvals, and overwrites. | `python3 scripts/bootstrap-check.py --self-test`. |
| `PRD-047-FR07` | Roadmap, journal, changelog, PRD HTML, docs HTML, and roadmap HTML are current and rendered shortstats are numeric. | Maintainer checks and rendered roadmap inspection. |

## Risk And Permission Model

- Stop if source package root, target root, target kind, package-state classification, release-reference status, dirty paths, identity collisions, deferred identities, or approved action IDs are unclear.
- Stop if a user asks npm to update, overwrite, adapt owner files, renumber PRDs/beads, install hooks, change CI, run app commands, edit app code, query registry freshness, resolve dist-tags, select a channel, or roll back.
- The facade command is only a convenience entry to the current Python apply path. It is not a package manager, release channel, updater, registry freshness source, copy approval, generated proof, or support-only hidden path.

## Module / Interface Candidates

| Candidate module or boundary | Public interface / caller expectation | Behavior contract | Test boundary | Owner file |
|---|---|---|---|---|
| `bin/precodeos.mjs` | `precodeos apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--json]`. | Prints and delegates to Python upgrade apply; no copy logic. | Clarity scenario and manual command review. | `tasks/prds/PRD-047-npm-approved-package-owned-apply.md` |
| `scripts/precode_cli.py` | `python3 scripts/precode_cli.py apply-package-owned --target <existing-precode-root> --approve-action <UP-ID> [--json]`. | Local facade prints the delegated Python command. | Clarity scenario fixture. | `tasks/prds/PRD-047-npm-approved-package-owned-apply.md` |
| `scripts/bootstrap-check.py` | Existing `--upgrade-preview --apply-upgrade-preview --approve-action <UP-ID>`. | Remains the only mutation engine and refusal-policy owner. | Bootstrap self-test. | `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md` |

## Agent Context Contract

- Primary authority file: `tasks/prds/PRD-047-npm-approved-package-owned-apply.md`
- Parent PRDs:
  - `tasks/prds/PRD-013-installable-precode-cli-wrapper.md`
  - `tasks/prds/PRD-016-installer-bootstrap-closeout.md`
  - `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md`
  - `tasks/prds/PRD-042-npm-update-plan-preview.md`
- Owner protocols:
  - `tasks/reference/BOOTSTRAP-CLOSEOUT-PROTOCOL.md`
  - `tasks/reference/INSTALL-UPDATE-MANIFEST-PROTOCOL.md`
  - `tasks/reference/BOOTSTRAP-CONFIDENCE-PROTOCOL.md`
  - `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`
  - `tasks/reference/EXTENSION-PROTOCOL.md`
- Files or folders likely in play:
  - `bin/precodeos.mjs`
  - `scripts/precode_cli.py`
  - `scripts/clarity-scenario-check.py`
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
  - JavaScript copy logic

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

- If implementation copies files from JavaScript, it violates this PRD.
- If `apply-package-owned` accepts no approval ID, it violates this PRD.
- If `latest`, npm acquisition, or update-plan preview is treated as overwrite permission, it violates this PRD.
- If dirty package files, owner files, active memory, PRDs, beads, hooks, CI, app code, or generated evidence are updated automatically, it violates this PRD.
- If generated preview output is treated as target-project truth, compatibility proof, or implementation acceptance, it violates this PRD.

## Candidate Bead Proposal

| Bead | Requirement IDs | Done when | Delegation mode | Test strategy | Review context | Primary authority | Validation |
|---|---|---|---|---|---|---|---|
| `B047-npm-approved-package-owned-apply` | `PRD-047-FR01` through `PRD-047-FR07` | Approved package-owned npm/local facade delegation, protocol/docs/navigation wording, clarity coverage, maintainer changelog, roadmap history, and generated docs/PRD/roadmap HTML are implemented and validated. | `human_in_loop` | `static_and_fixture` | `same_session_ok` | `tasks/prds/PRD-047-npm-approved-package-owned-apply.md` | bootstrap self-test, clarity scenario, package/docs/PRD/roadmap checks |

## Approval

- Approval state: approved by maintainer implementation request on 2026-07-31.
