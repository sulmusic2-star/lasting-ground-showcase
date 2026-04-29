from examples.packet_composer import compose_packet_sections, summarize_packet_readiness


def test_composer_keeps_warning_section_visible():
    sections = compose_packet_sections(
        {"validated_count": 2, "lane_count": 4, "warnings": ["missing", "caution"]},
        {
            "readiness": "review_ready",
            "review_queue": [{"label": "Permit History", "actions": ["find official source"]}],
        },
    )

    titles = [section["title"] for section in sections]
    assert titles == ["Source lane snapshot", "What the packet can say", "What stays uncertain", "Review focus"]
    assert "2 warning" in sections[2]["body"]


def test_composer_omits_uncertainty_section_when_no_warnings():
    sections = compose_packet_sections(
        {"validated_count": 4, "lane_count": 4, "warnings": []},
        {"readiness": "packet_ready", "review_queue": []},
    )

    assert [section["title"] for section in sections] == ["Source lane snapshot", "What the packet can say"]


def test_readiness_summary_uses_plain_language():
    assert summarize_packet_readiness({"readiness": "packet_ready"}) == "Packet-ready with strong source-lane coverage."
    assert summarize_packet_readiness({"readiness": "review_ready"}).startswith("Review-ready")
    assert summarize_packet_readiness({"readiness": "cautious_summary_only"}).startswith("Cautious summary only")
