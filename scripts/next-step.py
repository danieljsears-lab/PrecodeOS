#!/usr/bin/env python3
# Version: v0.1.4
# Last updated: 2026-05-08
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json

from os_compiler import compile_state, repo_root


def render(payload: dict[str, object]) -> str:
    details = payload.get("details") or {}
    warnings = payload.get("warnings") or []
    blockers = details.get("blockers") or []
    goal_frame = details.get("goal_frame") or {}
    user_decision = str(details.get("user_decision") or "repair state")
    decision_label = user_decision[:1].upper() + user_decision[1:]
    summary = details.get("plain_english_summary", details.get("recommended_action", "repair active state before continuing"))
    lines = [
        f"{decision_label}: {summary}",
        f"- What to do now: {summary}",
        f"- User decision: `{user_decision}`",
        f"- Active bead: `{details.get('current_bead', 'missing')}`",
        f"- State: `{details.get('current_bead_status', 'missing')}`",
        f"- Recommended action: {details.get('recommended_action', 'repair active state before continuing')}",
        f"- Category: `{details.get('action_category', 'unknown')}`",
        f"- Stop if: {details.get('stop_if', 'stop if workflow, scope, evidence, or approval is unclear')}",
        f"- Needs review: {details.get('needs_review', False)}",
        f"- Needs transition approval: {details.get('needs_transition', False)}",
        f"- Next bead: `{details.get('next_bead', 'not recorded')}`",
    ]
    if goal_frame:
        lines.extend(
            [
                "- Goal Frame:",
                f"  - Status: `{goal_frame.get('status', 'missing')}`",
                f"  - Owner: `{goal_frame.get('path', 'not recorded')}`",
                f"  - Horizon: `{goal_frame.get('horizon', 'not recorded')}`",
                f"  - Workflow guidance: `{goal_frame.get('workflow_guidance', 'not recorded')}`",
                f"  - Goal: {goal_frame.get('goal', 'not recorded')}",
                f"  - Advisory: {details.get('goal_frame_advisory', 'Goal Frames are advisory only.')}",
            ]
        )
    approval_prompt = details.get("approval_prompt")
    if approval_prompt:
        lines.append(f"- Approval prompt: {approval_prompt}")
    recovery_flow = str(details.get("recovery_flow") or "none")
    beginner_prompt = str(details.get("beginner_prompt") or "")
    if recovery_flow != "none" and beginner_prompt:
        lines.extend(
            [
                "- Recovery:",
                f"  - Flow: `{recovery_flow}`",
                f"  - Protocol: `{details.get('recovery_protocol', 'tasks/reference/RECOVERY-PROTOCOL.md')}`",
                f"  - Beginner prompt: {beginner_prompt}",
            ]
        )
    if blockers:
        lines.append("\nBlockers:")
        lines.extend(f"- {blocker}" for blocker in blockers)
    if warnings:
        lines.append("\nWarnings:")
        lines.extend(f"- {warning}" for warning in warnings)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show generated next-step guidance for the current Precode workspace.")
    parser.add_argument("--json", action="store_true", help="print machine-readable next-step guidance")
    args = parser.parse_args()

    payload = compile_state(repo_root()).get("next_step") or {
        "status": "warning",
        "warnings": ["next-step guidance unavailable"],
        "details": {},
    }
    if args.json:
        print(json.dumps({"tool": "next-step", **payload}, indent=2, sort_keys=True))
    else:
        print(render(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
