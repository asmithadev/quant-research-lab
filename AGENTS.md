# Repository instructions

## Purpose

Maintain a beginner-friendly public Markdown learning journal. Use Markdown for new learning notes instead of Word documents unless the user explicitly requests a document artifact.

## Privacy and scope

- Preserve existing local BRAIN files. They are private research records and are ignored by Git.
- Never stage actual alpha expressions, saved alpha IDs, submission results, account scores, credentials, datasets or potentially restricted platform material without explicit permission to share and confirmation sharing is allowed.
- Do not copy WorldQuant documentation into public notes. Use original explanations of general concepts.
- Treat the root Git allowlist as intentional. Do not broaden it or run `git add .` without reviewing every included file. Never use `git add -f` to bypass it.
- Review staged content before committing or pushing. Do not print or inspect credential stores.
- Use repository-local identity and authentication for the intended owner. Never change another account's connection, global Git settings or existing workflows.

## Learning workflow

- When the user shares a learning, update its concept, research, experiment or mistakes note and the chronological learning log.
- Record only work actually done. Separate observations, hypotheses and unresolved questions.
- Prefer small runnable Python exercises using synthetic data and the standard library. Add meaningful tests when they validate behavior.
- Make descriptive commits for coherent changes when authorized. Push when authenticated and authorized.
- Aim for 2–4 commits only on days with enough actual work; do not split changes artificially to hit a number.
- Never fabricate progress, backdate commits, make empty commits or edit files merely to fill a contribution graph.
- Do not commit or push automatically in the background. When there is no new learning, suggest a small useful task.

## Validation

Run `python3 -m unittest discover -s experiments/tests -v` when Python exercises change. Check Markdown links and review `git diff --cached` before publishing.


## Private alpha research guardrails

Before private BRAIN research, read `PRIVATE_GOLD_RESEARCH_PLAN.md` and `PRIVATE_BRAIN_GUARDRAILS.json` when present. Keep them and all account-specific research private and ignored. Run `python3 private_gold_research_audit.py --as-of YYYY-MM-DD` with the actual client review date before presenting a recorded candidate as ready. This audit checks saved evidence; it does not replace fresh platform checks. Never count eligibility checked against a different submitted-history snapshot. Keep platform eligibility separate from research quality, family distinctness and unknown portfolio effects. Final prize-based Challenge submission remains a user action. Do not auto-submit, auto-commit or auto-push.
