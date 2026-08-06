# Distribution — getting a skill from built to actually installed

Most of the loss in this system is not in building skills. It is in the last
inch: someone downloads a pack and never installs it, because nothing told them
a download is not an install.

## The file extension decides whether one-click install is possible

| Extension | What happens when it lands in a chat | Use it for |
|---|---|---|
| `.plugin` | Renders a rich preview card with an **Install** button. One click. | Any pack. This is the default. |
| `.skill` | Offers to save it to the person's account skills. | A single standalone skill. |
| `.zip` | Just a download. No button, no prompt, no install path from the chat. | Only as the fallback for the manual `Customize → Skills → Upload` route. |

**Same bytes, different conversion rate.** A pack served only as `.zip` requires
the recipient to already know about a settings menu they have probably never
opened. Serve `.plugin` first and keep `.zip` as the secondary link.

Convert an existing pack with `scripts/pack2plugin.py` in this plugin:

```
python3 scripts/pack2plugin.py PACK.zip --out ./dist
python3 scripts/pack2plugin.py ./packs/*.zip --out ./dist --dry-run
```

It finds every `SKILL.md` at any depth, repairs frontmatter whose `name` does not
match its directory, strips version suffixes so the plugin name stays stable
across releases (`DealCon-Skills-v3-11` → `dealcon-skills`), drops `__MACOSX`
cruft, carries over `agents/` and `commands/`, and writes the manifest. It leaves
the original `.zip` alone.

> **Why the stable name matters:** if the plugin name changes between versions,
> installing v2 does not upgrade v1 — it installs a second copy alongside it.

## Say the install step out loud, every time

When delivering a plugin or skill file, never stop at "here it is." State plainly:

> This is delivered, not installed. Accept the card above to install it — the
> download on its own does nothing.

And afterwards, report it as **delivered**, never as installed. You get no signal
whether the person accepted. Claiming otherwise puts a false entry in the
inventory, and the next audit inherits it.

## What a distribution page has to answer

The library page that lists packs is not the install guide. A person arriving
cold needs, in this order:

1. **What these words mean** — skill, pack, plugin, agent, in one line each, no jargon.
2. **What they need first** — plan tier, and the admin toggles a Team/Enterprise owner has to flip.
3. **Which path they are on** — decided by the extension of the file they have, not by what they know.
4. **The exact clicks**, with the real menu labels.
5. **The usual mistake** for that path, called out. (Download-and-close for `.plugin`; unzip-first for `.zip`.)
6. **How to tell it worked** — where to look, plus a real trigger phrase to test with.
7. **Where it does not work** — mobile cannot install; agents and scheduled jobs are Cowork-only.
8. **Troubleshooting**, phrased as symptoms the person would actually type.

Reference implementation: `localservicespotlight.com/install/`.

## Per-person vs team

Uploaded skills are private to one account and cannot be installed on someone
else's behalf. A plugin installs for whoever installs it; a **marketplace** added
once by URL then serves updates to everyone without another download.

Order of preference for anything more than one person needs:
**marketplace → plugin file → account skill upload.**

## Definition of done for a distribution change

- Every pack has a `.plugin` link, with `.zip` retained as the secondary option.
- Every pack row links to the install guide.
- The guide names the exact menus, and has been checked against the live product
  this month — Claude's menu labels move.
- Someone who has never installed one has followed it end to end without asking a
  question. Until that has happened, the guide is untested.
