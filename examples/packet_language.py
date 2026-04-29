from __future__ import annotations

from typing import Any

BANNED_CONCLUSION_TERMS = (
    "approved",
    "guaranteed",
    "requires permit",
    "violation",
    "safe to build",
    "no risk",
)


def build_packet_summary(validation_output: dict[str, Any]) -> list[str]:
    """Create cautious packet bullets from validation output.

    This keeps the public-facing summary tied to source status instead of letting
    incomplete evidence become a strong property conclusion.
    """
    address = validation_output["address_label"]
    jurisdiction = validation_output["jurisdiction"]
    support_depth = validation_output["support_depth"].replace("_", " ")
    warnings = validation_output.get("warnings", [])

    bullets = [
        f"{address} in {jurisdiction} has {validation_output['validated_count']} validated source lanes in this sample.",
        f"Support depth: {support_depth}.",
    ]

    if warnings:
        bullets.append(f"{len(warnings)} lane warning(s) should stay visible in the packet.")
    else:
        bullets.append("No lane warnings were generated from the provided sample sources.")

    bullets.append("The packet should describe source context and avoid property-specific legal, permit, inspection, or engineering conclusions.")
    return bullets


def find_overconfident_terms(text: str) -> list[str]:
    lowered = text.lower()
    return [term for term in BANNED_CONCLUSION_TERMS if term in lowered]


def assert_cautious_language(bullets: list[str]) -> None:
    combined = "\n".join(bullets)
    banned = find_overconfident_terms(combined)
    if banned:
        raise ValueError(f"Overconfident packet language detected: {', '.join(banned)}")
