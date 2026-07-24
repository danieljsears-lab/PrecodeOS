# PrecodeOS -- Tool Execution Protocol
<!-- ANCHOR: tool-execution-protocol -->

> AUTHORITY: Tool-call classes, command policy expectations, non-check tool logging, failure categories, external mutation rules, secret handling, and tool-execution advisory checks for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, task selection, product decisions, implementation plans, automatic command approval, generated progress state, or automatic bead transitions.
> LOAD_WHEN: Choosing, recording, reviewing, or approving tool calls; adding tool integrations; handling command failures; or distinguishing tool use from verification evidence.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.17
Last updated: 2026-07-24

## Purpose

Tool execution keeps Precode honest about what an agent actually ran.

A command can be useful without proving the work is done. Precode separates:

- tool use: an action happened
- verification evidence: a check proved something and was recorded
- user approval: a human approved a risky action

Tool execution is part of PrecodeOS's advisory repo-native harness contract. Command classes, run contracts, generated sidecars, recorded checks, and transparent facades make agent work inspectable, but they are not an agent runtime, sandbox, command approval layer, registry, optional pack, package manager, install/update system, or enforcement layer.

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` when choosing between low-token read-only tools, browser or screenshot-heavy tools, delegated agents, and external mutation tools.

Use `tasks/reference/RALPH-LOOP-PROTOCOL.md` when a host or user wants a bounded retry loop around one active bead. Ralph can record attempts and validators, but it is still subject to this protocol's command classes and approval rules.

Use `scripts/precode_cli.py`, the optional local `precode` console command, or the optional npm `precodeos` preview entry only as a facade over trusted repo commands. A wrapper command inherits the underlying command's tool-call class, approval gates, side effects, and evidence limits. It must print the underlying command before running it and must not approve work, hide mutation, widen files in play, mutate external systems, define package update behavior, define release-channel behavior, or make generated output authoritative. The npm entry is limited to read-only setup and upgrade previews and must not expose apply flags or postinstall target mutation.

Command surface triage is reader guidance only. Grouping commands by beginner daily work, setup/support/recovery, advanced evidence/review, and maintainer validation does not change tool-call classes, approve commands, choose tasks, create a router or registry, expand wrapper behavior, or make generated output authoritative. Beginner-facing command surfaces should expose advanced command families as trigger summaries and route detailed use to Prompt Patterns or the owner protocol instead of becoming a script menu.

`scripts/clarity-scenario-check.py` includes regression fixtures for command classification, generated-refresh demotion, optional CLI facade delegation, missing setup-apply approval, and Ralph approval-needed attempt handling. These fixtures prove boundary wording and refusal behavior stay stable; they are not command approval or verification proof for unrelated work.

Active memory remains exactly:

- `AGENT.md`
- `DECISIONS.md`
- `tasks/todo.md`

## Tool-Call Classes

Use these classes when describing important tool calls:

| Class | Meaning |
|---|---|
| `read_only` | Inspects local or external state without changing it. |
| `verification` | Runs a check intended to prove behavior or integrity. |
| `generated_refresh` | Refreshes generated reports or sidecars. |
| `local_mutation` | Changes local files, dependencies, state, generated artifacts, or repo configuration. |
| `external_mutation` | Changes GitHub, CI, deployments, dashboards, hosted services, issue trackers, or other external systems. |
| `destructive` | Deletes, resets, drops, force-pushes, rolls back, migrates destructively, or otherwise risks irreversible loss. |
| `secret_bearing` | Handles secrets, tokens, credentials, dashboard values, private exports, or sensitive raw output. |

## Command Policy In Beads

When a bead expects risky tools, the bead should name:

- allowed commands
- forbidden commands
- approval-required commands
- expected side effects
- rollback, cleanup, or blocked escape notes

Low-risk doc or validation beads can rely on the normal `Checks`, `Stop If`, and `Closeout Evidence` sections. Sensitive or external work should be explicit before the command runs.

Dependency installs and other local mutations are not automatically forbidden, but they are still side effects. They may continue only when the expected files stay inside `files_in_play` and the bead does not touch a sensitive surface. Ask first when the command changes dependencies, migrations, generated authority-like files, secrets, auth, data, payments, deployment, external services, releases, or shared branches.

## Allowed Actions

Risk-triggered run contracts use allowed actions as the plain-language wrapper over capability leases. A capability lease is not new permission; it is a stricter statement of the permissions already implied by the active bead, `files_in_play`, tool-call classes, approval gates, and stop conditions.

Use a bead Run Contract when sensitive, external, destructive, or `bounded-afk` work needs tighter boundaries:

- allowed paths or actions
- allowed tool classes
- forbidden actions
- approval required before risky actions
- proof needed and re-entry evidence
- stop conditions
- expiration condition

The lease is advisory contract state. It does not override sandbox permissions, approve commands automatically, widen `files_in_play`, skip recorded proof, accept review, merge work, or bypass user approval. `python3 scripts/run-contract-check.py` warns when allowed actions are broader than the active bead or when risky or bounded-AFK work lacks proof, re-entry evidence, approval, stop, or recovery details.

Future host adapters may consume `logs/run-contract.json` or `logs/run-contract.yaml` more strictly after real use proves the advisory contract is stable. That future path would still require extension review and must not silently create command approval, runtime enforcement, package-manager behavior, or generated-output authority.

## Evidence Distinction

`logs/check-results.jsonl` is the verification ledger. It records commands run through:

```text
bash scripts/record-check.sh -- <command>
```

`logs/tool-runs.jsonl` is a general tool-use ledger. It records important tool actions that may or may not be verification evidence.

A logged tool run does not count as a passing check unless it is also recorded through `record-check.sh` or accepted in Closeout Evidence with the required manual verification format.

`python3 scripts/session-friction-check.py` runs Session Friction Review as a read-only advisory check over safe local ledgers and compiled summaries. It may flag repeated failure categories, missing failure categories, unavailable commands or dependencies, sandbox or approval blocks, stale check or closeout evidence, generated refresh without verification, reviewed-memory context pressure, or no safe evidence found. Each finding must cite source evidence, confidence, freshness, proposed destination, and a suggested next human review step. The output is generated evidence only: it must not auto-edit active memory, shims, reviewed memory, owner files, generated reports, or command wrappers, and it must not approve commands, select tasks, promote memory, accept review, or create package-manager behavior.

Guardrail checks such as `python3 scripts/files-in-play-check.py`, `python3 scripts/bead-depth-check.py`, and `python3 scripts/next-step.py` are advisory evidence. They can warn, orient, or suggest a pause, but they do not approve commands, authorize out-of-scope edits, or replace explicit user approval for sensitive or external mutation. If adaptive depth warns before a command, the agent should explain the warning's shortest next action and either fix the bead metadata, strengthen proof, ask for approval, or split scope before treating the command path as clear.

`next-step` is the canonical generated router for the next human decision. Its `load_plan`, `single_next_protocol`, and `context_footprint` fields are context-routing evidence only; they do not approve tool calls or widen allowed tool classes.

`python3 scripts/ralph-loop.py` is a bounded bead-attempt engine. It may run one explicit attempt command and a validator set, then write `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md`. Ralph does not invent commands, approve risky commands, accept work, or approve transitions.

`python3 scripts/candidate-queue.py` is an approval-gated local Candidate Queue helper. Preview modes are read-only evidence and must say `mutates_now: false`. Apply mode is local mutation and requires explicit `--apply --approve-action <ID>`; that approval is approval for queue writeback only, not PRD approval, bead activation, `tasks/todo.md` mutation, implementation permission, external mutation, or `B###` reservation.

