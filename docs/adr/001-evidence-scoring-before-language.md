# ADR-001: Evidence scoring before packet language

## Context

A property report can sound certain even when records are incomplete. Its wording needs to reflect those gaps.

## Decision

Packet language is downstream of evidence scoring. Source lanes are scored for authority, freshness, support, and blockers before stronger language is composed.

## Tradeoff

This produces more cautious packets and requires more validation code. Readers can trace each statement to the records that support it.

## Consequences

- Weak lanes remain visible.
- Stronger wording requires stronger support.
- Generated packet sections can cite the validation state they came from.

## Code and tests

- [`examples/evidence_scoring.py`](../../examples/evidence_scoring.py)
- [`tests/test_evidence_scoring.py`](../../tests/test_evidence_scoring.py)
