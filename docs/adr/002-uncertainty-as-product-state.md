# ADR-002: Treat uncertainty as a product state

## Context

Reports need to show missing and outdated records so readers know what remains uncertain.

## Decision

Uncertainty should appear as caution, missing, or review-needed states in the packet workflow instead of being smoothed over.

## Tradeoff

The report has more cautions to read. Those cautions identify the records that need review.

## Consequences

- Missing lanes trigger packet cautions.
- Review states appear in the report as well as internal metadata.
- The product avoids overstating public context.

## Code and tests

- [`examples/packet_composer.py`](../../examples/packet_composer.py)
- [`examples/packet_language.py`](../../examples/packet_language.py)
- [`tests/test_packet_composer.py`](../../tests/test_packet_composer.py)
