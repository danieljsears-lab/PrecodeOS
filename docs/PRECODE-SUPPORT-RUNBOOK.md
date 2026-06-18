# PrecodeOS Support Runbook
<!-- ANCHOR: precode-support-runbook -->

> AUTHORITY: Public-safe support-engineer field guide for helping a new user capture initial intent, adopt PrecodeOS into a new or existing project, reach a valid first session, and learn the safe operating loop.
> NOT_AUTHORITY: Active memory, product truth, PRD approval, task selection, implementation acceptance, bead transition approval, private support operations, customer records, credentials, dashboard operations, or private roadmap tactics.
> LOAD_WHEN: Supporting a first-time PrecodeOS adoption, guiding a user from idea capture into setup, helping a user run their first safe session, or coaching an agent that is assisting support.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.26
Last updated: 2026-06-17

## Purpose

Use this runbook when you are helping someone else adopt PrecodeOS.

The support posture is:

- the user owns product facts, approvals, and risk decisions
- support asks, reflects, challenges, and routes
- the agent may inspect, summarize, propose, and validate
- durable state belongs in Precode owner files, beads, recorded checks, and generated evidence
- no separate support handoff artifact is required

PrecodeOS is not an app to launch. It is a repo-native operating layer: Markdown authority files, task contracts, adapters, scripts, and generated-evidence rules that live inside a project folder.

When users ask where to put reference files, notes, documents, screenshots, research, or design exports, route them to root-level `project-evidence/` in the target project. It is project-owned raw evidence, not active memory, not task approval, and not implementation instruction. Use Local Source Intake before promoting any conclusions into owner files.

## Fast Support Slot Flow

Use this flow when a support engineer has a short onboarding, setup, or unblocker slot.

1. Name the case in plain English: new project, existing project, first-use confusion, local app blocker, auth/demo blocker, or damaged setup.
2. Confirm the user owns product direction, scope, approval, and acceptance. Support owns technical diagnosis and narrow unblocking.
3. Identify the package source, target project, current folder, and current `git status` before copying or editing.
4. In an Ember bootcamp setting, run the fit check from `docs/PRECODE-GUIDED-SETUP.md` before installing or deferring PrecodeOS.
5. If Precode setup is the issue, run `python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>` from the package checkout. Use `--preview-manifest` when the user needs a dry-run view, `--supervised-setup-plan` before fresh-target setup approval, `--existing-project-adaptation-plan` after Existing Repo Intake, `--upgrade-preview` for existing Precode targets, and `--recovery-guidance` when setup is partial or confusing. For empty or nearly empty targets only, use `--apply-supervised-setup --approve-action <SP-ID>` after the user approves specific copy action IDs. For existing Precode targets, use `--apply-upgrade-preview --approve-action <UP-ID>` only for missing package-owned files that the upgrade preview marks as `review_package_copy_candidate`. If state is confusing, use `docs/PRECODE-TROUBLESHOOTING.md`.
6. Run only the narrow checks that match the symptom, then explain the result in plain language.
7. Close by naming the current bead or blocker, the next safe prompt, what remains unapproved, and where the student should go next.

## Stuck User Recovery

Use this when a beginner says `I am stuck`, `I am stuck, help me`, or cannot name the symptom.

Support should help the user get a prescriptive diagnosis without taking over product authority or approving repair:

1. Stop implementation.
2. Restate the symptom in plain English, or say the symptom is not known yet.
3. Name the first safe move: stop implementation and diagnose before repair.
4. Name the likely owner surface, or say it is unknown until active memory and checks are inspected.
5. Choose up to three read-only or advisory checks.
6. Give the next safe prompt or action.
7. State forbidden actions: no delete, overwrite, regenerate, transition approval, rollback, setup/update mutation, or destructive command without explicit approval.

Good first checks are usually `bash scripts/session-start.sh`, `python3 scripts/next-step.py`, `python3 scripts/state-check.py`, `python3 scripts/files-in-play-check.py`, `python3 scripts/completion-check.py`, or `python3 scripts/os-health.py`, depending on the symptom.

OS Health, Doctor Dashboard output, `next-step.py`, and stable-fix eligibility help diagnose only. Doctor Dashboard triage labels may say what to ask and what not to approve, but they do not approve repair, acceptance, transition, rollback, setup/update mutation, destructive commands, or generated-report regeneration.

