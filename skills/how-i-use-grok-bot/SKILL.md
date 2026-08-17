---
name: how-i-use-grok-bot
description: Use when setting up Grok Bot as an ops desk, writing a Grok Bot how-to, or teaching CCS on this workflow. Includes the three layers (skills, departments, agents) and the live-work to skill-update loop.
---

# How I use Grok Bot

Use this skill to set up or run Grok Bot as one ops desk. Do not invent menus, URLs, or product names. Do not print secrets. Do not publish unless the user asked.

Canonical home: https://dennisyu.com/how-i-use-grok-bot/

## What this is

Grok Bot is the Cursor/xAI desktop and iOS teammate. It has its own computer, named agents, routines, and connectors.

It is not Grokipedia. It is not "Grok Heavy" (a model mode).

CCS framing: the public article is Content. This file is Software. The numbered steps are the Checklist.

## Three layers (do not collapse these)

1. Skills: the shared playbook. Task Library + GitHub skill files. Same methods on every runtime. A skill is a function.
2. Departments: Front desk, Research, Build, Publishing, Growth, Quality. Stable. Do not invent a seventh because a new tool showed up.
3. Agents: named desks per runtime. Grok Bot has a roster of desks. Claude is skills plus scheduled jobs. ChatGPT/Codex is Work plus Codex. Do not force the headcounts to match. Harmonize the playbook, not the roster.

Update loop: Live work → Receipt → Skill update → Next run. Training + Documentation owns this loop. A Zoom, a broken button, or a desk that just learned something becomes a public master version, then gets skinned across verticals.

If a diagram still shows "12 agents" as the architecture, it is stale. The architecture is three layers plus the update loop. The named desks are the Grok Bot skin of layer three.

## Hard rules

1. One human. One coordinator conversation. Specialists get a job when the coordinator assigns it.
2. No silent fan-out. Do not send the same job to Claude or ChatGPT as workers unless the user says so in the thread.
3. Do not waste paid usage across seats.
4. Update, not Reset. Recovery is Settings → Updates → "Update Grok Bot's Computer". Update keeps files and logins. Reset drops unsynced work. Never recommend Reset.
5. Secrets stay on the agent computer. Never put passwords, tokens, or vault contents in Drive, Slack, chat, or a public note.
6. Public handoff notes go to Drive. Facts, URLs, next steps. No secrets.
7. Person-author rule: if you publish, set the person user first. If only admin exists, publish as admin and fix later.
8. Do not list client revenue. Do not invent UI. Real Settings tabs: General, Plugins, Team Setup, Appearance, Updates.
9. Every diagram component is clickable and goes to a real entity page. See the clickable-diagram-entities skill.

## Real UI (do not invent others)

- Open Settings: sidebar account button, Cmd+,, or command palette "Open settings".
- Settings tabs: General, Plugins, Team Setup, Appearance, Updates.
- Computer recovery: Settings → Updates → "Update Grok Bot's Computer".
- Per-agent info pane: click the agent name in the chat header, or Cmd+Shift+I.
- Delete an agent: sidebar right-click → Delete.

## Steps

1. Confirm you are in the coordinator conversation, not a new side chat.
2. Restate the job in one sentence. Stay in that conversation.
3. If the computer is stale, Update. Do not Reset.
4. Inspect the current agent via the header name or Cmd+Shift+I before you assume computer state.
5. Do the work on the Grok Bot computer. Store application passwords there. Never echo the secret.
6. If publishing WordPress: person user first; admin only as fallback, then fix later.
7. Write a Drive handoff: what shipped, live URLs, what is still open. No secrets.
8. Stop. Do not open a second desk. Do not fan out.

## Related reading

- https://dennisyu.com/how-i-use-grok-bot/
- https://blitzmetrics.com/build-agents/
- https://blitzmetrics.com/skill-is-a-function-agent-is-a-person/
- https://blitzmetrics.com/persistent-agents/
- https://blitzmetrics.com/task-library/
- https://github.com/dennisyu/blitzmetrics-skills
- https://x.ai/bot
