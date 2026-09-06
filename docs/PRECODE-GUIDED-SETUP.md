# PrecodeOS Guided Setup
<!-- ANCHOR: precode-guided-setup -->

> AUTHORITY: Beginner-safe, agent-operated setup for acquiring PrecodeOS from npm and adopting it into a new or existing project.
> NOT_AUTHORITY: Active memory, task selection, package publishing, hidden installer behavior, generated evidence truth, private roadmap, or implementation acceptance.
> LOAD_WHEN: First adopting PrecodeOS, helping a user set it up, or diagnosing what may be copied, preserved, adapted, validated, or recovered.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.2.0
Last updated: 2026-09-06

## What This Guide Is For

Use this guide only for setup, validation, recovery, and orientation. After setup validates, go to `tasks/templates/PRECODE-FIRST-SESSION-CARD.md` or `docs/PRECODE-DAILY-COCKPIT.md` and stop before product work unless the user separately approves it.

The v1 self-serve boundary is intentionally narrow:

- certified platform: macOS
- certified launch adapters: Codex, Claude Code, Cursor, and Gemini
- acquisition: npm primary; GitHub/local Python advanced fallback
- interaction: the agent operates mechanics; the user receives plain-English explanations and approves named actions
- support: documentation, agent guidance, and deterministic troubleshooting; no synchronous human assistance

This does not certify the complete idea-to-production journey or guarantee deployment and operations. Cursor and Gemini have deterministic conformance and maintainer-smoke evidence; external usability evidence remains pending. Codex and Claude Code are included in the six no-help sessions.

## Canonical Agent-Operated Setup

Give a certified coding agent this prompt from the project you want to use:

```text
Set up PrecodeOS in this project using the official npm package.

Identify and confirm this project folder as the target. Run:
npx @precodeos/precodeos fast-setup-preview --target <target-project-root>

Explain the package version, support status, prerequisites, target classification, proposed actions, approval IDs, validation requirements, recovery route, next safe action, and stop reason in plain English.

Do not mutate the target until I approve named current actions. Apply only the approved SP-ID or UP-ID values. Treat project-specific owner-file adaptation as a separate approval. Validate, route me to the First Session Card or Daily Cockpit, and stop before product work.
```

The user should not need to construct paths, interpret shell syntax, understand Python, know Git internals, or decode action IDs without explanation. The agent must identify the target, translate every proposal into plain English, and stop on ambiguity.

## Before You Start

The agent checks these prerequisites:

| Prerequisite | User expectation | If missing |
|---|---|---|
| macOS | Certified v1 path | Other platforms remain preview |
| Node.js 18+ and npm | Used for the canonical package command | Stop and explain how to install or locate it |
| Python 3 | Used by the repo-native setup authority behind the npm facade | Stop; the user does not need Python knowledge |
| Git | Used for safe state, preservation, and recovery evidence | Stop before mutation if state cannot be inspected |
| Certified coding agent | Codex, Claude Code, Cursor, or Gemini | Do not invent host-specific setup semantics |

Never put secrets, API keys, billing data, private customer data, credentials, or personal notes into Precode files. Confirm the target folder before any apply command.

## Preview First

The agent runs:

```bash
npx @precodeos/precodeos fast-setup-preview --target <target-project-root>
```

Preview must expose:

- package version and certified/preview support status
- target classification: empty, nearly empty, existing project, existing Precode, missing, or same as source
- prerequisite status
- proposed actions in plain English
- current `SP-ID` or `UP-ID` approvals beneath those explanations
- validation requirements
- recovery route
- next safe action
- stop reason

Preview is read-only generated evidence. It does not approve copying, owner-file adaptation, overwrite, hook installation, CI changes, app commands, product work, package update, rollback, PRD approval, bead activation, or transition.

## Choose The Target Route

### Empty Or Nearly Empty Project

The agent may propose package-copy actions with `SP-ID` values. The user must approve the named current actions before apply:

```bash
npx @precodeos/precodeos fast-setup-apply --target <target-project-root> --approve-action <SP-ID>
```

Apply copies only approved package-owned paths and refuses overwrite. It does not adapt `PRODUCT.md`, `PROJECT-CONTEXT.md`, `DECISIONS.md`, `tasks/todo.md`, or other project-specific truth. The agent must request separate approval for those adaptations, create target `tasks/todo.md` from `tasks/templates/PRECODE-TODO-TEMPLATE.md`, preserve anchors and authority fields, create exactly one setup or orientation bead marked `in_progress`, point `tasks/todo.md` at it, and then validate.

### Existing Project