For small repair claims, use the Bugfix Spec Lane before implementation. Ask the agent to name current behavior, expected behavior, unchanged behavior, owner file, root cause if known, fix approach, regression proof, and route decision. If the owner file, route, or proof path is unclear, keep the work in diagnosis instead of repair.

When the user can name the symptom but cannot choose the recovery path, route them to the No-Engineer Fallback Prompt Pack in `tasks/reference/PROMPT-PATTERNS.md`. It gives public-safe prompts for agent-lost, checks-failed, app-will-not-start, approved-too-much, copied-wrong-files, and stop-or-continue moments. Do not treat the pack as support approval, repair approval, app-code approval, secrets handling, external mutation, rollback, setup/update mutation, transition approval, or a replacement for the Recovery Protocol.

Support can say:

```text
I am going to separate product questions from technical blockers. If this is about who the product serves or what should be built, I will route you back to product coaching. If this is about setup, repo state, validation, local runtime, or auth blocking a demo, I will help diagnose and unblock it narrowly.
```

## Ember Bootcamp Precode Fit Check

Use this short check when a student is unsure whether to use PrecodeOS or stay in plain VS Code with Claude Code.

Route the student to PrecodeOS now when the work is a real product build, customer-facing or collaborator-supported, multi-step, likely to continue across sessions, or in need of scope control, evidence, recovery, or handoff.

Let the student stay in plain VS Code and Claude Code for now when the work is a throwaway prototype, a first-time coding practice session, a learning-only demo, early design exploration, or when setup basics are still blocking confidence.

Name the decision as reversible: the student can practice basics first and add PrecodeOS later, but should add PrecodeOS before serious multi-session product development. Once real development starts in VS Code, coach the student to keep development there instead of switching the product back and forth between design, prototype, web chat, and local coding surfaces.

## Bootcamp Safe Prompt Pack

Use this pack when an Ember bootcamp student is working in the official bootcamp scaffold. This scaffold is a bootcamp support convention, not a universal PrecodeOS requirement.

Official bootcamp scaffold:

- `frontend/` exists at repo root and contains the Next.js app.
- `precode/` exists at repo root and contains the Precode control layer only.
- `backend/` is created at repo root only when the first approved backend bead activates; generated backend application code belongs there.

### Scaffold Confirmation

```text
Before intake, planning, or implementation, confirm the bootcamp scaffold:

1. frontend/ exists at repo root and contains the Next.js app.
2. precode/ exists at repo root and contains the Precode control layer only.
3. backend/ is absent until an approved backend bead activates, or exists because that bead has already activated.

Do not start intake, create files, write code, or move project material until you confirm these boundaries. If the scaffold conflicts with active memory, PROJECT-CONTEXT.md, or the current bead, surface the conflict now.
```

### One Question At A Time

```text
Ask one blocking question at a time. Wait for the student's answer before asking the next one. Include a recommended answer when useful, but do not decide product direction, scope, acceptance, or repo topology for the student.
```

### Bead And Git Hygiene

```text
Before activating a new bead or starting a new support session, check git status and tell us whether current changes are clean, committed, generated evidence, or unfinished work from the current bead.

Bead boundaries should normally align with commit boundaries. If completed checked work is uncommitted, stop and propose a commit summary before moving forward. Push when the student's repo has a remote and the bootcamp support workflow expects remote backup or collaboration.

Do not treat this chat instruction as durable state by itself. If the rule needs to persist, put it in the appropriate Precode owner or support document.
```

### Build-Stage Error And Control-Layer Protocol

```text
During build work, diagnose ordinary app errors only inside the active bead and its files in play.

Stop and explain the issue before changing anything when the error appears to involve the Precode control layer, active memory, task state, validators, scripts, protocols, adapters, modes, generated reports, repo boundary confusion, secrets, CI, Git hooks, deployment, auth, payments, or personal data.

Do not modify files inside precode/ except when the active bead explicitly allows that exact Precode control-layer change. If a Precode framework file appears to cause the error, surface the symptom and escalation path to the support lead or maintainer instead of patching it casually.
```

## Case Priority

Support usually sees these cases in this order:

