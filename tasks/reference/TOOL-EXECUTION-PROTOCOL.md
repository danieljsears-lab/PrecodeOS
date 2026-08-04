# PrecodeOS -- Tool Execution Protocol
<!-- ANCHOR: tool-execution-protocol -->

> AUTHORITY: Tool-call classes, command policy expectations, non-check tool logging, failure categories, external mutation rules, secret handling, and tool-execution advisory checks for PrecodeOS.
> NOT_AUTHORITY: Active memory expansion, task selection, product decisions, implementation plans, automatic command approval, generated progress state, or automatic bead transitions.
> LOAD_WHEN: Choosing, recording, reviewing, or approving tool calls; adding tool integrations; handling command failures; or distinguishing tool use from verification evidence.
> CLASS: reference

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.1.23
Last updated: 2026-08-04

## Purpose

Tool execution keeps Precode honest about what an agent actually ran.

A command can be useful without proving the work is done. Precode separates:

- tool use: an action happened
- verification evidence: a check proved something and was recorded
- user approval: a human approved a risky action

Tool execution is part of PrecodeOS's advisory repo-native harness contract. Command classes, run contracts, generated sidecars, recorded checks, and transparent facades make agent work inspectable, but they are not an agent runtime, sandbox, command approval layer, registry, optional pack, package manager, install/update system, or enforcement layer. Internally, command classification and files-in-play guardrail assembly live behind `scripts/precode_commands.py` while `scripts/os_compiler.py` remains the stable compiler facade.

Use `tasks/reference/AGENT-ROUTING-PROTOCOL.md` when choosing between low-token read-only tools, browser or screenshot-heavy tools, delegated agents, and external mutation tools.

Use `tasks/reference/RALPH-LOOP-PROTOCOL.md` when a host or user wants a bounded retry loop around one active bead. Ralph can record attempts and validators, but it is still subject to this protocol's command classes and approval rules.

Use `tasks/prds/PRD-043-agent-access-level-guidance.md` when changing the plain-language access model itself. Access levels are guidance over the existing tool-call classes, `files_in_play`, Run Contracts, approval gates, and stop conditions. They are not permission grants, runtime enforcement, sandbox policy, command approval, schema-backed access metadata, or host-plugin configuration.

Use `scripts/precode_cli.py`, the optional local `precode` console command, or the optional npm `precodeos` entry only as a facade over trusted repo commands. A wrapper command inherits the underlying command's tool-call class, approval gates, side effects, and evidence limits. It must print the underlying command before running it and must not approve work, hide mutation, widen files in play, mutate external systems, define package update behavior, define release-channel behavior, or make generated output authoritative. The npm entry is limited to read-only setup, fast verified setup, upgrade, and update-plan previews plus `fast-setup-apply` delegation for explicitly approved current `SP-ID` or `UP-ID` copy actions and `apply-package-owned` delegation for explicitly approved missing package-owned `UP-ID` actions. It must not expose postinstall target mutation, dirty-file overwrite, owner-file adaptation, registry lookup, dist-tag resolution, channel selection, rollback automation, or package-manager behavior. Updater compatibility policy metadata is evidence interpretation governed by `tasks/prds/PRD-041-npm-updater-evidence-and-compatibility-policy.md`; update-plan preview metadata is grouped generated evidence governed by `tasks/prds/PRD-042-npm-update-plan-preview.md`; approved package-owned apply is governed by `tasks/prds/PRD-047-npm-approved-package-owned-apply.md`. None of these metadata or facade paths is a registry lookup, dist-tag resolver, channel selector, or package-manager permission.

Bootstrap setup diagnosis is command output evidence. It can name source/target clarity, target state, partial setup classification, recommended route, validation-after-apply, and forbidden next actions, but it does not approve command execution, copying, repair, rollback, setup/update mutation, product work, or package-manager behavior.

