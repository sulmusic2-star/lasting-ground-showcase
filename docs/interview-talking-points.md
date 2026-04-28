# Interview / Recruiter Talking Points

## 30-second version

Lasting Ground is a source-backed property review system. The core challenge was not just building a form or report. It was designing an evidence model that knows what a source can support, what it cannot support, and how to produce a readable artifact without overstating certainty.

## What it proves

- I can work in messy real-world domains where data is fragmented.
- I can design systems around evidence, validation, and public-facing claim boundaries.
- I can build full-stack product workflows, not just UI screens.
- I understand that good AI systems need deterministic rails and QA gates.
- I can turn complicated source context into artifacts normal people can read.

## Best technical answer

The key design decision was separating the evidence layer from the explanation layer. A system like this cannot let generated text invent certainty. Source records, support-depth rules, and validation gates need to decide what can be said before any public-facing artifact is generated.
