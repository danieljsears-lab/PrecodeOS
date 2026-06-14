# PrecodeOS -- Skill Playbook Protocol
<!-- ANCHOR: skill-playbook-protocol -->

> AUTHORITY: Skill playbook strategy, implemented prompt playbooks, v1 skill candidates, prompt-playbook boundaries, manifest contract, hidden-authority guardrails, candidate backlog, and alternatives for PrecodeOS skill-style surfaces.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command-wrapper behavior, optional pack installation, host-tool plugin registries, generated evidence truth, or implementation acceptance.
> LOAD_WHEN: Designing, reviewing, invoking, or comparing Precode skill-style prompt playbooks for host agents, beginner workflows, maintainer package review, or extension review.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-06-14

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

### Maintainer Package Review Skill

- Purpose: help maintain PrecodeOS as an OS package, not an app runtime.
- Owner sources: `_maintainer/MAINTAINER-NOTES.md`, `_maintainer/PRECODE-ROADMAP.md`, and `tasks/reference/EXTENSION-PROTOCOL.md`.
- Allowed actions: perform static package analysis, identify owner files, compare against package boundaries, and recommend a safe promotion path.
- Forbidden actions: run Precode as an app, publish, deploy, mutate external repository settings, activate beads, or make maintainer files part of public package authority.
- Gain: keeps package health, public/private boundary, roadmap, release-readiness, and maintainer context easier to invoke consistently.

### Skill / Extension Review Skill

- Purpose: evaluate any proposed skill against Precode's extension rules before it becomes a maintained surface.
- Owner source: `tasks/reference/EXTENSION-PROTOCOL.md`.
- Allowed actions: classify the proposed skill, name authority boundaries, mutation rules, generated evidence, validation, and promotion path.
- Forbidden actions: install the skill, add a registry, create optional packs, approve the extension, or edit Precode files without an approved implementation path.
- Gain: prevents skill sprawl and hidden authority before skills become an ecosystem.

### Product Conviction Packet Skill

```text
Name: Product Conviction Packet Skill
Purpose: Help a first-time non-technical builder research, explore, challenge, and package a rough idea before Precode Local Source Intake.
Load when: The user asks for an idea coach, Product Conviction Packet, pre-repo discovery, first-time founder discovery, SnapCamp/bootcamp idea shaping, or a skill-style product-discovery request before PRD creation.
Owner protocol or adapter: `tasks/reference/IDEA-TO-PRD-WORKFLOW.md`, `tasks/reference/PRODUCT-DISCOVERY-VALIDATION-PROTOCOL.md`, and `tasks/reference/LOCAL-SOURCE-INTAKE-PROTOCOL.md`
Allowed actions: Interview one question at a time, produce a Product Brief after at most three high-level product or business questions, guide source-cited research, separate facts from assumptions, challenge broad audience/missing workaround/risky scope/weak evidence supportively, and produce a Conviction Packet plus Local Source Intake handoff prompt.
Forbidden actions: Edit files, write `PRODUCT.md`, draft or approve a PRD, create or activate beads, start implementation, run mutating commands, treat research as validation, promote findings into authority, or decide the product for the builder.
Generated evidence, if any: None in Precode v1; the conversational output is source evidence that the user may later paste or store as local source material.
User approval required before: Any file edit, authority-file update, PRD draft/approval, bead proposal/activation, implementation, external mutation, or sensitive-surface action.
Stop conditions: The idea has no named user problem, no current workaround or evidence, sensitive information is being pasted, the first slice is too large to reason about, evidence is weak enough to require Product Discovery Interview Skill / Product Discovery Validation, or the user is asking to jump directly from raw discovery to coding.
Promotion path for findings: Bring the reviewed Conviction Packet into Local Source Intake; promote only through the PRD, `PRODUCT.md`, `DECISIONS.md`, another owner file, or a candidate/approved bead after user review.
```

When invoked, return a compact `Product Brief` first, then a `Conviction Packet` when the idea is ready. The Conviction Packet should include:

- idea in plain English
- intended user and situation
- painful before moment
- better after moment
- current workaround or evidence
- strongest evidence
- weakest assumption
- guided research notes with source links, dates or recency when available, confidence, and uncertainty
- MVP-ready first slice
- not-yet list
- smallest learning step
- sensitive surfaces
- recommended next Precode path
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
| Maintainer Package Review Skill | P1/P2 | Useful for maintainer leverage and preserving the "Precode as package" frame. |
| Skill / Extension Review Skill | P2 | Controls future growth before skills become an ecosystem. |
| Product Conviction Packet Skill | P2 | Useful for first-time builders and SnapCamp cohorts; keep it prompt-only, evidence-only, and subordinate to Idea-to-PRD, Product Discovery Interview Skill / Product Discovery Validation, and Local Source Intake. |
| Review / Acceptance Skill | P2/P3 | Valuable, but risky if it becomes a fake QA persona instead of evidence-tied review guidance. |
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
