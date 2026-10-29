# Engineering Decisions

## Missing records

The validator reports missing and incomplete source lanes as warnings. The report retains those warnings so readers can see which records still need checking.

## Validation before report text

The source-lane model evaluates supplied lane states before the report text is assembled. The language helper uses those results to describe support and missing evidence.

## Limits of the support label

A larger number of URLs does not automatically mean stronger support. In this synthetic example, the support-depth label uses counts of declared lane states. Missing review dates and empty claim lists produce warnings, but those warnings do not lower the label. The separate evidence-scoring module explores richer scoring rules; the source validator does not independently verify a record or its authority.

## Report scope

The packet can describe source context and uncertainty. It should not become legal, permit, inspection, or engineering advice.

## Reproducing the example

The example input, validation script, generated output, and tests are committed together so the behavior can be reviewed and reproduced from the repo.

## Warnings in the summary

The language helper uses validated lane counts and warnings to write the summary. A validation pass does not remove cautions from incomplete source lanes.
