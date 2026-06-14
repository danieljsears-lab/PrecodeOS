# PrecodeOS Guided Setup
<!-- ANCHOR: precode-guided-setup -->

> AUTHORITY: Beginner-safe guided setup for pulling PrecodeOS from GitHub and adopting it into a new or existing project.
> NOT_AUTHORITY: Active memory, private local file inventory, task selection, installer behavior, generated evidence truth, private roadmap, or implementation acceptance.
> LOAD_WHEN: First adopting PrecodeOS, helping a user set it up, or checking what should and should not be copied.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.9
Last updated: 2026-06-14

## What This Guide Is For

Use this guide when you want to put PrecodeOS into a project for the first time.

PrecodeOS is not an app you launch. It is a small repo-native operating layer for AI coding work: Markdown authority files, task contracts, adapter notes, validation scripts, and generated evidence rules that live inside a project folder.

If you are helping someone else through setup, use `docs/PRECODE-SUPPORT-RUNBOOK.md` alongside this guide. If setup state, copied files, validation output, or generated reports become confusing, use `docs/PRECODE-TROUBLESHOOTING.md`.

The safest setup path is manual and visible:

1. Pull PrecodeOS from its public GitHub repository.
2. Run the read-only Bootstrap Confidence check before copying anything.
3. Choose the first adoption fork: fresh install or existing repo intake.
4. Copy only the public package files that belong in the target project.
5. Adapt product and project owner files in plain English.
6. Validate memory before letting an agent build.
7. Stop for human review.

If you need the exact public package technical dictionary, use `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`. This setup guide explains the adoption path; the package inventory remains the public file map.

## Before You Start

You need:

- a local folder where you can clone or pull from GitHub
- a target project folder
- Git installed
- Python 3 available for validation scripts
- an AI coding agent that can read and edit local files

Do not paste secrets, API keys, billing data, private dashboard values, private customer data, or personal notes into Precode files.

If you have notes, documents, screenshots, research, design exports, or links that belong with the project, put them in root-level `project-evidence/`. That folder is for project-owned raw evidence, not active memory, not task approval, and not implementation instructions. Each project decides whether to track or ignore it in Git; review contents before committing.

Stop if you are unsure which folder is the PrecodeOS package checkout and which folder is your target project. Mixing those up is the easiest way to copy in the wrong direction.

## Bootstrap Confidence Check

Before copying, editing, installing hooks, or changing the target project, run the read-only Bootstrap Confidence helper from the PrecodeOS package checkout:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

The helper names the package source, target project, target kind, public file groups, excluded files, conflicts, missing dependencies, stop conditions, and first safe next action. By default it writes nothing.

After the basic check, use the install/update manifest dry-run preview when you want the next level of setup clarity without changing the target project:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest
```

The preview labels possible setup actions as `copy_candidate`, `adapt_candidate`, `preserve_existing`, `exclude`, `blocked`, or `deferred`. It is still generated evidence only. It does not approve copying, overwriting, hook installation, CI changes, active-memory edits, app commands, app-code edits, release channels, package-manager updates, rollback automation, or a `precode` CLI.

After the preview, use the supervised setup plan when you want a human-readable checklist before approving manual setup work:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
```

The plan adds action IDs, approval gates, exclusions, blockers, and validation steps. It implies the manifest preview and is still generated evidence only. It does not approve copying, owner-file edits, overwrites, hook installation, CI changes, active-memory edits, app commands, app-code edits, release channels, package-manager updates, rollback automation, or a `precode` CLI.

Use JSON when an agent or support script needs structured output:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --json
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --preview-manifest --json
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --json
```

Use generated evidence only when you explicitly want source-side setup evidence:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --write-evidence
```

`--write-evidence` writes only `logs/bootstrap-check.json` and `logs/bootstrap-check.md` in the PrecodeOS package source. It must not write into the target project. Bootstrap output is evidence only; it does not approve copying, overwriting, hook installation, CI changes, active-memory edits, or app-code changes.

