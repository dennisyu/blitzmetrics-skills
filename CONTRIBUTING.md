# Contributing safely

This repository is the canonical source for the BlitzMetrics Claude marketplace.
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

## Local checks

```bash
python3 scripts/validate_marketplace.py
python3 -m unittest discover -s tests -v
npx -y @anthropic-ai/claude-code@latest plugin validate .
```

The first check catches missing files, duplicate or unlisted skills, bad
frontmatter, and stale local references. The final check uses Claude's official
marketplace validator.

## What status words mean

- **Available:** present in the merged marketplace.
- **Installed:** visible in the named Claude account or workspace.
- **Enabled:** Claude is allowed to use it there.
- **Tested:** a fresh chat activated it and produced expected evidence.
- **Scheduled:** a job definition exists.
- **Observed:** a scheduled firing produced a timestamped output or failure.

Never substitute one state for another. In particular, `Scheduled` does not mean
`Observed`, and `Available` does not mean `Installed`.

## Release notes for members

Every member-facing notice must name the source commit/version, changed skills,
required sync action, a fresh-chat verification phrase, and the failure route. If a
legacy ZIP is supplied, label it as a snapshot and include the source commit. Never
call a reconstructed or article-derived pack canonical.
