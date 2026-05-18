# PrecodeOS — Project Context
<!-- ANCHOR: project-context -->

> AUTHORITY: Technical project constitution for stack choices, implementation conventions, architecture guardrails, integration boundaries, and project-specific build rules for PrecodeOS itself.
> NOT_AUTHORITY: Active memory, active task selection, feature requirements, route inventory, schema field definitions, pricing decisions, or generated progress state.
> LOAD_WHEN: Shaping PRDs, deriving architecture-affecting beads, onboarding an agent, resolving implementation convention questions, or checking whether new work fits the project constitution.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.2.8
Last updated: 2026-05-17

## Purpose

`PROJECT-CONTEXT.md` is the technical project constitution for PrecodeOS itself.

It gives agents and builders a stable place to look for how this repository builds and verifies the OS without adding another active-memory file.

Active memory remains:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

Load this file only when the work needs project-level context.

Use `PRODUCT.md` for builder-facing product direction: product promise, users and jobs, strategy and non-goals, current bets, success signals, and design or voice pointers.

## Project Shape

- Product summary: PrecodeOS is a repo-native control layer for AI coding agents: markdown-canonical, script-enforced, and built to prevent quiet drift. For builders, it functions as a small operating system for AI coding work by showing what matters, what is active, what is proven, and when to stop.
- Stack: Markdown authority/reference/execution documents; Python 3 compiler, validation, audit, and report scripts; Bash session/check/evidence wrappers; GitHub Actions for repository validation; JSON/JSONL generated evidence in `logs/`.
- Primary users or roles: Dan Sears / Recode as maintainer and builder; solo non-technical or technical builders adopting PrecodeOS; AI coding agents operating as navigator, explorer, builder, and review roles; reviewers who inspect bead closeout and transition safety.
- App directory: `.` (the repository root). There is no separate application runtime directory for B000.
- Deployment target: GitHub repository distribution and local filesystem use. GitHub Actions runs validation on pull requests and pushes.

## Operating Principles

- Keep the active-memory set tiny.
- Use `tasks/reference/STATE-MANAGEMENT-PROTOCOL.md` to recover from todo/bead drift, stale generated reports, or unclear state ownership.
- Prefer project conventions over new abstractions.
- Use one primary authority file per bead.
- Use `tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md` when the right path is unclear before activating or widening work.
- Use `tasks/reference/GOAL-FRAME-PROTOCOL.md` when durable intent needs reviewed orientation before workflow selection; Goal Frames remain advisory and must be reaffirmed when stale.
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
- Product promise, users and jobs, strategy, current bets, success signals, and design or voice pointers belong in `PRODUCT.md`.
- Product decisions and open questions belong in `DECISIONS.md`.
- Feature inventory and compiled functional requirements belong in `FEATURES.md`.
- Deep product definition belongs in `tasks/prds/*.md`.

## Implementation Conventions

- Follow the existing framework, folder, and naming patterns before introducing a new pattern.
- Keep public script entrypoints stable when refactoring internals; new helper modules may live under `scripts/` when they preserve current command behavior.
- Keep `scripts/next-step.py` as the canonical generated router for the next human decision, with `session-start.sh` displaying the same decision rather than inventing a second router.
- Use context-footprint output as advisory routing evidence: active memory, active bead, primary authority, one next protocol when needed, generated reports touched, and approximate document lines.
- Do not add a dependency unless the active bead allows it or the user approves it.
- Keep UI work consistent with the existing design system.
- Keep server-side validation and authorization close to the route/action boundary.
- Treat auth, payments, personal data, uploads, destructive actions, external integrations, and production configuration as sensitive surfaces.
- Use `tasks/reference/VERIFICATION-GUARDRAIL-PROTOCOL.md` before accepting high-risk work or crossing sensitive-surface approval gates.

## Integration Boundaries

Current project integrations:

- Auth: none in-app; local agents use the user's tool/session credentials.
- Database: none.
- Payments: none.
- Email: none.
- Hosting: GitHub repository hosting for source distribution.
- Analytics: none configured.
- External APIs: optional read-only GitHub access through `gh` for audit/import scripts when configured.
- Repository host: GitHub.
- CI provider: GitHub Actions via `.github/workflows/precode-validate.yml`.
- Issue tracker: GitHub Issues when the repository uses them; not required for B000.
- Deployment provider: none for an app runtime.
- Monitoring or error tracking: none configured.
- Safe health URLs for read-only uptime checks: none.
- Manual dashboards or setup surfaces: GitHub repository settings, Actions, Issues, Pull Requests, and project boards if enabled by the maintainer.

If an integration boundary changes, record the product or technical decision in `DECISIONS.md` and update the owning reference file.

## Project Extensions

Enabled project-specific Precode extensions:

