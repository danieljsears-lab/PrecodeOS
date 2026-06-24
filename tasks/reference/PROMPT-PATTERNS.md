# PrecodeOS -- Prompt Patterns
<!-- ANCHOR: prompt-patterns -->

> AUTHORITY: Beginner-friendly prompt patterns for operating PrecodeOS consistently across AI coding agents.
> NOT_AUTHORITY: Active memory, product decisions, feature requirements, task selection, implementation plans, generated progress state, or bead transitions.
> LOAD_WHEN: A user needs copyable prompts, an agent is preparing a handoff, or a session needs clearer context, review, intake, verification, or recovery instructions.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.40
Last updated: 2026-06-24

## Purpose

These prompts help a non-technical builder operate Precode without memorizing every protocol.

They are prompts, not authority. The agent must still follow active memory, the active bead, the primary authority file, and the relevant Precode protocol.

## Safe Prompt Pack

Use this pack when a session needs extra guardrails before setup, discovery, implementation, or handoff. These prompts are topology-neutral: they tell the agent to discover the actual source package, target project, app directory, owner files, and checks instead of assuming a fixed folder layout.

### Source And Target Confirmation

```text
Before setup or intake, confirm the PrecodeOS package source, the target project folder, the app directory or directories if known, the Precode owner files present, files that must not be copied or edited, current git status, and validation commands.

Do not copy files, create files, write code, install hooks, change CI, or update authority files until you explain the setup state and I approve the next narrow step.

If repo facts conflict with active memory, PROJECT-CONTEXT.md, or the setup guide, surface the conflict before continuing.
```

### Existing Repo Intake

```text
Run Existing Repo Intake after Bootstrap Confidence.
Use the PrecodeOS checkout as the package source and my existing app repo as the target.
Do not copy, edit, install hooks, change CI, run app commands, adapt owner files, approve a PRD, activate a bead, or write code.
Tell me the repo topology, likely app directories, stack, docs, likely checks, CI/deploy hints, generated and sensitive surfaces, owner-file gaps, conflicts, first safe next action, and stop conditions.
Treat the output as evidence only, not permission to mutate.
```

### Supervised Setup Plan

```text
Run the PrecodeOS supervised setup plan after Bootstrap Confidence and manifest preview.
Use the PrecodeOS checkout as the package source and my project folder as the target.
Do not copy, edit, install hooks, change CI, run app commands, create active memory, adapt owner files, approve a PRD, activate a bead, or write code.
Show the setup checklist, approval gates, exclusions, blockers, and validation steps.
Treat the setup plan as evidence only, not permission to mutate.
```

### Supervised Setup Apply

```text
Apply only the supervised setup action IDs I explicitly approve.
Use the PrecodeOS checkout as the source and my empty or nearly empty project folder as the target.
Run the supervised setup plan first, then apply only the approved review_copy_candidate action IDs I name.
Do not adapt owner files, overwrite files, install hooks, change CI, run app commands, write app code, approve a PRD, activate a bead, install a CLI, provide package-manager behavior, define release channels, or automate rollback.
After copying, show copied, skipped, blocked, and validation next steps.
```

### Existing Project Adaptation Plan

```text
Run the PrecodeOS existing-project adaptation plan after Existing Repo Intake.
Use the PrecodeOS checkout as the source and my existing app repo as the target.
Do not copy, edit, overwrite, install hooks, change CI, run app commands, write app code, approve a PRD, activate a bead, define release channels, provide package-manager behavior, or automate rollback.
Show owner-file creation or adaptation candidates, preserved project material, approval gates, blockers, and deferred actions.
Treat the plan as evidence only, not permission to mutate or adapt owner files.
```

### Package Upgrade Preview

```text
Run the PrecodeOS package upgrade preview for this existing Precode target.
Use the PrecodeOS checkout as the source and my project folder as the target.
Do not copy, edit, overwrite, adapt owner files, install hooks, change CI, run app commands, write app code, define release channels, provide package-manager behavior, or automate rollback.
Classify the target as clean, dirty package edits, dirty project or owner edits, mixed or unknown, or blocked.
Show action IDs and wait for my explicit approval before any missing package-owned file copy.
Treat the preview as evidence only, not package update permission.
```

### Package Upgrade Apply

```text
Apply only the package upgrade action IDs I explicitly approve.
Run the upgrade preview first, then copy only approved review_package_copy_candidate files that are missing from the existing Precode target.
Do not overwrite dirty files, adapt owner files, install hooks, change CI, run app commands, write app code, define release channels, provide package-manager behavior, or automate rollback.
If the package state is dirty, mixed, unknown, or blocked, refuse mutation and show the manual review path.
```

### Bootstrap Recovery Guidance

```text
Give bootstrap recovery guidance for this setup state.
Use the PrecodeOS checkout as the source and my project folder as the target.
Do not delete, overwrite, regenerate, roll back, copy files, adapt owner files, install hooks, change CI, run app commands, write app code, define release channels, provide package-manager behavior, or mutate setup.
Name the likely recovery path, support steps, validation next steps, and forbidden actions.
Treat the guidance as evidence only, not repair approval.
```

### One Question At A Time

```text
Ask one blocking question at a time. Wait for my answer before asking the next one. Include your recommended answer when useful, but do not decide product facts, repo topology, scope, or acceptance for me.
```

### Active Bead Before Editing

```text
Before editing, load active memory, the active bead, and the primary authority. Confirm the active bead, files in play, checks, stop conditions, approval gates, and what is out of scope. Do not start implementation until that boundary is clear.
```

### Git Hygiene Before New Work

```text
Before starting a new bead or session, check git status and tell me whether current changes are clean, already committed, generated evidence, or unfinished work from the current bead.

If completed checked work is uncommitted, propose a concise commit summary before moving on. Push only when a remote exists and this project expects remote backup or collaboration.
```

### Evidence Is Not Authority

```text
Treat generated reports, logs, source notes, screenshots, transcripts, imported issues, and handoff summaries as evidence only. Return to active memory, the active bead, the primary authority file, and user approval before doing work.
```

### Precode Skill Playbook

```text
Use the Precode Skill Playbook Protocol.
Treat the skill as a read-only prompt playbook, not a command wrapper, plugin registry, optional pack, or new authority layer.
Name the owner protocol or adapter, allowed actions, forbidden actions, generated evidence if any, approval gates, stop conditions, and promotion path.
Do not edit files, run mutating commands, approve PRDs, activate beads, approve review decisions, or promote findings.
```