`python3 scripts/files-in-play-check.py --command "<command summary>"` may classify a command as `continue`, `approval needed`, or `stop`. That classification is a beginner-facing stop sign, not permission. If it says approval is needed or stop, the agent must pause and ask for explicit user approval or a narrower path before running the command. If it says continue for a local mutation, keep the mutation inside `files_in_play` and stop if the command would install dependencies, widen scope, touch sensitive surfaces, or rewrite generated evidence as if it were authority.

`python3 scripts/files-in-play-check.py --edit-lock` is also advisory. It compares current changed paths with the active bead's `files_in_play` and generated-output exceptions. It does not create a filesystem lock, approve edits, or replace human review.

## Failure Categories

Use these categories for failed or blocked tool runs:

- `code_failure`
- `unavailable_command`
- `missing_dependency`
- `missing_credentials`
- `network_unavailable`
- `permission_or_sandbox_blocked`
- `user_approval_required`
- `destructive_action_blocked`
- `unknown`

Unknown is acceptable only when the failure cannot be classified yet.

## External Mutation Rules

External mutations require all of these:

- an approved bead names the external system
- the exact action or command is in scope
- the expected effect is clear
- the rollback or undo path is named, or the reason rollback is impossible is recorded
- the user approves the manual gate
- post-action evidence is recorded

