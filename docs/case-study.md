# Lasting Ground

Property research brings together records that often live in separate federal, state and municipal systems. The design question is how to make those records useful while keeping their identity, dates and limitations visible.

[Public search](https://lastingground.com) · [Code](../examples/) · [Decision records](adr/README.md)

## What this repository shows

The public examples use synthetic inputs. They cover source-lane validation, evidence scoring, report composition and constrained summary language. The application source and record-retrieval system are private.

## Technical decisions

### Keep missing records visible

The [source-lane validator](../examples/source_lane_validation.py) distinguishes validated, caution and missing states. It returns warnings for incomplete evidence and checks whether a validated lane has a review date and supported claims.

### Assemble the report from structured results

The [packet composer](../examples/packet_composer.py) builds report sections from the validation output. The [language helper](../examples/packet_language.py) keeps summaries tied to the information those results support.

### Make the example reproducible

The repository includes the example inputs, implementation and tests. A reader can inspect how a result was produced and run the same public example locally.

## Scope

These examples check supplied records and assemble reports. They do not establish live-source accuracy, statewide or national coverage, paid adoption, revenue or production readiness. The public site's search interface was inspected on October 26, 2026; answers depend on available records and may require access.

[Run the examples](../README.md#run-locally) · [Engineering decisions](engineering-decisions.md)