- Enabled adapters: `adapters/CLAUDE.md`, `adapters/CODEX.md`, `adapters/CURSOR.md`, `adapters/GEMINI.md`, `adapters/ANTIGRAVITY.md`, plus shim files `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md`.
- Enabled importers: `scripts/import-agent-spend.py` and `scripts/import-github-sources.py`.
- Enabled audits: `scripts/github-audit.py`, `scripts/scheduled-audit.sh`, `scripts/scheduled-audit.py`, and advisory `scripts/*-check.py` commands.
- Enabled generated reports: `OS-HEALTH.md`, `PROGRESS.md`, `logs/*.json`, `logs/*.jsonl`, `logs/*.md`, `logs/check-output/*`, and `logs/scheduled-audit-output/*`.
- Enabled external integrations: GitHub read-only audit/import when configured; no write integration is required for B000.
- Extension owner files: `tasks/reference/EXTENSION-PROTOCOL.md`, `tasks/reference/GITHUB-INTEGRATION-PROTOCOL.md`, `tasks/reference/SCHEDULED-AUDIT-PROTOCOL.md`, `tasks/reference/TOOL-EXECUTION-PROTOCOL.md`, `adapters/ADAPTER-INDEX.md`, and `docs/PRECODE-FILE-INVENTORY.md`.

Use `tasks/reference/EXTENSION-PROTOCOL.md` before adding new adapters, protocols, importers, audits, generated reports, bead templates, or external integrations.

## Scheduled Audit Configuration

Scheduled audits are opt-in read-only checks. They may report external system status, but they must not mutate GitHub, CI, deployments, issue trackers, monitoring systems, or dashboards.

- GitHub audit configured: yes, read-only when `git`/`gh` repository context is available.
- GitHub repository URL: not fixed in B000; derive from the local Git remote when available.
- GitHub default branch: not fixed in B000; derive from the repository when available.
- GitHub pull request branch naming convention: no required convention yet.
- GitHub primary workflow names: `Precode Validate`.
- GitHub issue tracker mode: optional GitHub Issues.
- GitHub linked project board: none required for B000.
- GitHub safe read-only status checks: repository metadata, open pull requests/issues, and GitHub Actions status through read-only commands.
- CI audit configured: yes, through GitHub Actions validation and read-only audit scripts.
- Deployment audit configured: no.
- Issue tracker audit configured: optional.
- Dependency/security audit configured: no package dependency audit is configured because B000 has no package manager manifest.
- Monitoring audit configured: no.
- Uptime audit configured: no.
- Dashboard setup audit configured: no.

## Project-Specific Checks

B000 and other OS-kernel documentation changes should use these checks unless the active bead narrows or expands them:

- `bash scripts/record-check.sh -- bash scripts/validate-memory.sh`
- `bash scripts/record-check.sh -- python3 scripts/version-check.py`
- `bash scripts/record-check.sh -- python3 scripts/file-inventory.py --check`
- `bash scripts/record-check.sh -- python3 scripts/local-hygiene-check.py`
- `bash scripts/record-check.sh -- python3 scripts/completion-check.py`

For Python script behavior changes, add a targeted command that exercises the changed script and records output. For shell script behavior changes, run the changed script in its intended mode through `record-check.sh`.

## Testing And Evidence

- A generated test is not evidence until it is run.
- A screenshot is review input until it is linked from closeout or recorded evidence.
- An external QA note or AI critique is review input until its findings are resolved or recorded in Closeout Evidence.
- Passing checks should be recorded with `bash scripts/record-check.sh -- <command>`.
- Manual verification must say what was checked, by whom, and whether it passed, failed, or remains blocked.
- Stronger work needs stronger proof: code, UI, data, integrations, deployment, and security work should use the Verification Guardrail Protocol tiers rather than relying on memory validation alone.

## Implementation Shape

- Use `tasks/reference/SYSTEM-DESIGN-PATTERN-PROTOCOL.md` before introducing or rejecting a design pattern, external service boundary, state flow, strategy-style rule boundary, audit trail, or auth/access boundary.
- When `scripts/os_compiler.py` grows a distinct domain, extract that domain into an internal service module while keeping existing command paths and generated JSON shapes stable.
- Keep role contracts compact: Navigator, Explorer, Builder, and Review should say what to load, decide, avoid, and return without becoming new active-memory files or autonomous personas.
- Defer a broad diagnostic `doctor` command and installable `precode` CLI until router-first behavior and bootstrap/install needs are proven.
- Treat PRD shards as destination documents and beads as journey units; `tasks/todo.md` remains the active journey pointer.
- New or amended code-changing beads should declare advisory `delegation_mode`, `test_strategy`, and `review_context` metadata when useful.
- Prefer vertical slices for user-facing work, failing-first test strategy when practical, and fresh-context review for medium/high-risk code-changing work.
- For meaningful implementation logic, define the deep-module interface, behavior contract, and test boundary before delegating internals.
- Use shared domain language for UI labels, module/interface names, tests, and fixtures when terms matter; glossary memory is evidence only unless promoted to an owner file.
- Use Local Hygiene before cleanup: truth is not cleanup; evidence is preserved; caches are disposable only when ignored and regeneratable.
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
