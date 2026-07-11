# PrecodeOS -- Engineering Quality Standards Protocol
<!-- ANCHOR: engineering-quality-standards-protocol -->

> AUTHORITY: Lightweight pre-coding engineering quality floor, beginner-readable standards taxonomy, proportional risk routing, agent explanation contract, human approval questions, and stop conditions before implementation.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, production readiness certification, security certification, compliance approval, generated proof, code-quality scoring, external engineering framework authority, lint replacement, release approval, or a required stage for every bead.
> LOAD_WHEN: A user asks what engineering quality standard or standards taxonomy applies before coding, an active bead is about to move into implementation, or a simple implementation request may hide architecture, security, data, dependency, deployment, or multi-system risk.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-07-11

## Purpose

Engineering Quality Standards give a non-technical builder one plain way to check whether the agent is applying appropriate engineering judgment before code changes begin:

```text
Before coding, show me the engineering quality standard you are applying here.
```

This protocol is a thin quality floor, not a new required stage for every bead. It should reduce blind delegation without making routine work feel like an architecture review.

Use the smallest explanation that controls the risk. For simple work, one short quality-floor statement is enough. For riskier work, the agent should route to the existing owner protocol instead of expanding this protocol into a larger process.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Quality Floor

Before coding, the agent should briefly answer:

- What quality risk does this task have?
- What is the simplest acceptable implementation shape?
- What boundary or owner file matters, if any?
- What evidence will prove the work?
- What should stop or require human approval?

The answer should be short enough for a beginner to approve, challenge, or redirect. Avoid pattern names, architecture labels, and production claims unless they clarify a real risk.

## Proportional Use

| Work shape | Expected response | Continue when |
|---|---|---|
| Low-risk work, such as copy, styling, docs wording, or one local interaction | One short quality-floor statement naming scope, simplest change, and proof. | The active bead is clear, files in play are narrow, no sensitive surface appears, and a relevant check or manual verification is named. |
| Medium-risk work, such as meaningful logic, a shared component, a small API change, or behavior crossing a few files | Compact quality check naming scope, simplicity, boundary, proof, and stop conditions. | The boundary and proof path are clear enough to implement inside the active bead. |
| High-risk work, such as auth, private data, payments, uploads, migrations, new dependencies, deployment, external services, state workflows, or multi-system changes | Stop and route to the relevant owner protocol. | The risk has been shaped through the owner protocol, required approvals are explicit, and the active bead still has one bounded outcome. |

Do not turn every implementation into a long checklist. If the user asks for this prompt during a tiny task, answer briefly and continue inside the active bead.

## Routing

Route to existing protocols when the quality-floor answer reveals higher risk:

| Risk revealed | Route to |
|---|---|
| Auth, data, API, integration, dependency, migration, workflow, or multi-system risk needs pre-bead shaping | `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` |
| Implementation shape, business-rule location, provider boundary, state flow, strategy boundary, audit trail, auth/access boundary, or deep module needs explanation | `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` |
| Proof quality, test strategy, manual verification, sensitive-surface gate, rollback, or false-done risk is unclear | `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` |
| Command risk, destructive action, external mutation, secrets, provider dashboards, or approval-sensitive tool use appears | `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` |
| Work is nearly done and needs a named advisory review lens | `tasks/reference/REVIEW-LANES-PROTOCOL.md`; use Engineering Quality Review Lane when the narrow question is whether completed work respected this quality floor. |
| User-facing shipping, deployment, rollback, smoke evidence, or docs freshness risk appears | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` |

This protocol should point to those owner protocols. It should not duplicate them.

## Standards Taxonomy

The Engineering Quality Standards Taxonomy translates professional engineering standards into Precode-native routing questions. Use it when the quality-floor answer feels vague, when a user asks which standard applies, or when an agent names a professional concept without showing the owner surface or proof path.

This taxonomy is teaching and routing guidance. It is not a checklist required for every bead, a scorecard, a production-readiness certification, a code-quality certification, or public package authority for external frameworks.

| Plain standard concept | Beginner question | Precode route |
|---|---|---|
| Small, bounded change | Is this the simplest change that satisfies the active bead and proof path? | Continue with the Engineering Quality floor when scope, files, proof, and stop conditions are clear. |
| Clear ownership and boundaries | Where should the behavior, durable fact, state change, provider call, or business rule live? | Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` when implementation shape or owner boundary needs explanation. |
| Configuration and environment discipline | Are secrets, config, dashboard values, dependencies, or environment assumptions being hard-coded or changed without an owner? | Use `tasks/reference/ARCHITECTURE-SHAPING-PROTOCOL.md` for dependency, integration, migration, API, data, or multi-system shaping; use `tasks/reference/TOOL-EXECUTION-PROTOCOL.md` for secrets, command risk, dashboards, or external mutation. |
| Reviewable proof | What check, test, manual verification, or evidence will prove this specific change without pretending it proves more? | Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` when proof quality, test strategy, rollback, or false-done risk is unclear. |
| Review discipline | Is the work complete enough for a named advisory review lens, and what approval is still human? | Use `tasks/reference/REVIEW-LANES-PROTOCOL.md`; use Engineering Quality Review Lane only when the narrow question is whether completed work respected this floor. |
| Release and deployment caution | Is this about user-facing shipping, deployment, rollback, smoke evidence, docs freshness, or external status? | Use `tasks/reference/RELEASE-READINESS-PROTOCOL.md`; do not turn the pre-coding quality floor into release approval. |
| Maintainable code shape | Is the agent using names, structure, and local patterns that a future maintainer can read without importing a new architecture? | Continue with the Engineering Quality floor for low-risk work; route to System Design Pattern or Architecture Shaping when the shape affects shared modules, APIs, state, data, dependencies, or multiple systems. |

External ideas such as Twelve-Factor, SOLID, Clean Code, review discipline, CI, deployability, configuration, dependencies, boundaries, proof, and release readiness may be named only as educational source concepts translated into these Precode routing questions. They do not replace the owner protocols, project tests, linters, code review, release readiness, human approval, or the active bead.

## Output Contract

Use this shape when the user asks for the engineering quality standard:

```text
Engineering quality floor:
- Quality risk: low | medium | high
- Standard I am applying:
- Simplest acceptable shape:
- Boundary or owner file:
- Evidence to prove it:
- Stop or approval trigger:
- Routing: continue | use Architecture Shaping | use System Design Pattern | use Verification Guardrail | use Tool Execution | use Review Lanes | use Release Readiness
```

For low-risk work, keep each line short. For high-risk work, stop after naming the route and do not start implementation until the relevant owner protocol has been satisfied.

## Advisory Text-Contract Check

`python3 scripts/engineering-quality-check.py --check` runs the Engineering Quality Text-Contract Checker. It is optional advisory validation of the quality-floor text contract, not a gate.

The checker looks for quality-risk, simplest-shape, boundary, proof, stop-condition, and routing signals in Precode artifact text. It also checks for forbidden certification, scorecard, and checker-gate wording. It may inspect the active bead's declared primary authority, files in play, checks, and Stop If section so missing proof or stop-condition signals are visible before coding.

The checker is advisory only. It does not inspect app code, run linters, run tests, approve implementation, activate beads, accept review, create proof, certify production readiness, certify security or compliance, score code quality, create a checker gate, or replace human approval. It does not approve implementation and does not create a scorecard.

`python3 scripts/engineering-quality-check.py --check --repo-heuristics-preview` adds the Engineering Quality Repo Heuristics Preview. Use it only when changed-file repo-shape risk may contradict the quality-floor answer. The preview compares read-only git changed-file summaries with the active bead's primary authority, files in play, checks, and Stop If section. It may warn about undeclared changed files, broad cross-surface edits, dependency or config touches, docs/protocol/PRD touches, script touches, missing matching checks, or generated-evidence gaps.

Repo heuristics preview is repo-shape risk only. If git metadata is unavailable, the output must say that explicitly and continue with declared Precode artifact signals only. The preview does not inspect app code deeply, parse ASTs, run linters, run tests, approve implementation, accept review, certify production readiness, score code quality, create proof, create a checker gate, replace Review Lanes, replace Release Readiness, or make warnings block ordinary low-risk work.

For post-implementation review, use Engineering Quality Review Lane in the Review Lanes Protocol. That lane is owned by `tasks/prds/PRD-038-engineering-quality-review-lane.md` and reviews whether completed or nearly completed work respected this floor. It is advisory review input only; it does not accept implementation, approve review, certify code quality, certify production readiness, create follow-up tasks, replace tests or linters, inspect app code, add repo heuristics, add language-aware analysis, or expand this protocol into a full standards taxonomy. It does not add repo heuristics and does not add language-aware analysis.

The Standards Taxonomy is now implemented as beginner-readable teaching and routing guidance in this protocol. The checker may validate that public package text preserves the taxonomy contract, but it does not validate application code against external frameworks, create a scorecard, approve implementation, approve review, approve release, certify production readiness, or certify code quality.

## Standards In Plain English

Use these as prompts for judgment, not as a broad checklist:

- Keep the change inside the active bead and files in play.
- Prefer the simplest shape that can satisfy the requirement and proof path.
- Keep business rules, provider calls, state transitions, auth checks, and durable facts in clear owner boundaries.
- Keep configuration, secrets, dashboard values, and environment assumptions out of code unless the owner file and active bead explicitly allow the change.
- Prove behavior with the narrowest useful recorded check or structured manual verification.
- Stop when the work touches sensitive surfaces, broad architecture, new dependencies, external mutation, production actions, or unclear acceptance.
- Ask the Standards Taxonomy question when an agent uses a professional standard name without saying what it means for this bead, which owner protocol applies, and what proof is enough.

"Production-grade" is a direction for judgment. It is not a certification claim. Passing this quality floor does not prove the software is production-ready, secure, compliant, scalable, or released.

## Forbidden Uses

Do not use this protocol to:

- approve PRDs, activate beads, accept implementation, approve review, approve release, approve transitions, or choose tasks
- create a required stage for every bead
- certify production readiness, security, accessibility, compliance, scalability, reliability, or code quality
- replace linters, typecheckers, tests, code review, release readiness, or manual verification
- create a scorecard, generated proof, code-quality rating, checker gate, command wrapper, registry, optional pack, package-manager behavior, or release-channel behavior
- hide product, architecture, API, data, security, dependency, deployment, or release decisions inside implementation

## Failure Modes

- Ceremony creep: the agent turns a tiny task into a long engineering ritual.
- Rhetorical quality: the agent uses professional words without naming scope, boundary, proof, or stop conditions.
- Hidden authority: the quality-floor answer stores durable facts that belong in an owner file, PRD, bead, or decision.
- False confidence: the answer implies production readiness or security assurance without recorded evidence and human approval.
- Duplicated protocol work: the agent recreates Architecture Shaping, System Design Pattern, Verification, Tool Execution, Review Lanes, or Release Readiness instead of routing to them.