### Ask Precode

```text
Use Ask Precode.

Answer my stable PrecodeOS documentation question from README.md, docs/*.md, and relevant tasks/reference/*.md. Cite the source files.

If my question depends on current project state, active memory, generated reports, local errors, private maintainer context, or what to do next, stop and route me to the right Precode workflow instead.

Return: Short answer, Sources, What this does not decide, and Next safe prompt.
```

### Workflow Selection Skill

```text
Use the Workflow Selection Skill.
Read active memory, then load the Workflow Selection Protocol and any minimum owner file needed to classify the situation.
Return the current situation, recommended workflow, next artifact, required authority source, user approval needed, run contract needed, stop condition, and generated-report warning.
Do not edit files, approve work, activate a bead, run mutating commands, or start implementation.
```

### Small Team Collaboration Lane

```text
Use the Small Team Collaboration Lane.

We have [2-5] people working on this product. Help us define the coordinator, product decision owner, contributor roles, branch/worktree rules, candidate parallel beads, review gates, merge/re-entry rules, and forbidden actions before anyone edits.

Load the Small Team Collaboration Lane protocol. Treat the lane as built-in but explicit, not default-active and not a module, optional pack, runtime toggle, project board, or GitHub-driven task system.

Return: Team situation, Coordinator and decision owner, Branch/worktree rule, Candidate parallel beads, Per-teammate startup prompt, Review and merge evidence, Approval gates, Stop conditions, Promotion path, and Generated-report warning.

Do not edit files, approve PRDs, activate beads, approve merge, mutate GitHub, deploy, run mutating commands, or treat team notes, PRs, branch status, or generated handoff packets as authority.
```

### Small Team Collaboration Preview

```text
Use the Small Team Collaboration Lane preview.

Run `python3 scripts/team-collaboration-check.py` for local read-only preview evidence. If I explicitly ask for GitHub evidence and `gh` is available, run `python3 scripts/team-collaboration-check.py --github`.

Return the current branch/worktree, integration branch, active bead, one-active-bead status, files in play, owner-file impact candidates, re-entry risks, Team Merge And Re-entry Review Pack fields, teammate assignment packet fields, forbidden uses, and generated-report warning.

Do not create branches or worktrees, push, pull, rebase, merge, create or approve pull requests, mutate GitHub, update owner files, approve PRDs, activate beads, accept implementation, approve merge, deploy, or treat generated preview output as authority.
```

### Session Friction Review

```text
Use Session Friction Review.

Run `python3 scripts/session-friction-check.py` as a read-only advisory review of repeated tool failures, stale evidence, generated-refresh gaps, and memory/context pressure.

Return findings with category, cited source refs, confidence, freshness, recommended destination, suggested next human review step, and generated-report warning.

Do not create memory cards. Do not edit owner files. Do not approve commands, choose tasks, approve PRDs, activate beads, accept implementation, create wrappers, or treat `logs/session-friction-review.json` or checker output as proof or authority.
```

### Team Assignment Packet Prompts v2

```text
Use the Small Team Collaboration Lane.

Prepare a teammate assignment packet for [teammate] on [branch/worktree]. Name the coordinator, product decision owner, teammate role, assigned bead, primary authority, files in play, checks, stop conditions, evidence to return, approval gates, and what must happen before merge/re-entry review.

Use `can run in parallel` only to mean branch/worktree-isolated teammate work after coordinator approval.

Use `scripts/team-collaboration-check.py` output only as generated preview evidence. Do not create the branch/worktree, activate the bead, choose work from GitHub, approve merge, or turn this packet into owner-file authority.
```

### Teammate Startup In A Team Lane

```text
This repo is using the Small Team Collaboration Lane.

Load active memory, the team coordination notes, and the bead assigned to this branch or worktree. Confirm my teammate role, branch/worktree, assigned bead, primary authority, files in play, checks, stop conditions, evidence I must return, and what requires coordinator approval before editing.

Do not rely on chat history, generated reports, PR status, or teammate notes as authority. Do not edit until the branch/worktree and bead boundary are clear.
```

### Team Merge And Re-entry Review Pack

```text
Use the Small Team Collaboration Lane review path.

Review this contributor branch or worktree for merge/re-entry readiness. Compare the assigned bead, primary authority, changed files, recorded checks, manual verification, owner-file impacts, conflicts with the integration branch, stale branch or stale evidence signals, open questions, and follow-up bead candidates. Use `python3 scripts/team-collaboration-check.py --integration-branch <branch>` when a read-only preview would clarify re-entry risk.

Recommend only continue, review, split, block, or coordinator merge/re-entry review. Do not accept implementation, approve merge, activate another bead, mutate GitHub, deploy, or promote findings into owner files.
```

### Product Discovery Interview Skill

```text
Use the Product Discovery Interview Skill.

I need to know whether this idea is worth defining before PRD shaping.

Load the Product Discovery Validation Protocol. Interview me one question at a time. Challenge assumptions supportively, especially if the audience is broad, the user problem is vague, the current workaround is missing, evidence is weak, demand is only imagined, or the first slice is too large.

Return the Discovery Summary with the target user and situation, user problem, current alternatives or workarounds, primary hypothesis or learning target, strongest evidence, weakest assumption, evidence strength, assumption categories, demand or pricing signal, smallest non-code learning step, what would change our mind, sensitive surfaces, recommendation of proceed, pause, narrow, or kill, reason, recommended next Precode workflow, likely authority files, and the guardrail reminder.

Treat the output as evidence only. Do not write a PRD, update PRODUCT.md, create or activate beads, choose tasks, run mutating commands, or code.
```

### Hypothesis Review / Learning Loop

```text
Use Hypothesis Review / Learning Loop on this Discovery Summary, Candidate Queue entry, Local Source Intake summary, PRD Source Inputs section, or Planning Brief.

Tell me what was tested, what was learned, whether the hypothesis is untested, tested, narrowed, killed, promoted, stale, or not applicable, and the next safe Precode workflow.

Return: review target, authority checked, hypothesis or learning target, evidence reviewed, learning status, learning outcome, stale or untested signals, recommended next Precode workflow, user approval needed, stop condition, and generated-report warning.

Treat the output as evidence only. Do not approve product direction, rank candidates, create or activate beads, update owner files, choose tasks, require analytics, create a database, or code.
```

### Accessibility Advisor Fit Interview

