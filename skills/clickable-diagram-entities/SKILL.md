---
name: clickable-diagram-entities
description: Use whenever building a diagram or showing something with multiple sub-components. Every component must link to a real entity page. Skip thin stubs. 200+ tasks go to the Task Library, not 200 new pages.
---

# Clickable diagram entities

Use this whenever you build a diagram, roster, or any visual with multiple sub-components. This is a global rule.

## The rule

Every visible component is a link to a real page with more detail. That is the SEO tree: drill from the top entity to the next entity, never a dead picture.

A component is a box, row, department, desk, task, runtime, or loop step the reader can point at.

## What counts as a real page

Link to an existing canonical URL first. Do not invent a new page that only restates the parent.

Skip (and say so) when a new page would be a thin stub or would confuse the tree:

- 200+ Task Library tasks already have SOPs. The Task Library box links to https://blitzmetrics.com/task-library/ and https://blitzmetrics.com/task-library-dashboard/. Do not spawn 200 new WordPress pages.
- Named Grok Bot desks live on https://dennisyu.com/how-i-use-grok-bot/. Do not create one-paragraph bios.
- The six departments already live on https://blitzmetrics.com/skill-is-a-function-agent-is-a-person/. Link there unless a department already has its own definitive article.
- A private desk is not a public entity. Do not link it.

## Preferred destinations (verify live before publish)

- Skills / playbook: https://github.com/dennisyu/blitzmetrics-skills
- Task Library: https://blitzmetrics.com/task-library/
- Task Library Dashboard: https://blitzmetrics.com/task-library-dashboard/
- How we turned tasks into skills: https://blitzmetrics.com/how-we-turned-239-tasks-into-an-ai-runnable-skill-library/
- Six departments / skill vs agent: https://blitzmetrics.com/skill-is-a-function-agent-is-a-person/
- Build agents: https://blitzmetrics.com/build-agents/
- Persistent agents / update loop: https://blitzmetrics.com/persistent-agents/
- Grok Bot hub: https://dennisyu.com/how-i-use-grok-bot/
- Claude: https://blitzmetrics.com/how-to-use-claude/
- ChatGPT: https://blitzmetrics.com/how-to-use-chatgpt-business-marketing-mechanic-episode-8/
- Learn-Do-Teach / 9 Triangles: https://blitzmetrics.com/9-triangles-framework-scalable-home-service-businesses/

## How to make the diagram clickable

A flat PNG is not done. Use one of these, in order:

1. Linked cards or a table under the picture, one row per component, each href live.
2. Inline SVG with an `<a>` around each region.
3. HTML image map only if SVG is not allowed.

Then live-check every href. Do not publish until outbound links return 200.

## Definition of done

- Every public component has a href.
- Every href is a real, live entity page (or a justified skip written next to it).
- No new thin stubs.
- No mermaid-only diagrams on WordPress (they do not stay clickable).
- Secrets, revenue, and private desks stay off the map.
