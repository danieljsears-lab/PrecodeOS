# Precode OS -- System Design Pattern Protocol
<!-- ANCHOR: system-design-pattern-protocol -->

> AUTHORITY: Prescriptive guidance for choosing practical implementation shapes, system design patterns, and owner files before coding.
> NOT_AUTHORITY: Active memory, product decisions, approved requirements, task selection, bead activation, implementation plans, generated progress state, or external mutations.
> LOAD_WHEN: A feature may need architecture shape, external integration boundaries, state flows, interchangeable rules, audit trails, auth/access boundaries, or a plain-English explanation of whether a design pattern is warranted.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

This protocol helps non-technical builders ask for the right implementation shape before an agent starts coding.

Use it when a feature feels bigger than a text or styling change, when an agent proposes a design pattern, or when business rules could become scattered across the app.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Prescriptive Pattern Guidance

Start with these defaults:

| Situation | Recommended shape | Why this matters | Owner file | What to ask the agent | Evidence that the shape worked |
|---|---|---|---|---|---|
| Feature talks to Stripe, GitHub, email, AI, webhooks, or another external service | Adapter or facade | Provider details stay in one place instead of leaking through UI, API routes, and tests. | `API.md`, `ARCHITECTURE.md`, or `PROJECT-CONTEXT.md` | "Show me the adapter/facade boundary before coding." | One boundary owns provider calls; tests or checks prove the app can use it through that boundary. |
| Feature has steps, approvals, statuses, or blocked states | State flow | The agent must know what can happen next, what cannot happen, and what each status means. | `ARCHITECTURE.md`, `USER-FLOWS.md`, or a PRD | "List the states and allowed transitions before implementation." | Statuses and transitions are named; verification covers at least one valid and one invalid transition when risk warrants it. |
| Feature has multiple modes, providers, pricing rules, routing rules, or policies | Strategy-style boundary | Changeable rules stay behind one decision point instead of being copied into many places. | `ARCHITECTURE.md` or `PROJECT-CONTEXT.md` | "Where should the interchangeable rule or provider decision live?" | The chosen rule/provider can change without editing unrelated UI or data code. |
| Feature needs to know who did what, when, or why | Audit trail | Irreversible or important actions stay explainable later. | `DATA-MODELS.md`, `SECURITY.md`, or `ARCHITECTURE.md` | "What action history should be recorded and where?" | Evidence records the action, actor, timestamp, result, and relevant object without storing secrets. |
| Feature involves login, roles, permissions, private data, uploads, billing, or security config | Auth/access boundary | Sensitive decisions must be centralized and reviewed before users can be exposed. | `SECURITY.md` and `ARCHITECTURE.md` | "Define the access boundary and approval gate before coding." | Verification proves allowed and denied access paths, plus manual approval for sensitive changes. |
| Feature is a one-off copy, layout, styling, or small local behavior change | Direct change using existing conventions | A named pattern would add ceremony without reducing risk. | active bead | "Is this simple enough to build directly?" | The changed file stays narrow, checks pass, and no new architecture is introduced. |

If no row fits, stop and ask what shape the feature wants before implementation.

## Pattern Families In Plain English

- Creation patterns decide how objects, services, clients, or providers get made.
- Structure patterns decide where boundaries live and how code is insulated from change.
- Behavior patterns decide how rules, actions, workflows, and state changes happen.
- Product workflow patterns describe user-facing shapes like wizards, approvals, queues, settings, dashboards, and audit trails.

Use pattern names only after naming the problem they solve.

## What To Avoid

- One giant file doing everything.
- Business rules scattered across UI, API, database, and background-job code.
- External APIs called directly from many places.
- Workflows tracked only in comments, vague text, or hidden assumptions.
- Factories, strategies, state machines, or adapters before there is real complexity.
- Generated code treated as owned architecture without human review.
- Pattern names used as decoration instead of solving a specific risk.

## Pattern Decision Ownership

- `ARCHITECTURE.md` owns major module boundaries, state flows, route structure, and structural decisions.
- `PROJECT-CONTEXT.md` owns project-wide conventions, stack choices, provider preferences, and implementation principles.
- `API.md` owns API, webhook, external service, and server boundary patterns.
- `DATA-MODELS.md` owns entity relationships, audit trail storage, and schema implications.
- `SECURITY.md` owns auth, role, permission, privacy, and sensitive-surface boundaries.
- PRDs own product workflow shape, user acceptance behavior, and requirement-level intent.
- `DECISIONS.md` owns durable choices to introduce, reject, or defer a pattern.
- The active bead owns scoped execution only.

If a pattern choice affects more than the active bead, record it in the correct owner file or stop for approval.

## Design Shape Output

When asked to choose a shape, return:

- Situation:
- Recommended shape:
- Why this matters:
- Owner file:
- Simpler alternative:
- Approval needed:
- Verification evidence:
- Stop condition:

This output is guidance only. It does not approve a PRD, activate a bead, choose the next task, or rewrite owner files.

## Approval Gates

Stop for user approval before:

- introducing a new architecture boundary across multiple modules
- changing auth, roles, permissions, billing, private data, uploads, deployments, or security config
- replacing an existing provider or external service boundary
- adding a state machine or audit trail that changes user-visible behavior
- promoting generated pattern guidance into an owner file

## Advisory Check

`scripts/pattern-check.py` is advisory. It may warn about missing boundary owners, state-flow ambiguity, strategy/configuration drift, audit-trail ownership gaps, broad architecture work inside implementation beads, named patterns without a recorded reason, or unnecessary abstraction for simple work.

Warnings are generated evidence only. They do not choose tasks, approve PRDs, activate beads, change bead state, or edit active memory.
