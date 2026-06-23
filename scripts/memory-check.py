#!/usr/bin/env python3
# Version: v0.1.4
# Last updated: 2026-06-23
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


def card_reference(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "path": card.get("path"),
        "title": card.get("title"),
        "memory_space": card.get("memory_space", "default"),
        "category": card.get("category"),
        "freshness": card.get("freshness"),
        "status": card.get("status"),
        "authority_owner_if_promoted": card.get("authority_owner_if_promoted", "none"),
        "demotion": demotion_reason(card),
        "citation": card.get("citation"),
    }


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
                "category": card.get("category"),
                "freshness": card.get("freshness"),
                "status": card.get("status"),
                "authority_owner_if_promoted": card.get("authority_owner_if_promoted", "none"),
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


def retrieval_readiness_review(
    all_cards: list[dict[str, Any]],
    selected_cards: list[dict[str, Any]],
    details: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    terms = query_terms(args.query or "")
    token_budget = details.get("token_budget") if isinstance(details.get("token_budget"), dict) else {}
    oversized_paths = token_budget.get("oversized_cards") if isinstance(token_budget.get("oversized_cards"), list) else []
    card_count_warning = bool(token_budget.get("card_count_warning"))
    promotion_needed_cards = [card for card in selected_cards if card.get("status") == "needs_promotion"]
    stale_or_superseded_cards = [
        card
        for card in selected_cards
        if card.get("freshness") in {"stale", "superseded"} or card.get("status") in {"superseded", "archived"}
    ]
    low_confidence_cards = [card for card in selected_cards if card.get("confidence") == "low"]
    oversized_cards = [card for card in selected_cards if card.get("path") in oversized_paths]

    partial_matches: list[tuple[int, dict[str, Any]]] = []
    if terms and not selected_cards:
        for card in all_cards:
            score = recall_score(card, terms)
            if score > 0:
                partial_matches.append((score, card))
        partial_matches.sort(key=lambda item: (-item[0], str(item[1].get("path") or "")))

    hygiene_blockers = bool(
        oversized_cards
        or card_count_warning
        or promotion_needed_cards
        or stale_or_superseded_cards
        or low_confidence_cards
    )
    if not all_cards:
        recommendation = "stay_filesystem_first"
        rationale = "No reviewed cards exist yet; create reviewed filesystem memory before considering richer retrieval."
    elif hygiene_blockers:
        recommendation = "split_or_promote_cards_first"
        rationale = "Memory hygiene or token-pressure issues should be fixed before considering richer retrieval."
    elif terms and not selected_cards:
        recommendation = "extension_review_required"
        rationale = "The query found no exact reviewed-memory match; repeated misses after card hygiene may justify extension review."
    elif terms and partial_matches:
        recommendation = "extension_review_required"
        rationale = "The query only found weak partial matches; repeated weak matches after card hygiene may justify extension review."
    else:
        recommendation = "stay_filesystem_first"
        rationale = "Reviewed filesystem memory and selective recall remain sufficient based on the current evidence."

    return {
        "mode": "retrieval_readiness_review",
        "status": "reviewed",
        "query": args.query or "",
        "terms": terms,
        "card_count": len(selected_cards),
        "total_cards": len(all_cards),
        "memory_spaces": details.get("by_space") or {},
        "token_pressure": {
            "card_count_warning": card_count_warning,
            "oversized_cards": oversized_paths,
            "selected_oversized_cards": [card_reference(card) for card in oversized_cards],
            "token_budget": token_budget,
        },
        "demoted_signals": {
            "promotion_needed_cards": [card_reference(card) for card in promotion_needed_cards],
            "stale_or_superseded_cards": [card_reference(card) for card in stale_or_superseded_cards],
            "low_confidence_cards": [card_reference(card) for card in low_confidence_cards],
        },
        "query_evidence": {
            "matched_cards": len(selected_cards) if terms else 0,
            "no_query": not bool(terms),
            "no_exact_match": bool(terms and not selected_cards),
            "weak_match_examples": [
                {
                    **card_reference(card),
                    "score": score,
                    "snippet": recall_snippet(card, terms, limit=260),
                }
                for score, card in partial_matches[: max(1, args.limit)]
            ],
            "single_query_evidence_only": bool(terms),
        },
        "recommendation": recommendation,
        "rationale": rationale,
        "search_method": {
            "keyword": "implemented",
            "semantic": "not_implemented; extension_review_required_before_any_backend",
            "hybrid_backend": "not_implemented; no Postgres, pgvector, Docker, MCP, REST API, dashboard, shared backend, semantic index, embeddings, automatic writes, or cross-machine store required",
        },
        "safe_next_step": "Use cited reviewed-memory evidence only. Split oversized cards, promote owner-file claims manually, or run Extension Review before any semantic/shared retrieval backend work.",
        "does_not_approve": [
            "semantic_search",
            "shared_backend",
            "card_creation",
            "owner_file_promotion",
            "task_selection",
            "active_memory_expansion",
            "backend_dependency",
        ],
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

    if not any([args.query, args.category, args.freshness, args.status, args.needs_promotion, args.recall, args.retrieval_review]):
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
    if args.retrieval_review:
        next_payload["retrieval_review"] = retrieval_readiness_review(cards, selected, details, args)
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
            "category": "lesson",
            "authority_owner_if_promoted": "none",
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
            "category": "lesson",
            "authority_owner_if_promoted": "none",
            "summary": "Old selective recall note.",
            "glossary_excerpt": "",
            "export_summary": "Old selective recall note.",
            "search_text": "stale selective recall",
            "citation": {"path": "memory/cards/stale.md", "source_pointers": ["logs/old.jsonl"]},
        },
        {
            "path": "memory/cards/glossary.md",
            "title": "Shared Domain Terms",
            "memory_space": "product",
            "confidence": "high",
            "freshness": "watch",
            "status": "needs_promotion",
            "category": "project_glossary",
            "authority_owner_if_promoted": "tasks/prds/PRD-123-example.md",
            "summary": "Reviewed shared vocabulary for naming review.",
            "glossary_excerpt": "Client intake means the first structured request a customer submits. UI example: Intake form. Test example: client_intake_validates_required_fields.",
            "export_summary": "Reviewed shared vocabulary for client intake naming.",
            "search_text": "project_glossary client intake shared vocabulary naming review tasks/prds/prd-123-example.md",
            "citation": {
                "path": "memory/cards/glossary.md",
                "title": "Shared Domain Terms",
                "category": "project_glossary",
                "freshness": "watch",
                "status": "needs_promotion",
                "source_pointers": ["tasks/prds/PRD-123-example.md"],
                "authority_owner_if_promoted": "tasks/prds/PRD-123-example.md",
                "glossary_excerpt": "Client intake means the first structured request a customer submits.",
            },
        },
        {
            "path": "memory/cards/oversized.md",
            "title": "Oversized Memory",
            "memory_space": "default",
            "confidence": "high",
            "freshness": "current",
            "status": "reviewed",
            "category": "lesson",
            "authority_owner_if_promoted": "none",
            "summary": "A very large reviewed memory card should be split before adding retrieval infrastructure.",
            "glossary_excerpt": "",
            "export_summary": "A very large reviewed memory card should be split before adding retrieval infrastructure.",
            "search_text": "large oversized token pressure split retrieval infrastructure",
            "citation": {"path": "memory/cards/oversized.md", "source_pointers": ["logs/large.jsonl"]},
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
    glossary_args = argparse.Namespace(query="client intake", category="project_glossary", freshness=None, status=None, needs_promotion=False, recall=False)
    glossary_matches = filter_cards(cards, glossary_args)
    if len(glossary_matches) != 1 or glossary_matches[0].get("category") != "project_glossary":
        print("memory-check self-test failed: glossary category filter did not isolate the card")
        return 1
    glossary_recall = selective_recall(glossary_matches, argparse.Namespace(query="client intake", limit=5))
    glossary_recalls = glossary_recall.get("recalls") if isinstance(glossary_recall.get("recalls"), list) else []
    if not glossary_recalls or "Client intake" not in str(glossary_recalls[0].get("snippet") or ""):
        print("memory-check self-test failed: glossary recall did not include the glossary excerpt")
        return 1
    if "needs owner-file promotion" not in str(glossary_recalls[0].get("demotion") or ""):
        print("memory-check self-test failed: glossary promotion need was not demoted")
        return 1
    review_details = {
        "by_space": {"default": 3, "product": 1},
        "token_budget": {
            "oversized_cards": ["memory/cards/oversized.md"],
            "card_count_warning": False,
        },
    }
    no_query_review = retrieval_readiness_review(cards, cards, review_details, argparse.Namespace(query=None, limit=5))
    if no_query_review.get("recommendation") == "extension_review_required":
        print("memory-check self-test failed: no-query review forced extension review")
        return 1
    cleanup_review = retrieval_readiness_review(cards, cards, review_details, argparse.Namespace(query=None, limit=5))
    if cleanup_review.get("recommendation") != "split_or_promote_cards_first":
        print("memory-check self-test failed: oversized or promotion-needed cards did not recommend cleanup first")
        return 1
    demoted = cleanup_review.get("demoted_signals") if isinstance(cleanup_review.get("demoted_signals"), dict) else {}
    if not demoted.get("stale_or_superseded_cards") or not demoted.get("low_confidence_cards"):
        print("memory-check self-test failed: stale or low-confidence cards were not demoted in retrieval review")
        return 1
    clean_cards = [card for card in cards if card.get("path") == "memory/cards/current.md"]
    miss_review = retrieval_readiness_review(clean_cards, [], {"by_space": {"default": 1}, "token_budget": {}}, argparse.Namespace(query="semantic backend", limit=5))
    if miss_review.get("recommendation") != "extension_review_required":
        print("memory-check self-test failed: unmatched clean query did not require extension review before backend work")
        return 1
    if "semantic_search" not in miss_review.get("does_not_approve", []):
        print("memory-check self-test failed: retrieval review did not preserve backend non-approval")
        return 1
    empty_review = retrieval_readiness_review([], [], {"by_space": {}, "token_budget": {}}, argparse.Namespace(query="semantic backend", limit=5))
    if empty_review.get("recommendation") == "extension_review_required":
        print("memory-check self-test failed: empty memory set forced extension review")
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
    parser.add_argument("--retrieval-review", action="store_true", help="Review whether filesystem memory hygiene is sufficient before any optional retrieval backend work.")
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
