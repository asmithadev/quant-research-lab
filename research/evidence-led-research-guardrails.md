# Evidence-led research guardrails

A strong individual backtest and a useful portfolio addition are different questions. This note records my research process, not a trading strategy or platform scoring formula.

## Before an experiment

Write the economic hypothesis, expected direction, horizon and failure conditions. Verify what each input measures and when it becomes available. Fix a baseline and a small, justified experiment budget before seeing results. Avoid changing many settings until one version looks attractive.

## Keep separate decisions

| Question | Evidence needed |
| --- | --- |
| Does the experiment run correctly? | Valid inputs, units, timing and missing-data behavior |
| Does it satisfy external eligibility requirements? | Explicit, current check results |
| Does the result look robust? | Separate training and test summaries, regime weaknesses and sensible sensitivity checks |
| Does it add something different? | Economic-family review and portfolio overlap evidence |
| Has a proposed action actually completed? | A verified final state, not merely a clicked button |

Passing one row does not answer the others. An unavailable statistic stays **unknown** rather than being treated as zero or as a pass.

## Eligibility is tied to a state

An eligibility check belongs to a particular experiment and comparison set. Save that comparison-set identifier with the result. If the set changes, mark the old check stale and run it again before acting. A list of individually acceptable alternatives is not a guarantee that all can be used sequentially.

## Diversification is more than a different expression

Two experiments can share the same economic exposure despite different syntax, lookback lengths or universes. Record shared components and distinguish expression similarity from portfolio-return correlation. Controls should address a stated economic risk, not inject noise or disguise duplicates.

Prefer genuinely different mechanisms and defensible evidence over collecting flattering labels. Compare marginal portfolio contribution where the evidence is available; do not infer it from individual performance alone.

## Protect the evaluation

Inspect training, validation and test results separately. Once a test period has influenced decisions, it is no longer untouched evidence. Keep a log of failed experiments and the number of trials to make selection bias visible. State narrow margins and weak regimes alongside attractive averages.

## Record decisions honestly

Each research record should capture the hypothesis, inputs and timing assumptions, exact setup, baseline, observations, unresolved questions, validation status, comparison-set snapshot and decision with reasons. Distinguish a research preference from a platform requirement.

Quality and consistency are useful goals, but they do not justify filler experiments or invented progress. Learning logs describe work actually performed. Account-specific research and sensitive records remain private; public examples use synthetic or explicitly shareable data.