The npm preview routes to Existing Repo Intake and exposes no existing-app apply path. Run intake before proposing adaptation:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --existing-project-adaptation-plan
```

Preserve current product facts, code, docs, checks, CI, and Git state. The adaptation plan is evidence only. Existing paths are never bulk-overwritten.

### Existing Precode Project

The preview may propose only missing package-owned paths with current `UP-ID` values:

```bash
npx @precodeos/precodeos update-plan-preview --target <existing-precode-root>
npx @precodeos/precodeos fast-setup-apply --target <existing-precode-root> --approve-action <UP-ID>
```

Dirty package files, owner files, identity collisions, ambiguous state, and existing paths require stop-and-review. `latest`, a registry version, or a generated update plan is not overwrite permission.

## Validate And Orient

After approved copying and separately approved project-specific adaptation, the agent runs from the target:

```bash
bash scripts/validate-memory.sh
python3 scripts/file-inventory.py --check
```

It also inspects Git state and any project-specific checks named in owner files. Setup is not ready for orientation while active memory is invalid, required package paths are missing, state is ambiguous, or validation fails.

A successful setup may emit `ready_for_orientation` as generated evidence. That result means the bounded setup gates passed. It does not choose product work, approve a PRD, activate a product bead, accept implementation, or certify the complete idea-to-production journey.

When ready, open `tasks/templates/PRECODE-FIRST-SESSION-CARD.md` for the linear first session or `docs/PRECODE-DAILY-COCKPIT.md` for normal work. The agent stops before product work.

## Recovery

If setup is partial, confusing, or blocked, run:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --recovery-guidance
```

Recovery guidance names the likely route but does not repair, overwrite, delete, reset, roll back, install hooks, change CI, or approve mutation. Preserve the target and its Git state before taking another action.

Stop when:

- source or target is unclear
- source and target are the same folder
- the target is missing
- existing files or Git state cannot be classified safely
- a prerequisite is missing
- the current proposal lacks plain-English actions and current approval IDs
- validation fails or an orientation result overstates what was proven

## Safe Existing-File Refresh With Audit Report

Existing-file refresh is an advanced, explicit path for Git-clean, package-owned files that already exist and differ from source. Preview first:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <existing-precode-root> --refresh-existing-preview
```

Only approved current `RF-ID` actions may refresh eligible files, and the target hash must still match the preview:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <existing-precode-root> --refresh-existing-preview --apply-refresh-existing --approve-action <RF-ID>
```

User-created files, owner files, active memory, dirty files, missing files, secrets, hooks, CI, PRDs, beads, and generated evidence remain excluded. Apply writes an audit report; the report is evidence, not future permission or rollback authority.

## Advanced GitHub And Python Fallback

Use this only when npm is unavailable, package provenance needs direct inspection, or a technically comfortable operator deliberately chooses the transparent fallback.

```bash
git clone https://github.com/danieljsears-lab/PrecodeOS.git
cd PrecodeOS
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --fast-verified-setup-preview
```

For an approved copy action:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --fast-verified-setup-apply --approve-action <SP-ID|UP-ID>
```

The local commands have the same authority, approval, overwrite, validation, and recovery boundaries as npm. This fallback is not the beginner path and does not create a second setup contract.

## What The Npm Package Contains

The npm distribution contains the repo-native core, public docs, owner-file templates, a clean `tasks/templates/PRECODE-TODO-TEMPLATE.md`, reusable schemas, adapters, validation scripts, and generated docs reading surface. It excludes PrecodeOS's live `tasks/todo.md`, package-development PRDs, package-development beads, generated PRD HTML, private maintainer material, local agent state, generated logs, caches, secrets, and credentials.

The public GitHub source retains package-development material for transparency. Its presence in GitHub does not make it target-project content.

## Setup Completion Checklist

- Correct target confirmed.
- Package version and support status explained.
- Prerequisites passed or setup stopped.
- Target classified correctly.
- Proposed actions explained before IDs.
- Only current approved IDs applied.
- Existing and user-created paths preserved.
- Owner-file adaptation separately approved.
- Active memory and inventory validated.
- Recovery route and stop reason understood.
- Builder can explain what was installed and what remains authoritative.
- Builder reaches First Session Card or Daily Cockpit.
- Agent stops before product work.

Failure of preservation, secrets handling, mutation gates, authority boundaries, or package integrity blocks the affected launch path.

## Where To Go Next

- First session: `tasks/templates/PRECODE-FIRST-SESSION-CARD.md`
- Normal work: `docs/PRECODE-DAILY-COCKPIT.md`
- Symptom lookup: `docs/PRECODE-TROUBLESHOOTING.md`
- File ownership: `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`
- Adapter contract: `adapters/ADAPTER-INDEX.md`

Do not start product work from this setup guide.