Command surface triage is reader guidance only. Grouping commands by beginner daily work, setup/support/recovery, advanced evidence/review, and maintainer validation does not change tool-call classes, approve commands, choose tasks, create a router or registry, expand wrapper behavior, or make generated output authoritative. Beginner-facing command surfaces should expose advanced command families as trigger summaries and route detailed use to Prompt Patterns or the owner protocol instead of becoming a script menu.

The Authority Map Query CLI is a read-only navigation command for maintainer, contributor, and AI-assistant orientation over existing authority-map contracts. `python3 scripts/authority-map-query.py` and the transparent `precode authority-map` facade may identify candidate owner files, surface classes, authority, non-authority, and load triggers, but the output does not approve commands, choose tasks, replace owner files, approve PRDs, activate beads, enforce runtime behavior, or create package-manager behavior.

Product Code Quality Snapshot may discover likely project-owned lint/check commands from manifests or common config files, but that discovery is not command approval. `python3 scripts/product-code-quality-snapshot.py` does not run lint, tests, typechecks, package managers, fixers, or app code. Running any suggested command remains a separate user-approved tool action under this protocol.

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

## Agent Access Levels

Use these plain access levels when a builder asks what an agent may do right now. They translate command risk into beginner-readable language while preserving the existing tool-call classes as the canonical machine-readable vocabulary.

| Access level | Plain meaning | Existing Precode mapping | Human gate |
|---|---|---|---|
| `inspect` | The agent may read local or external information without changing it. | `read_only`; active memory, owner files, source evidence, and generated reports as evidence only. | Ask if the source may contain secrets or private data. |
| `verify` | The agent may run checks intended to prove behavior or package integrity. | `verification`; record through `record-check.sh` when used as proof. | Ask if the check is expensive, external, secret-bearing, or mutating. |
| `local-change` | The agent may change local files inside the approved bead boundary. | `local_mutation`; `files_in_play`; active bead scope. | Ask before dependency installs, generated authority-like rewrites, scope widening, or sensitive surfaces. |
| `sensitive` | The agent may prepare or inspect sensitive work only after the risk and proof path are explicit. | `secret_bearing` or sensitive-surface local mutation; `SECURITY.md`; Run Contract when needed. | Explicit approval before secrets, credentials, auth, private data, payments, security config, or dashboard values. |
| `external-change` | The agent may change a hosted service, GitHub, CI, deployment, dashboard, issue tracker, release, or shared branch only after approval. | `external_mutation`; external mutation rules; Run Contract when needed. | Explicit approval naming action, affected system, recovery path, and evidence. |
| `destructive` | The agent must stop before irreversible or hard-to-reverse work. | `destructive`; deletion, reset, drop, force-push, destructive migration, rollback. | Stop until the user explicitly approves the exact command, expected effect, rollback or blocked escape, and evidence plan. |

If multiple levels apply, use the highest-risk level. For example, a local edit in `SECURITY.md` is not merely `local-change`; it is sensitive work and needs the matching approval and proof path. Access levels do not override sandbox permissions, broaden `files_in_play`, approve commands, accept implementation, approve review, merge work, deploy, release, or activate another bead.

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

Future host adapters may consume `logs/run-contract.json` or `logs/run-contract.yaml` more strictly after real use proves the advisory contract is stable. That future path would still require extension review and must not silently create command approval, runtime enforcement, package-manager behavior, executable release-channel behavior, or generated-output authority.

## Evidence Distinction

`logs/check-results.jsonl` is the verification ledger. It records commands run through:

```text
bash scripts/record-check.sh -- <command>
```

`logs/tool-runs.jsonl` is a general tool-use ledger. It records important tool actions that may or may not be verification evidence.

A logged tool run does not count as a passing check unless it is also recorded through `record-check.sh` or accepted in Closeout Evidence with the required manual verification format.

