#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

LaneStatus = Literal["validated", "caution", "missing"]


@dataclass(frozen=True)
class LaneCheck:
    lane_id: str
    label: str
    status: LaneStatus
    source_type: str
    reviewed_on: str | None
    supports_count: int
    warning: str | None


def load_packet(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def validate_lane(lane: dict[str, Any]) -> LaneCheck:
    status = lane.get("status")
    if status not in {"validated", "caution", "missing"}:
        raise ValueError(f"Unexpected status for {lane.get('lane_id')}: {status}")

    supports = lane.get("supports") or []
    reviewed_on = lane.get("reviewed_on")
    warning = None

    if status == "validated" and not reviewed_on:
        warning = "validated lane is missing a reviewed date"
    elif status == "validated" and not supports:
        warning = "validated lane has no supported claims"
    elif status == "missing":
        warning = "lane is missing and must be disclosed in the packet"
    elif status == "caution":
        warning = "lane is incomplete; packet language should stay cautious"

    return LaneCheck(
        lane_id=str(lane["lane_id"]),
        label=str(lane["label"]),
        status=status,
        source_type=str(lane.get("source_type", "unknown")),
        reviewed_on=reviewed_on,
        supports_count=len(supports),
        warning=warning,
    )


def decide_support_depth(checks: list[LaneCheck]) -> str:
    validated = sum(1 for check in checks if check.status == "validated")
    caution = sum(1 for check in checks if check.status == "caution")
    missing = sum(1 for check in checks if check.status == "missing")

    if missing == 0 and caution <= 1 and validated >= 3:
        return "higher_support"
    if validated >= 2:
        return "standard_support_with_caution"
    return "lower_support"


def build_validation_output(packet: dict[str, Any]) -> dict[str, Any]:
    checks = [validate_lane(lane) for lane in packet["source_lanes"]]
    warnings = [check.warning for check in checks if check.warning]

    return {
        "packet_id": packet["packet_id"],
        "address_label": packet["address_label"],
        "jurisdiction": packet["jurisdiction"],
        "lane_count": len(checks),
        "validated_count": sum(1 for check in checks if check.status == "validated"),
        "caution_or_missing_count": sum(1 for check in checks if check.status != "validated"),
        "support_depth": decide_support_depth(checks),
        "warnings": warnings,
        "packet_language_rule": "Describe source context, disclose incomplete lanes, and avoid property-specific legal, permit, inspection, or engineering conclusions.",
        "lane_checks": [check.__dict__ for check in checks],
    }


def main() -> None:
    base = Path(__file__).resolve().parent
    packet = load_packet(base / "sample_packet_input.json")
    output = build_validation_output(packet)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
