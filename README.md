# Lasting Ground

Property research with official records and their sources in view.

[Public search](https://lastingground.com) · [Case study](docs/case-study.md) · [Technical decisions](docs/engineering-decisions.md)

![Lasting Ground public search interface, captured October 26, 2026](https://raw.githubusercontent.com/sulmusic2-star/sulmusic2-star.github.io/main/assets/property-search-20261026.png)

## Public examples

This repository contains synthetic Python examples of source validation, evidence scoring and report assembly. The full application and its source-acquisition system are private. These examples can be inspected offline; they do not establish the application's geographic coverage or the correctness of a live property answer.

## Start with the code

- [Source validation](examples/source_lane_validation.py) keeps validated, caution and missing records distinct.
- [Evidence scoring](examples/evidence_scoring.py) models source authority, freshness and review actions.
- [Packet composition](examples/packet_composer.py) assembles sections from validation results.
- [Packet language](examples/packet_language.py) constrains wording when evidence is incomplete.

The [architecture notes](docs/system-architecture.md) and [decision records](docs/adr/README.md) explain the structure.

## Run locally

Requires Python 3.11 or newer.

```bash
python -m pip install -e ".[dev]"
make ci
python examples/source_lane_validation.py
```

The tests apply to the public examples. See the [testing notes](docs/testing.md) for their scope.

## Scope

The public search interface is available at [lastingground.com](https://lastingground.com). Answers depend on the records available for an address, and access may be required. The screenshot shows the public search page on October 26, 2026.

This work provides informational source context. It does not replace a survey, an official determination or legal, engineering, insurance or lending advice.

[Tim Sullivan](https://sulmusic2-star.github.io/) · [Contact](mailto:hello@lastingground.com)
