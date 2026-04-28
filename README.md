# Lasting Ground — Source-Backed Property Review System

> A public showcase for a full-stack, evidence-first property resilience review system.

This repository is intentionally a **sanitized portfolio case study**, not the private production source. It shows the product architecture, evidence model, validation posture, and sample artifact shape without exposing private implementation details, source-acquisition methods, credentials, or operational playbooks.

## What Lasting Ground does

Lasting Ground turns fragmented public and official property context into structured review artifacts for homeowners, buyers, and local partners.

The system is built around a simple rule:

> If the source does not support the claim, the product should not pretend certainty.

That means the product is not framed as legal, engineering, inspection, or permit advice. It is a source-backed translation layer: collect relevant public/official context, show what is known, disclose what is uncertain, and package it in a way a non-technical person can read.

## What this project demonstrates

- Full-stack product architecture across frontend, backend, reports, and operator workflows
- Evidence-first source registry design
- Deterministic rules for support depth and claim boundaries
- Region/town pack architecture for local context
- Validation gates before stronger public claims are made
- Report/packet generation thinking
- Operational QA and release-readiness practices
- Honest uncertainty handling in a regulated/real-world domain

## High-level architecture

```mermaid
flowchart TD
  A[Address / Property Input] --> B[Source Registry]
  B --> C[Regional + Town Context Packs]
  B --> D[Official / Public Source Adapters]
  C --> E[Screening + Routing Rules]
  D --> E
  E --> F[Support Depth Decision]
  F --> G[Review Artifact / Packet]
  F --> H[Operator QA Queue]
  H --> I[Release Gate]
  I --> G
```

## Core design principles

### 1. Source-backed before confident

The system distinguishes between source-backed local detail, regional/default context, missing evidence, and unsupported claims.

### 2. Deterministic where it matters

The private implementation uses explicit rules and validation gates for claim boundaries. LLM-style writing may help explain results, but it should not invent evidence.

### 3. Local context matters

A coastal town, island town, inland town, and dense city can require different source surfaces. The architecture treats local context as a first-class part of the product.

### 4. Public-facing language has to be careful

The product avoids acting like a lawyer, inspector, engineer, or permitting authority. It packages context and source links; it does not replace professional review.

## Public-safe sample artifacts

This showcase includes simplified examples:

- [`docs/system-architecture.md`](docs/system-architecture.md)
- [`docs/evidence-model.md`](docs/evidence-model.md)
- [`docs/support-depth-model.md`](docs/support-depth-model.md)
- [`sample-artifacts/sample-review-packet-outline.md`](sample-artifacts/sample-review-packet-outline.md)
- [`sample-artifacts/sample-source-register.md`](sample-artifacts/sample-source-register.md)
- [`docs/security-and-redaction.md`](docs/security-and-redaction.md)

## What is intentionally not included

- production source code
- source acquisition scripts
- private town pack internals
- private validation datasets
- customer/property records
- credentials, API keys, or deployment config
- exact promotion thresholds or operational wave playbooks
- private business strategy docs

## Why this is a serious build

Most demos stop at a UI. Lasting Ground required a deeper operating model:

- data provenance
- claim boundaries
- source durability
- region/town variance
- artifact generation
- QA and release gates
- public language safety

That is the work that makes a real product different from a mockup.

## Status

Public sanitized showcase. Production system private.