After Bootstrap Confidence confirms the source and target, choose the first adoption fork:

- Use the fresh install path when the target is empty or nearly empty.
- Use Existing Repo Intake when the target already has app code, docs, CI, product history, or active work.

For an existing app, treat manifest preview and supervised setup-plan actions as provisional until Existing Repo Intake has run. Do not turn generated setup evidence into copy commands or owner-file edits.

For an existing app, run:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
```

Existing Repo Intake is also read-only by default. It summarizes the app shape, likely app directories, stack, docs, likely checks, CI/deploy hints, generated and sensitive surfaces, owner-file gaps, conflicts, stop conditions, and first safe next action. Its output is evidence only, not permission to copy, overwrite, run checks, change CI, adapt owner files, approve a PRD, activate a bead, or write app code.

## Ember Bootcamp Fit Check: PrecodeOS Or Plain VS Code?

Use this fit check if you are in an Ember bootcamp and are unsure whether to set up PrecodeOS now or keep practicing in plain VS Code with Claude Code.

Use PrecodeOS now when:

- you are building a real product you may show to customers, users, coworkers, or collaborators
- the app has multiple steps, screens, integrations, data flows, or future sessions
- an engineer, instructor, or teammate may need to understand or continue the work
- you need scope control, evidence, checkpoints, recovery, or a clear handoff
- you are moving from rough design or workbook material into serious product build work

Stay in plain VS Code and Claude Code for now when:

- you are making a throwaway prototype, quick sketch, or learning-only demo
- you are still learning how to open the project, use VS Code, run commands, or talk to Claude Code
- you are doing early UI or design exploration before choosing what belongs in the real app
- setup basics are blocking you and practicing the tool first would reduce confusion
- the work is not intended to survive beyond the exercise

This is a two-way door. It is okay to practice basics first and add PrecodeOS later. Before you begin serious multi-session product development, especially work you want engineers or instructors to support, add PrecodeOS so the repo has a clear task, scope, and proof trail.

Once real development starts in VS Code, keep development there. You may use design or prototype tools to explore ideas, but do not keep bouncing the product between Ember, Claude Design, Claude Code web, and local VS Code. Bring the chosen design or handoff material into the project, then develop locally from the project folder.

## Step 1: Pull PrecodeOS From GitHub

Start by getting a clean local copy of the public PrecodeOS package.

If you do not have it yet:

```bash
git clone https://github.com/danieljsears-lab/PrecodeOS.git
```

If you already have it:

```bash
cd PrecodeOS
git pull
```

Then inspect it:

```bash
git status
find . -maxdepth 2 -type f | sort
```

You are using this checkout as the package source. Do not treat it as the target app you are building unless your goal is to maintain PrecodeOS itself.

After you know the target project path, run Bootstrap Confidence before setup:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

## Step 2: Ask The Agent To Orient First

Before copying or editing, ask your agent to explain what it sees.

```text
I want to adopt PrecodeOS into a project.
Treat PrecodeOS as a package source, not as an app to run.
Do not copy, edit, install hooks, run setup scripts, or change my target project yet.
First identify the PrecodeOS package checkout, the target project folder, the public file groups that may be copied, the files that must not be copied, and the validation commands we will run after setup.
Use `python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>` if available.
Explain the plan in plain English and stop for my approval.
```

Expect the agent to name:

- the PrecodeOS package checkout
- the target project folder
- whether this is a new project or existing project
- the public file groups to copy
- the private, generated, local, and secret files to exclude
- conflicts, missing dependencies, and the first safe next action from Bootstrap Confidence
- the first validation command

Stop if the agent tries to run a broad installer, invents a `precode` CLI command, installs hooks silently, or starts editing application code.

## Step 3: Choose The First Adoption Fork

Use the new-project path first if you are starting from an empty or nearly empty repository.

Use the existing-project path if your target project already has application code, product docs, project conventions, or active work.

### Path A: New Project

In a new project, the goal is to create the PrecodeOS operating layer before product work starts.

Ask:

```text
Set up PrecodeOS for a new project.
Use the public PrecodeOS checkout as the source package.
Do not write application code.
Create or adapt only the Precode operating files needed for a first safe session.
Before changing anything, show me the copy checklist and the files that will be excluded.
```

After the user approves, copy the public package files by supervised file group. Do not use a bulk overwrite command.

For a new project, the setup should include:

| File group | Include |
|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` |
| Product and project owner files | `PRODUCT.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` |
| Public orientation docs | `README.md`, `docs/`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `TRADEMARK.md`, `NOTICE`, `LICENSE` |
| Agent shims and adapters | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `adapters/` |
| Work structure | `tasks/beads/`, `tasks/prds/`, `tasks/reference/`, `tasks/templates/`, `modes/`, `memory/` |
| Project evidence guide | `project-evidence/PROJECT-EVIDENCE-GUIDE.md` |
| Scripts and checks | `scripts/`, `.githooks/`, `.github/workflows/` when the target repo wants GitHub validation |
| Public generated-log guide | `logs/LOG-EVIDENCE-TAXONOMY.md` |

