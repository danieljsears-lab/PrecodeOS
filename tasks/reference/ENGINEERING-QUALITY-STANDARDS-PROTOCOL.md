# PrecodeOS -- Engineering Quality Standards Protocol
<!-- ANCHOR: engineering-quality-standards-protocol -->

> AUTHORITY: Lightweight pre-coding engineering quality floor, proportional risk routing, agent explanation contract, human approval questions, and stop conditions before implementation.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, implementation acceptance, production readiness certification, security certification, compliance approval, generated proof, code-quality scoring, lint replacement, release approval, or a required stage for every bead.
> LOAD_WHEN: A user asks what engineering quality standard the agent is applying before coding, an active bead is about to move into implementation, or a simple implementation request may hide architecture, security, data, dependency, deployment, or multi-system risk.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: (c) 2026 Dan Sears / Recode
Document version: v0.1.1
Last updated: 2026-06-29

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
| Work is nearly done and needs a named advisory review lens | `tasks/reference/REVIEW-LANES-PROTOCOL.md` |
| User-facing shipping, deployment, rollback, smoke evidence, or docs freshness risk appears | `tasks/reference/RELEASE-READINESS-PROTOCOL.md` |

This protocol should point to those owner protocols. It should not duplicate them.

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

Standards Taxonomy remains deferred. Use repeated checker warning patterns to decide which engineering-standard concepts need beginner-readable teaching later. Do not import external engineering frameworks into this protocol as public package authority before that evidence exists.

## Standards In Plain English

Use these as prompts for judgment, not as a broad checklist:

- Keep the change inside the active bead and files in play.
- Prefer the simplest shape that can satisfy the requirement and proof path.
- Keep business rules, provider calls, state transitions, auth checks, and durable facts in clear owner boundaries.
- Keep configuration, secrets, dashboard values, and environment assumptions out of code unless the owner file and active bead explicitly allow the change.
- Prove behavior with the narrowest useful recorded check or structured manual verification.
- Stop when the work touches sensitive surfaces, broad architecture, new dependencies, external mutation, production actions, or unclear acceptance.

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