```text
Use the Accessibility Advisor Fit Interview.

Help me decide whether to invoke the Accessibility Advisor for this bead, review, or release candidate. Ask one question at a time. Inspect only the current bead, owner-file requirement, release-candidate profile, or context I provide that is needed to decide fit.

Return: Recommendation of invoke advisor, not needed, or defer; Reason; Accessibility target; Evidence needed; Manual review needed; Unresolved risk; and Stop condition.

Treat this as an opt-in fit interview. Do not make accessibility review mandatory for every UI/interface bead, claim legal compliance, certify WCAG/ADA conformance, accept implementation, approve review, approve release, create follow-up tasks, run mutating commands, mutate external systems, or edit files.
```

### Maintainer Package Review Skill

```text
Use the Maintainer Package Review Skill.
Treat PrecodeOS as an OS package I maintain, not as an app to execute.
Use Plan Mode or an equivalent read-only planning posture when available.

Read _maintainer/MAINTAINER-NOTES.md first, then load only the maintainer roadmap, strategy, package reference, protocol, changelog, inventory, or boundary file relevant to this package-maintenance question. Do not read AGENT.md, DECISIONS.md, or tasks/todo.md for this maintainer review.

Use the Skill Playbook Protocol and Extension Protocol for any proposed package capability, skill playbook, adapter, protocol, generated report, command wrapper, registry, optional pack, external integration, install/update behavior, or package-health surface.

Return: Title, Summary, Relevant context and owner files, Proposed package or roadmap change, Public/private boundary notes, Risks and challenged assumptions, Maintainer changelog impact, Protocol impact, Public reference-document impact, Validation plan, and Explicit assumptions.

Do static package analysis only unless I explicitly ask for mutation outside planning mode. Do not run Precode as an app, edit files during planning, write generated evidence, activate beads, approve PRDs, approve transitions, approve review decisions, publish, deploy, install, update, mutate external systems, add command-wrapper behavior, add registries, create optional packs, or make maintainer files part of public package authority.
```

### Skill / Extension Review Skill

```text
Use the Skill / Extension Review Skill.

Review this proposed Precode skill or extension before it becomes a maintained surface. Load the Extension Protocol and Skill Playbook Protocol, then inspect only the proposed skill or extension material I provide.

Return: Review target, Extension type, Owner source, Authority boundaries, Mutation and external-system risk, Generated evidence, Approval gates, Validation needed, Promotion path, Rollback or removal note, Risks, Recommendation, and Stop condition.

Recommend only accept-shape, revise, split, defer, or reject. Do not edit files, install skills, approve the extension, add a registry, create optional packs, run mutating commands, mutate external systems, promote generated findings, or bypass owner protocols.
```

### Review / Acceptance Skill

```text
Use the Review / Acceptance Skill.

Review the active bead for acceptance readiness. Load active memory, the active bead, the primary authority, closeout evidence, recorded checks, manual verification, relevant run contract or release-readiness note if present, and the diff or changed-file summary.

If I ask "do you accept these changes?", treat that as a review request. If the active bead is still `in_progress`, it must switch the active bead to `review` first before any acceptance recommendation. Do not mark the bead `done` from this prompt.

Return: Review target, Authority checked, Evidence reviewed, Missing proof, Acceptance questions, Risks or drift, Recommendation, Approval still required, and Follow-up or promotion path.

Recommend only accepted, revise, split, blocked, or stop. Do not accept implementation, approve the review decision, activate the next bead, create follow-up tasks, approve release, run mutating commands, or treat generated reports or confidence as proof.
```

### Requirement-To-Proof Review

```text
Review the proof for this requirement, bug behavior, or acceptance criterion as a requirement-to-proof trace.
Load the active bead, primary authority, recorded checks, manual verification, closeout evidence, and relevant PRD acceptance oracle when present.

Return: Requirement, bug behavior, or acceptance criterion; Evidence lane; Recorded source; What this proves; What this does not prove; Remaining uncertainty; Missing proof; Acceptance question; Recommendation.

Do not accept implementation, approve review, approve release, activate the next bead, create follow-up tasks, run mutating commands, or treat generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, generated reports, or confidence as proof by themselves.
```

### Build Attribution Review

```text
Review the Build Attribution Ledger for this bead or recent work.
Load the active bead, Closeout Evidence, generated Build Attribution Ledger when available, bead build journal when needed, and any relevant small-team or GitHub evidence as evidence only.

Return: human contributor, contributor role, agent/tool surface, attribution reviewer, attribution uncertainty, evidence confidence, missing attribution, Git-hint-only attribution, and the source that must be reviewed next.

Do not choose tasks, accept implementation, approve review, approve merge, approve release, assign blame, score contributors, mutate GitHub, or treat generated ledger output as authority.
```

### Review Lanes

```text
Use the Review Lanes Protocol for this active bead.

Run exactly one lane: Security Review Lane, Release / Docs Freshness Review Lane, or Dependency Graph Review Lane.

Load the active bead, primary authority, files in play or changed-file summary, recorded checks, manual verification, closeout evidence, Work Graph evidence when dependency relationships are being reviewed, and only the owner files needed for this lane.

Return: Lane, Review target, Authority checked, Evidence reviewed, Findings, Missing proof, Acceptance questions, Recommendation, Approval still required, and Promotion path.

Recommend only accepted, revise, split, blocked, or stop. Do not accept implementation, approve review, approve release, approve transitions, approve parallel execution, certify security or compliance, create follow-up tasks, rewrite owner files, run mutating commands, mutate GitHub, mutate external systems, or treat generated reports, Work Graph reports, screenshots, browser notes, GitHub status, or confidence as proof.
```

### Precode Idea Coach