Then adapt these files before starting product work:

- `PRODUCT.md`: product promise, users, strategy, bets, success signals, and voice
- `PROJECT-CONTEXT.md`: app directory, stack, conventions, checks, integrations, and sensitive boundaries
- `DECISIONS.md`: hard decisions already known for this project
- `tasks/todo.md`: the first setup bead and current state

### Path B: Existing Project

In an existing project, the goal is to add Precode without flattening the project history, conventions, or current work.

Run Existing Repo Intake before copying or adapting Precode files:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
```

Ask:

```text
Set up PrecodeOS for an existing project.
Use the public PrecodeOS checkout as the source package.
Do not overwrite existing project files without naming each conflict first.
Do not write application code.
First inspect the target repo structure, existing docs, package files, app directory, test commands, secrets boundaries, and current git status.
Then show me a setup plan with conflicts, proposed owner-file adaptations, and validation commands.
```

Safe inspection commands include:

```bash
git status
find . -maxdepth 2 -type f | sort
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
```

The support person or agent should identify:

- existing docs that may overlap with Precode owner files
- the real app directory
- existing test, lint, build, and typecheck commands
- secrets or env-file patterns that must not be copied into Precode docs
- any generated folders or build outputs that Precode should ignore
- whether GitHub Actions should be added now or deferred
- owner-file gaps and proposed adaptation points
- stop conditions before setup mutation

For existing projects, do not overwrite:

- existing `README.md`
- existing product, architecture, API, security, or data-model docs
- app source code
- package manager files
- CI files
- environment files
- generated output

Instead, ask the agent to propose how existing project facts should be reflected in Precode owner files, then stop for review.

## Step 4: Exclude Private, Generated, Local, And Secret Files

Do not copy these from the package checkout into a user's project:

| Exclusion | Why |
|---|---|
| Private local planning material | Local context that is not part of the reusable public package. |
| `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md` | Generated reports, not source authority. |
| `logs/*.json`, `logs/*.jsonl`, `logs/*.yaml`, generated `logs/*.md` | Generated evidence from one repo, not setup source for another repo. |
| `logs/check-output/`, `logs/scheduled-audit-output/` | Local command output and audit snapshots. |
| `.agent-state/`, `.claude/`, `.codex/`, `.cursor/`, `.vscode/`, `.idea/` | Local agent, editor, and IDE state. |
| `.env`, `.env.*`, `secrets/`, `credentials/`, key and certificate files | Secrets and environment material. |
| `__pycache__/`, test caches, coverage output, local virtual environments | Regeneratable local cache or environment output. |

Keep `logs/LOG-EVIDENCE-TAXONOMY.md` if the package includes it. That file explains generated log semantics and is public documentation.

Keep `project-evidence/PROJECT-EVIDENCE-GUIDE.md` if the package includes it. After setup, the folder belongs to the target project and may contain user-selected raw evidence. Do not copy private evidence from one project into another.

## Step 5: Validate Before Work Starts

After the files are in place and owner files have been adapted, run the first validation command from the target project root:

```bash
bash scripts/validate-memory.sh
```

Then start the first session:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
```

The first session should explain:

- active memory is only `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- the active bead
- the primary authority file
- files in play
- checks to run
- stop conditions
- blockers or missing setup

Stop if active memory includes extra files, the active bead is unclear, the app directory is wrong, or the checks are vague.

## Step 6: First Safe Agent Prompt

Use this after setup validation passes:

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md.
Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked.
Do not start coding yet.
```

If the project is still only being set up, use:

```text
This is still PrecodeOS setup.
Do not write product app code.
Help me verify that PRODUCT.md, PROJECT-CONTEXT.md, DECISIONS.md, and tasks/todo.md match this target project.
Name any missing information and stop for my review.
```

## Support Engineer Runbook

Use this section when you are helping someone else adopt PrecodeOS.

For a short support slot, start with the fast support flow in `docs/PRECODE-SUPPORT-RUNBOOK.md`, then use this guide for the setup mechanics.

### Preflight

Confirm:

- the user has a target project folder
- the user understands that PrecodeOS is a package layer, not an app runtime
- the public PrecodeOS repo has been cloned or pulled
- the target repo has a clean or understood `git status`
- no secrets are being pasted into prompts or docs
- Bootstrap Confidence has named source, target, target kind, conflicts, exclusions, and first safe next action
- the user can approve each file group before copy/adaptation

### Target-Project Inspection

Run safe inspection only:

```bash
git status
find . -maxdepth 2 -type f | sort
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

For an existing project, also inspect the package-manager and framework files that already exist. Do not rewrite them as part of Precode setup.

Prepare a short setup note for the user:

```text
I found the target project, the likely app directory, existing docs, existing checks, and files that could conflict with Precode owner files.
I will not overwrite conflicts automatically.
I will copy or adapt Precode by file group, then run memory validation.
Here are the conflicts and choices that need your approval:
```

### Validation Checklist

After setup:

- run `bash scripts/validate-memory.sh`
- run `python3 scripts/file-inventory.py --check` if the full script set was copied
- run `bash scripts/session-start.sh`
- confirm generated reports are evidence only
- confirm the first active bead is setup or orientation, not product implementation
- confirm project-specific checks in `PROJECT-CONTEXT.md`
- confirm any packet, design, PRD, or handoff input was ingested through the support runbook path or named as the next blocker

### Escalation And Stop Conditions

Stop and ask the user before:

- overwriting an existing project document
- installing Git hooks
- adding or changing GitHub Actions
- changing package manager files
- editing app code
- moving or renaming Precode files
- adding active-memory files
- touching secrets, env files, dashboard values, deployment settings, billing, auth, payments, or personal data
- approving a bead transition

If setup is blocked, record the blocker in plain English and propose a narrow setup or unblocker bead. Do not widen setup into product work.

## Where To Go Next

After guided setup, use:

- `docs/PRECODE-SUPPORT-RUNBOOK.md` when assisting another user through adoption and first use
- `docs/PRECODE-TROUBLESHOOTING.md` when setup, state, checks, or generated reports are confusing
- `docs/PRECODE-USER-GUIDE.md` for day-to-day operation
- `docs/PRECODE-OS-README.md` for the Builder OS mental model
- `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` for the public package file dictionary
- `tasks/templates/PRODUCT-IDEATION-WORKBOOK.md` if the product idea is still rough

Do not use private local files as public setup instructions. Do not treat generated reports as authority. Do not approve implementation until the setup bead and checks are clear.
