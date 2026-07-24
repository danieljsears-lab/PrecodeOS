# PrecodeOS — Security
<!-- ANCHOR: security -->

> AUTHORITY: Security template for target projects plus package-level security posture for the PrecodeOS package itself.
> NOT_AUTHORITY: Feature prioritization, route inventory, schema field ownership, or active task selection.
> LOAD_WHEN: Work touches auth, payments, personal data, uploads, destructive actions, external integrations, secrets, production configuration, package copy/apply behavior, local command execution, generated evidence, GitHub helpers, CI, or the optional local CLI facade.
> CLASS: reference

Creator: Dan Sears / Recode
Document version: v0.2.2
Last updated: 2026-06-19

## Purpose

This file has two roles:

- In a target project, it is the owner template for that project's security, privacy, auth, and sensitive-surface rules.
- In the PrecodeOS package, it records the package security posture for local scripts, setup/copy helpers, generated evidence, adapters, GitHub helpers, CI, and the optional local command facade.

Do not store secrets, credentials, private keys, dashboard values, production configuration, private customer records, or sensitive raw exports in this file.

## Sensitive Surfaces

- Auth:
- Payments:
- Personal data:
- Uploads:
- Secrets:
- External services:
- Destructive actions:

## PrecodeOS Package Security Posture

PrecodeOS is a repo-native package, not a hosted app runtime. Its main package-security risks are local filesystem mutation, command execution, generated evidence being mistaken for authority, setup/copy boundaries, Git/GitHub helper behavior, and public/private publishing hygiene.

Confirmed package constraints:

- Runtime dependencies: none declared in `pyproject.toml`.
- Local CLI: `scripts/precode_cli.py` is a facade over curated repo commands and must print underlying commands before running them.
- Setup mutation: `scripts/bootstrap-check.py` apply modes must require explicit approved action IDs and refuse broad copy, overwrite, owner-file adaptation, hook/CI installation, app-code edits, executable release-channel behavior, package-manager behavior, and rollback automation. Advisory release-reference metadata in upgrade preview is generated evidence only; it is not update permission or npm updater behavior.
- Generated evidence: files under `logs/`, `OS-HEALTH.md`, `PRECODE-HELP.md`, `PROGRESS.md`, generated docs, and generated PRD review pages must not approve tasks, commands, transitions, releases, or implementation acceptance.
- External systems: GitHub helpers and scheduled audits are read-only by default unless a separate approved path explicitly allows mutation.
- CI: GitHub Actions should use least privilege, preserve read-only validation unless an explicit maintainer decision changes it, and must not require secrets for ordinary package validation.

Deterministic local regression fixtures cover the main copy and command boundaries: setup/apply refusal, upgrade/apply refusal, overwrite refusal, unknown or non-copy action IDs, secret/local/generated path exclusions, optional CLI facade command visibility, Ralph approval-needed command handling, and generated-refresh evidence demotion. These fixtures protect refusal behavior; they are not vulnerability certification, command approval, release approval, or external-system evidence.

## Package Security Review Expectations

For package-facing changes, review whether the change affects:

- command execution, subprocess calls, shell helpers, or command wrappers
- copy, restore, checkpoint, setup, upgrade, cleanup, or generated refresh behavior
- secrets, credentials, env files, private keys, certificates, dashboards, production config, or sensitive raw evidence
- GitHub, CI, external status, importers, scheduled audits, or other external systems
- generated reports, sidecars, HTML surfaces, or evidence ledgers that could be mistaken for authority
- package install/update boundaries, executable release channels, optional packs, registries, or package-manager semantics

Use this baseline for repeatable package-security review:

- Identify the package surface being changed and the primary owner file or script.
- Check the package threat surfaces above before relying on generic scanner output.
- Run relevant repo validation and any installed advisory scanners.
- If an advisory scanner is unavailable, record it as unavailable instead of silently skipping it.
- Review scanner output manually before treating it as a finding.
- Promote confirmed findings through the appropriate owner file, PRD, approved bead, or maintainer roadmap decision.
- Keep generated reports, scanner output, and maintainer-local notes as evidence until a human promotes a conclusion.

Security review does not certify that PrecodeOS is free of vulnerabilities. It does not approve release, compliance, production safety, external mutation, follow-up task creation, command execution, PRD approval, bead activation, or implementation acceptance.

## Advisory Scanner Set

When the tools are installed, a maintainer may run this advisory local scan set:

```bash
python3 -m pip_audit
bandit -r scripts
shellcheck scripts/*.sh
gitleaks detect --source .
actionlint .github/workflows/precode-validate.yml
```

If a tool is unavailable, record it as unavailable instead of silently skipping it or installing dependencies without approval. Review scanner output manually before treating it as a real finding.