| Case | Default posture |
|---|---|
| New project | Mainline walkthrough. Capture enough user-owned intent, then set up Precode before product implementation. |
| Existing project | Variant. Preserve existing code, docs, checks, and conventions; adapt Precode around them. |
| First-use operation | Always included. Setup is not done until the user can run a first safe session. |
| Incorrect copy or damaged setup | Rare repair path. Stop, identify the symptom, consult troubleshooting, and validate before resuming. |

## Non-Negotiables

Do not paste or store secrets, credentials, billing details, customer records, private dashboard values, private transcripts, or sensitive personal data in Precode files or prompts.

Do not run broad overwrite commands, install Git hooks, change CI, edit app code, approve a bead transition, or mutate external systems during first setup unless the user explicitly approves a narrow action and the active setup work allows it.

Do not create product truth for the user. If the product is fuzzy, help the user capture a Conviction Packet / Precode Ingestion Packet or PRD-ready source summary. That packet is evidence only until it is reviewed and placed in the right Precode owner file after setup.

Do not treat `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, or files under `logs/` as authority. Generated reports are evidence only. The Doctor Dashboard inside OS Health explains warning sources, plain-English triage labels, and repair paths, but it does not approve commands, task selection, transitions, or acceptance.

## Mainline Walkthrough: New Project

### 1. Frame The Session

Start by naming what will and will not happen.

Support can say:

```text
We are going to capture enough of your intent to set up Precode safely. You will own the product facts and approvals. I will help organize them, point out gaps, and stop before anything risky. We are not coding the product yet.
```

Agent guardrail:

```text
Treat this as PrecodeOS support setup, not app implementation. Ask for user-owned facts, summarize them as evidence, and do not edit, copy, overwrite, install hooks, run setup scripts, or write app code until the user approves a narrow setup step.
```

### 2. Capture User-Owned Intent

Ask for enough context to seed owner files later:

- product promise
- intended user
- painful before moment
- better after moment
- smallest useful version
- known constraints
- obvious risks or unknowns

Use plain language. Challenge gently when the answer is broad, solution-first, or unsupported.

Support can say:

```text
I am not going to decide the product for you. I am going to reflect what you said, name assumptions, and ask which parts feel true enough to carry into setup.
```

The output at this point is a Conviction Packet / Precode Ingestion Packet or PRD-ready source summary in the conversation. It is not a durable PRD yet and does not approve implementation.

### 3. Confirm Source And Target

Before copying anything, identify:

- the clean PrecodeOS package checkout
- the target project folder
- whether the target is empty, nearly empty, or already has project material
- the public file groups that may be copied
- private, generated, local, and secret material that must not be copied
- the validation commands to run after setup

Safe inspection commands:

```bash
git status
find . -maxdepth 2 -type f | sort
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root>
```

Stop if the source package and target project are unclear. Mixing them up is the easiest first-time failure.

Bootstrap Confidence is read-only by default. It names target kind, public file groups, exclusions, conflicts, missing dependencies, first safe next action, and stop conditions. Its output is generated evidence only, not permission to copy, overwrite, install hooks, change CI, edit active memory, or write app code.

When the user needs the next setup checklist before approving manual work, run:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan
```

The supervised setup plan includes the manifest preview, action IDs, approval gates, exclusions, blockers, and validation steps. It is generated evidence only, not permission to copy, adapt owner files, overwrite target material, install hooks, change CI, edit active memory, run app commands, or write app code.

For an empty or nearly empty target, apply only the specific copy action IDs the user approves:

```bash
python3 scripts/bootstrap-check.py --source <precode-package-root> --target <target-project-root> --supervised-setup-plan --apply-supervised-setup --approve-action <SP-ID>
```

This copies only approved `review_copy_candidate` actions and reports copied, skipped, blocked, and validation next steps. It is not an owner-file adaptation engine, existing-repo migration, overwrite command, hook installer, CI installer, app-command runner, app-code writer, release channel, package-manager flow, rollback tool, or `precode` CLI.

After Bootstrap Confidence, choose the first adoption fork:

- Fresh install for empty or nearly empty targets.
- Existing Repo Intake for repos with app code, docs, CI, product history, or active work.

