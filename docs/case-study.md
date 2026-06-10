# Case Study — Lasting Ground

*Source-backed property review for Massachusetts. A live, paid product I designed and operate solo.*

[Live site → lastingground.com](https://lastingground.com) · [Sample packet (PDF)](assets/lasting-ground-sample-packet.pdf) · [System architecture](system-architecture.md) · [ADRs](adr/README.md)

> **A note on scope.** This case study describes *what* the system does, *how it is architected*, and *how I built and operate it*. The source-acquisition pipeline — how specific records are discovered, accessed, and normalized — is the product's competitive moat and is deliberately kept proprietary. Everything below is true and verifiable from the live site and this repo; the parts that aren't here are omitted on purpose, not missing.

---

## The problem

Before someone buys, renovates, or lends against a Massachusetts property, the same questions come up every time: Is it in a FEMA flood zone, and what will insurance cost? Has it been officially mapped out of the floodplain? What's the base flood elevation versus the ground? Are there wetlands, a conservation restriction, contamination nearby, or zoning limits on what you can build?

Today the answers are scattered across dozens of disconnected government systems — federal flood maps, state GIS layers, and a different permit portal for nearly every one of Massachusetts' 351 cities and towns. Getting a real answer means hours of manual lookups, and most people either skip it or pay for a slow, generic report.

**Lasting Ground turns one address into a source-cited answer set in seconds** — and tells you, for every line, exactly which official source it came from and when.

---

## What it is

A live product with a real funnel: type an address → get a free snapshot of the strongest signals → buy the full property-check packet (four pages plus a sources-and-confidence appendix). It runs on a serverless edge front end (Cloudflare Pages + Functions, Google Places address resolution, Stripe checkout) backed by a large Python engine that does the actual source work.

Concrete, live examples (these run today):
- A Quincy waterfront address returns its FEMA zone **with the governing FIRM panel and effective date**, a found **Letter of Map Amendment** (the official document that can remove a mandatory-insurance requirement), and the town's **Community Rating System class and the NFIP premium discount** that comes with it.
- A Nantucket address returns a base-flood-elevation answer that **surfaces its own source disagreement** — the approved packet value versus a live map re-query — instead of quietly picking one. Knowing what you *don't* know is the whole point in a regulated domain.

---

## Architecture (at altitude)

```
Address ─▶ verify + resolve to parcel ─▶ fan out to official sources (parallel)
                                              │
        FEMA flood / FIRM / LOMA-LOMR / CRS ──┤
        State + regional GIS layers ──────────┤─▶ deterministic answer catalog
        Municipal records (where available) ──┤      (each answer carries
                                              │       source name + date + scope)
                                              ▼
                              support-depth + routing rules
                                              ▼
                          audit gate ─▶ free snapshot / paid packet
                                          (paywall enforced server-side)
```

- **~200 backend services** in a Python/FastAPI engine (thousands of modules), with source registries, schedulers, and nightly refresh runners.
- Each address triggers **a dozen-plus live queries** against official federal, state, and regional sources; every returned answer is stamped with its source and the date it was checked.
- **Source families:** FEMA NFHL (flood zones, FIRM panels, map amendments), the OpenFEMA NFIP program data, MassGIS and regional GIS layers, state environmental and natural-heritage layers, state historic inventory, and municipal public records where a town publishes them. *(Which municipal systems, and how they're accessed and normalized, is the proprietary part.)*
- **Per-town / per-region "support-depth" tiers** — a coastal town, an island town, and an inland city expose different things, so local context is modeled as a product feature with explicit freshness dates, not hardcoded.

---

## The engineering decisions that actually matter

The UI is the easy 20%. These are the choices that made it a product instead of a demo:

1. **Verify-first, never a determination.** The system separates source-backed local detail, regional defaults, named gaps ("we couldn't confirm X"), and out-of-scope questions. If a source doesn't support a claim, the product doesn't make it. In a domain adjacent to insurance, lending, and permitting, the careful sentence *is* the product.
2. **An audit gate between "computed" and "customer-visible."** Capability is built behind a gate and only reaches a customer after it passes review — so the live packet never silently degrades when an upstream source changes.
3. **Server-enforced trust boundary.** Locked answers are genuinely absent from the API payload, not hidden in the browser — the paywall is a real boundary, not CSS.
4. **Edge caching with honest status.** A cold address resolves in a few seconds across many live source queries; a repeat is sub-second, with the cache state reported explicitly rather than hidden.
5. **Source-conflict honesty.** When two official sources disagree, the answer says so. Most systems hide this; surfacing it is what a careful buyer or attorney actually needs.

---

## How I built and operate it (the part that's unusual)

I built and run this **solo, by orchestrating AI coding agents** — primarily Claude Code and OpenAI Codex — as a small engineering team with a defined operating model:

- **A division of labor with review gates.** One agent does data and engine work in the canonical repo; another acts as the review/promotion/deploy gate. Nothing reaches customers without passing that gate.
- **Verification over trust.** Every build is checked against live sources and a test suite before it ships; I treat agent output as a draft to be proven, not accepted.
- **Incident recovery as a first-class skill.** I've recovered the system from real failures (a repository-corruption event, a destructive data regression) without losing the product.

The judgment — architecture, what to trust, what to keep proprietary, what's safe to tell a customer — is mine. The agents are a force multiplier that lets one person ship and operate something that normally takes a team. That operating model, not any single feature, is the thing I'd bring to a team adopting AI-native development.

There's a second, quieter judgment in the product: I use AI agents to *build* it, but the engine itself is deterministic. The compliance-critical answers (flood zone, insurance, zoning) never pass through a language model. In a domain next to insurance and lending, an answer has to be reproducible and traceable to an official source every time, so the model stays out of the hot path and the sources speak for themselves. Knowing where AI belongs, and where it doesn't, is what the whole product rests on.

---

## Results

- **Live and paid.** Real product, real checkout, in production at lastingground.com.
- **Deep where it counts.** Parcel-level zoning is wired for 23 Massachusetts towns including the entire Cape; flood-insurance answers (zone, FIRM panel, map amendments, CRS discount, base-flood-elevation-vs-ground) are live statewide.
- **Verifiable engineering.** This repo ships runnable example logic with **18 passing tests at 93.29% line coverage in CI**, architecture docs, and decision records — so a reviewer can inspect the *kind* of work without the proprietary internals.

---

## Honest limits

It's a solo-operated system, so resilience and bus-factor are real considerations I manage deliberately. Cold-query latency on a brand-new address is a few seconds because the answers are genuinely live, not pre-canned. Coverage is deepest in the highest-value markets first (coastal and island Massachusetts) and expands by design rather than all at once. And the product is explicitly **informational** — it names the board, agency, or licensed-professional lane a question belongs to without ever making that determination itself.

---

[lastingground.com](https://lastingground.com) · [hello@lastingground.com](mailto:hello@lastingground.com) · [Portfolio](https://sulmusic2-star.github.io/)
