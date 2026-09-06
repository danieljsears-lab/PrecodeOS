# PrecodeOS
<!-- ANCHOR: readme -->

> AUTHORITY: Public GitHub landing page, beginner-first orientation, quickstart, support boundary, and curated navigation for PrecodeOS.
> NOT_AUTHORITY: Active memory, task selection, PRD approval, bead activation, generated evidence, implementation status, package update permission, or maintainer-private roadmap authority.
> LOAD_WHEN: A user, contributor, reviewer, or AI assistant needs the public package compass before choosing a more specific guide or protocol.
> CLASS: reference

[![Precode Validate](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml/badge.svg)](https://github.com/danieljsears-lab/PrecodeOS/actions/workflows/precode-validate.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

## Start Here

PrecodeOS is a repo-native control layer that helps people shape ideas and develop software with AI coding agents while keeping intent, scope, evidence, approval, and recovery visible to the human builder.

Use one route:

1. Not installed: open [Guided Setup](docs/PRECODE-GUIDED-SETUP.md).
2. Installed: open the [Daily Cockpit](docs/PRECODE-DAILY-COCKPIT.md).
3. Rough idea: in the Daily Cockpit, say `Ideation: use First PRD Walkthrough for my rough idea.`
4. Broken or confusing state: open [Troubleshooting](docs/PRECODE-TROUBLESHOOTING.md) or say `I am stuck, help me.`

`README.md` is the compass. Guided Setup owns setup. Daily Cockpit is the normal operating surface. User Guide is the annex. Troubleshooting owns symptom lookup. Do not read them as competing start pages.

## V1 Support Boundary

The September 2026 v1 self-serve claim is deliberately bounded to **installation, validation, orientation, and next-safe-action identification**. PrecodeOS supports production-readiness governance and professional output quality; it does not guarantee that an unassisted user can complete the full idea-to-production journey, and deployment or operations remain optional ecosystem capabilities.

| Surface | V1 position | Evidence boundary |
|---|---|---|
| Audience | Nontechnical and semi-technical AI-assisted builders | Nontechnical no-help readiness remains gated by external sessions |
| Platform | macOS certified | Windows remains preview until platform-specific setup and recovery testing |
| Acquisition | npm primary | GitHub/local Python is the transparent advanced fallback |
| Codex | Certified for launch | Conformance-certified; external no-help result pending |
| Claude Code | Certified for launch | Conformance-certified; external no-help result pending |
| Cursor | Certified for launch | Conformance-certified; external usability evidence pending |
| Gemini | Certified for launch | Conformance-certified; external usability evidence pending |

Certification means the Precode instruction, approval, validation, recovery, and output contract conforms on the named host. It does not claim equal usability evidence across hosts.

## Quickstart

Give a certified coding agent this prompt from the project you want to use:

```text
Set up PrecodeOS in this project using the official npm package.

Identify and confirm this project folder as the target. Run:
npx @precodeos/precodeos fast-setup-preview --target <target-project-root>

Explain the package version, support status, prerequisites, target classification, proposed actions, approval IDs, validation requirements, recovery route, next safe action, and stop reason in plain English.

Do not mutate the target until I approve named current actions. Apply only the approved SP-ID or UP-ID values. Treat owner-file adaptation as a separate approval. Validate, route me to the First Session Card or Daily Cockpit, and stop before product work.
```

Preview is read-only. The agent may propose this apply command only after showing current actions and receiving explicit approval:

```bash
npx @precodeos/precodeos fast-setup-apply --target <target-project-root> --approve-action <SP-ID|UP-ID>
```

The npm entry is a transparent Node facade over the package's Python setup authority. It has no postinstall mutation, does not overwrite existing paths, does not adapt owner files, and does not install hooks, change CI, run app code, select tasks, approve PRDs, activate beads, or approve product work. A generated `ready_for_orientation` result, when available, is evidence only.

For npm failure or advanced inspection, use the [GitHub and local Python fallback in Guided Setup](docs/PRECODE-GUIDED-SETUP.md#advanced-github-and-python-fallback). Do not make GitHub cloning or Python command knowledge a beginner prerequisite.

## What It Does

PrecodeOS gives an AI-assisted project a durable, inspectable operating model:

- tiny active memory across `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`
- one active bead with bounded files in play
- one owner per durable product, architecture, API, data, security, or acceptance fact
- explicit human approval at setup, product, review, transition, release, and risky-action gates
- checks and manual verification over agent confidence
- recovery-before-momentum behavior
- generated output as evidence, never authority
- thin tool adapters over one shared core

It is intentionally not an agent runtime, dashboard, sandbox, hosted control plane, registry, marketplace, package manager, telemetry system, or role-agent framework.

## Who It Is For

PrecodeOS is for builders who can open a project folder and use a certified coding agent but should not need Git internals, Python knowledge, shell fluency, or approval-ID interpretation.

Use it when work is durable, user-facing, sensitive, multi-file, hard to prove, or likely to span sessions. Skip it for a throwaway sketch where mistakes are cheap and nothing needs durable ownership.

The evidence does not yet support an unqualified “creates production-grade software” claim. The narrower claim is useful and defensible: PrecodeOS supplies production-readiness governance and professional-quality decision, scope, proof, review, and recovery surfaces. The project still needs its own implementation, testing, security, deployment, and operational competence.

## Core Invariants

- **Tiny active memory:** load only what the current session needs.
- **One active unit:** a bead, not chat momentum, defines current work.
- **One owner per fact:** durable truth has a named home.
- **Design judgment before code:** shape intent and acceptance before implementation.
- **Evidence over confidence:** recorded checks and manual verification support completion claims.
- **Generated output is not authority:** reports summarize; they do not decide.
- **Human approval at transitions:** agents propose; humans approve.
- **Tool-neutral core:** adapters translate the same operating model.

## Capability Snapshot

| Builder job | Capability | V1 evidence posture |
|---|---|---|
| Adopt | Agent-operated npm preview/apply, target classification, Existing Repo Intake, recovery | Launch-critical |
| Orient | First Session Card, Daily Cockpit, tiny active memory, next-step guidance | Launch-critical |
| Shape | Idea coach, Product Brief, Conviction Packet, Local Source Intake | Structurally present; full self-serve spine not demonstrated |
| Specify | PRDs, acceptance, conditional architecture shaping, owner files | Stronger for semi-technical builders |
| Build | One active bead, files-in-play guardrails, recorded tool/check evidence | Requires project-specific technical capability |
| Review | Review lanes, quality guidance, release-readiness evidence, human gates | Advisory; does not accept or release |
| Recover | Troubleshooting, state checks, checkpoints, blocked escape paths | Core product promise |

## First Product Spine

```text
Idea -> Brief -> Packet -> Intake -> Owner Files? -> PRD -> Architecture? -> Bead -> Proof -> Review -> Close
```

`Owner Files?` is the reviewed promotion gate for stable facts. `Architecture?` is conditional for auth, data, APIs, integrations, migrations, external services, or other meaningful technical risk. Six setup-and-orientation sessions do not prove this complete spine; it requires separate validation.

## Project Map

| Area | Location |
|---|---|
| Active memory | `AGENT.md`, `DECISIONS.md`, `tasks/todo.md` |
| Owner truth | `PRODUCT.md`, `PROJECT-CONTEXT.md`, `FEATURES.md`, `ACCEPTANCE.md`, `ARCHITECTURE.md`, `API.md`, `DATA-MODELS.md`, `SECURITY.md`, `CODEBASE-GUIDE.md` |
| Work | `CANDIDATE-QUEUE.md`, `tasks/prds/`, `tasks/beads/`, `tasks/templates/` |
| Protocols and prompts | `tasks/reference/` |
| Agent compatibility | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `adapters/` |
| Validation and evidence | `scripts/`, `logs/`, generated health and progress reports |

The npm package excludes PrecodeOS's live `tasks/todo.md`, package-development PRDs, package-development beads, and generated PRD HTML. It includes a clean todo template instead. Package-development state remains in the public source repository for transparency but is not distributed as target-project state.

## Docs Compass

| Need | Open |
|---|---|
| Install or recover setup | [Guided Setup](docs/PRECODE-GUIDED-SETUP.md) |
| Run daily work | [Daily Cockpit](docs/PRECODE-DAILY-COCKPIT.md) |
| Use a one-page first session | [First Session Card](tasks/templates/PRECODE-FIRST-SESSION-CARD.md) |
| Get deeper operating guidance | [User Guide](docs/PRECODE-USER-GUIDE.md) |
| Understand the model | [OS README](docs/PRECODE-OS-README.md) |
| Learn the software-building bridge | [How To Build Software With Precode](docs/HOW-TO-BUILD-SOFTWARE-WITH-PRECODE.md) |
| Diagnose a symptom | [Troubleshooting](docs/PRECODE-TROUBLESHOOTING.md) |
| Find an owner or file contract | [Package File Inventory](docs/PRECODE-PACKAGE-FILE-INVENTORY.md) |
| Browse prompts | [Prompt Patterns](tasks/reference/PROMPT-PATTERNS.md) |
| Select one workflow | [Workflow Selection Protocol](tasks/reference/WORKFLOW-SELECTION-PROTOCOL.md) |

Do not begin by browsing every protocol. Start from the route that matches the current moment and load one deeper surface only when needed.

## For Agents

Load `AGENT.md`, `DECISIONS.md`, and `tasks/todo.md`, then explain the active bead, primary authority, files in play, checks, and stop conditions before editing.

Treat generated reports as evidence. Before sensitive, destructive, external, dependency, or broad cleanup work, name the access level and ask for explicit approval. If setup or state is confusing, route to Guided Setup or Troubleshooting instead of guessing.

## For Reviewers And Contributors

Useful checks:

```bash
bash scripts/validate-memory.sh
python3 scripts/version-check.py
python3 scripts/file-inventory.py --check
python3 scripts/bootstrap-check.py --self-test
python3 scripts/adapter-conformance-check.py
python3 scripts/npm-package-check.py
python3 scripts/package-knowledge-lint.py --check
python3 scripts/clarity-scenario-check.py
```

See [Contributing](CONTRIBUTING.md), [Governance](GOVERNANCE.md), and [Trademark](TRADEMARK.md). Generated checks support review; they do not approve changes, merge, release, or publishing.

## FAQ

### Is PrecodeOS an app?

No. It is a repo-native package of Markdown authority files, task contracts, scripts, generated evidence rules, and thin adapters.

### Does it replace the coding agent?

No. The agent executes scoped work. PrecodeOS keeps durable intent, proof, approval, and recovery visible across tools and sessions.

### What is a bead?

A bead is one bounded unit of work with scope, owner files, checks, stop conditions, and closeout evidence.

### Are generated reports authority?

No. They are evidence and navigation only.

### Is v1 ready for nontechnical self-serve use?

Not yet proven. The launch gate requires three of three safe no-help completions for that persona. If only semi-technical participants pass, v1 will narrow its self-serve audience and keep nontechnical adoption in preview or guided use.

## Release Status

The package remains prerelease until the September launch gates pass. Safety, authority integrity, package integrity, truthful claims, orientation, and recovery are pass/fail gates; roadmap scores cannot compensate for failure.

## License, Trademark, And Provenance

PrecodeOS is open source under Apache License 2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE), and [TRADEMARK.md](TRADEMARK.md).

Created by Dan Sears / Recode. Canonical site: <https://www.precodeos.org>.

## Document Metadata

Creator: Dan Sears / Recode
License: Apache-2.0
Copyright: © 2026 Dan Sears / Recode
Document version: v0.2.0
Last updated: 2026-09-06
