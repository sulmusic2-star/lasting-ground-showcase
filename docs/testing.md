# Testing

Lasting Ground's public examples test the source-lane validation path before packet language is generated.

## Run locally

```bash
python -m pip install -e ".[dev]"
make ci
python examples/source_lane_validation.py
```

## Coverage

A committed coverage snapshot lives at [`docs/coverage-summary.md`](coverage-summary.md). Re-run it with:

```bash
make coverage
```

## What is covered

- validation output matches the committed sample JSON
- missing lanes become visible warnings
- validated lanes need supported claims and review dates
- support-depth labels follow supplied lane-state counts; the validator does not independently check record quality
- unexpected lane statuses are rejected
- packet summaries avoid overconfident language
- evidence scores reflect source authority, freshness, support, and missing lanes
- packet sections keep uncertainty and review focus visible

## Limits

These tests cover fictional inputs and public example code. They do not establish live record accuracy or the behavior of the full application.
