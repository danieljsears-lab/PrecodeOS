# Precode OS — Project Context Template
<!-- ANCHOR: project-context -->

> AUTHORITY: Project constitution template for stack choices, implementation conventions, architecture guardrails, integration boundaries, and project-specific build rules.
> NOT_AUTHORITY: Active memory, active task selection, feature requirements, route inventory, schema field definitions, pricing decisions, or generated progress state.
> LOAD_WHEN: Shaping PRDs, deriving architecture-affecting beads, onboarding an agent, resolving implementation convention questions, or checking whether new work fits the project constitution.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.1.0
Last updated: 2026-04-26

## Purpose

`PROJECT-CONTEXT.md` is the project constitution.

It gives agents and builders a stable place to look for how the target project builds software without adding another active-memory file.

Active memory remains:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Load this file only when the work needs project-level context.

## Project Shape

- Product:
- Stack:
- Primary users or roles:
- App directory:
- Deployment target:

## Operating Principles

- Keep the active-memory set tiny.
- Use `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` to recover from todo/bead drift, stale generated reports, or unclear state ownership.
- Prefer project conventions over new abstractions.
- Use one primary authority file per bead.
- Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when the right path is unclear before activating or widening work.
- Use `tasks/reference/LONG-HORIZON-PLANNING-PROTOCOL.md` when reviewing future, blocked, deferred, follow-up, or PRD-approved work without making it active.
- Use `tasks/reference/SESSION-COMPLETION-HANDOFF-PROTOCOL.md` when closing sessions, reviewing bead completion, or handing work to another agent.
- Use `tasks/reference/DECOMPOSITION-PROTOCOL.md` when slicing broad work into beads or deciding that something is not a bead yet.
- Keep feature work traceable to approved PRD shards and requirement IDs.
- Prefer small, valuable, reviewable changes over broad implementation sweeps.
- Record evidence through `bash scripts/record-check.sh -- <command>`.
- Treat generated files as reports, not instructions.
- Stop before crossing a manual approval gate.

## Architecture Guardrails

- Route structure belongs in `ARCHITECTURE.md` or the target project's architecture authority file.
- Schema field names, relationships, and field semantics belong in `DATA-MODELS.md` or the target project's schema authority file.
- API route conventions and server-side boundaries belong in `API.md` or the target project's API authority file.
- Security policy and threat model belong in `SECURITY.md`.
- Acceptance and completion criteria belong in `ACCEPTANCE.md`.
- Product decisions and open questions belong in `DECISIONS.md`.
- Feature inventory and compiled functional requirements belong in `FEATURES.md`.
- Deep product definition belongs in `tasks/prds/*.md`.

## Implementation Conventions

- Follow the existing framework, folder, and naming patterns before introducing a new pattern.
- Do not add a dependency unless the active bead allows it or the user approves it.
- Keep UI work consistent with the existing design system.
- Keep server-side validation and authorization close to the route/action boundary.
- Treat auth, payments, personal data, uploads, destructive actions, external integrations, and production configuration as sensitive surfaces.
- Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` before accepting high-risk work or crossing sensitive-surface approval gates.

## Integration Boundaries

List project integrations here:

- Auth:
- Database:
- Payments:
- Email:
- Hosting:
- Analytics:
- External APIs:
- Repository host:
- CI provider:
- Issue tracker:
- Deployment provider:
- Monitoring or error tracking:
- Safe health URLs for read-only uptime checks:
- Manual dashboards or setup surfaces:

If an integration boundary changes, record the product or technical decision in `DECISIONS.md` and update the owning reference file.

## Project Extensions

List enabled project-specific Precode extensions here. Extensions are reference or evidence surfaces, not active memory.

- Enabled adapters:
- Enabled importers:
- Enabled audits:
- Enabled generated reports:
- Enabled external integrations:
- Extension owner files:

Use `tasks/reference/EXTENSION-PROTOCOL.md` before adding new adapters, protocols, importers, audits, generated reports, bead templates, or external integrations.

## Scheduled Audit Configuration

Scheduled audits are opt-in read-only checks. They may report external system status, but they must not mutate GitHub, CI, deployments, issue trackers, monitoring systems, or dashboards.

- GitHub audit configured: `yes | no`
- GitHub repository URL:
- GitHub default branch:
- GitHub pull request branch naming convention:
- GitHub primary workflow names:
- GitHub issue tracker mode:
- GitHub linked project board:
- GitHub safe read-only status checks:
- CI audit configured: `yes | no`
- Deployment audit configured: `yes | no`
- Issue tracker audit configured: `yes | no`
- Dependency/security audit configured: `yes | no`
- Monitoring audit configured: `yes | no`
- Uptime audit configured: `yes | no`
- Dashboard setup audit configured: `yes | no`

## Testing And Evidence

- A generated test is not evidence until it is run.
- A screenshot is review input until it is linked from closeout or recorded evidence.
- An external QA note or AI critique is review input until its findings are resolved or recorded in Closeout Evidence.
- Passing checks should be recorded with `bash scripts/record-check.sh -- <command>`.
- Manual verification must say what was checked, by whom, and whether it passed, failed, or remains blocked.
- Stronger work needs stronger proof: code, UI, data, integrations, deployment, and security work should use the Verification Guardrail Protocol tiers rather than relying on memory validation alone.

## Implementation Shape

- Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` before introducing or rejecting a design pattern, external service boundary, state flow, strategy-style rule boundary, audit trail, or auth/access boundary.
- Prefer the simplest shape that preserves clarity, safety, and future change.
- Prefer existing framework and project conventions before adding a named pattern.
- Pattern guidance is advisory evidence only; durable pattern choices belong in `ARCHITECTURE.md`, `PROJECT-CONTEXT.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `DECISIONS.md`, PRDs, or the active bead as appropriate.

## Context Loading

Use `tasks/reference/CONTEXT-ENGINEERING-PROTOCOL.md` when deciding what an agent should load, when source material is evidence instead of instruction, or when a handoff needs a compact Context Pack.

Load this file when:

- creating or approving a PRD shard
- deriving beads from a PRD
- work may affect architecture, stack, conventions, dependencies, external services, or verification strategy
- an agent is unsure which project convention applies

Do not load this file when:

- the active bead is narrow and its primary authority is sufficient
- the question belongs to a more specific authority file
- generated health or progress reports already point back to the active memory set
