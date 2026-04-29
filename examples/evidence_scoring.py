from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date
from typing import Any, Literal

Confidence = Literal["strong", "usable_with_caution", "weak_or_missing"]
Readiness = Literal["packet_ready", "review_ready", "cautious_summary_only"]

SOURCE_TYPE_POINTS = {
    "official_public_layer": 35,
    "local_public_reference": 32,
    "local_public_records": 28,
    "regional_reference": 20,
    "unknown": 8,
}

STATUS_POINTS = {
    "validated": 34,
    "caution": 12,
    "missing": 0,
}


@dataclass(frozen=True)
class EvidenceScore:
    lane_id: str
    label: str
    score: int
    confidence: Confidence
    reviewed_age_days: int | None
    review_actions: list[str]


def _parse_reviewed_on(value: str | None) -> date | None:
    if not value:
        return None
    return date.fromisoformat(value)


def _freshness_points(reviewed_on: str | None, *, as_of: date) -> tuple[int, int | None, list[str]]:
    reviewed = _parse_reviewed_on(reviewed_on)
    if reviewed is None:
        return 0, None, ["add reviewed date"]

    age = (as_of - reviewed).days
    if age <= 30:
        return 18, age, []
    if age <= 180:
        return 10, age, ["refresh before publishing strong language"]
    return 2, age, ["refresh stale source lane"]


def score_source_lane(lane: dict[str, Any], *, as_of: date) -> EvidenceScore:
    lane_id = str(lane["lane_id"])
    label = str(lane["label"])
    status = str(lane.get("status", "missing"))
    source_type = str(lane.get("source_type", "unknown"))
    supports = lane.get("supports") or []

    review_actions: list[str] = []
    if status == "missing":
        review_actions.append("find official or public source lane")
    elif status == "caution":
        review_actions.append("keep caveat visible in packet")

    source_points = SOURCE_TYPE_POINTS.get(source_type, SOURCE_TYPE_POINTS["unknown"])
    status_points = STATUS_POINTS.get(status, 0)
    support_points = min(len(supports) * 5, 15)
    freshness_points, age, freshness_actions = _freshness_points(lane.get("reviewed_on"), as_of=as_of)
    review_actions.extend(freshness_actions)

    if status == "validated" and not supports:
        review_actions.append("attach supported claim before using lane")

    raw_score = source_points + status_points + support_points + freshness_points
    if status == "missing":
        raw_score = 0
    score = max(0, min(100, raw_score))

    if score >= 78 and not review_actions:
        confidence: Confidence = "strong"
    elif score >= 45:
        confidence = "usable_with_caution"
    else:
        confidence = "weak_or_missing"

    return EvidenceScore(lane_id, label, score, confidence, age, review_actions)


def build_evidence_matrix(packet: dict[str, Any], *, as_of: date) -> dict[str, Any]:
    scores = [score_source_lane(lane, as_of=as_of) for lane in packet["source_lanes"]]
    missing_count = sum(1 for score in scores if score.score == 0)
    strong_count = sum(1 for score in scores if score.confidence == "strong")
    average_score = round(sum(score.score for score in scores) / len(scores), 1) if scores else 0

    if missing_count == 0 and strong_count >= 3 and average_score >= 74:
        readiness: Readiness = "packet_ready"
    elif missing_count <= 1 and average_score >= 50:
        readiness = "review_ready"
    else:
        readiness = "cautious_summary_only"

    review_queue = [
        {"lane_id": score.lane_id, "label": score.label, "actions": score.review_actions}
        for score in scores
        if score.review_actions
    ]

    return {
        "packet_id": packet["packet_id"],
        "address_label": packet["address_label"],
        "as_of": as_of.isoformat(),
        "average_score": average_score,
        "strong_lane_count": strong_count,
        "missing_lane_count": missing_count,
        "readiness": readiness,
        "scores": [asdict(score) for score in scores],
        "review_queue": review_queue,
    }
