# Lasting Ground Evaluator Guide

Use this if you are reviewing the repository quickly and want the strongest proof first.

## Thirty-second path

1. Open the live demo: https://sulmusic2-star.github.io/lasting-ground-showcase/
2. Open the sample PDF packet: https://sulmusic2-star.github.io/lasting-ground-showcase/assets/lasting-ground-sample-packet.pdf
3. Inspect the advanced evidence logic:
   - [`examples/evidence_scoring.py`](../examples/evidence_scoring.py)
   - [`examples/packet_composer.py`](../examples/packet_composer.py)
   - [`examples/source_lane_validation.py`](../examples/source_lane_validation.py)
4. Check tests and coverage:
   - [`docs/testing.md`](testing.md)
   - [`docs/coverage-summary.md`](coverage-summary.md)
   - [GitHub Actions CI](https://github.com/sulmusic2-star/lasting-ground-showcase/actions/workflows/ci.yml)
5. Read the case study: https://sulmusic2-star.github.io/case-studies/lasting-ground/

## What this project is meant to prove

- Full-stack workflow thinking: source inputs, validation gates, support-depth decisions, generated artifacts.
- Evidence discipline: source authority, freshness, missing-lane blockers, cautious packet language.
- Operational design: review queues, release gates, sample artifacts, testable rules.
- Communication: turning a complex domain into a packet a non-technical reader can understand.

## Files worth reading

| File | What to look for |
|---|---|
| `examples/evidence_scoring.py` | Source authority scoring, freshness checks, readiness classification, review actions. |
| `examples/packet_composer.py` | Packet sections assembled from validation output instead of free-form claims. |
| `examples/source_lane_validation.py` | Lane status validation, warning generation, support-depth rules. |
| `examples/packet_language.py` | Guardrails against overconfident packet language. |
| `tools/build_sample_packet_assets.py` | PDF/cover artifact generation. |

## Why it is not just a PDF demo

The PDF is the visible artifact. The examples show the operating system behind it: source-lane validation, evidence scoring, readiness decisions, review queues, and cautious language boundaries.
