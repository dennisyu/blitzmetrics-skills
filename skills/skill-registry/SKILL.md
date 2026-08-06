---
name: "skill-registry"
description: "Keep every BlitzMetrics / Local Service Spotlight skill centrally available and activatable. Use when adding a new skill, auditing the skill inventory, wiring a skill into a scheduled job or agent, reconciling what is installed against the canonical pack, or when someone asks 'is this skill part of our framework', 'where do our skills live', 'why isn't this skill running', or 'add this to the skill pack'."
---

# Skill Registry

**Use this whenever a new capability gets built.** A method that lives in a chat thread, a Google Doc, or a loose `.skill` file is not part of the framework — nothing propagates it, no agent can find it, and no scheduled job can activate it. This skill is the intake gate that prevents that.

## The five places a skill can live

Know which one you are touching. They propagate very differently.

| # | Registry | Scope | Propagates to | Who can write to it |
|---|---|---|---|---|
| 1 | **Plugin** (`.plugin` file → marketplace) | Whole team | Everyone who installs it, on every device, in every session | Anyone who can publish the plugin |
| 2 | **Account skills** (claude.ai) | One person | That person's sessions only | Only the account owner, by accepting a delivered `.skill` file |
| 3 | **Cloud scheduled tasks** | One account | Fresh cloud session per firing | Anyone with the account, via the scheduled-task tools |
| 4 | **Local Cowork scheduled jobs** (desktop) | One machine | That machine only. **Invisible to cloud sessions** — they do not appear in a cloud `list_triggers` call | The desktop app |
| 5 | **Canonical pack + Monday sync** | Whole team | Rebuilds each person's skill plugin when the pack changes | Whoever maintains the pack |

**Registry 1 is the only one that scales.** Account skills are per-person and cannot be installed by an agent on the user's behalf — the owner has to accept the file. If a capability matters to more than one person, it belongs in the plugin.

## Intake gate — run this for every new skill

Do not consider a skill "done" until all six pass.

1. **Does it exist as a `SKILL.md` with valid frontmatter?** `name` (kebab-case, matching the directory) and a third-person `description` containing the literal phrases someone would actually type.
2. **Is it inside a plugin's `skills/` directory** — not a loose file, not only a chat attachment?
3. **Is the plugin packaged and delivered** as a `.plugin` file, so the team can install it?
4. **Is it in the canonical pack**, so the Monday sync propagates it instead of silently skipping it?
5. **Can a scheduled job activate it?** Write the trigger prompt that would invoke it, and confirm the skill's description contains the phrases that prompt uses. A skill whose description does not match its own trigger prompt will not load.
6. **Is it in the inventory** — `references/inventory.md` in this skill — with its registry, owner, and cadence?

If a step cannot be completed in this session, **say so explicitly and name who has to do it.** Reporting a skill as "shipped" when it is sitting in a chat thread is the specific failure this gate exists to prevent.

## Shipping it so people actually install it

Building the skill is not the hard part. The loss is in the last inch — someone
downloads a pack and never installs it, because nothing told them a download is
not an install. → `references/distribution.md`

The short version:

- **Ship `.plugin`, not `.zip`.** A `.plugin` file renders an Install button in
  the chat. A `.zip` is just a download with no install path from there. Same
  bytes, completely different outcome. Convert with `scripts/pack2plugin.py`.
- **Say the install step out loud every time you deliver one.** "This is
  delivered, not installed — accept the card above."
- **Report delivered, never installed.** You get no signal that they accepted.
- **Link the install guide** from every place a file can be downloaded.

## Wiring a skill into a scheduled job

A scheduled task starts a **fresh session with no memory of the conversation that created it**. So:

- Write the trigger prompt as a complete standalone instruction.
- Name the skill explicitly in the prompt (`Use the geo-visibility-audit skill.`). Do not rely on implicit triggering in an unattended run.
- Name the client, the properties, and where the output goes — the fresh session knows none of it.
- State the deliverable and its destination (post to thread X, save to folder Y). An unattended run with no destination produces nothing anyone sees.
- Use the **scheduled-task tools** (`create_trigger`, `send_later`, `list_triggers`, `update_trigger`, `delete_trigger`). Never use the in-process cron tools — anything they schedule dies when the session ends and the job silently never runs.

Cron is UTC. Convert from the owner's local time, and shift the day fields if the conversion crosses midnight.

## Wiring a skill into an agent

Put an agent definition in the plugin's `agents/` directory when the skill should run as a delegated, self-contained job — a weekly audit, a fan-out across clients, anything a person would otherwise babysit. The agent's `description` needs `<example>` blocks showing the triggering conditions, and its body is the system prompt. See `agents/geo-auditor.md` in this plugin as the working model.

## Reconciliation — run monthly, or when something feels missing

1. List what is actually installed: account skills, and the skills inside each installed plugin.
2. List what the canonical pack claims to contain.
3. Diff them. **Every skill in the pack but not installed is a propagation failure; every skill installed but not in the pack is an orphan that will be wiped by the next sync rebuild.**
4. For each recurring scheduled job, confirm the skill it names still exists under that exact name. Renaming a skill silently breaks every job that calls it.
5. Check the local desktop scheduled jobs separately. They do not appear in a cloud listing, so a cloud-only audit will report them as absent when they are running fine — and will miss them entirely when they are broken.
6. Record the result in `references/inventory.md` and report the diff, not just the totals.

## Field lessons

- **A `.skill` file delivered into a chat is a delivery, not an installation.** You get no signal whether the person saved it. Report it as delivered, never as saved, and follow up.
- **Sessions cannot install skills.** The skill files on disk are a read-only cache; editing them changes nothing durable. Package and deliver, or publish the plugin — those are the only two real paths.
- **The description is the activation surface.** A skill nobody can trigger is inventory, not capability. Write descriptions with the words people actually type, then test by using one of those phrases cold.
- **Name the gap out loud.** When a capability exists but is not yet propagating, saying so plainly is more valuable than a clean-looking summary that hides it.

## Pairs with

`skill-creator` (authoring and evals) · `cowork-plugin` (packaging and publishing) · the weekly MAA cadence.
Inventory and the current gap list: `references/inventory.md`.
