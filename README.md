# BlitzMetrics Skills for Claude

The canonical marketplace for the 27 BlitzMetrics and Local Service Spotlight
skills used across authority, content, client operations, and quality assurance.

## Install

Members should start with the illustrated guide:
[localservicespotlight.com/install](https://localservicespotlight.com/install/).
When Claude asks for the marketplace repository, paste:

```text
https://github.com/dennisyu/blitzmetrics-skills
```

Then install `blitzmetrics-everything`.

The guide and repository have different jobs:

- The **install guide** tells a nontechnical member where to click and how to test.
- This **GitHub repository** is the source Claude reads and maintainers review.
- GitHub's `/upload/main` page is for maintainers and is not an install link.

The repository is one update channel, so members do not need a new ZIP for every
release. Sync behavior varies by Claude surface and settings: third-party
marketplace auto-update may need to be enabled, or a member may need to choose
**Sync** or **Update**. An update is verified only after the account shows the new
commit/version and a fresh chat passes an activation test.

## What was installed

Start a new chat and ask in plain language. For example:

> “Harvest my positive mentions.”
>
> “Run my weekly brand MAA.”
>
> “How do I show up in ChatGPT?”

Claude should select the relevant skill. Seeing the plugin in a list proves it is
installed; a successful fresh-chat trigger proves that skill is working.

## Bundles

Most people should install `blitzmetrics-everything`.

| Bundle | What it covers |
|---|---|
| `blitzmetrics-everything` | All 27 skills |
| `authority-and-reputation` | Knowledge Panel, AI search, reviews, and proof |
| `content-engine` | Articles, video, repurposing, and distribution |
| `client-operations` | Cadence, access, reporting, and audits |
| `quality-and-standards` | Nine Triangles, verification, QA, judgment, and the registry |

## Skills, agents, and scheduled jobs

- A **skill** is a written recipe Claude can use when asked.
- An **agent** carries out a multi-step assignment using skills and tools.
- A **scheduled job** tells an agent when to run.
- A **receipt** is timestamped evidence that a run succeeded or failed.

Creating a schedule is not proof that it ran. See [ACCEPTANCE.md](ACCEPTANCE.md)
for installation, update, and fleet-job checks.

## For maintainers

The `skills/` folder is the single source of truth. Bundles in
`.claude-plugin/marketplace.json` are selections over it; skills are not copied
between bundles.

Never commit from GitHub's `/upload/main` page. Create a branch and pull request,
then let the validation workflow check the manifest, local references, converter,
and Claude marketplace format. Full instructions are in
[CONTRIBUTING.md](CONTRIBUTING.md).

Do not rename an existing skill or bundle without a migration. Installed copies
and scheduled prompts are keyed by name, so a rename can create a duplicate and
silently break jobs that call the old name.
