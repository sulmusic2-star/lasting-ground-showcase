import json
from pathlib import Path

import pytest

from examples.source_lane_validation import build_validation_output, decide_support_depth, validate_lane

BASE = Path(__file__).resolve().parents[1]


def load_sample_packet():
    return json.loads((BASE / "examples" / "sample_packet_input.json").read_text())


def test_sample_packet_validation_matches_committed_output():
    packet = load_sample_packet()
    expected = json.loads((BASE / "examples" / "sample_validation_output.json").read_text())

    assert build_validation_output(packet) == expected


def test_missing_lane_becomes_visible_warning():
    missing_lane = {
        "lane_id": "permit_history",
        "label": "Permit History Packet",
        "source_type": "local_public_records",
        "status": "missing",
        "reviewed_on": None,
        "supports": [],
    }

    check = validate_lane(missing_lane)

    assert check.status == "missing"
    assert check.warning == "lane is missing and must be disclosed in the packet"


def test_validated_lane_needs_supported_claims_and_review_date():
    no_review_date = {
        "lane_id": "state_gis_context",
        "label": "State GIS Context",
        "source_type": "official_public_layer",
        "status": "validated",
        "reviewed_on": None,
        "supports": ["regional screening context"],
    }
    no_supports = {
        **no_review_date,
        "reviewed_on": "2026-04-28",
        "supports": [],
    }

    assert validate_lane(no_review_date).warning == "validated lane is missing a reviewed date"
    assert validate_lane(no_supports).warning == "validated lane has no supported claims"


def test_support_depth_requires_more_than_source_count():
    packet = load_sample_packet()
    checks = [validate_lane(lane) for lane in packet["source_lanes"]]

    assert decide_support_depth(checks) == "standard_support_with_caution"

    for lane in packet["source_lanes"]:
        lane["status"] = "validated"
        lane["reviewed_on"] = "2026-04-28"
        lane["supports"] = lane.get("supports") or ["source context"]

    stronger_checks = [validate_lane(lane) for lane in packet["source_lanes"]]
    assert decide_support_depth(stronger_checks) == "higher_support"


def test_unexpected_status_is_rejected():
    with pytest.raises(ValueError, match="Unexpected status"):
        validate_lane({"lane_id": "x", "label": "Bad Lane", "status": "approved"})