```text
Use the Product Conviction Packet Skill as my pre-repo idea coach.

I am a first-time non-technical builder with a rough product idea. Run this as a guided PrecodeOS product-coach interview inside Claude Code, Claude, Codex, or an equivalent agent surface. If Claude Code Plan Mode or an equivalent planning mode is available, use it.

Help me research, explore, challenge, and narrow the idea before I create a PRD or ask anyone to code. Use plain language. If you use a product-management term, define it in one sentence.

Stage 1: Orientation. Confirm we are discussing one idea, name the user type if known, and remind me not to paste secrets, credentials, billing data, private customer records, raw transcripts, dashboard values, production config, or sensitive personal data.

Stage 2: First Three Questions. Interview me one question at a time. Ask only high-level product or business questions at first. After at most three questions, summarize a Product Brief with: product idea, intended user, painful before moment, better after moment, current workaround or evidence, assumptions, primary hypothesis or learning target when useful, not-yet list, smallest useful version, and next best question.

Stage 3: Challenge And Clarity. Challenge me supportively but firmly when the audience is too broad, the painful moment is vague, the problem is framed as a solution, the current workaround is missing, evidence is weak, scope is too large, feature lists appear before user moments are clear, or sensitive surfaces appear. Force plain-English answers for user, painful before moment, better after moment, current workaround or evidence, weakest assumption, and first useful slice. Do not debate endlessly; move non-blocking concerns to Not yet.

Stage 4: Evidence And Assumption Check. Rate evidence strength as very weak, weak, medium, strong, or strongest. Name the primary hypothesis or learning target, strongest evidence, weakest assumption, what would change our mind, and the smallest non-code learning step.

Stage 5: Candidate Capability Matrix. Translate possible features into candidate capabilities, not approved requirements:

| Candidate capability | User moment | Existing evidence | New insight | Risk | MVP fit | Recommendation |
|---|---|---|---|---|---|---|

Guide source-cited research when useful. For each source, include the link, date or recency if available, the claim it supports, confidence, uncertainty, and what question it helps answer. Treat research as weak evidence unless it shows user behavior, a current workaround, spend, switching effort, prototype use, payment, or another costly action.

If worth-building uncertainty becomes the main question, route me to the Product Discovery Interview Skill / Product Discovery Validation instead of trying to turn weak evidence into a Conviction Packet.

Stage 6: Handoff. When the idea is clear enough, produce a Conviction Packet with: idea in plain English, intended user and situation, painful before moment, better after moment, current workaround or evidence, evidence strength, primary hypothesis or learning target, strongest evidence, weakest assumption, what would change our mind, guided research notes, MVP-ready first slice, not-yet list, smallest learning step, sensitive surfaces, recommended next Precode path, Local Source Intake readiness, and Local Source Intake handoff prompt.

Do not write a PRD, create beads, update PRODUCT.md, create a roadmap or backlog, or code. If there are useful not-yet ideas, suggest Candidate Queue entries for my review instead of treating them as approved work. Treat every output as evidence only until I review it and bring the distilled packet into Precode Local Source Intake.
```

### Candidate Queue Review

```text
Use the Candidate Queue Protocol.

Review `CANDIDATE-QUEUE.md` as parked intent, not task authority.

Tell me: what ideas are parked, which need research, which are worth shaping, which are blocked or stale, which might become PRDs, which approved PRDs have candidate beads, and which reviewed candidates have product-value ratings, themes, or near-bead sketches.

Also tell me what the Candidate Queue cannot answer: the active task, what the agent should build next, whether a PRD is approved, whether a bead is active, or whether a ranked item is authorized for implementation.

Return: Current candidate, status, evidence used, primary hypothesis or learning target, recommended next path, promotion target, user approval needed, stop condition, and generated-report warning.

Do not update active memory, approve a PRD, activate a bead, reserve B### bead IDs, treat product-value rating as implementation priority, choose next work, or start coding.
```

### Add Candidate Queue Entry

```text
Add or draft a Candidate Queue entry for this intent.

Use `CQ-###-short-name`, status, user intent, evidence or source pointers, open questions, primary hypothesis or learning target, evidence strength, weakest assumption, reviewed rank if I provide one, promotion target, blocked or stale reason, related PRDs, candidate bead visibility, next review trigger, and last reviewed date.

Ranking is review order only, not implementation priority. Product-value rating is product value only. Do not create a PRD, create or activate beads, reserve bead IDs, update `tasks/todo.md`, or code.
```

### Candidate Queue Shaping Proposal

```text
Use the Candidate Queue Protocol.

Draft a JSON shaping proposal for this Candidate Queue ID.

Include candidate_id, shaping_status, product_value_rating, product_value_rationale, themes, weakest_assumption, and near_bead_sketches. Use near-bead sketch IDs like CQ-001-short-name-S01.

Treat P0/P1/P2/P3 as product value only, not implementation priority. Near-bead sketches are not bead files and must not use B### IDs.

Do not approve a PRD, activate a bead, update tasks/todo.md, choose next work, or code.
```

### Build-React-Learn Exploratory Prototype Bead

```text
Use Build-React-Learn for an exploratory prototype bead.

Build: define one tiny reversible prototype option inside the current PRD or approved exploration scope.
React: after the build, help me review what worked, what failed, what changed my mind, what evidence exists, and what this does not prove.
Learn: recommend whether to keep, revise, rebuild, discard, split, amend the PRD, run Plan Loop, use Hypothesis Review, park a Candidate Queue item, or propose the next bead.

Use normal Precode bead rules: one active bead, explicit files in play, checks, stop conditions, closeout evidence, and user approval before any transition. Do not create a new bead-kind enum, treat the prototype as product approval, accept implementation, approve a PRD, choose the next task, or activate another bead.
```

Closeout prompt:

```text
For this exploratory prototype bead, show the prototype decision: keep, revise, rebuild, discard, split, or promote learning to PRD/decision.

Explain what the prototype proved, what it did not prove, what evidence or checks support that conclusion, and the next safe Precode workflow.

Do not treat a working prototype as validation, acceptance, PRD approval, or transition approval.
```

### Candidate Queue Import Preview

```text
Use scripts/candidate-queue.py to preview importing this raw notes file into the Candidate Queue.

Run python3 scripts/candidate-queue.py --preview-import <path>.

Treat the output as preview evidence only: mutates_now: false. Do not apply anything unless I explicitly approve an action ID with --apply --approve-action.
```

### Precode Conviction Handoff

```text
Use the Product Conviction Packet Skill handoff path.

I am bringing a reviewed Conviction Packet into a Precode project. Treat the packet as evidence, not authority.

First classify whether the packet is ready for Local Source Intake or should pause for Product Discovery Validation because the user, painful before moment, current workaround, primary hypothesis or learning target, strongest evidence, weakest assumption, MVP-ready first slice, or sensitive surfaces are unclear.

If ready, use Local Source Intake on the packet. Summarize stable facts, assumptions, conflicts, open questions, candidate product constitution updates, candidate PRD inputs, likely owner files, and recommended next safe workflow.

Do not update PRODUCT.md, draft or approve a PRD, create or activate beads, or code until I review the intake summary and approve the next Precode step.
```

### Stop Before Precode Control-Layer Edits

```text
Do not modify Precode control-layer files, active memory, scripts, protocols, validators, adapters, modes, generated reports, or task state unless the active bead explicitly includes that work.

