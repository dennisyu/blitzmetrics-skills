# Local Service Spotlight Skills for Agents

The canonical public source for all 28 Local Service Spotlight skills used across
authority, content, measurement, client operations, and quality assurance. The
method lives in portable Markdown. Model-specific manifests are adapters over that
source, not competing copies.

## Install

Claude members should start with the illustrated guide:
[localservicespotlight.com/install](https://localservicespotlight.com/install/).
When Claude asks for the marketplace repository, paste:

```text
https://github.com/dennisyu/local-service-spotlight-skills
```

Then install `lss-everything`. Other runtimes use the same `skills/`
directories through their supported Git, plugin, workspace-rule, or file workflow.
See the adapter and receipt matrix in
[`skills/skill-registry/references/distribution.md`](skills/skill-registry/references/distribution.md).

If you already added `https://github.com/dennisyu/blitzmetrics-skills` or
installed `blitzmetrics-everything`, remove that marketplace and add this one.
GitHub redirects the old repository URL. Claude still needs a fresh install of
`lss-everything` because plugin names are keyed in the account.

The guide and repository have different jobs:

- The **install guide** tells a nontechnical member where to click and how to test.
- This **GitHub repository** is the source maintainers review and adapters package.
- GitHub's `/upload/main` page is for maintainers and is not an install link.

The repository is one release channel, so members do not need a new ZIP for every
release. Sync behavior varies by runtime, surface, and settings. A pull-request
branch is only **Candidate**; a merged, validated commit proves **Available**. An
update is verified only after the named environment reports the accepted
commit/version and a fresh session passes an activation test. A scheduled job is
verified only after an observed firing leaves a receipt.

## One source, several adapters

| Layer | Current source | What repository validation proves |
|---|---|---|
| Portable behavior | `skills/*/SKILL.md` plus generated `AGENTS.md` | Every declared skill and shared rule is present and internally consistent |
| Claude | `.claude-plugin/marketplace.json` | Marketplace structure and inventory validate |
| Grok | `.grok-plugin/plugin.json` | Adapter points at the same skills and has version parity |
| Codex, Cursor, ChatGPT, and other agents | Surface-specific install or packaging outside this repository | Nothing about a named account until its commit and cold-start receipt are recorded |

Never describe a vendor wrapper, uploaded knowledge snapshot, local cache, or custom
bot as canonical. It can be replaced without losing the method; the reviewed skill
and its source commit are the durable asset.

## What was installed

Start a new chat and ask in plain language. For example:

> “Harvest my positive mentions.”
>
> “Run my weekly brand MAA.”
>
> “How do I show up in ChatGPT?”

Claude should select the relevant skill. Seeing the plugin in a list proves only
that the package is visible. A named environment reporting the accepted commit
proves **Synced**; a successful fresh-chat trigger proves **Activated**.

## Bundles

Most people should install `lss-everything`.

| Bundle | What it covers |
|---|---|
| `lss-everything` | All 28 skills |
| `authority-and-reputation` | Knowledge Panel, AI search, reviews, and proof |
| `content-engine` | Articles, video, repurposing, and distribution |
| `client-operations` | Onboarding, cadence, access, reporting, and audits |
| `quality-and-standards` | Nine Triangles, verification, QA, judgment, and the registry |

## Skills, agents, and scheduled jobs

- A **skill** is a written recipe an agent can use when asked.
- An **agent** carries out a multi-step assignment using skills and tools.
- A **scheduled job** tells an agent when to run.
- A **receipt** is timestamped evidence that a run succeeded or failed.

Creating a schedule is not proof that it ran. See [ACCEPTANCE.md](ACCEPTANCE.md)
for installation, update, and fleet-job checks.

## House rules travel inside every skill

Every rule the team has learned lives once, as one file, in
[`standards/`](standards/) — never ship a black button, nothing autoplays with
sound, no popup on load, every link and entity claim resolves, personal-brand
heroes are immersive, and the rule about rules: capture what you learn in the
same session.

`scripts/sync_shared_rules.py` stamps each applicable rule verbatim into `AGENTS.md`
and the distributed `SKILL.md` files, so the rules arrive with the pack even though
`standards/` itself is not distributed. CI rejects a pull request when even one
copy is missing or stale.

The same file also carries the patterns that detect a violation in real HTML, and
`scripts/fleet_check.py` compiles them into a live sweep:

```bash
python3 scripts/fleet_check.py --self-test          # prove the checks bite
python3 scripts/fleet_check.py --targets fleet.example.txt
```

One file therefore produces the agent instruction, the human checklist, and the
automated check — Content · Checklist · Software from a single source, so the
rule and the thing that enforces it cannot disagree.

**Adding a house rule to the whole fleet is dropping one markdown file into
`standards/`.** How and why, in plain language:
[HOW-KNOWLEDGE-PROPAGATES.md](HOW-KNOWLEDGE-PROPAGATES.md).

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
