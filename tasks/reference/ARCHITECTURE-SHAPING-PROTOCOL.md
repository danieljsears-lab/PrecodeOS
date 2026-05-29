# PrecodeOS -- Architecture Shaping Protocol
<!-- ANCHOR: architecture-shaping-protocol -->

> AUTHORITY: Risk-triggered architecture-shaping interview, Architecture Brief format, routing rules, stop conditions, and PRD-to-bead handoff guidance before architecture-sensitive work becomes candidate beads.
> NOT_AUTHORITY: Active memory, product approval, implementation plan, final architecture decision, owner-file replacement, task selection, bead activation, generated progress, or coding permission.
> LOAD_WHEN: An approved PRD touches auth, data models, APIs, integrations, dependencies, migrations, external services, multi-step workflows, multi-system changes, or another implementation risk that should be visible before bead proposals.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-05-29

## Purpose

Architecture Shaping helps a non-technical builder steer the implementation risk and boundary decisions that an AI coding agent will later work inside.

Use this protocol after PRD approval and before bead proposals when the product destination is clear but the architecture-sensitive path is not yet safe enough to decompose.

The output is an Architecture Brief. The brief is evidence only. It can guide PRD amendments, owner-file updates, planning beads, unblocker beads, run contracts, and safer decomposition, but it does not approve coding or become architecture authority by itself.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Trigger Rules

Run Architecture Shaping when an approved PRD touches any of these surfaces:

- auth, roles, permissions, privacy, billing, uploads, or private user data
- data sources, data models, migrations, retention, destructive changes, or audit history
- API routes, webhooks, background jobs, external services, provider SDKs, or third-party dashboards
- new dependencies, environment variables, secrets, deployment assumptions, or manual setup
- multi-step workflows, statuses, approvals, queues, retries, blocked states, or user-visible state transitions
- multi-system changes where UI, API, data, security, external services, or operations must move together
- any work that would otherwise require `required_planning_depth: PRD+architecture` or `PRD+architecture+test-plan`

Skip Architecture Shaping when the work is simple copy, styling, docs-only behavior, or a small local change with no meaningful architecture risk.

If the PRD is not approved, return to PRD shaping. If worth-building uncertainty is still material, use Product Discovery Validation instead.

## Interview Rules

Ask adaptive questions one at a time. Each question should expose or resolve a risk that can change decomposition, approval gates, owner files, verification, or whether the PRD must change.

Each question should include:

- the plain-English decision or risk
- the recommended default
- the tradeoff
- what changes if the builder answers differently

Do not ask the builder to choose framework internals, file names, database implementation details, or pattern names unless the choice exposes a real product, risk, cost, trust, or approval tradeoff.

Good question areas:

- Which systems, providers, or data sources are involved?
- What user data or private information is touched?
- Who is allowed to do the action, and who must be denied?
- What existing source of truth should win if systems disagree?
- What manual setup, dashboard work, secret, or dependency might block implementation?
- Does the work need a state flow, audit trail, provider boundary, or migration plan before coding?
- What proof would make the builder comfortable that the risky path works?

Stop asking when the remaining unknowns are low-risk implementation choices the coding agent can inspect and decide inside the approved boundaries.

## Architecture Brief Format

Use this compact format.

```text
## Architecture Brief

- Source PRD:
- Requirement IDs:
- Brief status: evidence_only

### Triggering Risk Surfaces
- Auth/access:
- User or private data:
- Data model or migration:
- API, webhook, or background job:
- External service or integration:
- Dependency, secret, or environment:
- Multi-step workflow or state:
- Multi-system coordination:

### Boundary Notes
- Data sources and source of truth:
- Integration boundaries:
- API/server boundaries:
- Auth/access boundary:
- State flow or audit trail:
- Manual setup or dashboard steps:
- Dependencies or environment needs:

### Owner File Impacts
- `ARCHITECTURE.md`:
- `API.md`:
- `DATA-MODELS.md`:
- `SECURITY.md`:
- `PROJECT-CONTEXT.md`:
- PRD amendment:
- `DECISIONS.md`:

### Approval Gates And Stop Conditions
- Approval required before:
- Stop if:
- Return to PRD if:
- Propose an unblocker or planning bead if:

### Verification Evidence Expected
- Automated checks:
- Manual verification:
- Sensitive-path proof:
- Evidence not sufficient:

### Bead Implications
- Required planning depth:
- Likely slice type:
- Run contract needed:
- Candidate first bead shape:
- Unresolved blockers:

### Do Not Decide Yet
- Repo facts the coding agent must inspect before choosing internals:
- Implementation choices intentionally left to the coding agent:
```

Keep the brief short enough that a builder can approve, challenge, or redirect it. Prefer plain nouns over pattern names until the risk is clear.

## Handoff To System Design Patterns

Architecture Shaping asks:

```text
What risks and boundaries must be clear before decomposition?
```

`tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` answers:

```text
What implementation shape may fit this risk?
```

Use the System Design Pattern Protocol after or during Architecture Shaping when the brief reveals a likely adapter, facade, state flow, strategy-style rule boundary, audit trail, auth/access boundary, or deep module boundary.

Do not merge the Architecture Brief into a full implementation plan. The brief should constrain the next coding agent, not pre-code the solution.

## Stop Rules

Stop bead proposal and return to the PRD when shaping reveals a product-changing technical risk, acceptance change, user-visible workflow change, or unresolved requirement question.

Recommend an owner-file update when shaping reveals a durable architecture, API, schema, security, project-context, or decision fact. The Architecture Brief itself remains evidence until promoted into the correct owner file.

Propose a narrow planning or unblocker bead when one unknown must be investigated before safe decomposition, such as a provider capability, migration feasibility, secret/dashboard setup, or repo convention.

Skip the bridge when the feature remains low-risk after inspection. Record the skip reason in the PRD architecture-impact section or bead proposal notes.

## PRD-To-Bead Handoff

Before deriving candidate beads for architecture-sensitive work, confirm:

- the source PRD is approved
- the Architecture Brief names the risk surfaces or explains why the bridge was skipped
- product-changing technical risks have returned to PRD amendment or open questions
- owner-file-level decisions are recommended for promotion instead of hidden in the brief
- the first bead has one outcome, one primary authority, one verification strategy, bounded files in play, approval gates, and stop conditions
- `required_planning_depth` matches the risk: usually `PRD+architecture` or `PRD+architecture+test-plan`
- a Run Contract is included or explicitly not needed when sensitive, external, destructive, or bounded-AFK execution appears

If these are not true, the next artifact is not a bead yet.

## Value Test

For the first 3-5 real PRDs that use Architecture Shaping, record lightly in the brief or closeout notes:

- risks surfaced before implementation that were not obvious in the PRD
- whether surfaced risks caused PRD amendment, owner-file update, planning or unblocker bead, run contract, or safer decomposition
- whether the brief prevented architecture overreach, vague beads, or premature coding
- whether the founder could approve, challenge, or redirect the proposed shape in plain English

The primary success signal is hidden risk surfaced before bead proposal. Better bead quality is downstream proof.

## Failure Modes

- Architecture overreach: the brief becomes a speculative full implementation plan.
- Vague output: the brief names risk but does not change approval gates, owner files, verification, or decomposition.
- User burden: the interview asks the builder to choose internals the coding agent should decide after repo inspection.
- Hidden authority: the brief stores durable architecture facts that belong in `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `PROJECT-CONTEXT.md`, a PRD amendment, or `DECISIONS.md`.
- Premature code: the brief is treated as permission to implement without bead activation.
