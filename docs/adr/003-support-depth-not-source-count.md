# ADR-003: Separate support depth from source count

## Context

A large number of public links does not automatically mean the packet can support stronger local claims. The system needs a clearer standard than raw source count.

## Decision

Support depth is modeled as a decision layer. Source lanes must satisfy required coverage and quality expectations before the output can present stronger local context.

## Tradeoff

Some packets remain more conservative even when several sources exist. The benefit is that quality and coverage matter more than volume.

## Consequences

- Source count is not treated as proof by itself.
- Support-depth language stays tied to lane quality.
- Reviewers can distinguish regional context from stronger local support.

## Public proof

- [`examples/source_lane_validation.py`](../../examples/source_lane_validation.py)
- [`docs/support-depth-model.md`](../support-depth-model.md)
- [`tests/test_source_lane_validation.py`](../../tests/test_source_lane_validation.py)
