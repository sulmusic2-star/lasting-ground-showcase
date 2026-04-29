# System Architecture

Lasting Ground is organized around a source-backed review workflow.

```mermaid
flowchart LR
  subgraph Intake
    A[Address Input]
    B[Address Normalization]
  end

  subgraph Evidence
    C[Source Registry]
    D[Official/Public Source Records]
    E[Region/Town Packs]
  end

  subgraph Reasoning
    F[Screening Rules]
    G[Support Depth Classification]
    H[Uncertainty + Missing Evidence Flags]
  end

  subgraph Output
    I[Review Packet]
    J[Source Appendix]
    K[Operator QA Notes]
  end

  A --> B --> C
  C --> D
  C --> E
  D --> F
  E --> F
  F --> G
  G --> H
  H --> I
  H --> J
  H --> K
```

## Layers

### Frontend

Public-facing intake and explanation surfaces. The frontend should make the product understandable without overpromising certainty.

### Backend

API services for address handling, screening, report generation, source registry access, and operational dashboards.

### Packs

Reusable regional and town-specific context packs. Packs separate local source coverage from generic defaults.

### Validation

Release gates and support-depth checks prevent the product from overstating what the source set can actually prove.

## Shareable abstraction

The key architectural lesson is to separate evidence collection, deterministic routing, claim boundaries, and user-facing explanation.
