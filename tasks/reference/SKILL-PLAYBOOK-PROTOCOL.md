# PrecodeOS -- Skill Playbook Protocol
<!-- ANCHOR: skill-playbook-protocol -->

> AUTHORITY: Skill playbook strategy, v1 skill candidates, prompt-playbook boundaries, manifest contract, hidden-authority guardrails, candidate backlog, and alternatives for PrecodeOS skill-style surfaces.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, command-wrapper behavior, optional pack installation, host-tool plugin registries, generated evidence truth, or implementation acceptance.
> LOAD_WHEN: Designing, reviewing, invoking, or comparing Precode skill-style prompt playbooks for host agents, beginner workflows, maintainer package review, or extension review.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-06-06

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

## V1 Skill Set

### Workflow Selection Skill

- Purpose: help a beginner choose discovery, intake, PRD, bead, review, repair, or handoff without jumping to code.
- Owner source: `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md`.
- Allowed actions: read active memory, load Workflow Selection, inspect the minimum relevant owner files, and return the required workflow-selection fields.
- Forbidden actions: edit files, approve PRDs, activate beads, start implementation, run mutating commands, or treat generated reports as task authority.
- Gain: reduces "what do I ask next?" friction and protects against premature implementation.

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
| Workflow Selection Skill | P1 | First v1 candidate because it has the highest beginner value and turns next-step discipline into an easier invocation path. |
| Maintainer Package Review Skill | P1/P2 | Useful for maintainer leverage and preserving the "Precode as package" frame. |
| Skill / Extension Review Skill | P2 | Controls future growth before skills become an ecosystem. |
| Product Discovery Interview Skill | P2 | Useful for cohorts, but already covered by docs and protocols; add after workflow selection proves the pattern. |
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
