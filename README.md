# Quant Research Lab

A personal learning journal for quantitative research and Python, alongside my WorldQuant BRAIN learning journey.

The focus is understanding concepts, practicing careful experiments, and recording what I learn. Examples use synthetic data. This repository does not contain trading-ready alphas or performance claims.

## Explore

| Folder | What belongs here |
| --- | --- |
| [concepts](concepts/README.md) | Original explanations of research and statistics concepts |
| [research](research/README.md) | General lessons about hypotheses, validation and research process |
| [experiments](experiments/README.md) | Small Python exercises using synthetic or explicitly shareable data |
| [mistakes](mistakes/README.md) | Specific mistakes, corrections and prevention habits |
| [learning-log](learning-log/README.md) | A chronological record of work actually completed |

## First experiment

Using Python 3, from the repository root:

```sh
python3 experiments/returns_basics.py
python3 -m unittest discover -s experiments/tests -v
```

No third-party dependencies are required.

## Updating the journal

1. Capture a real learning or question in the relevant folder, in my own words.
2. Add a dated learning-log entry explaining what changed and what remains unclear.
3. Run relevant examples or tests and review the diff for private material.
4. Make a descriptive commit for a coherent piece of work; push when authorized.

Two to four commits can be a useful daily range **when there is enough genuine work**. It is not a quota. No empty commits, backdating, invented progress or cosmetic edits just to create contributions. No background daily-commit promise. If there is no new work, choose a useful learning task instead.

## Publication boundary

Keep actual alpha expressions, saved alpha IDs, submission results, account scores, credentials, private data and potentially restricted WorldQuant material out of this repository. Publish them only after explicit permission to share and confirmation that sharing is allowed. Explain general ideas originally rather than copying platform documentation.

The existing local BRAIN documents and research logs are preserved outside the Git allowlist. Markdown is the default for future learning notes; there is no need to maintain separate Word documents for this journal.

This is an educational journal, not investment advice or a promise of returns.