For existing apps, run:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
```

Existing Repo Intake is read-only by default. It names repo topology, likely app directories, stack, docs, likely checks, CI/deploy hints, generated and sensitive surfaces, owner-file gaps, conflicts, first safe next action, and stop conditions. Its output is evidence only, not permission to copy, overwrite, run checks, change CI, approve product facts, activate beads, or write app code.

### 4. Set Up By Supervised File Group

Use `docs/PRECODE-GUIDED-SETUP.md` as the setup guide and `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` as the public package file dictionary.

For a new project, copy public package files by supervised group, not by blind overwrite:

- active memory: `AGENT.md`, `DECISIONS.md`, `tasks/todo.md`
- product and project owner files
- public orientation docs
- agent shims and adapters
- tasks, modes, memory templates, and reference protocols
- `project-evidence/PROJECT-EVIDENCE-GUIDE.md` as the marker and user guidance for project-owned raw evidence
- scripts, hooks, and workflows only when approved for the target repo
- `logs/LOG-EVIDENCE-TAXONOMY.md`

Exclude private local planning material, generated reports, generated logs, local agent/editor state, caches, virtual environments, env files, secrets, credentials, keys, and certificates.

If Bootstrap Confidence reports blockers, stop setup until they are resolved. If it reports conflicts, name each conflict and get user approval before adapting or copying anything.

### 5. Adapt Owner Files

Use the captured user-owned facts to propose minimal setup adaptations:

- `PRODUCT.md`: product promise, users, smallest useful version, success signals, and voice
- `PROJECT-CONTEXT.md`: app directory, stack if known, checks, conventions, integrations, and sensitive boundaries
- `DECISIONS.md`: hard decisions already known
- `tasks/todo.md`: first setup or orientation bead and current state

Support may draft, but the user approves the facts. If a fact is uncertain, mark it as an assumption or open question in the proper owner file rather than presenting it as settled.

### 6. Validate Before First Use

From the target project root, run:

```bash
bash scripts/validate-memory.sh
python3 scripts/file-inventory.py --check
```

If the full script set was not copied, explain which validation is unavailable and why. Do not treat missing validation as success.

### 7. Guide The First Safe Session

Run or ask the agent to run:

```bash
bash scripts/session-start.sh
python3 scripts/next-step.py
```

Then ask the agent to explain:

- active memory
- current bead
- primary authority
- files in play
- checks
- stop conditions
- blockers
- generated-report warning

First safe prompt:

```text
Before editing, load only Precode active memory: AGENT.md, DECISIONS.md, and tasks/todo.md. Then tell me the active bead, primary authority, files in play, checks, stop conditions, and anything blocked. Do not start coding yet.
```

Setup is not complete until the user can explain what the active bead is and when they should stop.

## Existing Project Variant

For an existing project, preserve the project before adapting Precode. Treat this as the existing-app branch at the first adoption fork, not as a fresh install with extra conflicts.

Run Existing Repo Intake after Bootstrap Confidence and before copying or adapting Precode files:

```bash
python3 scripts/existing-repo-intake.py --source <precode-package-root> --target <target-project-root>
```

Inspect first:

- current `git status`
- existing README and docs
- package manager and framework files
- real app directory
- test, lint, build, and typecheck commands
- CI and GitHub Actions
- generated folders and ignored paths
- secrets and environment boundaries
- owner-file gaps and proposed adaptation points
- stop conditions before setup mutation

Do not overwrite existing project docs or app files. Instead, propose how existing facts should be reflected in Precode owner files.

Support can say:

```text
I found existing project material. I will not overwrite it automatically. I will run Existing Repo Intake, name each conflict, propose where the fact belongs in Precode, and stop for your approval before changing anything.
```

If the project already has active work, make the first Precode bead setup or orientation. Do not turn setup into product implementation.

## First-Use Coaching

Teach the user this loop:

```text
orient -> decide -> plan -> build -> prove -> stop or approve the next transition
```

Key ideas to reinforce:

- active memory is only `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- one bead is active at a time
- generated reports are evidence only
- recorded checks are stronger than agent confidence
- the user approves risk and task transitions
- unclear state is a reason to stop, not push through

If the user feels lost, use `docs/PRECODE-TROUBLESHOOTING.md` before editing files.

### Claude Checkpoint False Approval

Use this procedure when a student reports that Claude ran a checkpoint, claimed a bead was complete, invented manual verification, or seemed to approve its own work.

First separate the three actions:

