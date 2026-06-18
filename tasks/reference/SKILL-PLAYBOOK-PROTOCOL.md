# PrecodeOS -- Skill Playbook Protocol
<!-- ANCHOR: skill-playbook-protocol -->

> AUTHORITY: Skill playbook strategy, implemented prompt playbooks, v1 skill candidates, prompt-playbook boundaries, manifest contract, hidden-authority guardrails, candidate backlog, and alternatives for PrecodeOS skill-style surfaces.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command-wrapper behavior, optional pack installation, host-tool plugin registries, generated evidence truth, or implementation acceptance.
> LOAD_WHEN: Designing, reviewing, invoking, or comparing Precode skill-style prompt playbooks for host agents, beginner workflows, maintainer package review, or extension review.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.14
Last updated: 2026-06-18

## Purpose

Skill playbooks make PrecodeOS easier to invoke from host AI coding agents without making skills a second operating model.

In v1, a Precode skill is a read-only prompt playbook. It tells the host agent what Precode owner files or protocols to load, what output to return, what approval gates to preserve, and what not to do. It does not add active memory, run mutating commands, approve work, activate beads, or promote generated findings.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Strategic Line

Skills should make Precode easier to invoke, not bigger to trust.

The benefit of skills is adoption and reliability: beginners can ask for a named workflow, and agents get a bounded playbook that says what to load, what to return, and when to stop. The main risk is hidden authority, so every skill playbook must point back to Precode owner files instead of becoming the source of truth.

Use the Context Layer Matrix in `docs/PRECODE-PACKAGE-FILE-INVENTORY.md` when designing or reviewing a skill playbook. A skill playbook is an invocation layer: it may point to active memory, owner protocols, source evidence, generated reports, or maintainer context when allowed, but it must not merge those layers or become an authority source itself.

## Skill Surface Model

| Surface | v1 posture | Why |
|---|---|---|
| Prompt playbook | Adopt | Best fit for beginner invocation, host-agent compatibility, and hidden-authority control. |
| Read-only command wrapper | Defer | Useful for diagnostics later, but it needs stable command boundaries, approval rules, and generated-evidence handling. |
| Mutating command wrapper | Reject for v1 | Too likely to bypass beads, owner files, manual gates, and package trust. |
| Optional pack | Defer | Useful only after the kernel, setup path, manifest, and update boundaries are quieter. |

A prompt playbook may tell an agent to inspect files and summarize. It must not tell an agent to edit files, write generated evidence, approve transitions, run installers, mutate external systems, or treat command output as authority.

## Implemented Prompt Playbooks

### Ask Precode Docs Skill

