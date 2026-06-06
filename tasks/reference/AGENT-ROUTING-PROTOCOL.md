# PrecodeOS -- Agent Routing Protocol
<!-- ANCHOR: agent-routing-protocol -->

> AUTHORITY: Cross-agent model tier selection, context-budget discipline, delegation boundaries, and tool-routing preferences for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, product decisions, task selection, bead activation, provider pricing guarantees, adapter-specific configuration, external mutation approval, or verification evidence.
> LOAD_WHEN: Choosing an AI coding agent model, reasoning effort, subagent/delegation path, context compaction or handoff point, or tool path for a PrecodeOS task.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.4
Last updated: 2026-06-06

## Purpose

Agent routing helps Precode use enough intelligence without turning every task into an expensive, bloated, or stale-context session.

This protocol is provider-neutral. It defines the decision language. Tool adapters translate the language into Claude, Codex, Gemini, Cursor, Antigravity, or future agent settings.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Routing Tiers

Use the cheapest tier that can safely complete the current work.

| Tier | Use When | Avoid When |
|---|---|---|
| `fast` | Mechanical edits, simple searches, low-risk summaries, obvious validation, small isolated fixes. | The task needs product judgment, architectural tradeoffs, broad debugging, or high-risk review. |
| `default` | Normal coding, scoped repo exploration, synthesis, test fixing, and everyday implementation inside a clear bead. | The work is mostly mechanical, or ambiguity/stakes/novelty are high. |
| `deep` | Architecture, ambiguous bugs, security-sensitive work, product tradeoffs, unclear failures, or high-blast-radius review. | The task is bounded, repetitive, or already has a clear implementation path. |
| `long-horizon` | Multi-step work where continuity, checkpoints, and durable handoff matter more than latency. | The bead is not approved, files/checks are unbounded, or a human approval gate is unresolved. |

Escalate only when the current tier cannot safely decide. De-escalate when the next step becomes mechanical.

## Routing Rules

- Model choice, reasoning effort, or subagent choice must not override the active bead, files in play, stop conditions, approval gates, or review requirements.
- If the work needs a second outcome, authority owner, verification strategy, or risk model, split the bead before routing to a stronger model.
- Use `deep` for stakes plus ambiguity plus novelty. Do not use it as the default for routine execution.
- Use `long-horizon` only with explicit checkpoints, review context, and a clear escape path.
- If a delegated agent realizes it needs a smarter tier, broader scope, or new approval, it returns that finding to the parent instead of escalating independently.
- Record durable spend when telemetry is available; missing spend is unknown, not zero.

## Context Budget

Treat about 80% context usage as the point to prepare a checkpoint, compaction, restart, or handoff.

This is a recommended operating threshold, not a hard invariant. The goal is to preserve enough room for tool output, diffs, test results, closeout evidence, and review.

Before compacting, restarting, or handing off, produce a compact Context Pack:

- current bead
- done-when target
- primary authority
- files in play
- out of scope
- checks and latest evidence
- allowed actions and proof needed when the active bead has a Run Contract
- stop conditions and approval gates
- decisions or assumptions made this session
- changed files
- remaining work and next exact check

After compaction, restart, or handoff, re-read active memory, the active bead, and the primary authority before continuing. Do not rely on chat history to preserve authority.

## Delegation Boundaries

Delegation may help when a bounded side task can run separately from the main context.

Precode role contracts are intentionally small: Navigator, Explorer, Builder, and Review describe what to load, decide, avoid, and return. They are not autonomous personas, task selectors, or a fake product organization. Use them to keep a host tool's native subagents or modes bounded by the active bead and Run Contract.

Delegation must not:

- activate another bead
- bypass human review
- mutate external systems without the active bead and user approval
- widen files in play
- exceed a Run Contract's allowed actions, proof needed, approval gates, or expiration condition
- create recursive agent chains without explicit tool support and clear bounds
- turn an `afk_candidate` bead into unsupervised product or architecture ownership

Prefer delegation for bounded repo exploration, focused review, isolated implementation slices with disjoint files, or long-running verification that can report back with evidence. Sensitive, external, destructive, or `bounded-afk` delegated work should have a Run Contract before delegation.

Explorer is the preferred contract for read-only repo discovery. It returns findings and cited paths; it does not edit, activate, approve, or continue into implementation.

## Tool Routing

Prefer the lowest-token, lowest-side-effect tool that can answer the question.

Use this default order when it fits the task:

1. Local text search or structured file reads for repo facts.
2. Read-only commands or dry-run checks for local state.
3. Text fetches or official docs for public web facts when current information matters.
4. Browser or screenshot-heavy tools for dynamic pages, authenticated flows, visual QA, or interactions that text tools cannot inspect.
5. External mutation tools only when the active bead allows them and the user approves the manual gate.

If a repeated tool pattern becomes durable and useful, propose a reusable command, script, skill playbook, or adapter improvement through the Extension Protocol and Skill Playbook Protocol. Do not create hidden automation from a one-off workaround.

`python3 scripts/next-step.py` owns generated routing output. It may expose `single_next_protocol`, `load_plan`, and `context_footprint` so the agent can choose the smallest useful context before reaching for heavier tools.

A future `precode doctor` or installable `precode` CLI should wrap proven commands only after the router and bootstrap surfaces have stabilized; do not make them prerequisites for normal repo use.

## Adapter Mapping

Adapters own provider-specific mapping:

- Claude-specific model aliases, subagent settings, and compaction environment variables belong in `adapters/CLAUDE.md`.
- Codex/OpenAI model choice, reasoning effort, and cloud/background delegation guidance belong in `adapters/CODEX.md`.
- Gemini, Cursor, Antigravity, and future tools should map only the controls they actually expose.

When a tool does not expose a native setting for a routing or compaction concept, fall back to Precode checkpoint, handoff, and review discipline.
