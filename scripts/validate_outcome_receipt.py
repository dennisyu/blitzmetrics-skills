#!/usr/bin/env python3
"""Validate recursive-improvement outcome receipts without third-party packages.

Repository tests prove that files agree. This validator proves that a proposed
process improvement names the evidence and decision it is based on. It does not
verify the underlying CRM, finance, call, or analytics record; the receipt must
link to that source for an independent reviewer.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any


CLAIM_TYPES = {
    "business-effectiveness",
    "operational-reliability",
    "safety-or-compliance",
}
DECISIONS = {"propose", "canary", "promote", "hold", "revert"}
TIERS = {
    "business-outcome",
    "qualified-demand",
    "conversion",
    "diagnostic",
    "activity",
    "native-reliability-or-safety",
}
QUALITIES = {"verified", "estimated", "not-connected"}
COMMIT = re.compile(r"^[0-9a-f]{7,40}$")
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def _mapping(value: Any, path: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{path} must be an object")
        return {}
    return value


def _nonempty(mapping: dict[str, Any], key: str, path: str, errors: list[str]) -> Any:
    value = mapping.get(key)
    if value is None or value == "" or value == [] or value == {}:
        errors.append(f"{path}.{key} is required")
    return value


def _nonempty_string(
    mapping: dict[str, Any], key: str, path: str, errors: list[str]
) -> Any:
    value = _nonempty(mapping, key, path, errors)
    if value is not None and value not in ("", [], {}) and not isinstance(value, str):
        errors.append(f"{path}.{key} must be a string")
    return value


def validate_receipt(receipt: Any) -> list[str]:
    """Return deterministic validation errors; an empty list is a structural pass."""
    errors: list[str] = []
    root = _mapping(receipt, "receipt", errors)
    if not root:
        return errors

    if root.get("schema_version") != 1:
        errors.append("receipt.schema_version must be 1")
    _nonempty_string(root, "receipt_id", "receipt", errors)
    recorded_at = _nonempty_string(root, "recorded_at", "receipt", errors)
    if isinstance(recorded_at, str):
        try:
            datetime.fromisoformat(recorded_at.replace("Z", "+00:00"))
        except ValueError:
            errors.append("receipt.recorded_at must be ISO-8601 with timezone")
        else:
            if datetime.fromisoformat(recorded_at.replace("Z", "+00:00")).tzinfo is None:
                errors.append("receipt.recorded_at must include a timezone")

    source_commit = _nonempty_string(root, "source_commit", "receipt", errors)
    if isinstance(source_commit, str) and not COMMIT.fullmatch(source_commit):
        errors.append("receipt.source_commit must be a 7-40 character lowercase Git SHA")
    skill = _nonempty_string(root, "skill", "receipt", errors)
    if isinstance(skill, str) and not KEBAB.fullmatch(skill):
        errors.append("receipt.skill must be stable kebab-case")

    claim_type = _nonempty_string(root, "claim_type", "receipt", errors)
    if claim_type not in CLAIM_TYPES:
        errors.append(f"receipt.claim_type must be one of {sorted(CLAIM_TYPES)}")
    decision = _nonempty_string(root, "decision", "receipt", errors)
    if decision not in DECISIONS:
        errors.append(f"receipt.decision must be one of {sorted(DECISIONS)}")
    if not isinstance(root.get("public_safe"), bool):
        errors.append("receipt.public_safe must be true or false")

    change = _mapping(root.get("change"), "receipt.change", errors)
    _nonempty_string(change, "hypothesis", "receipt.change", errors)
    _nonempty_string(change, "intervention", "receipt.change", errors)
    _nonempty_string(change, "keep_threshold", "receipt.change", errors)
    _nonempty_string(change, "revert_threshold", "receipt.change", errors)

    scope = _mapping(root.get("scope"), "receipt.scope", errors)
    for key in ("cohort", "period_start", "period_end", "timezone"):
        _nonempty_string(scope, key, "receipt.scope", errors)

    outcome = _mapping(root.get("primary_outcome"), "receipt.primary_outcome", errors)
    for key in (
        "metric",
        "tier",
        "definition",
        "source",
        "quality",
        "attribution_window",
    ):
        _nonempty_string(outcome, key, "receipt.primary_outcome", errors)
    for key in ("baseline", "result", "sample_size"):
        _nonempty(outcome, key, "receipt.primary_outcome", errors)
    tier = outcome.get("tier")
    quality = outcome.get("quality")
    if tier not in TIERS:
        errors.append(f"receipt.primary_outcome.tier must be one of {sorted(TIERS)}")
    if quality not in QUALITIES:
        errors.append(
            f"receipt.primary_outcome.quality must be one of {sorted(QUALITIES)}"
        )

    guardrails = root.get("guardrails")
    if not isinstance(guardrails, list) or not guardrails:
        errors.append("receipt.guardrails must contain at least one measured counter-metric")
    else:
        for index, guardrail_value in enumerate(guardrails):
            path = f"receipt.guardrails[{index}]"
            guardrail = _mapping(guardrail_value, path, errors)
            _nonempty_string(guardrail, "metric", path, errors)
            _nonempty(guardrail, "baseline", path, errors)
            _nonempty(guardrail, "result", path, errors)
            _nonempty_string(guardrail, "source", path, errors)
    alternatives = root.get("alternative_explanations")
    if not isinstance(alternatives, list) or not alternatives:
        errors.append("receipt.alternative_explanations must contain at least one entry")
    else:
        for index, alternative in enumerate(alternatives):
            if not isinstance(alternative, str) or not alternative.strip():
                errors.append(
                    f"receipt.alternative_explanations[{index}] must be a non-empty string"
                )
    evidence = root.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append("receipt.evidence must contain at least one source receipt or artifact")
    else:
        for index, artifact in enumerate(evidence):
            if not isinstance(artifact, str) or not artifact.strip():
                errors.append(f"receipt.evidence[{index}] must be a non-empty string")

    if decision == "promote":
        if quality != "verified":
            errors.append("a promoted change requires a verified primary outcome")
        if claim_type == "business-effectiveness" and tier not in {
            "business-outcome",
            "qualified-demand",
        }:
            errors.append(
                "a business-effectiveness promotion requires a business-outcome or "
                "qualified-demand primary metric; diagnostics can propose or canary only"
            )
        if claim_type != "business-effectiveness" and tier != "native-reliability-or-safety":
            errors.append(
                "a reliability/safety promotion must use its native verified outcome and "
                "must not imply a business-effectiveness claim"
            )

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipts", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.receipts:
        try:
            receipt = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"FAIL {path}: {exc}")
            failed = True
            continue
        errors = validate_receipt(receipt)
        if errors:
            failed = True
            print(f"FAIL {path}")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"PASS {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
