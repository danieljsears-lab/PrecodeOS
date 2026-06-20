#!/usr/bin/env python3
# Version: v0.1.2
# Last updated: 2026-06-20
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


def query_terms(query: str) -> list[str]:
    return [term for term in query.lower().split() if term]


def recall_score(card: dict[str, Any], terms: list[str]) -> int:
    search_text = str(card.get("search_text") or "").lower()
    return sum(1 for term in terms if term in search_text)


def recall_snippet(card: dict[str, Any], terms: list[str], limit: int = 420) -> str:
    source = " ".join(
        str(card.get(field) or "")
        for field in ["summary", "glossary_excerpt", "export_summary"]
    ).strip()
    source = " ".join(source.split())
    if not source:
        return ""

    lower_source = source.lower()
    hit_positions = [lower_source.find(term) for term in terms if term and lower_source.find(term) >= 0]
    if not hit_positions:
        return source[:limit]

    start = max(0, min(hit_positions) - 120)
    end = min(len(source), start + limit)
    prefix = "..." if start > 0 else ""
    suffix = "..." if end < len(source) else ""
    return f"{prefix}{source[start:end]}{suffix}"


def demotion_reason(card: dict[str, Any]) -> str:
    reasons: list[str] = []
    if card.get("confidence") == "low":
        reasons.append("low confidence")
    if card.get("freshness") in {"stale", "superseded"}:
        reasons.append(f"{card.get('freshness')} freshness")
    if card.get("status") in {"archived", "superseded"}:
        reasons.append(f"{card.get('status')} status")
    if card.get("status") == "needs_promotion":
        reasons.append("needs owner-file promotion before authority")
    return "; ".join(reasons) if reasons else "none"


def selective_recall(cards: list[dict[str, Any]], args: argparse.Namespace) -> dict[str, Any]:
    terms = query_terms(args.query or "")
    if not terms:
        return {
            "mode": "selective_recall",
            "status": "no_query",
            "no_useful_memory_found": True,
            "reason": "Selective recall requires --query so it does not force weak memory into context.",
            "generated_evidence_only": True,
        }

    scored: list[tuple[int, dict[str, Any]]] = []
    for card in cards:
        score = recall_score(card, terms)
        if score > 0:
            scored.append((score, card))

    scored.sort(key=lambda item: (-item[0], str(item[1].get("path") or "")))
    selected = scored[: max(1, args.limit)]
    recalls: list[dict[str, Any]] = []
    for score, card in selected:
        recalls.append(
            {
                "path": card.get("path"),
                "title": card.get("title"),
                "memory_space": card.get("memory_space", "default"),
                "score": score,
                "snippet": recall_snippet(card, terms),
                "citation": card.get("citation"),
                "demotion": demotion_reason(card),
                "generated_evidence_only": True,
            }
        )

    return {
        "mode": "selective_recall",
        "status": "matches" if recalls else "no_match",
        "query": args.query or "",
        "terms": terms,
        "limit": args.limit,
        "matched_cards": len(scored),
        "returned_snippets": len(recalls),
        "no_useful_memory_found": not recalls,
        "recalls": recalls,
        "search_method": {
            "keyword": "implemented",
            "semantic": "deferred_optional_extension",
            "hybrid_backend": "deferred; no Postgres, pgvector, Docker, MCP, REST API, or shared backend required",
        },
        "safe_next_step": "Use only the cited snippets, then verify against active memory, the active bead, and the relevant owner file before acting.",
        "generated_evidence_only": True,
    }


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
    token_budget = details.get("token_budget") if isinstance(details.get("token_budget"), dict) else {}

    if not any([args.query, args.category, args.freshness, args.status, args.needs_promotion, args.recall]):
        payload["search"] = {
            "filtered": False,
            "matched_cards": len(cards),
            "total_cards": len(cards),
            "token_budget": token_budget,
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
        "token_budget": token_budget,
        "generated_evidence_only": True,
        "safe_next_step": "Cite matching cards, then verify against active memory, the active bead, and the relevant owner file before acting.",
    }
    if args.recall:
        next_payload["recall"] = selective_recall(selected, args)
    return next_payload


def self_test() -> int:
    cards = [
        {
            "path": "memory/cards/current.md",
            "title": "Current Lesson",
            "memory_space": "default",
            "confidence": "high",
            "freshness": "current",
            "status": "reviewed",
            "summary": "Use selective recall to retrieve cited snippets instead of loading whole memory files.",
            "glossary_excerpt": "",
            "export_summary": "Use selective recall to retrieve cited snippets instead of loading whole memory files.",
            "search_text": "current lesson selective recall cited snippets",
            "citation": {"path": "memory/cards/current.md", "source_pointers": ["logs/example.jsonl"]},
        },
        {
            "path": "memory/cards/stale.md",
            "title": "Stale Lesson",
            "memory_space": "default",
            "confidence": "low",
            "freshness": "stale",
            "status": "reviewed",
            "summary": "Old selective recall note.",
            "glossary_excerpt": "",
            "export_summary": "Old selective recall note.",
            "search_text": "stale selective recall",
            "citation": {"path": "memory/cards/stale.md", "source_pointers": ["logs/old.jsonl"]},
        },
    ]
    args = argparse.Namespace(query="selective recall", limit=5)
    result = selective_recall(cards, args)
    recalls = result.get("recalls") if isinstance(result.get("recalls"), list) else []
    if result.get("no_useful_memory_found") or len(recalls) != 2:
        print("memory-check self-test failed: expected two recall snippets")
        return 1
    if len(str(recalls[0].get("snippet") or "")) > 420:
        print("memory-check self-test failed: snippet is too large")
        return 1
    if recalls[1].get("demotion") == "none":
        print("memory-check self-test failed: stale low-confidence memory was not demoted")
        return 1
    miss_args = argparse.Namespace(query="unmatched", limit=5)
    miss = selective_recall(cards, miss_args)
    if not miss.get("no_useful_memory_found"):
        print("memory-check self-test failed: weak miss was not rejected")
        return 1
    print("memory-check self-test: pass")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Search or audit reviewed Precode memory cards without mutating state.")
    parser.add_argument("--query", help="Search title, summary, topics, category, source pointers, and glossary text.")
    parser.add_argument("--category", help="Filter by reviewed memory category.")
    parser.add_argument("--freshness", help="Filter by freshness: current, watch, stale, or superseded.")
    parser.add_argument("--status", help="Filter by status: reviewed, needs_promotion, superseded, or archived.")
    parser.add_argument("--needs-promotion", action="store_true", help="Show only cards that need owner-file promotion review.")
    parser.add_argument("--recall", action="store_true", help="Return concise cited recall snippets instead of expecting whole-card context loading.")
    parser.add_argument("--limit", type=int, default=5, help="Maximum selective recall snippets to return.")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic memory-check fixtures.")
    args = parser.parse_args()
    args.limit = max(1, args.limit)
    if args.self_test:
        return self_test()

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
