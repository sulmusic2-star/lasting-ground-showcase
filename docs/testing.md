# Testing

Lasting Ground's public examples test the source-lane validation path before packet language is generated.

## Run locally

```bash
python -m pip install pytest
pytest -q
python examples/source_lane_validation.py
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
