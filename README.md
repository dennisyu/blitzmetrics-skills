# BlitzMetrics Skills for Claude

Every skill we use, installable in one click.

## Install (about 60 seconds, once)

1. Open Claude on a computer — web, desktop app, or Cowork.
2. Go to **Customize → Plugins → Add from repository**.
3. Paste this address:

```
https://github.com/dennisyu/blitzmetrics-skills
```

4. Click **Install** on **`blitzmetrics-everything`**.

That's it. You now have all 26 skills, and you'll get every future update
automatically — you never download anything again.

Never done this before? Step-by-step with screenshots:
**https://localservicespotlight.com/install/**

## What you just installed

Start a new chat and say what you want in plain language. You don't type
commands — the right skill loads itself.

> "Harvest my positive mentions."
> "Run my weekly brand MAA."
> "How do I show up in ChatGPT?"

## Want just one area instead of everything?

Same address, different pick. Most people should take `blitzmetrics-everything`.

| Bundle | What it covers |
|---|---|
| `blitzmetrics-everything` | All 26 skills. **Start here.** |
| `authority-and-reputation` | Knowledge Panel, AI search, reviews, proof |
| `content-engine` | Articles, video, repurposing, distribution |
| `client-operations` | Cadence, access, reporting, audits |
| `quality-and-standards` | Verification, QA, judgment, the skill registry |

## Want it to run without you?

Skills wait for you to ask. **Agents** and **scheduled jobs** run on their own —
the weekly report that posts itself, the daily monitor. That's Cowork, and it's
covered at the install link above.

## For maintainers

One `skills/` folder is the single source of truth. Bundles in
`.claude-plugin/marketplace.json` are just *selections* over it — a skill is
never duplicated.

**Adding a skill:** drop `skills/<name>/SKILL.md`, add `"./skills/<name>"` to
`blitzmetrics-everything` and to any topical bundle. Push. Everyone gets it on
their next sync.

**Never rename a skill or a bundle.** Installs are keyed by name — a rename
installs a second copy alongside the old one instead of upgrading it.