- `bash scripts/checkpoint.sh` reports current state; it does not accept a bead.
- `python3 scripts/bead-transition.py` proposes whether a next bead is eligible.
- `python3 scripts/bead-transition.py --approve` mutates bead state and must require explicit human approval.

Ask the student for the exact Claude transcript around the checkpoint, especially lines where Claude claimed checks passed, manual verification happened, or the bead was approved. Then run only read-only diagnostics from the project root:

```bash
python3 scripts/bead-transition.py --json
python3 scripts/completion-check.py
git status --short
```

Compare Claude's claims with the active bead Closeout Evidence and `logs/check-results.jsonl`. If Claude claimed manual verification it did not actually perform, treat that closeout as untrusted. Repair the Closeout Evidence to say what was actually checked, record remaining uncertainty plainly, and use `revise`, `blocked`, or `manual_testing` instead of `accepted`.

Support can say:

```text
A checkpoint is a status report, not approval. We are going to compare Claude's claims with recorded checks and manual verification. If the evidence was invented or overstated, we will mark the bead honestly and stop before activating anything new.
```

## Engineer Initiation From User Packet

Use this section when an engineer receives a user's Conviction Packet / Precode Ingestion Packet, Student Experience Ingestion Packet, frontend design files, and optional existing PRD.

Treat the packet, Experience artifacts, design files, screenshots, Figma exports, design-system notes, and existing PRDs as source evidence unless the bootcamp explicitly marks a PRD-like input as student-approved product direction. Even then, the combined packet does not automatically activate a bead or authorize coding.

The initiation path is:

```text
ingestion packet + Experience artifacts + optional PRD
  -> Local Source Intake
  -> owner-file map
  -> PRD readiness or amendment
  -> Experience/core-spine impact check
  -> candidate bead for the core spine
  -> user-approved active bead
  -> implementation
```

Start by classifying the project state:

| Entry state | First move | Do not do |
|---|---|---|
| Fresh Precode setup | Set up and validate Precode first, then ingest the packet and design files. | Do not let source inputs skip setup validation. |
| Existing non-Precode project | Inspect the repo, existing docs, existing PRD/design, app directory, checks, and conflicts before adapting Precode. | Do not overwrite project conventions or treat the external PRD as already approved Precode authority. |
| Existing Precode project | Load active memory, identify the active bead, then intake the new packet, design, or PRD as local source evidence. | Do not widen the active bead, amend a PRD, or start coding without the normal approval path. |

### Precode Ingestion Close Gate

An engineer setup session is not complete until the Precode ingestion state is explicit.

Before closing, confirm:

- the entry state was classified
- setup validation ran, or the exact validation blocker is named
- source inputs were treated as evidence, not authority
- Local Source Intake or Client Engagement Intake was completed when packets, design files, Ember handoffs, backend plans, sprint plans, or existing PRDs are present
- affected owner files or the next safe action are named
- no PRD, bead, implementation, repo topology, or product decision was approved by implication
- in bootcamp Experience handoffs, Claude Code creates or proposes a bounded bead before coding starts

If any item is missing, close on the blocker and next safe prompt instead of calling setup done.

Copyable engineer prompt:

```text
I am initiating PrecodeOS from user-provided source inputs.

Inputs:
- Conviction Packet / Precode Ingestion Packet: [path or pasted reviewed summary]
- Student Experience Ingestion Packet, if present: [path or pasted reviewed summary]
- Experience artifacts, frontend design files, screenshots, Figma export, or design-system notes: [paths or links]
- Existing PRD, if any: [path]

Treat these inputs as evidence, not automatic implementation authority. Do not write code yet.

First classify the entry state: fresh Precode setup, existing non-Precode project, or existing Precode project.

Then use Local Source Intake to summarize stable facts, assumptions, conflicts or stale inputs, privacy redactions, Experience/core-spine implications, Core Spine Gate status, open questions, candidate requirements, candidate non-goals, candidate acceptance signals, feedback gathered, feedback still needed, and affected owner files.

Tell me whether the next safe action is setup validation, owner-file adaptation, PRD drafting, PRD amendment, Experience/core-spine review, decomposition into one candidate core-spine bead, or a narrow unblocker.

Stop before updating authority files, approving a PRD, activating a bead, or coding.
```

For design-heavy inputs, the engineer should explicitly identify:

- visual intent
- target user and minimum value moment
- core workflow spine
- Core Spine Gate status
- screens, states, and user flows
- interactions, empty states, loading states, and error states
- responsive expectations
- feedback gathered before coding and feedback still needed after prototype
- design-system constraints or missing design-system decisions
- accessibility concerns
- unresolved design decisions that could change implementation

Do not let frontend design files become implementation instructions until design facts are mapped to owner files and PRD requirements. If a design conflicts with current code, active memory, an approved PRD, `PRODUCT.md`, `PROJECT-CONTEXT.md`, or another owner file, current authority wins until the user approves an amendment.

### Bootcamp Experience Design To Claude Code

Use this path when a student has an approved bootcamp PRD input and Experience artifacts from Claude Design, Ember UI Builder, or an equivalent AI-assisted UI/UX canvas.

Before the student opens the design canvas, have them use the packet's Design Canvas Input Prompt to turn approved PRD input, idea-shaping notes, reference images, workflow examples, and not-yet boundaries into a short design-tool brief. The brief should focus the rough artifact on the minimum workflow that gives the target user value; it is not approval for extra screens, visual polish, or future platform scope.

The student-facing output is `tasks/templates/STUDENT-EXPERIENCE-INGESTION-PACKET.md`. The first Claude Code action should be creating one bounded Precode bead for the core spine, not immediate coding.

Support engineers may work in parallel on local environment and scaffold readiness. They should not own product direction, PRD decisions, Experience artifacts, acceptance, feedback interpretation, or scope.

Copyable parallel-readiness support prompt:

```text
Check whether this student's local environment and scaffold are ready for Claude Code implementation.

You may inspect:
- local environment setup
- repo and scaffold shape
- package source and target folder boundaries
- dependency, runtime, local app, or auth blockers
- setup validation state
- the narrow technical unblock needed next

Do not change PRD direction, Experience artifacts, product scope, acceptance, feedback interpretation, bead activation, or design direction. Do not implement starter screens from product judgment.

Report:
- environment status
- scaffold status
- runtime or auth blockers
- setup validation status
- exact next technical unblock
- student-owned product or acceptance decisions still blocking implementation
- confirmation that support did not change product scope, design direction, acceptance, or feedback interpretation
```

Before Claude Code creates or proposes the bead, the packet should record the Core Spine Gate status and any target-user feedback gathered before coding. If the gate is blocked, stop on the missing workflow evidence instead of turning the design into implementation scope.

Copyable student handoff prompt:

```text
Use this approved bootcamp PRD input and Student Experience Ingestion Packet to create one Precode bead for the core spine implementation.

First inspect the "Complete Before Claude Code Handoff" checklist and the packet fields.

If any required field is missing, ambiguous, or marked unknown in a way that changes implementation scope, ask me for the missing information and stop. Do not create a bead yet.

If this packet has a formal Precode PRD shard in tasks/prds/, you may draft one ready candidate bead file for the core spine. Do not update tasks/todo.md, activate the bead, or code.

If this packet only has a bootcamp-approved PRD-like input and no formal Precode PRD shard, produce a candidate bead proposal only and stop. Tell me that normal Precode intake or PRD promotion is required before activation.

Summarize the core scope, minimum value moment, Core Spine Gate status, files likely in play, acceptance checks, key screen states, responsive behavior to verify, feedback gathered before coding, manual verification steps, stop conditions, and what is explicitly not included.

Preserve the approved PRD intent and Experience core spine.

Do not code until I approve the bead through Precode.
```

After the coded prototype exists, route demo notes, target-user feedback, and minimum-value observations into the Student Completion Evidence Packet or normal closeout evidence. Do not treat demo notes as implementation acceptance or product validation by themselves.

## Client Engagement Intake

Use `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` when a client arrives with an existing project, external PRD, frontend design files, Ember Handover Agent artifacts, `Backend-dev-plan.md`, backend sprint plans, or an existing codebase.

Support and engineers should answer immediate engagement questions this way:

