from __future__ import annotations

from typing import Any


def compose_packet_sections(validation_output: dict[str, Any], evidence_matrix: dict[str, Any]) -> list[dict[str, Any]]:
    """Turn validation and evidence scoring into a reviewer-friendly packet outline."""
    warnings = validation_output.get("warnings", [])
    readiness = evidence_matrix["readiness"].replace("_", " ")

    sections: list[dict[str, Any]] = [
        {
            "title": "Source lane snapshot",
            "priority": 1,
            "body": f"{validation_output['validated_count']} of {validation_output['lane_count']} source lanes are validated; readiness is {readiness}.",
        },
        {
            "title": "What the packet can say",
            "priority": 2,
            "body": "Describe source context, reviewed dates, and which lanes support the summary.",
        },
    ]

    if warnings:
        sections.append(
            {
                "title": "What stays uncertain",
                "priority": 3,
                "body": f"Keep {len(warnings)} warning(s) visible instead of turning incomplete lanes into conclusions.",
            }
        )

    if evidence_matrix.get("review_queue"):
        lane_labels = ", ".join(item["label"] for item in evidence_matrix["review_queue"][:3])
        sections.append(
            {
                "title": "Review focus",
                "priority": 4,
                "body": f"Next review pass should focus on: {lane_labels}.",
            }
        )

    return sections


def summarize_packet_readiness(evidence_matrix: dict[str, Any]) -> str:
    readiness = evidence_matrix["readiness"]
    if readiness == "packet_ready":
        return "Packet-ready with strong source-lane coverage."
    if readiness == "review_ready":
        return "Review-ready, with caveats still visible before stronger packet language."
    return "Cautious summary only until missing or weak source lanes improve."
