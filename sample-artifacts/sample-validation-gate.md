# Sample Validation Gate

This is a shareable example of how a source-backed review system can prevent overclaiming.

## Gate checks

| Check | Shareable rule | Pass example | Fail example |
|---|---|---|---|
| Source present | Every key claim needs a named source | Source appendix includes reviewed public source | Claim appears without source |
| Scope boundary | Source context cannot become legal/engineering advice | "May be relevant to review routing" | "Will be approved" |
| Freshness | Stale source dates must be visible | Reviewed date included | No review date shown |
| Local support | Local claim needs local source support | Town source cited | Only broad regional context available |
| Missing evidence | Missing lanes must be disclosed | "No local packet found in public sample" | Silent omission |

## Example outcome

```text
Result: publish with caution
Reason: regional and local source context exists, but one local record lane is incomplete.
Public wording: "The packet found public context that may be relevant, but this lane should be verified before making a property-specific conclusion."
```

## Why this matters

The system should make useful artifacts without pretending that incomplete public records are complete certainty.