- Separate backend repo, monorepo, or single repo is a client-owned topology decision. Precode records the decision in `PROJECT-CONTEXT.md` and layout conventions in `CODEBASE-GUIDE.md`; it does not prescribe the topology.
- External PRDs and product specs feed Local Source Intake and PRD normalization. They do not replace Precode PRD shards.
- Ember handover artifacts and backend sprint plans feed Local Source Intake and Decomposition. They do not become parallel Precode execution tracks by default.
- Existing codebases are valid source inputs, inspected read-only first, then mapped to owner files, conflicts, and setup or PRD/adaptation needs.
- Client PRDs that do not match Precode's PRD shape are normalized through Local Source Intake first, then the PRD Protocol creates or amends a Precode PRD shard.

Copyable client engagement prompt:

```text
Use the Client Engagement Intake Protocol.

Client materials:
- Existing project or repository: [path/link/status]
- Client PRD or product spec: [path/link]
- Frontend design files, screenshots, Figma export, or design-system notes: [path/link]
- Ember Handover Agent or backend plan, including Backend-dev-plan.md if present: [path/link]
- Sprint plan or implementation task list: [path/link]

Treat all client materials as evidence, not authority. Do not write code, approve a PRD, create or activate beads, change repo topology, run installers, mutate external systems, or overwrite project files.

First classify the entry state, repo topology, existing codebase facts, source conflicts, privacy or secrets redactions, owner files likely affected, and whether the client PRD needs normalization into a Precode PRD shard.

Tell me the next safe action: setup/adaptation, Local Source Intake, PRD draft, PRD amendment, architecture/API/data/security owner-file update, decomposition into candidate beads, or a narrow unblocker.
```

## Demo And Engineering Readiness

Use this section when a student is preparing to show or hand off a prototype during a cohort, workshop, or support slot.

Before a demo or engineer session:

- refresh or start the local app early enough to catch slow reloads
- have auth, login, and required test accounts ready
- skip onboarding during the demo unless onboarding is the product being tested
- keep the demo focused on the value proposition and feedback-worthy slice
- ask the student what exact feedback or technical unblock they need
- separate "prototype runs" from "idea is validated"

If the app does not start, loads slowly, or auth blocks the demo, move to `docs/PRECODE-TROUBLESHOOTING.md`. Do not use a demo deadline as a reason to skip active memory, validation, secrets boundaries, or user approval.

For student-by-student completion evidence, use `tasks/templates/STUDENT-COMPLETION-EVIDENCE-PACKET.md`. The packet is the shared progress artifact for the student, instructor, and support engineer. It should stay short, public-safe, and evidence-only: instructors can help summarize product evidence, support engineers can note narrow technical unblocks, and the student owns product decisions, approvals, acceptance, and next direction.

## Bootcamp Role Boundaries

Use this section when PrecodeOS adoption is happening inside a guided bootcamp, workshop, or cohort.

### Beginner Discovery Routing

Use this routing when a student arrives with messy notes, a Product Brief, guided research, or a Conviction Packet before PRD creation.

| Student state | Support response | Do not do yet |
|---|---|---|
| Messy idea or scattered notes | Route to the Product Ideation Workbook or Product Conviction Packet prompt. Ask for a Product Brief after at most three high-level questions. | Do not create a PRD, bead, or code. |
| Product Brief exists but evidence is weak | Ask the student/instructor to name current workaround, strongest evidence, weakest assumption, smallest learning step, and whether to proceed, pause, narrow, or kill. | Do not treat excitement or online research as validation. |
| Conviction Packet exists | Bring the reviewed packet into Local Source Intake as evidence. | Do not route directly to PRD drafting or Claude Code implementation. |
| Approved PRD-like input plus Experience artifacts exist | Use `tasks/templates/STUDENT-EXPERIENCE-INGESTION-PACKET.md` before Claude Code creates one bounded bead. | Do not let raw discovery notes substitute for approved PRD-like input. |

Conviction means MVP-ready clarity, not validated demand. A good packet names intended user, painful before moment, better after moment, current workaround or evidence, strongest evidence, weakest assumption, MVP-ready first slice, not-yet list, smallest learning step, and sensitive surfaces.

Instructors own the learning and product-thinking layer:

- help students move from rough ideas to prototype progress
- ask clarifying and challenging questions
- help the student summarize evidence
- explain PrecodeOS concepts in plain language
- protect student ownership of product decisions, approvals, and acceptance
- preserve the distinction between "prototype works" and "idea is validated"
- help students turn messy notes into a Product Brief or Conviction Packet before PRD shaping

The Student owns the product direction, decisions, approvals, and acceptance for their prototype.