`python3 scripts/session-friction-check.py` runs Session Friction Review as a read-only advisory check over safe local ledgers and compiled summaries. It may flag repeated failure categories, missing failure categories, unavailable commands or dependencies, sandbox or approval blocks, stale check or closeout evidence, generated refresh without verification, reviewed-memory context pressure, or no safe evidence found. Each finding must cite source evidence, confidence, freshness, proposed destination, and a suggested next human review step. The output is generated evidence only: it must not auto-edit active memory, shims, reviewed memory, owner files, generated reports, or command wrappers, and it must not approve commands, select tasks, promote memory, accept review, or create package-manager behavior.

`python3 scripts/usage-evidence-review.py`, `precode usage-evidence-review`, and `precodeos usage-evidence-review` run Local Opt-In Usage Evidence Review under `tasks/prds/PRD-048-precode-usage-evidence-review.md`. The review is local, opt-in, read-only, no-write, no-submit, no-network, and explicit about unknowns by default. It may summarize safe local Precode evidence such as tool-run categories, check freshness, setup/refresh preview signals when present, generated-report freshness, scheduled-audit presence, session-friction findings, loop-run presence, and spend-import presence, but it must not collect raw transcripts, secrets, app logs, app analytics, dashboard values, production data, user identity records, support case records, contributor scoring, productivity ranking, or long raw command output. The output is generated evidence only: it must not prove adoption, choose roadmap work, approve PRDs or beads, accept implementation, approve release, create support records, submit evidence, create issues, authorize telemetry, or mutate external systems. `python3 scripts/sanitized-evidence-pack.py --template` may print the submitted-packet shape and `python3 scripts/sanitized-evidence-pack.py --review <packet-file>` may review a user-supplied packet locally, but that helper must not write packet files, submit to GitHub, create issues, call hosted endpoints, approve promotion, create support records, authorize telemetry, or mutate external systems. `python3 scripts/cohort-support-evidence-rollup.py --packet <packet-file>` and `precode cohort-support-rollup --packet <packet-file>` aggregate only explicit packet files supplied by path or glob; they must not scan the repo by default, write rollup files, submit evidence, create issues, call endpoints, create support records, grade builders, score contributors, prove adoption, choose roadmap work, approve PRDs or beads, accept implementation, authorize telemetry, or mutate external systems. Any outbound analytics or network submission is external-system work and requires a separate approved readiness gate plus explicit user submission or approval.

Guardrail checks such as `python3 scripts/files-in-play-check.py`, `python3 scripts/bead-depth-check.py`, and `python3 scripts/next-step.py` are advisory evidence. They can warn, orient, or suggest a pause, but they do not approve commands, authorize out-of-scope edits, or replace explicit user approval for sensitive or external mutation. If adaptive depth warns before a command, the agent should explain the warning's shortest next action and either fix the bead metadata, strengthen proof, ask for approval, or split scope before treating the command path as clear.

`next-step` is the canonical generated router for the next human decision. Its `load_plan`, `single_next_protocol`, and `context_footprint` fields are context-routing evidence only; they do not approve tool calls or widen allowed tool classes.

`python3 scripts/ralph-loop.py` is a bounded bead-attempt engine. It may run one explicit attempt command and a validator set, then write `logs/ralph-attempts.jsonl` and `logs/ralph-summary.md`. Ralph does not invent commands, approve risky commands, accept work, or approve transitions.

`python3 scripts/candidate-queue.py` is an approval-gated local Candidate Queue helper. Preview modes are read-only evidence and must say `mutates_now: false`. Apply mode is local mutation and requires explicit `--apply --approve-action <ID>`; that approval is approval for queue writeback only, not PRD approval, bead activation, `tasks/todo.md` mutation, implementation permission, external mutation, or `B###` reservation.

`python3 scripts/files-in-play-check.py --command "<command summary>"` may classify a command as `continue`, `approval needed`, or `stop` and may expose the matching access level. That classification is a beginner-facing stop sign, not permission. If it says approval is needed or stop, the agent must pause and ask for explicit user approval or a narrower path before running the command. If it says continue for a local mutation, keep the mutation inside `files_in_play` and stop if the command would install dependencies, widen scope, touch sensitive surfaces, or rewrite generated evidence as if it were authority.

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