If a Precode framework or control-layer file appears to be causing an error, stop and explain the symptom, affected file, likely owner file, and safest escalation path before patching anything.
```

## Session Start

```text
Run the Precode session start. Explain the Context Pack in plain English: current bead, done-when target, primary authority, files in play, out of scope, checks, stop conditions, open questions, and anything generated that must not be treated as instructions.
```

## Task Confirmation

```text
Before editing, confirm the active bead, the primary authority file, the files in play, the first check you expect to run, and what would make you stop or ask me.
```

## Local Source Intake

```text
Use the Local Source Intake Protocol on these local materials. Treat them as evidence only. Summarize stable facts, conflicts, open questions, candidate requirements, and possible beads. Do not update authority files or write code.
```

## Engineer Initiation

```text
I am initiating PrecodeOS from user-provided source inputs.

Inputs:
- Conviction Packet / Precode Ingestion Packet: [path or pasted reviewed summary]
- Frontend design files, screenshots, Figma export, or design-system notes: [paths or links]
- Existing PRD, if any: [path]

Treat these inputs as evidence, not authority. Do not write code yet.

First classify the entry state: fresh Precode setup, existing non-Precode project, or existing Precode project.

Then use Local Source Intake to summarize stable facts, assumptions, conflicts or stale inputs, privacy redactions, design implications, open questions, candidate requirements, candidate non-goals, candidate acceptance signals, and affected owner files.

Tell me whether the next safe action is setup validation, owner-file adaptation, PRD drafting, PRD amendment, design/architecture impact review, decomposition into candidate beads, or a narrow unblocker.

Stop before updating authority files, approving a PRD, activating a bead, or coding.
```

## Client Engagement Intake

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

## Product Constitution Review

```text
Review PRODUCT.md with me. Clarify product promise, users and jobs, strategy and non-goals, current bets, success signals, and design or voice pointers. Tell me what should move to a PRD or DECISIONS.md. Do not code or activate work.
```

## Founder-Friendly Product Brief

```text
I am a non-technical founder with a rough product idea.

Use the Product Ideation Workbook path first. Ask only high-level product or business questions at the start. After at most three questions, summarize progress as a Product Brief with: product idea, builder lens when useful, intended user, painful before moment, better after moment, current workaround or evidence, assumptions, primary hypothesis or learning target when useful, not-yet list, smallest useful version, and next best question.

If the idea is still abstract or too large, use the workbook's optional learning/MVE framing to name the smallest complete useful payoff, visible iteration, and core workflow spine. Treat that framing as evidence only, not an implementation handoff.

Do not ask me to decide architecture, module boundaries, test strategy, owner files, acceptance matrices, or system behavior yet. Do not write a PRD, create beads, update PRODUCT.md, or code.
```

## PRD Shaping

```text
Use the PRD Protocol to shape this idea. Check PRODUCT.md for product fit when relevant. If this is a net-new rough product idea, start from the workbook or Product Brief and keep early questions product-facing. Help me clarify the problem, non-goals, before/after user moment, sensitive surfaces, verification evidence, and smallest first bead. Translate technical sections for me after product alignment. Do not start implementation.
```

## Alignment / Product Brief

```text
Use the Idea To PRD Workflow to align this idea before planning. Ask one high-level product or business question at a time, include your recommended answer, and after at most three questions summarize progress as a Product Brief plus one next best question. Do not ask me to choose architecture, module boundaries, test strategy, owner files, or acceptance matrices until a real risk surfaces. Do not write a PRD, propose beads, or code until implementation-changing questions are resolved or marked non-blocking.
```

## Ubiquitous Language Review

```text
Use the Ubiquitous Language Protocol. Identify the terms I introduced, their plain-English meanings, aliases, avoid or confusing terms, source pointers, freshness, and examples in UI/code/tests/docs/support/user language. Do not code or promote anything without approval.
```

## Glossary Card Proposal

```text
Turn these reviewed terms into a proposed project_glossary memory card. Include domain terms with plain-English meanings, aliases, avoid terms, source pointers for each useful term group, examples in UI/code/tests/docs/support/user language, freshness, and authority owner if promoted. Do not write the card until I approve, and do not treat the proposed card as authority.
```

## Domain Naming Review

```text
Before naming modules, interfaces, tests, fixtures, routes, UI labels, docs, or support language, compare the proposed names to the PRD Domain Language, current code, owner files, and any reviewed project_glossary cards. Tell me which names match user language, which are acceptable technical translations, which are confusing or stale, and what needs owner-file promotion or a follow-up bead before broad renaming.
```

## Destination PRD Review

```text
Review this PRD as a destination document. Confirm the user problem, domain language, non-goals, before/after moment, plain-English acceptance checks, stale source inputs, agent-facing technical translation, and smallest first vertical slice. Do not activate any bead.
```

## Requirements Gap And Conflict Review

```text
Use Requirements Gap And Conflict Review.

Review this PRD, spec, design note, or requirement set before PRD approval, design promotion, bead derivation, or implementation.

Load the PRD Protocol, Verification Guardrail Protocol, the requirement source I provide, and only the owner files needed to understand authority. Check the requirement set as a whole for ambiguous language, conflicting constraints, missing edge cases, unstated assumptions, stale or conflicting source inputs, unverifiable acceptance oracles, and owner-file follow-ups needed before implementation.

Return exactly:

Review target:
Authority checked:
Requirement gaps:
Conflicts:
Missing edge cases:
Unstated assumptions:
Acceptance weaknesses:
Suggested owner-file updates:
Stop conditions:
Recommendation: revise | clarify | split | ready-for-human-approval-review | stop

Ask questions and suggest fixes only. Do not approve the PRD, rewrite owner files, create or activate beads, convert findings into implementation instructions, accept design promotion, run mutating commands, or treat the review output as proof.
```

## Bugfix Spec Lane

```text
Use the Bugfix Spec Lane before editing this small repair.

Load the active bead, the likely owner file, the Recovery Protocol, and the Verification Guardrail Protocol. Return a compact bugfix spec with:

Current behavior:
Expected behavior:
Unchanged behavior:
Owner file:
Root cause if known:
Fix approach:
Regression proof:
Route decision: current_bead | needs_evidence | recovery_repair | PRD/bead | release_readiness

Do not edit yet. If the owner file, route decision, or proof path is unclear, stop and ask for the missing information or checks first.

