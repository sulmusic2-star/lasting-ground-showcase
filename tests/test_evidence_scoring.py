from datetime import date

from examples.evidence_scoring import build_evidence_matrix, score_source_lane

AS_OF = date(2026, 4, 29)


def test_official_validated_recent_lane_scores_strong():
    score = score_source_lane(
        {
            "lane_id": "gis",
            "label": "State GIS",
            "source_type": "official_public_layer",
            "status": "validated",
            "reviewed_on": "2026-04-20",
            "supports": ["regional context", "source appendix"],
        },
        as_of=AS_OF,
    )

    assert score.score == 97
    assert score.confidence == "strong"
    assert score.review_actions == []


def test_stale_lane_stays_usable_but_gets_review_action():
    score = score_source_lane(
        {
            "lane_id": "conservation",
            "label": "Conservation",
            "source_type": "local_public_records",
            "status": "caution",
            "reviewed_on": "2025-01-01",
            "supports": ["possible review direction"],
        },
        as_of=AS_OF,
    )

    assert score.confidence == "usable_with_caution"
    assert "refresh stale source lane" in score.review_actions
    assert "keep caveat visible in packet" in score.review_actions


def test_missing_lane_scores_zero_and_queues_action():
    score = score_source_lane(
        {
            "lane_id": "permit",
            "label": "Permit",
            "source_type": "local_public_records",
            "status": "missing",
            "reviewed_on": None,
            "supports": [],
        },
        as_of=AS_OF,
    )

    assert score.score == 0
    assert score.confidence == "weak_or_missing"
    assert score.review_actions == ["find official or public source lane", "add reviewed date"]


def test_matrix_turns_sample_into_review_ready_not_packet_ready():
    packet = {
        "packet_id": "packet-1",
        "address_label": "42 Harbor View Road",
        "source_lanes": [
            {"lane_id": "gis", "label": "GIS", "source_type": "official_public_layer", "status": "validated", "reviewed_on": "2026-04-28", "supports": ["a", "b"]},
            {"lane_id": "zoning", "label": "Zoning", "source_type": "local_public_reference", "status": "validated", "reviewed_on": "2026-04-28", "supports": ["a"]},
            {"lane_id": "conservation", "label": "Conservation", "source_type": "local_public_records", "status": "caution", "reviewed_on": "2026-04-28", "supports": ["a"]},
            {"lane_id": "permit", "label": "Permit", "source_type": "local_public_records", "status": "missing", "reviewed_on": None, "supports": []},
        ],
    }

    matrix = build_evidence_matrix(packet, as_of=AS_OF)

    assert matrix["readiness"] == "review_ready"
    assert matrix["missing_lane_count"] == 1
    assert len(matrix["review_queue"]) == 2


def test_matrix_can_promote_when_all_lanes_are_strong():
    packet = {
        "packet_id": "packet-strong",
        "address_label": "42 Harbor View Road",
        "source_lanes": [
            {"lane_id": str(i), "label": f"Lane {i}", "source_type": "official_public_layer", "status": "validated", "reviewed_on": "2026-04-28", "supports": ["a", "b"]}
            for i in range(4)
        ],
    }

    assert build_evidence_matrix(packet, as_of=AS_OF)["readiness"] == "packet_ready"