The Student should:

- explain the intended user, painful before moment, better after moment, and first useful slice in plain language
- distinguish MVP-ready conviction from validated demand
- make and approve product decisions, scope tradeoffs, non-goals, and acceptance calls
- use PrecodeOS prompts and evidence gates to stay oriented, bounded, and able to verify progress
- summarize what evidence supports continuing, narrowing, pausing, or changing direction
- ask instructors for product-thinking help when the idea, scope, or evidence is unclear
- ask support engineers for technical help when system setup, troubleshooting, or implementation blockers stop progress
- avoid treating "the prototype works" as proof that the idea is validated

Mentors are past bootcamp students who help first-time students navigate the cohort as guides, advisors, connectors, peers, and role models.

Mentors should:

- help students build confidence by sharing lived experience from the bootcamp
- provide light product idea support without owning product direction, scope, approval, acceptance, or evidence interpretation
- help students understand which role to ask for help: instructor for product thinking, support engineer for technical unblocking
- encourage students through uncertainty, stuck points, and normal first-time-builder discomfort
- model good PrecodeOS habits such as asking clarifying questions, keeping scope small, and separating working prototypes from validated ideas
- connect students to relevant cohort resources, examples, instructors, support engineers, or peers
- avoid replacing instructors, performing technical troubleshooting, or becoming the hidden product owner

Support engineers own technical support and unblocking when needed:

- help students with system requirements installation and maintenance
- perform technical troubleshooting and diagnosis
- implement narrow technical fixes when a student is blocked
- manage the escalation workflow, ensuring that issues are resolved promptly and efficiently
- explain the technical change plainly
- avoid owning product direction, scope, acceptance, or evidence interpretation

When routing is unclear, ask what decision is actually blocked. Product direction, scope, user evidence, and acceptance go back to the student with instructor support. Cohort navigation and confidence can involve mentors. Local setup, repo state, validation failures, local runtime, auth, and implementation blockers belong with support engineers. PrecodeOS package defects or unclear official guidance should be escalated to the Precode maintainer or lead support channel.

Mentor involvement may be lightly noted when it materially affects student confidence, navigation, or routing. Do not turn mentorship into heavy evidence overhead.

For cohort completion, do not count a working prototype as strong PrecodeOS evidence by itself. The Student should also be able to explain the problem, user, narrowed first useful slice, at least one non-goal, what was verified or demoed, and what evidence supports continuing, narrowing, pausing, or changing direction. Use `tasks/templates/STUDENT-COMPLETION-EVIDENCE-PACKET.md` when the cohort needs a consistent completion snapshot.

## Repair Path For Incorrect Setup

If files were copied incorrectly, overwritten, moved, renamed, or edited casually:

1. Stop implementation.
2. Identify the symptom in plain English.
3. Re-read active memory if it exists.
4. Compare expected files against `docs/PRECODE-PACKAGE-FILE-INVENTORY.md`.
5. Use `docs/PRECODE-TROUBLESHOOTING.md` and `tasks/reference/RECOVERY-PROTOCOL.md`.
6. Explain the repair path before editing anything.
7. Validate before resuming.

Repair is not auto-repair. Do not delete evidence, reset the repo, or rewrite generated reports to make the state look clean.

## Close The Support Session

Do not create a separate support artifact by default. End by orienting the user to existing Precode surfaces:

- what was set up or adapted
- which checks passed or remain blocked
- whether source inputs were ingested, deferred, or named as the next blocker
- the current bead
- the next safe prompt
- what not to approve yet
- where to go for troubleshooting

Support can say:

```text
Your durable project state is in the Precode files, not in my notes. Start next time with session-start, ask the agent to explain the active bead, and stop if generated reports or chat confidence start acting like authority.
```

## Related Guides

- `docs/PRECODE-GUIDED-SETUP.md` for the public setup path
- `docs/PRECODE-TROUBLESHOOTING.md` for symptom lookup
- `docs/PRECODE-USER-GUIDE.md` for day-to-day use
- `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` for the public package file dictionary
- `tasks/reference/RECOVERY-PROTOCOL.md` for conservative repair
- `tasks/reference/CLIENT-ENGAGEMENT-INTAKE-PROTOCOL.md` for client PRDs, external designs, backend plans, sprint plans, and existing codebases
