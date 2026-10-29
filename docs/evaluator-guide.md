# Reviewing the Lasting Ground examples

Start with the report, then inspect the code that produces it.

## Where to start

1. Open the live demo: https://sulmusic2-star.github.io/lasting-ground-showcase/
2. Open the sample PDF packet: https://sulmusic2-star.github.io/lasting-ground-showcase/assets/lasting-ground-sample-packet.pdf
3. Inspect the record checks and report code:
   - [`examples/evidence_scoring.py`](../examples/evidence_scoring.py)
   - [`examples/packet_composer.py`](../examples/packet_composer.py)
   - [`examples/source_lane_validation.py`](../examples/source_lane_validation.py)
4. Check tests and coverage:
   - [`docs/testing.md`](testing.md)
   - [`docs/coverage-summary.md`](coverage-summary.md)
   - [GitHub Actions CI](https://github.com/sulmusic2-star/lasting-ground-showcase/actions/workflows/ci.yml)
5. Read the case study: https://sulmusic2-star.github.io/case-studies/lasting-ground/

## What the examples cover

The Python examples take fictional records through validation, evidence scoring and report assembly. They show how missing information affects the output and which records need review. They do not retrieve or independently verify live property records.

## Files worth reading

| File | What to look for |
|---|---|
| `examples/evidence_scoring.py` | Source authority scoring, freshness checks, readiness classification, review actions. |
| `examples/packet_composer.py` | Packet sections assembled from validation output instead of free-form claims. |
| `examples/source_lane_validation.py` | Lane status validation, warning generation, support-depth rules. |
| `examples/packet_language.py` | Guardrails against overconfident packet language. |
| `tools/build_sample_packet_assets.py` | PDF/cover artifact generation. |

## Follow a result

Compare the input records, validation output and PDF. Warnings should remain visible when a record is missing or incomplete.