Treat this spec as advisory only. It does not approve repair, accept implementation, approve a PRD, activate a bead, approve release, approve rollback, approve setup/update mutation, approve destructive commands, create implementation tasks, or become generated proof.
```

## Implemented Bead Reversal

```text
This already-implemented bead may need to be reversed or superseded.

Load the active memory, the prior bead, its Closeout Evidence, recorded checks, the current owner file, and the Implemented Bead Reversal Workflow PRD or protocol if one exists.

Tell me the superseded bead, reversal target, reversal reason, preserved behavior, likely files in play, checks needed, manual verification needed, approvals still required, and whether this should become a separate reversal bead.

Do not reopen a done bead, delete evidence, rewrite transition logs, treat Git revert as proof, approve rollback, approve transition, mutate setup/update behavior, run destructive commands, mutate GitHub, mutate external systems, or start implementation until I approve the separate reversal bead path.
```

## Bead Decomposition

```text
Use the Decomposition Protocol to turn this approved work into candidate beads. Each candidate should have one outcome, one primary authority, bounded files in play, a verification strategy, dependencies, and a clear reason it is small enough.
```

## Dependency Graph Review Lane

```text
Use the Review Lanes Protocol for this active bead.
Run exactly one lane: Dependency Graph Review Lane.

Load the active bead, primary authority, changed-file summary or files in play, recorded checks, relevant PRD/bead/dependency/follow-up/transition references, and `logs/work-graph.md` or compiled Work Graph summary when available.

Show lane, review target, authority checked, evidence reviewed, findings, missing proof, acceptance questions, recommendation, approval still required, and promotion path.

Focus on blocked work, missing or non-done dependencies, duplicate or out-of-order work, broad files in play, unsafe parallel assumptions, ambiguous follow-up destination, owner-file overlap, and stale generated graph evidence.

If Work Graph evidence is stale or misleading, tell me which owner files, beads, PRDs, closeout notes, or recorded evidence need repair before regenerating the graph. Do not edit generated reports as source truth.

Recommend only accepted, revise, split, blocked, or stop. Do not choose tasks, approve transitions, accept implementation, approve parallel execution, create follow-up tasks, rewrite owner files, run tasks, mutate GitHub, mutate external systems, or treat Work Graph reports or confidence as proof.
```

## Vertical-Slice Decomposition

```text
Use the Decomposition Protocol to propose journey beads from this destination PRD. Prefer vertical slices that produce observable feedback. Avoid schema-only, backend-only, frontend-only, or tests-later first beads unless you explain why it is a risk-first or unblocker slice. Include delegation_mode, test_strategy, and review_context.
```

## AFK-Candidate Review

```text
Before marking a bead afk_candidate, verify that it has bounded files in play, explicit checks, stop conditions, a test_strategy, review_context, and no hidden approval gate. Confirm this does not activate parallel execution or bypass human review.
```

## Architecture Shaping

```text
Use the Architecture Shaping Protocol for this approved PRD before deriving beads. Interview me one question at a time about the auth, data, API, integration, dependency, migration, workflow, or multi-system risks that matter. Produce an evidence-only Architecture Brief with owner-file impacts, approval gates, verification evidence, bead implications, and what the coding agent should inspect before choosing internals.
```

## System Design Shape

```text
Use the System Design Pattern Protocol before coding. Start with the simplest shape that can work. Tell me what implementation shape this feature needs, why it matters, the owner file, the simpler alternative, approval gates, verification evidence, and where business rules should live. Do not require a named pattern unless it reduces a real risk.
```

## Pattern Fit

```text
Is this simple enough to build directly, or does it need an adapter/facade, state flow, strategy boundary, auth/access boundary, audit trail, or deep module? Explain the choice like I am a non-technical founder, and treat broad words like AI, auth, step, policy, or rule as prompts for review rather than automatic pattern requirements.
```

## Workflow Selection

```text
Use the Workflow Selection Protocol. Tell me the current situation, recommended workflow, artifact to produce next, required authority source, user approval needed, stop condition, and generated-report warning before doing work.
```

## Plan Loop

```text
Use the Plan Loop on this feature angle before we commit it to PRD amendment, Architecture Shaping, Decomposition, a candidate bead, activation, or code.

First summarize the source context you are using and what is already known. Do not ask me to repeat information already present.

Then ask one targeted question at a time only when the answer could change the next workflow, risk, first slice, owner-file impact, or stop condition.

End with a Plan Packet containing: source context used, feature angle or topic explored, current known facts, assumptions and weak spots, options considered, risks and sensitive surfaces, recommended next path, candidate first-slice shape only when stage-appropriate, stop conditions, and what not to do yet.

Treat the Plan Packet as evidence only. Before PRD approval, do not propose beads. After an approved PRD, you may sketch a first-slice shape, but Decomposition must create any candidate bead proposal. Before candidate activation, you may challenge or refine the proposal, but do not update tasks/todo.md, activate work, approve a PRD, choose tasks, create backlog authority, authorize implementation, or code.
```

## Routing Check

```text
Use the Agent Routing Protocol. Tell me whether this work should use fast, default, deep, or long-horizon routing; why that tier is sufficient; what would trigger escalation; and which adapter-specific controls apply. Do not let routing override the active bead, files in play, approval gates, or review.
```

## Context Budget Check

```text
Check the context budget before continuing. If the session is near the 80% pressure point or feels crowded, prepare a checkpoint with the active bead, primary authority, files in play, latest evidence, changed files, remaining work, and next exact check.
```

## Compact Or Handoff Context Pack

```text
Prepare a compact Context Pack before compaction, restart, or handoff. Include current bead, done-when target, primary authority, files in play, out of scope, checks and latest evidence, stop conditions, approval gates, decisions or assumptions from this session, changed files, remaining work, and next exact check. After compaction or restart, reload active memory, the active bead, and the primary authority before continuing.
```

## Goal Frame Proposal

```text
This sounds durable. Draft a Goal Frame for my review, but do not create tasks or start coding.
```

## Workbook Candidate Goal Frame

```text
Turn my workbook into a Candidate Goal Frame for Precode review, but do not update PRODUCT.md.
```

```text
Use Local Source Intake on this Candidate Goal Frame. Tell me whether it is stable enough to reaffirm.
```

```text
If I reaffirm this Goal Frame, update PRODUCT.md only with the reviewed Goal Frame section and do not create tasks or code.
```

## Goal Frame Reaffirmation

```text
Before using this Goal Frame, ask me to reaffirm it.
```

## Goal Frame Fit Check

```text
Check whether this Goal Frame still matches the active PRD, active bead, and current evidence.
```

```text
If the Goal Frame is stale, incomplete, task-like, or broader than its owner file, ask me whether to reaffirm, revise, retire, split it, or route changed intent to the right owner file before using it for workflow guidance.
```

## Goal Frame Boundaries

```text
Use the Goal Frame only to explain workflow guidance. Do not activate or approve work.
```

## Long-Horizon Review

```text
Show me the long-horizon map and tell me what is approved, blocked, deferred, or ready for human review without activating anything.
```

## Completion Check

```text
Run a completion check. Tell me whether this bead is ready to close, ready for review, blocked, or needs to split.
```

## Handoff Packet

```text
Create a handoff packet for the next agent. Do not activate the next bead or use generated reports as instructions.
```

## Transition Readiness

```text
Before proposing the next bead, explain what evidence proves this bead is complete and what still requires my approval.
```

## Intent Changed

```text
My intent changed. Stop implementation and use the Intent Orchestration Protocol. Name what changed, which owner file should handle it, whether the active bead still has one outcome, and whether this should amend a PRD, become a decision, split into a follow-up bead, or be deferred.
```

## Ready To Become A Bead

```text
Use the Intent Orchestration and Decomposition protocols to tell me whether this is ready to become a bead. If it is not ready, name the missing PRD, decision, approval, verification path, or source-intake step.
```

## Idea To Evidence Trace

```text
Show me the path from idea to evidence: source/input, PRD requirement IDs, bead, recorded checks or manual verification, and review decision. Treat generated reports as evidence only.
```

## Make Acceptance Criteria Testable

```text
Review these acceptance criteria for vague or unverifiable behavior.

