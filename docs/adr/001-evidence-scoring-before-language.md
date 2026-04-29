# ADR-001: Evidence scoring before packet language

## Context

A property packet can look confident even when the supporting public context is incomplete. The system needs to prevent readable language from outrunning the source evidence.

## Decision

Packet language is downstream of evidence scoring. Source lanes are scored for authority, freshness, support, and blockers before stronger language is composed.

## Tradeoff

This produces more cautious packets and requires more validation code. The benefit is that the artifact stays source-bounded and reviewable.

## Consequences

- Weak lanes remain visible.
- Stronger wording requires stronger support.
- Generated packet sections can cite the validation state they came from.

## Public proof

- [`examples/evidence_scoring.py`](../../examples/evidence_scoring.py)
- [`tests/test_evidence_scoring.py`](../../tests/test_evidence_scoring.py)
