# Evidence Model

The evidence model is built to answer four questions:

1. What source supports this statement?
2. Is the source official, public, regional, local, or derived?
3. How current and durable is it?
4. What should the product refuse to claim from it?

## Source record shape

```yaml
source_id: local_conservation_public_records
jurisdiction: sample-town
source_type: official_public_record
coverage_lane: conservation_or_wetlands_context
last_reviewed: 2026-04-28
supports:
  - local public-source routing context
  - source appendix citation
 does_not_support:
  - legal determination
  - permit approval prediction
  - engineering conclusion
```

## Claim boundary

A source can support context without supporting a conclusion. That distinction is central to the product.

Example:

- Safe: "The packet found a town conservation source that may be relevant to review routing."
- Unsafe: "This property will require conservation approval."

## Why this matters

Public property data is fragmented and uneven. A credible system has to model uncertainty explicitly instead of smoothing it away.