For GitHub Collaboration Hub work, external mutation includes enabling or disabling Issues, changing issue templates in the live repository outside a normal code change, creating or editing labels, creating or editing project boards, assigning issues, commenting on issues or pull requests, closing issues, transferring issues, pinning or locking issues, approving pull requests, rerunning workflows, and changing repository settings. Public issue intake is source evidence; it is not approval for any of those actions.

For delegated re-entry, tool logs, agent summaries, CI status, PR status, review comments, workflow runs, and cloud-agent completion notes are evidence only. They may help fill scope returned, changed files, checks and results, manual verification, unresolved risks, external status evidence, and forbidden actions not taken, but they do not approve commands, accept implementation, approve merge, approve transition, mutate GitHub, deploy, release, or promote owner-file changes.

Scheduled audits, importers, generated reports, and advisory checks must remain read-only.

## Tool Routing Preference

Prefer the lowest-token, lowest-side-effect tool that can answer the question:

1. local text search or structured file reads for repo facts
2. read-only commands or dry-run checks for local state
3. text fetches or official docs for public web facts when current information matters
4. browser or screenshot-heavy tools only for dynamic pages, authenticated flows, visual QA, or interactions text tools cannot inspect
5. external mutation tools only when the active bead allows them and the user approves the manual gate

This preference does not replace evidence requirements. A cheap tool answer is still source material unless it is recorded through the appropriate verification path.

When a host supports subagents, map them to Precode's compact role contracts instead of broad personas. Explorer should stay read-only, Builder should stay inside files in play, and Review should judge evidence rather than continue implementation.

AI-readable indexes such as `llms.txt` are context-routing aids only. They can help an agent choose a small starting source, but current-state claims still require direct inspection of active memory, the active bead, source Markdown, or generated evidence.

## Secret Handling

Never store secrets, tokens, credentials, dashboard values, private keys, raw private transcripts, or sensitive raw command output in `logs/tool-runs.jsonl`.

If a tool touches secrets, log only that the action was `secret_bearing`, whether it was approved, and where safe redacted evidence lives.

Do not store long raw command output, secrets, credentials, or dashboard values in Ralph attempt logs. Store short summaries and safe output references only.

## Logging Tool Runs

Use:

```text
bash scripts/log-tool-run.sh --tool <tool> --class <class> --status <pass|fail|blocked> --command "<summary>"
```

Use `--dry-run` before writing when checking the shape.

Prefer concise command summaries over raw shell with secrets or private paths. Use `output_ref` only for safe, redacted artifacts.

## Advisory Check

`scripts/tool-execution-check.py` is advisory. It may warn about approval gaps, destructive actions, missing failure categories, vague checks, generated refresh without verification evidence, or stale command evidence.

Warnings are generated evidence only. They do not approve tool calls, select tasks, or replace user judgment.