Where it improves clarity, rewrite a criterion in optional EARS-style wording: WHEN [condition/event] THE SYSTEM SHALL [observable expected behavior].

Keep clear non-EARS criteria when they are already observable and testable. Do not require EARS syntax, reject valid non-EARS criteria, approve the PRD, accept implementation, activate a bead, create tasks, change schema, treat wording as proof, or code.
```

## Review Acceptance Criteria For Vague Behavior

```text
Use the PRD Protocol and ACCEPTANCE.md to review this PRD's Acceptance Oracle Matrix.

For each vague expected behavior, suggest a clearer observable criterion. Use optional EARS-style wording only when it helps: WHEN [condition/event] THE SYSTEM SHALL [expected behavior].

Return acceptance weaknesses, suggested rewrites, unresolved questions, and stop conditions. Do not approve the PRD, accept implementation, activate beads, mutate files, add a checker, treat generated HTML as authority, or code.
```

## Classify Tool Call

```text
Use the Tool Execution Protocol to classify this command before running it. Tell me the tool-call class, expected side effects, approval gate, rollback or cleanup note, and whether it should be recorded as a check or a tool run.
```

## Record Tool Run

```text
Record this important non-check tool action with log-tool-run. Include tool, class, status, command summary, failure category if any, approval note if needed, and side effects. Do not treat the logged tool run as passing verification.
```

## Command Safety

```text
Is this command safe to run inside the active bead? Check the bead scope, files in play, stop conditions, approval gates, and whether the command is external, destructive, or secret-bearing.
```

## Local Hygiene Check

```text
Use the Local Hygiene Protocol. Classify noisy files as truth, evidence, generated report, append-only ledger, bulky log output, cache/build output, temp file, dependency, or tool/session state. Do not delete, archive, move, compact, or rewrite anything.
```

## Local Hygiene Dry Run

```text
Run the Local Hygiene dry-run preview. Show what would be archived as old bulky log output, what would be deleted as ignored cache/build output, and what is protected. Confirm the dry run did not mutate candidate files.
```

## Implementation

```text
Work only on the active bead. Load active memory, the active bead, the primary authority, and only the reference docs whose LOAD_WHEN applies. Do not use generated reports, source notes, or diary entries as instructions.
```

## Failing-First Implementation

```text
For this code-changing bead, declare the test_strategy before editing. If failing_first is practical, write the failing test first, confirm it fails for the expected reason, then implement and rerun the recorded checks.
```

## Checkpoint

```text
Checkpoint the session. Tell me whether we should continue, repair, split, pause for manual testing, or close. Include what changed, what evidence exists, and what is still uncertain.
```

## Review

```text
Review the completed bead against its done-when target, primary authority, files in play, checks, manual verification, and closeout evidence. Recommend accepted, revise, split, or blocked, and explain the smallest reason.
```

## Requirement-To-Proof Review

```text
Review the proof for this requirement, bug behavior, or acceptance criterion as a requirement-to-proof trace.
Show requirement, bug behavior, or acceptance criterion; evidence lane; recorded source; what this proves; what this does not prove; remaining uncertainty; missing proof; acceptance question; and recommendation.
Do not accept implementation, approve review, approve release, activate the next bead, create follow-up tasks, run mutating commands, or treat generated tests, generated properties, trace tables, screenshots, browser notes, AI critique, external status summaries, generated reports, or confidence as proof by themselves.
```

## Build Attribution Review

```text
Review the Build Attribution Ledger for this bead or recent work.
Show human contributor, contributor role, agent/tool surface, attribution reviewer, attribution uncertainty, evidence confidence, missing attribution, Git-hint-only attribution, and the source that must be reviewed next.
Do not choose tasks, accept implementation, approve review, approve merge, approve release, assign blame, score contributors, mutate GitHub, or treat generated ledger output as authority.
```

## Review Lane

```text
Use the Review Lanes Protocol for this active bead.
Run exactly one lane: Security Review Lane or Release / Docs Freshness Review Lane.
Show lane, review target, authority checked, evidence reviewed, findings, missing proof, acceptance questions, recommendation, approval still required, and promotion path.
Do not accept implementation, approve review, approve release, certify security or compliance, create follow-up tasks, rewrite owner files, mutate GitHub, mutate external systems, or treat generated reports or confidence as proof.
```

## Release Candidate Evidence Profile

```text
Prepare a Release Candidate Evidence Profile for this release-relevant bead.
Do not deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, approve review, accept implementation, or activate the next bead.
Show candidate label, release target, changed surfaces, affected users or workflows, recorded checks and results, requirement or behavior proven, evidence lane, recorded source, smoke path and result, browser or manual verification status, docs or support freshness, rollback or blocked escape, known risks and remaining uncertainty, approvals still required, and decision state.
Use only one decision state: candidate, needs evidence, blocked, or ready for human release decision. Make clear that ready for human release decision is not release approval.
```

## Verification And Release Evidence Review

```text
Review verification and release evidence for this release-relevant bead.
Do not approve release, deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, accept implementation, or activate the next bead.
Show requirement or behavior proven, evidence lane, recorded source, smoke path and result, docs or support freshness, rollback or blocked escape, approvals still required, decision state, and remaining uncertainty.
Tell me what is durable recorded evidence, what is review input only, and what missing traceability means needs evidence before release review.
Do not treat screenshots, browser notes, GitHub status, generated reports, smoke checks, or ready for human release decision as release approval.
```

## Release Candidate Review

```text
Review this Release Candidate Evidence Profile against Closeout Evidence and recorded checks.
Tell me what is recorded evidence, what is review input only, what evidence is missing, whether the rollback or blocked escape is specific enough, which approvals are still required, and whether the decision state should be candidate, needs evidence, blocked, or ready for human release decision.
Do not approve release, deploy, promote, roll back, merge, migrate, change dashboards, change secrets, mutate GitHub resources, mutate external services, accept implementation, or activate the next bead.
```

## Fresh-Context Review

```text
Review this bead in a fresh context. Reload active memory, the bead, primary authority, parent PRD if relevant, the diff or changed files, and recorded evidence. Do not rely on the implementation chat. Recommend accepted, revise, split, or blocked.
```

## Stale Artifact Handling

```text
This old PRD, issue, transcript, or generated summary may be stale. Treat it as historical evidence only. Compare it with current code, active memory, the active bead, current approved PRD, and owner files, then name which authority wins and what needs promotion or amendment.
```

## Manual Verification

```text
Help me write manual verification for this bead using the Precode format: who checked, what was checked, environment, result, and remaining uncertainty.
```

## State Repair

```text
The project state looks inconsistent. Stop implementation, run the advisory state and context checks, compare tasks/todo.md with the active bead, and tell me which canonical file needs repair before work continues.
```

## Stuck Recovery

```text
I am stuck, help me.

