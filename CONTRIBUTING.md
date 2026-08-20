# Contributing safely

This repository is the canonical public source for portable BlitzMetrics skills and
their model-specific adapters.
A green-looking agent report is not proof that a change reached a user or ran on
schedule. Changes therefore move through a branch, automated checks, review, and
an acceptance receipt.

## Never upload directly to `main`

Do not send contributors to GitHub's `/upload/main` page and do not choose
**Commit directly to the `main` branch**. That route can replace the canonical
files without validation or review.

Instead:

1. Create a branch such as `skill/<short-name>` or `fix/<short-name>`.
2. Add or edit files on that branch.
3. Open a pull request using the repository template.
4. Wait for all validation checks to pass.
5. Review the diff, then merge.
6. If behavior or distribution changed, complete the relevant checks in
   [ACCEPTANCE.md](ACCEPTANCE.md).

For recurring distribution, follow
`skills/skill-registry/references/update-contract.md`. The GitHub commit is the
release identity; a ZIP filename or modification date is not.

## Adding a skill

1. Add `skills/<skill-name>/SKILL.md`. The directory and frontmatter `name` must
   be the same stable kebab-case value.
2. Add `./skills/<skill-name>` to `blitzmetrics-everything` in
   `.claude-plugin/marketplace.json` and any appropriate topical bundle.
3. Do not rename an existing skill or bundle. Treat a rename as a migration:
   audit scheduled prompts and installed copies first.
4. Run the checks below.

## Capturing a house rule

**A rule that lives only in an article is a rule the next agent will break.** The
black-button rule was published on 17 May 2026 and broken by an agent holding the
whole pack in context on 15 August 2026, because it was never in `standards/`.

When anyone states a rule — the account owner, a client, an audit, or your own
failure — capture it in the same session:

```bash
python3 scripts/new_standard.py "No autoplay with sound" \
  --from "Dennis Yu, Cowork session, 2026-08-16" \
  --applies-to published-html
```

Then write the rule, add machine checks if an honest one exists, and sync:

```bash
python3 scripts/fleet_check.py --self-test    # proves the checks actually fire
python3 scripts/sync_shared_rules.py          # stamps it into every applicable skill
```

`--from` is required. Provenance is how we see which channels leak: if a source
never appears in `captured_from`, that source is not being captured.

A direct instruction can propose a standard from provenance. A claim that a tactic
improves business performance must also carry an outcome receipt. Views, rankings,
traffic, engagement, and things produced can justify a test; they cannot promote a
business-effectiveness rule. Validate a receipt before review:

```bash
python3 scripts/validate_outcome_receipt.py path/to/private-receipt.json
```

Keep client-specific receipts private. Put the sanitized reusable rule, decision,
and non-sensitive evidence in the pull request.

Adding a rule is a file drop — no code change, no bundle edit. Plain language
walkthrough: [HOW-KNOWLEDGE-PROPAGATES.md](HOW-KNOWLEDGE-PROPAGATES.md).

## Local checks

```bash
python3 scripts/sync_shared_rules.py --check
python3 scripts/fleet_check.py --self-test
python3 scripts/validate_marketplace.py
python3 -m unittest discover -s tests -v
npx -y @anthropic-ai/claude-code@latest plugin validate .
```

Shared house rules live under `standards/`, one file per rule. After changing
one, run `python3 scripts/sync_shared_rules.py` to update the self-contained copy
inside every distributed skill. Never hand-edit a generated block; validation
rejects missing or stale copies, for every rule, in every skill.

`--self-test` runs each rule's machine checks against the passing and failing
samples in its own header. A check with no bite is the failure mode that matters:
it reports every site clean forever and looks exactly like a working check.

## What status words mean

- **Available:** present in the merged marketplace.
- **Synced:** the named environment reports the accepted source commit/version.
- **Enabled:** the named agent surface is allowed to use it there.
- **Activated:** a fresh session invoked it and produced expected evidence.
- **Scheduled:** a job definition exists.
- **Observed:** a scheduled firing produced a timestamped output or failure.
- **Accepted:** the observed canary passed its assertions and has a rollback target.

Never substitute one state for another. In particular, `Scheduled` does not mean
`Observed`, and `Available` does not mean `Synced`.

## Release notes for members

Every member-facing notice must name the source commit/version, changed skills,
required sync action, a fresh-chat verification phrase, and the failure route. If a
legacy ZIP is supplied, label it as a snapshot and include the source commit. Never
call a reconstructed or article-derived pack canonical.
