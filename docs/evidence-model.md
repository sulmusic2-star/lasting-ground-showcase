# Evidence Model

Each record needs to answer four questions:

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

A record can provide background without supporting a property-specific conclusion.

Example:

- Safe: "The packet found a town conservation source that may be relevant to review routing."
- Unsafe: "This property will require conservation approval."

## Missing information

Public property records vary in coverage and age. The report needs to show those limits.