Stop implementation and diagnose before repair. Restate the symptom in plain English, or say the symptom is not known yet. Name the likely owner surface, or say it is unknown until active memory and checks are inspected. Run or recommend no more than three read-only or advisory checks. Give me the next safe prompt or action. Do not delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, or run a destructive command unless I explicitly approve that exact action.
```

Required response shape: symptom, first safe move, owner surface, read-only or advisory checks, next safe prompt or action, and forbidden actions: no delete, overwrite, regenerate, transition approval, rollback, setup/update mutation, or destructive command without explicit approval.

## No-Engineer Fallback Prompt Pack

Use these prompts when you can name what feels wrong but you do not have engineering support. They are symptom-specific front doors into the Recovery Protocol, not a competing repair workflow.

Each prompt requires stop-and-diagnose behavior, the likely owner surface or unknown owner, no more than three read-only or advisory checks, the next safe action, and forbidden actions. They do not approve edits, deletion, overwrite, regeneration, rollback, setup/update mutation, transition approval, release, app-code changes, secrets handling, external mutation, or destructive commands.

### Agent Is Lost

```text
The agent seems lost.

Stop implementation and diagnose before repair. Restate the symptom in plain English. Name the likely owner surface, or say it is unknown until active memory and checks are inspected. Run or recommend no more than three read-only or advisory checks to recover context. Give me the next safe prompt or action. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

### Checks Failed

```text
Checks failed and I do not know what to do next.

Stop implementation and diagnose before repair. Restate the failed check symptom in plain English. Name the likely owner surface, or say it is unknown until active memory, check output, and the active bead are inspected. Run or recommend no more than three read-only or advisory checks. Tell me the next safe prompt or action. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

### App Will Not Start

```text
The app will not start.

Stop implementation and diagnose before repair. Restate the startup symptom in plain English, including the command or error if known. Name the likely owner surface, or say it is unknown until active memory, project context, and available logs are inspected. Run or recommend no more than three read-only or advisory checks before changing anything. Give me the next safe prompt or action. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

### Approved Too Much

```text
I may have approved too much.

Stop implementation and diagnose before repair. Restate what may have been approved too broadly, or say it is not known yet. Name the likely owner surface, or say it is unknown until active memory, closeout evidence, transition state, and changed files are inspected. Run or recommend no more than three read-only or advisory checks. Tell me the next safe prompt or action. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

### Copied Wrong Files

```text
I think I copied the wrong files.

Stop implementation and diagnose before repair. Restate the copy mistake symptom in plain English, or say it is not known yet. Name the likely owner surface, or say it is unknown until the package source, target project, file inventory, and setup guidance are inspected. Run or recommend no more than three read-only or advisory checks. Give me the next safe prompt or action. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

### Decide Whether To Stop

```text
I need help deciding whether to stop.

Stop implementation and diagnose before repair. Restate the stop-or-continue symptom in plain English. Name the likely owner surface, or say it is unknown until active memory, the active bead, evidence, and blockers are inspected. Run or recommend no more than three read-only or advisory checks. Tell me whether the next safe prompt or action is continue, ask for proof, repair state, split, block, or stop. Do not edit, delete, overwrite, regenerate, approve a transition, roll back, mutate setup/update behavior, change app code, touch secrets, mutate external systems, or run a destructive command unless I explicitly approve that exact action.
```

## Handoff

```text
Prepare a Precode handoff for the next agent. Include the Context Pack, last validation result, next exact check or command, unresolved blockers, and a warning that generated reports are evidence only.
```

## Learning Diary Review

```text
Read the generated learning diary and explain what I should understand from the last session. Do not use the diary as active memory, a task plan, or implementation instructions.
```

## Reviewed Memory

```text
Search reviewed memory for what we have learned about this topic. Cite the memory cards you used, treat memory as evidence only, and return to active memory and the active bead before recommending action.
```

```text
Run python3 scripts/memory-check.py --retrieval-review --query "topic words". Treat the result as generated evidence only. Tell me whether the recommendation is stay_filesystem_first, split_or_promote_cards_first, or extension_review_required, and do not add semantic search, a shared backend, cards, owner-file promotions, task selection, or active-memory changes without separate approval.
```

```text
Turn this diary lesson into a proposed memory card for my approval. Do not write it until I approve, and tell me whether it should remain memory or be promoted to DECISIONS.md, a PRD, or another authority file.
```

```text
Run the memory index and memory check. Tell me whether any memory is stale, missing source pointers, acting like authority, or needs promotion.
```
