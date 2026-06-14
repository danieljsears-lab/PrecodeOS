#!/usr/bin/env python3
# Version: v0.1.1
# Last updated: 2026-06-14
# Owner: PrecodeOS
# Created by Dan Sears / Recode.
# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

import argparse
import json
from typing import Any

from os_compiler import compile_state, repo_root


def matches_query(card: dict[str, Any], query: str) -> bool:
    terms = [term for term in query.lower().split() if term]
    if not terms:
        return True
    search_text = str(card.get("search_text") or "").lower()
    return all(term in search_text for term in terms)


def filter_cards(cards: list[Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    for item in cards:
        if not isinstance(item, dict):
            continue
        if args.query and not matches_query(item, args.query):
            continue
        if args.category and item.get("category") != args.category:
            continue
        if args.freshness and item.get("freshness") != args.freshness:
            continue
        if args.status and item.get("status") != args.status:
            continue
        if args.needs_promotion and item.get("status") != "needs_promotion":
            continue
        selected.append(item)
    return selected


def filtered_payload(payload: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    details = payload.get("details") if isinstance(payload.get("details"), dict) else {}
    cards = details.get("cards") if isinstance(details.get("cards"), list) else []
    selected = filter_cards(cards, args)

    if not any([args.query, args.category, args.freshness, args.status, args.needs_promotion]):
        payload["search"] = {
            "filtered": False,
            "matched_cards": len(cards),
            "total_cards": len(cards),
            "generated_evidence_only": True,
        }
        return payload

    next_details = dict(details)
    next_details["cards"] = selected
    next_details["card_count"] = len(selected)
    next_details["current_cards"] = [
        card for card in selected if card.get("freshness") in {"current", "watch"} and card.get("status") == "reviewed"
    ]
    next_details["promotion_needed_cards"] = [card for card in selected if card.get("status") == "needs_promotion"]
    next_details["stale_or_superseded_cards"] = [
        card for card in selected if card.get("freshness") in {"stale", "superseded"} or card.get("status") in {"superseded", "archived"}
    ]
    next_details["low_confidence_cards"] = [card for card in selected if card.get("confidence") == "low"]
    next_details["promotion_needed"] = [str(card.get("path")) for card in next_details["promotion_needed_cards"]]
    next_details["stale_or_superseded"] = [str(card.get("path")) for card in next_details["stale_or_superseded_cards"]]

    next_payload = dict(payload)
    next_payload["details"] = next_details
    next_payload["search"] = {
        "filtered": True,
        "query": args.query or "",
        "category": args.category or "",
        "freshness": args.freshness or "",
        "status": args.status or "",
        "needs_promotion": bool(args.needs_promotion),
        "matched_cards": len(selected),
        "total_cards": len(cards),
        "generated_evidence_only": True,
        "safe_next_step": "Cite matching cards, then verify against active memory, the active bead, and the relevant owner file before acting.",
    }
    return next_payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Search or audit reviewed Precode memory cards without mutating state.")
    parser.add_argument("--query", help="Search title, summary, topics, category, source pointers, and glossary text.")
    parser.add_argument("--category", help="Filter by reviewed memory category.")
    parser.add_argument("--freshness", help="Filter by freshness: current, watch, stale, or superseded.")
    parser.add_argument("--status", help="Filter by status: reviewed, needs_promotion, superseded, or archived.")
    parser.add_argument("--needs-promotion", action="store_true", help="Show only cards that need owner-file promotion review.")
    args = parser.parse_args()

    state = compile_state(repo_root())
    payload = state.get("memory") or {
        "status": "missing",
        "generated_report_warning": "Reviewed memory search is generated evidence only.",
        "warnings": ["filesystem memory summary unavailable"],
        "details": {},
    }
    print(json.dumps({"tool": "memory-check", **filtered_payload(payload, args)}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
