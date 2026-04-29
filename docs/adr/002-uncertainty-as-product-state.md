# ADR-002: Treat uncertainty as a product state

## Context

Missing or stale source lanes are easy to hide in a clean-looking packet. That would make the output simpler, but less honest.

## Decision

Uncertainty should appear as caution, missing, or review-needed states in the packet workflow instead of being smoothed over.

## Tradeoff

The output feels less magically complete. The benefit is that reviewers can see the source boundary and understand what still needs review.

## Consequences

- Missing lanes trigger packet cautions.
- Review states become part of the artifact, not internal-only metadata.
- The product avoids overstating public context.

## Public proof

- [`examples/packet_composer.py`](../../examples/packet_composer.py)
- [`examples/packet_language.py`](../../examples/packet_language.py)
- [`tests/test_packet_composer.py`](../../tests/test_packet_composer.py)
