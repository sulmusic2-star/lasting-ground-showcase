# Lasting Ground Code Examples

Small examples that show how the evidence model can become a validation output before a packet is generated.

## Files

- [`sample_packet_input.json`](sample_packet_input.json) — fictional source-lane input
- [`source_lane_validation.py`](source_lane_validation.py) — validation logic for lane status, warnings, and support depth
- [`sample_validation_output.json`](sample_validation_output.json) — generated output from the validation script
- [`packet_language.py`](packet_language.py) — cautious packet summary helpers
- [`sample_packet_summary.txt`](sample_packet_summary.txt) — generated language sample

## Run it

```bash
python3 examples/source_lane_validation.py
python3 - <<'PY'
import json
from pathlib import Path
from examples.packet_language import build_packet_summary
print("\n".join(build_packet_summary(json.loads(Path("examples/sample_validation_output.json").read_text()))))
PY
```

## What it shows

- treating missing evidence as a visible product state
- separating source support from final packet language
- using validation gates before generating stronger claims
- making support depth depend on source quality, not just source count
- keeping generated packet language cautious and source-tied
