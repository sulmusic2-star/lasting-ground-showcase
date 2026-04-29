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
- support depth is not promoted from source count alone
- unexpected lane statuses are rejected
- packet summaries avoid overconfident language

## Why this matters

The product depends on not overstating evidence. The tests show how incomplete sources stay visible instead of turning into confident claims.
