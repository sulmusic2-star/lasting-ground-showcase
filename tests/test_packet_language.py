import json
from pathlib import Path

import pytest

from examples.packet_language import assert_cautious_language, build_packet_summary, find_overconfident_terms

BASE = Path(__file__).resolve().parents[1]


def load_validation_output():
    return json.loads((BASE / "examples" / "sample_validation_output.json").read_text())


def test_packet_summary_matches_committed_sample():
    bullets = build_packet_summary(load_validation_output())
    expected = (BASE / "examples" / "sample_packet_summary.txt").read_text().splitlines()

    assert bullets == expected


def test_packet_summary_keeps_warnings_visible():
    bullets = build_packet_summary(load_validation_output())

    assert any("2 lane warning" in bullet for bullet in bullets)
    assert any("standard support with caution" in bullet for bullet in bullets)


def test_language_guard_finds_overconfident_terms():
    text = "This property is approved and guaranteed with no risk."

    assert find_overconfident_terms(text) == ["approved", "guaranteed", "no risk"]


def test_language_guard_accepts_cautious_summary():
    assert_cautious_language(build_packet_summary(load_validation_output()))


def test_language_guard_rejects_bad_summary():
    with pytest.raises(ValueError, match="Overconfident packet language"):
        assert_cautious_language(["This property is approved and safe to build."])