```text
Name: Ask Precode Docs Skill
Purpose: Help a user ask stable PrecodeOS documentation questions without needing to identify source files.
Load when: The user asks for Ask Precode, asks a stable question about PrecodeOS docs, asks where to find guidance, or asks what a Precode concept means.
Owner protocol or adapter: `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`
Allowed actions: Search `README.md`, `docs/*.md`, and relevant `tasks/reference/*.md`; answer in plain language; cite source files; suggest the next safe prompt or document.
Forbidden actions: Edit files, run commands, inspect current active memory, diagnose current project state, cite `_maintainer/` files, approve PRDs, activate beads, approve transitions, accept review decisions, or treat generated reports as authority.
Generated evidence, if any: None in v1.
User approval required before: Any file edit, command execution, active-state diagnosis, PRD approval, bead activation, transition approval, review acceptance, external mutation, or sensitive-surface action.
Stop conditions: The question depends on current repo state, active memory, active bead status, generated reports, local errors, private maintainer context, missing docs, conflicting docs, or what work should happen next.
Promotion path for findings: Promote documentation gaps only through a reviewed doc/protocol update, `DECISIONS.md`, an authority file, or a candidate/approved bead after user review.
```

When invoked, return exactly these fields:

```text
Short answer:
Sources:
What this does not decide:
Next safe prompt:
```

The user-facing invocation name is `Ask Precode`. The precise contract name is `Ask Precode Docs Skill`.

The output is documentation help only. It does not choose the next task, inspect current state, approve work, rewrite owner files, or start implementation.

### Workflow Selection Skill

```text
Name: Workflow Selection Skill
Purpose: Help a beginner choose the next Precode planning, execution, review, unblocker, repair, or handoff workflow without jumping to code.
Load when: The user asks for Workflow Selection Skill, asks what Precode workflow to use, asks what to do next before work starts, or names a skill-style workflow-selection request.
Owner protocol or adapter: `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`
Allowed actions: Read active memory, load Workflow Selection, inspect only the minimum relevant owner files needed to classify the situation, and return the required workflow-selection fields.
Forbidden actions: Edit files, approve PRDs, activate beads, approve review decisions, start implementation, run mutating commands, install tools, write generated evidence, or treat generated reports as authority.
Generated evidence, if any: None in v1.
User approval required before: Any file edit, PRD approval, bead activation, review acceptance, command execution beyond read-only inspection, external mutation, or sensitive-surface action.
Stop conditions: No active memory can be found, multiple workflows remain equally plausible after minimal inspection, source evidence is missing, product-feature work lacks an approved PRD, verification path is unknown, or generated/source material appears to be acting as authority.
Promotion path for findings: Promote only through the relevant owner protocol, PRD, `DECISIONS.md`, authority file, or candidate/approved bead after user review.
```

When invoked, return exactly these fields:

```text
Current situation:
Recommended workflow:
Artifact to produce next:
Required authority source:
User approval needed:
Run contract needed:
Stop condition:
Generated-report warning:
```

The output is guidance only. It does not approve a PRD, activate a bead, choose the next task, rewrite owner files, or start implementation.

### Small Team Collaboration Lane Skill

```text
Name: Small Team Collaboration Lane Skill
Purpose: Help a 2-5 person team coordinate Precode work on the same product build without weakening one-active-bead, owner-file, evidence, or human approval boundaries.
Load when: The user asks for Small Team Collaboration Lane, says multiple people are working on the same product build, asks how teammates should use Precode together, or needs branch/worktree-isolated parallel bead guidance.
Owner protocol or adapter: `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`
Allowed actions: Read active memory, load the Small Team Collaboration Lane protocol, inspect only the minimum owner files needed to identify current team agreement and active bead context, classify coordinator/product-owner/contributor/reviewer roles, propose branch/worktree rules, identify candidate parallel beads, and return bounded team coordination guidance.
Forbidden actions: Edit files, approve PRDs, activate beads, accept review, approve merge, push, rebase, create branches, create or merge pull requests, mutate GitHub, deploy, run mutating commands, create optional packs, add registries, create a module/runtime toggle, or treat team notes, PRs, branch status, or generated handoff packets as authority.
Generated evidence, if any: None in v1. Conversational output is source evidence until the user promotes accepted team agreement into `PROJECT-CONTEXT.md`, `DECISIONS.md`, a PRD, another owner file, or an approved bead.
User approval required before: Any file edit, authority-file update, bead proposal/activation, branch/worktree mutation, GitHub mutation, merge, review acceptance, transition approval, release action, external mutation, or sensitive-surface action.
Stop conditions: No coordinator or product decision owner is named; team agreement is absent from shared repo authority; multiple active beads are requested in one checkout; a teammate cannot name branch/worktree, bead, authority, files, checks, or stop conditions; GitHub status is being treated as authority; merge/deploy/external mutation is requested without approval; or the work needs conflict review before continuing.
Promotion path for findings: Promote accepted team agreement into `PROJECT-CONTEXT.md`, `DECISIONS.md`, a PRD, an owner file, or candidate/approved beads after user review.
```

When invoked, return exactly these fields:

```text
Team situation:
Coordinator and decision owner:
Branch/worktree rule:
Candidate parallel beads:
Per-teammate startup prompt:
Review and merge evidence:
Approval gates:
Stop conditions:
Promotion path:
Generated-report warning:
```

The output is coordination guidance only. It does not activate team mode automatically for every user, activate multiple beads in one checkout, approve merge, accept work, mutate GitHub, or replace the Small Team Collaboration Lane protocol.

### Product Discovery Interview Skill

```text
Name: Product Discovery Interview Skill
Purpose: Help a user run a worth-building discovery interview before PRD shaping when the user problem, current workaround, evidence, demand signal, or smallest learning step is uncertain.
Load when: The user asks for Product Discovery Interview Skill, asks whether an idea is worth defining, asks for a skill-style product-discovery interview, or has a broad, risky, market-facing, paid, evidence-poor, or solution-first idea where worth-building uncertainty is the main question.
Owner protocol or adapter: `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`
Allowed actions: Interview one question at a time, inspect user-provided idea and evidence, apply the discovery evidence ladder, identify the current workaround, strongest evidence, weakest assumption, demand or pricing signal, sensitive surfaces, smallest non-code learning step, and return the Product Discovery Validation Discovery Summary.
Forbidden actions: Edit files, write `PRODUCT.md`, draft or approve a PRD, create or activate beads, choose tasks, start implementation, run mutating commands, treat research as validation, treat discovery output as proof that the idea is worth building, promote findings into authority, or decide the product for the builder.
Generated evidence, if any: None in Precode v1; the conversational Discovery Summary is source evidence that the user may later paste or store as local source material.
User approval required before: Any file edit, authority-file update, PRD draft/approval, bead proposal/activation, implementation, external mutation, command execution, or sensitive-surface action.
Stop conditions: The user asks to code, asks for a PRD before discovery uncertainty is resolved, needs to paste secrets or sensitive personal data, lacks a named user or current workaround, has evidence too weak for PRD shaping, or needs a broader pre-repo idea-coaching loop instead of a narrow worth-building interview.
Promotion path for findings: Bring the reviewed Discovery Summary into Local Source Intake, Idea-to-PRD, a PRD Discovery Evidence section, `PRODUCT.md`, `DECISIONS.md`, another owner file, or a candidate/approved bead only after user review.
```

When invoked, return exactly the Product Discovery Validation `Discovery Summary` fields:

```text
Discovery Summary:
- Idea:
- Target user and situation:
- User problem:
- Current alternatives or workarounds:
- Strongest evidence:
- Weakest assumption:
- Evidence strength: very weak | weak | medium | strong | strongest
- Assumption categories in play: desirability | viability | feasibility | usability | ethical
- Demand or pricing signal:
- Smallest non-code learning step:
- What would change our mind:
- Sensitive surfaces:
- Recommendation: proceed | pause | narrow | kill
- Reason:
- Recommended next Precode workflow:
- Authority files likely affected:
- Guardrail reminder: discovery is evidence only, not PRD approval, task activation, or permission to code.
```

The output is evidence only. It does not validate demand, approve PRDs, activate beads, choose the next task, rewrite owner files, or start implementation.

### Accessibility Advisor Fit Interview

```text
Name: Accessibility Advisor Fit Interview
Purpose: Help a user decide whether to invoke the Accessibility Advisor for a specific bead, review, or release candidate before accessibility evidence becomes part of acceptance risk.
Load when: The user asks whether accessibility review is needed, a bead or owner file explicitly mentions accessibility review, a release/review decision depends on accessibility confidence, or Workflow Selection routes uncertainty here.
Owner protocol or adapter: `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`, `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`, and `tasks/reference/RELEASE-READINESS-PROTOCOL.md` when release-relevant.
Allowed actions: Interview one question at a time, inspect only the current bead, owner-file requirement, release-candidate profile, or user-supplied context needed to decide fit, and return an invocation recommendation plus target, evidence, manual review, unresolved risk, and stop condition.
Forbidden actions: Edit files, accept implementation, approve a review decision, approve release, claim legal compliance, certify WCAG/ADA conformance, run background audits, make accessibility review mandatory for every UI bead, create follow-up tasks, activate beads, run mutating commands, or mutate external systems.
Generated evidence, if any: None in v1. The conversational fit interview is advisory review input until the user invokes the advisor and records the resulting accessibility advisory in Closeout Evidence, a release-candidate profile, an owner file, or another reviewed artifact.
User approval required before: Any file edit, acceptance decision, release action, external mutation, follow-up bead creation, owner-file update, command execution beyond read-only inspection, or adding accessibility advisory fields to closeout/release evidence.
Stop conditions: The target feature or user-facing surface is unclear; the user expects legal compliance advice; evidence would require credentials, sensitive data, external mutation, or undisclosed users; the review target is broader than one bead or release candidate; or the user asks the advisor to accept, release, or certify the work.
Promotion path for findings: If invoked, record the advisor output in Closeout Evidence, Release Candidate Evidence Profile, the relevant owner file, a candidate/approved follow-up bead, or reviewed memory only after user review.
```

When invoked, ask one question at a time until the recommendation is clear, then return exactly these fields:

```text
Recommendation: invoke advisor | not needed | defer
Reason:
Accessibility target:
Evidence needed:
Manual review needed:
Unresolved risk:
Stop condition:
```

The output is a fit recommendation only. It does not require accessibility review for all UI/interface work, prove accessibility, accept implementation, approve release, or replace human judgment.

### Review / Acceptance Skill

```text
Name: Review / Acceptance Skill
Purpose: Help a user review whether one active bead is ready for an evidence-based acceptance decision.
Load when: The user asks for Review / Acceptance Skill, asks whether a bead is ready to accept, asks for an evidence-tied review recommendation, or needs to distinguish confidence, review input, missing proof, and acceptance blockers after closeout.
Owner protocol or adapter: `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`, `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`, and `modes/REVIEW.md`
Allowed actions: Read active memory, the active bead, the primary authority file, closeout evidence, recorded checks, manual verification notes, relevant run contract, accessibility advisory output when invoked, release-readiness note when present, and a changed-file or diff summary; compare evidence to the bead and authority; return acceptance questions, missing proof, risks, and a review recommendation.
Forbidden actions: Edit files, approve PRDs, accept implementation, approve review decisions, activate beads, approve transitions, create follow-up tasks, start implementation, deploy, release, mutate external systems, run mutating commands, treat generated reports as authority, or treat confidence as proof.
Generated evidence, if any: None in v1. The conversational recommendation is review input only until the user records or acts on it through normal closeout, owner-file, PRD, bead, or transition paths.
User approval required before: Any file edit, review acceptance, PRD approval, bead activation, transition approval, follow-up bead creation, release action, external mutation, sensitive-surface action, or command execution beyond read-only inspection.
Stop conditions: Active memory or the active bead is missing; the primary authority is unclear; recorded checks are missing or stale; manual verification is missing when required; invoked accessibility advisory evidence is incomplete; closeout evidence is incomplete; a sensitive-surface, release, deploy, rollback, or external-service approval gate is unresolved; the diff cannot be inspected; or the work appears broader than one bead.
Promotion path for findings: Promote accepted lessons, follow-ups, or defects only through Closeout Evidence, `DECISIONS.md`, the owning PRD or authority file, a candidate/approved bead, release-readiness evidence, or reviewed memory after user review.
```

When invoked, return exactly these fields:

```text
Review target:
Authority checked:
Evidence reviewed:
Missing proof:
Acceptance questions:
Risks or drift:
Recommendation: accepted | revise | split | blocked | stop
Approval still required:
Follow-up or promotion path:
```

The output is a review recommendation only. It does not accept implementation, approve the review decision, activate the next bead, create follow-up tasks, approve release, or replace recorded checks and manual verification.

### Requirements Gap And Conflict Review Skill

```text
Name: Requirements Gap And Conflict Review Skill
Purpose: Help a user inspect a PRD, spec, design note, or requirement set for ambiguity, conflicts, missing edge cases, unstated assumptions, and weak acceptance before approval or implementation.
Load when: The user asks for Requirements Gap And Conflict Review, asks whether requirements are clear enough to approve, asks for PRD/spec conflict review, or needs to catch requirement drift before bead derivation, design promotion, or implementation.
Owner protocol or adapter: `tasks/reference/PRD-PROTOCOL.md`, `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`, and `modes/REVIEW.md`
Allowed actions: Read the supplied PRD/spec/source, load only the owner files needed to understand authority, compare the requirement set against PRD approval and verification expectations, identify gaps, conflicts, missing edge cases, unstated assumptions, acceptance weaknesses, and owner-file follow-ups, and return advisory questions and suggested fixes.
Forbidden actions: Edit files, approve PRDs, approve design promotion, activate beads, create tasks, start implementation, rewrite owner files, accept implementation, run mutating commands, treat review output as proof, or convert findings into implementation instructions.
Generated evidence, if any: None in v1. The conversational review is review input only until the user promotes accepted fixes through the PRD, owner file, decision, review bead, candidate bead, or normal approval path.
User approval required before: Any file edit, PRD approval, owner-file update, bead proposal/activation, implementation, review acceptance, external mutation, sensitive-surface action, or command execution beyond read-only inspection.
Stop conditions: The review target is missing; authority files are unclear; source inputs conflict in a way that changes implementation; requirement IDs or acceptance oracles are absent for approval-bound work; sensitive-surface decisions are unresolved; or the user asks the skill to approve, rewrite, activate, or implement.
Promotion path for findings: Promote accepted findings only through PRD amendment, `DECISIONS.md`, the relevant owner file, Architecture Shaping, Review mode, a candidate/approved bead, or reviewed memory after user review.
```

When invoked, return exactly these fields:

```text
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
```

The output is advisory review input only. It does not approve the PRD, accept design promotion, create implementation instructions, activate work, or replace human approval.

### Maintainer Package Review Skill

```text
Name: Maintainer Package Review Skill
Purpose: Help Dan maintain PrecodeOS as an OS package without treating the package as an app runtime or turning private maintainer context into public authority.
Load when: Dan asks to maintain, review, roadmap-plan, boundary-check, design, or assess changes to the PrecodeOS package itself, especially when the question involves public/private boundaries, skill playbooks, extension review, roadmap fit, maintainer changelog impact, protocol impact, public reference-document impact, release-readiness posture, or package-health analysis.
Owner protocol or adapter: `_maintainer/MAINTAINER-NOTES.md`, `_maintainer/PRECODE-ROADMAP.md`, `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`, and `tasks/reference/EXTENSION-PROTOCOL.md`
Allowed actions: Read `_maintainer/MAINTAINER-NOTES.md` first, then load only the maintainer roadmap, strategy, public package, protocol, reference, changelog, inventory, or boundary files relevant to the package-maintenance question; perform static package, roadmap, boundary, protocol-impact, reference-document, changelog-impact, and extension analysis; identify owner files, promotion path, validation path, and safe implementation scope; and return a bounded maintainer plan.
Forbidden actions: Read normal active memory for this skill, run Precode as an app, launch app runtimes, edit files during planning, write generated evidence, activate beads, approve PRDs, approve transitions, approve review decisions, publish, deploy, install, update, mutate external systems, add command-wrapper behavior, add registries, create optional packs, or make maintainer files part of public package authority.
Generated evidence, if any: None in v1. Conversational output is maintainer planning input only until Dan promotes accepted findings through the relevant public owner file, maintainer roadmap, changelog, protocol, reference document, PRD, decision, or approved bead.
User approval required before: Any file edit, public package change, maintainer changelog update, roadmap update, protocol/reference update, generated-evidence write, PRD approval, bead proposal/activation, transition approval, review acceptance, command execution beyond read-only inspection, external mutation, publication, deployment, installation, update behavior, registry behavior, optional-pack behavior, or sensitive-surface action.
Stop conditions: The goal is ambiguous enough that package surface, owner files, or done criteria cannot be named; the request would treat PrecodeOS as an app runtime; public/private authority boundaries are unclear; maintainer-private material would become public authority; normal active memory would be loaded as maintainer context; implementation would skip required changelog, protocol, or reference-document follow-through; or the proposal implies installer, update-channel, package-manager, registry, optional-pack, command-wrapper, external-mutation, release, or deployment behavior without a separate approved package change.
Promotion path for findings: Promote accepted findings only through `_maintainer/PRECODE-ROADMAP.md`, `_maintainer/CHANGELOG.md`, the relevant public protocol or reference document, a PRD, `DECISIONS.md`, another public authority file, or a candidate/approved bead after Dan review.
```

When invoked, use Plan Mode or an equivalent read-only planning posture when the host supports it. Return exactly these fields:

```text
Title:
Summary:
Relevant context and owner files:
Proposed package or roadmap change:
Public/private boundary notes:
Risks and challenged assumptions:
Maintainer changelog impact:
Protocol impact:
Public reference-document impact:
Validation plan:
Explicit assumptions:
```

The output is maintainer planning input only. It does not implement changes, approve work, activate beads, publish package state, or make private maintainer context public package authority.

### Skill / Extension Review Skill

```text
Name: Skill / Extension Review Skill
Purpose: Help review a proposed Precode skill or extension against extension rules before it becomes a maintained surface.
Load when: The user asks for Skill / Extension Review Skill, asks whether a proposed Precode skill, adapter, protocol, importer, audit, generated report, bead template, role contract, or external integration is safe to add, or asks for extension-review help before implementation.
Owner protocol or adapter: `tasks/reference/EXTENSION-PROTOCOL.md`, `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`, and the proposed skill or extension material supplied by the user.
Allowed actions: Read the proposed skill or extension material, classify the extension type, identify the owner protocol or adapter, name authority boundaries, mutation rules, generated evidence, approval gates, validation command, promotion path, rollback or removal note, and hidden-authority risks, and return an advisory review recommendation.
Forbidden actions: Edit files, install skills, approve extensions, approve PRDs, activate beads, approve review decisions, run mutating commands, mutate external systems, add a registry, create optional packs, promote generated findings, bypass owner protocols, or treat the review output as package authority.
Generated evidence, if any: None in v1. The conversational review is advisory input only until the user promotes accepted findings through the owning protocol, adapter, PRD, decision, authority file, or approved bead.
User approval required before: Any file edit, extension addition, skill installation, protocol or adapter update, PRD approval, bead activation, command execution beyond read-only inspection, generated-evidence write, external mutation, registry or optional-pack behavior, or sensitive-surface action.
Stop conditions: The proposed capability lacks a clear owner protocol or adapter; active memory would expand; generated output would become authority; mutation or external-system behavior is unclear; user approval gates are missing; secrets or privacy handling is unspecified; validation cannot be named; rollback or removal is unclear; or the proposal implies installer, registry, optional-pack, marketplace, CLI, package-manager, or command-wrapper behavior without a separate approved extension.
Promotion path for findings: Promote accepted findings only through `tasks/reference/EXTENSION-PROTOCOL.md`, the relevant owner protocol or adapter, a PRD, `DECISIONS.md`, another authority file, or a candidate/approved bead after user review.
```

When invoked, return exactly these fields:

```text
Review target:
Extension type:
Owner source:
Authority boundaries:
Mutation and external-system risk:
Generated evidence:
Approval gates:
Validation needed:
Promotion path:
Rollback or removal note:
Risks:
Recommendation: accept-shape | revise | split | defer | reject
Stop condition:
```

The output is an extension-shape review only. It does not approve the extension, install a skill, edit files, add a registry, create optional packs, run commands, mutate external systems, or replace the Extension Protocol.

## V1 Skill Set

### Ask Precode Docs Skill

- Purpose: help a user ask stable PrecodeOS documentation questions without knowing which files to search.
- Owner source: `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`.
- Allowed actions: search `README.md`, `docs/*.md`, and relevant `tasks/reference/*.md`; answer in plain language; cite source files; and suggest the next safe prompt or document.
- Forbidden actions: edit files, run commands, inspect active memory, diagnose current repo state, cite `_maintainer/`, approve work, activate beads, approve transitions, or treat generated reports as authority.
- Gain: gives beginners a simple docs-help affordance while keeping Markdown docs and protocols canonical.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Workflow Selection Skill

- Purpose: help a beginner choose discovery, intake, PRD, bead, review, repair, or handoff without jumping to code.
- Owner source: `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`.
- Allowed actions: read active memory, load Workflow Selection, inspect the minimum relevant owner files, and return the required workflow-selection fields.
- Forbidden actions: edit files, approve PRDs, activate beads, start implementation, run mutating commands, or treat generated reports as task authority.
- Gain: reduces "what do I ask next?" friction and protects against premature implementation.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Product Discovery Interview Skill

- Purpose: help a user run a narrow worth-building interview before PRD shaping when evidence, current workaround, demand signal, or smallest learning step is uncertain.
- Owner source: `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`.
- Allowed actions: interview one question at a time, apply Product Discovery Validation, and return the Discovery Summary with evidence strength and `proceed | pause | narrow | kill`.
- Forbidden actions: edit files, approve PRDs, create or activate beads, choose tasks, start implementation, or treat discovery output as validation/proof.
- Gain: makes the Product Discovery Validation protocol easier to invoke without duplicating the broader Product Conviction Packet idea-coaching path.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Small Team Collaboration Lane Skill

- Purpose: help a 2-5 person founder-led or peer builder team coordinate Precode work through explicit team agreement, branch/worktree isolation, contributor evidence, coordinator review, and merge/re-entry gates.
- Owner source: `tasks/reference/TEAM-COLLABORATION-PROTOCOL.md`.
- Allowed actions: read active memory and the team protocol, inspect the minimum owner files needed to identify team agreement and active bead context, and return team coordination fields.
- Forbidden actions: edit files, approve PRDs, activate beads, accept implementation, merge, mutate GitHub, deploy, create optional packs, add registries, create modules, or treat teammate notes, PRs, branch status, or generated handoff packets as authority.
- Gain: gives teams one explicit invocation path while preserving single-builder defaults and one active bead per checkout.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Review / Acceptance Skill

- Purpose: help a user decide whether one active bead is ready for an evidence-based acceptance decision.
- Owner sources: `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md`, `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md`, `modes/REVIEW.md`, the active bead, primary authority, closeout evidence, recorded checks, manual verification, and diff or changed-file evidence.
- Allowed actions: read the review evidence, compare it to the bead and authority, identify missing proof and risks, and recommend `accepted`, `revise`, `split`, `blocked`, or `stop`.
- Forbidden actions: accept implementation, approve review decisions, activate beads, create follow-up tasks, approve releases, run mutating commands, or treat generated reports or confidence as proof.
- Gain: reduces false-done drift at the review boundary while keeping human acceptance and transition approval intact.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Maintainer Package Review Skill

- Purpose: help maintain PrecodeOS as an OS package, not an app runtime.
- Owner sources: `_maintainer/MAINTAINER-NOTES.md`, `_maintainer/PRECODE-ROADMAP.md`, `tasks/reference/SKILL-PLAYBOOK-PROTOCOL.md`, `tasks/reference/EXTENSION-PROTOCOL.md`, and only the package references relevant to the maintainer question.
- Allowed actions: read maintainer notes first, inspect relevant package/roadmap/protocol/reference/changelog surfaces, identify owner files and boundary risks, and return a bounded maintainer plan.
- Forbidden actions: read normal active memory for this skill, run Precode as an app, edit files during planning, write generated evidence, publish, deploy, install, update, mutate external systems, activate beads, approve PRDs/transitions/reviews, add wrappers/registries/optional packs, or make maintainer files public package authority.
- Gain: keeps package health, public/private boundary, roadmap, release-readiness, and maintainer context easier to invoke consistently.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Skill / Extension Review Skill

- Purpose: evaluate any proposed skill against Precode's extension rules before it becomes a maintained surface.
- Owner sources: `tasks/reference/EXTENSION-PROTOCOL.md`, this protocol, and the proposed skill or extension material supplied by the user.
- Allowed actions: classify the proposed extension type, name the owner source, authority boundaries, mutation and external-system risk, generated evidence, approval gates, validation needed, promotion path, rollback or removal note, and hidden-authority risks.
- Forbidden actions: install skills, approve extensions, edit files from review output, add registries, create optional packs, run mutating commands, mutate external systems, promote generated findings, or bypass owner protocols.
- Gain: prevents skill sprawl and hidden authority before skills become an ecosystem.
- Status: implemented as a read-only prompt playbook in this protocol and `tasks/reference/PROMPT-PATTERNS.md`.

### Product Conviction Packet Skill

```text
Name: Product Conviction Packet Skill
Purpose: Help a first-time non-technical builder run a guided product-coach interview that researches, explores, challenges, clarifies, and packages a rough idea before Precode Local Source Intake.
Load when: The user asks for an idea coach, Product Conviction Packet, pre-repo discovery, first-time founder discovery, SnapCamp/bootcamp idea shaping, or a skill-style product-discovery request before PRD creation.
Owner protocol or adapter: `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`, `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`, and `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
Allowed actions: Interview one question at a time, help the builder choose the closest lens without creating a separate workflow, produce a Product Brief after at most three high-level product or business questions, guide source-cited research, separate facts from assumptions, run a Challenge And Clarity pass, challenge broad audience/missing workaround/risky scope/weak evidence supportively but firmly, rate evidence strength, optionally use visible-iteration/MVE framing to name the smallest complete useful payoff and core workflow spine, translate possible features into candidate capabilities, classify Local Source Intake readiness, and produce a Conviction Packet plus Local Source Intake handoff prompt.
Forbidden actions: Edit files, write `PRODUCT.md`, draft or approve a PRD, create or activate beads, create a roadmap or backlog, start implementation, run mutating commands, treat research as validation, promote findings into authority, or decide the product for the builder.
Generated evidence, if any: None in Precode v1; the conversational output is source evidence that the user may later paste or store as local source material.
User approval required before: Any file edit, authority-file update, PRD draft/approval, bead proposal/activation, implementation, external mutation, or sensitive-surface action.
Stop conditions: The idea has no named user problem, no current workaround or evidence, sensitive information is being pasted, the first slice is too large to reason about, evidence is weak enough to require Product Discovery Interview Skill / Product Discovery Validation, or the user is asking to jump directly from raw discovery to coding.
Promotion path for findings: Bring the reviewed Conviction Packet into Local Source Intake; promote only through the PRD, `PRODUCT.md`, `DECISIONS.md`, another owner file, or a candidate/approved bead after user review.
```

When invoked, run as a guided interview inside Claude Code or an equivalent agent surface. Use Claude Code Plan Mode or an equivalent planning mode when available. Return a compact `Product Brief` first, then run Challenge And Clarity, Evidence And Assumption Check, optional Learning/MVE Framing, Candidate Capability Matrix, and a `Conviction Packet` when the idea is ready. The Conviction Packet should include:

- idea in plain English
- builder lens when useful
- intended user and situation
- painful before moment
- better after moment
- current workaround or evidence
- evidence strength: very weak | weak | medium | strong | strongest
- strongest evidence
- weakest assumption
- what would change our mind
- guided research notes with source links, dates or recency when available, confidence, and uncertainty
- optional visible iteration, core workflow spine, and smallest complete useful payoff when those clarified the idea
- MVP-ready first slice
- not-yet list
- smallest learning step
- sensitive surfaces
- recommended next Precode path
- Local Source Intake readiness
- Local Source Intake handoff prompt

## Manifest Contract

Every proposed Precode skill playbook should declare:

```text
Name:
Purpose:
Load when:
Owner protocol or adapter:
Allowed actions:
Forbidden actions:
Generated evidence, if any:
User approval required before:
Stop conditions:
Promotion path for findings:
```

If any field is unclear, the skill is not ready to become a maintained Precode surface.

## Guardrails

- Do not add a fourth active-memory file.
- Do not make skill files authoritative over their owner protocols.
- Do not let a skill choose tasks, approve PRDs, activate beads, approve review decisions, or promote findings.
- Do not make generated skill output an instruction source.
- Do not let a host tool's skill registry become the Precode package registry.
- Do not hide command execution inside skill instructions.
- Do not use skill playbooks to bypass `tasks/reference/EXTENSION-PROTOCOL.md`.
- Keep tool-specific installation notes in adapters or host-specific packaging docs, not in the shared kernel.

## Candidate Backlog

| Candidate | Priority | Recommendation |
|---|---:|---|
| Ask Precode Docs Skill | Implemented | User-facing docs-help prompt; keep it stable-documentation-only and cite canonical docs/protocols. |
| Workflow Selection Skill | Implemented | First v1 skill playbook; keep it prompt-only and subordinate to Workflow Selection. |
| Product Discovery Interview Skill | Implemented | Worth-building interview prompt; keep it evidence-only and subordinate to Product Discovery Validation. |
| Small Team Collaboration Lane Skill | Implemented | Team coordination prompt; keep it read-only, explicit, branch/worktree-isolated, and subordinate to the Small Team Collaboration Lane protocol. |
| Review / Acceptance Skill | Implemented | Evidence-tied bead acceptance review prompt; keep it recommendation-only and subordinate to closeout, verification, and Review mode. |
| Accessibility Advisor Fit Interview | Implemented | Opt-in interview for deciding whether accessibility advisory review is needed; keep it advisory-only and avoid compliance or default-UI gate behavior. |
| Requirements Gap And Conflict Review Skill | Implemented | Pre-approval requirements/spec review prompt; keep it advisory-only and subordinate to PRD Protocol, Verification Guardrail, and Review mode. |
| Maintainer Package Review Skill | Implemented | Maintainer package-analysis prompt; keep it read-only, Plan Mode-oriented when available, and subordinate to maintainer notes, roadmap authority, Skill Playbook Protocol, and Extension Protocol. |
| Skill / Extension Review Skill | Implemented | Extension-shape review prompt; keep it advisory-only and subordinate to the Extension Protocol. |
| No-Engineer Fallback Prompt Pack | Implemented outside skill set | Implemented as Prompt Patterns and user/support docs, not a skill playbook; keep it subordinate to Recovery Protocol and approval gates. |
| Product Conviction Packet Skill | P2 | Useful for first-time builders and SnapCamp cohorts; keep it prompt-only, evidence-only, and subordinate to Idea-to-PRD, Product Discovery Interview Skill / Product Discovery Validation, and Local Source Intake. |
| Release Readiness Skill | P3 | Better after release-readiness, manifest, and package-health lanes mature. |

## Better Alternatives

Use a protocol doc when behavior is core Precode workflow authority.

Use a script or check when repeatable validation matters more than host-agent style.

Use an adapter when behavior is tool-specific.

Use docs or prompt patterns when the main need is teaching, onboarding, or copyable user language.

Use optional packs only after the kernel, setup path, install/update manifest, and package-health boundaries are stable enough that extension packaging will clarify rather than compete.

## Review Questions

Before accepting a skill playbook, ask:

- What existing owner file already owns this behavior?
- Does the skill reduce invocation friction without expanding authority?
- Could the same gain come from a protocol, prompt pattern, adapter note, or script?
- What would a beginner think this skill is allowed to do?
- What must the skill explicitly refuse to do?
- What output is evidence only?
- What user approval gate remains intact?
