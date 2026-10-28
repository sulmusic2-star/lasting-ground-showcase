# Engineering Decisions

## Model missing evidence as a product state

A weak source lane should not disappear from the output. Missing and incomplete lanes become visible warnings so the packet stays useful without pretending certainty.

## Separate evidence from explanation

The source-lane model decides what is supported before any human-readable packet language is written. This keeps generated text from inventing stronger claims than the sources allow.

## Support depth is earned, not counted

A larger number of URLs does not automatically mean stronger support. In this synthetic example, the support-depth label uses counts of declared lane states. Missing review dates and empty claim lists produce warnings, but those warnings do not lower the label. The separate evidence-scoring module explores richer scoring rules; the source validator does not independently verify a record or its authority.

## Keep packet language constrained

The packet can describe source context and uncertainty. It should not become legal, permit, inspection, or engineering advice.

## Make validation reproducible

The example input, validation script, generated output, and tests are committed together so the behavior can be reviewed and reproduced from the repo.

## Guard language after validation

Even after source validation passes, packet text still needs guardrails. The language helper keeps summaries tied to validated lane counts, visible warnings, and cautious source-context wording.
