---
name: model-judgment
description: The operating layer that makes boil-the-ocean affordable — let the agent use its OWN judgment to route each task to the cheapest model tier that clears the quality bar, delegating bulk work DOWN to smaller models in subagents and escalating hard judgment UP to the top model. Read alongside boil-the-ocean; this governs WHICH engine runs each part of every skill.
---

# Model Judgment — pick the right engine for each part of the job

This file sits beside `boil-the-ocean`. Boil-the-ocean says *do the whole thing, don't stop at 90%*. This file says *here's how to power the whole thing so doing it completely stays cheap*. Together: full coverage (boil-the-ocean) at a fraction of the cost (model-judgment). Neither changes WHAT a skill produces — only HOW it runs.

## The principle

Don't dictate the model. **Let the agent use its own judgment to choose one.**

The old habit was to run everything through one premium model — the harvest, the boilerplate, the file-wrangling, AND the one hard judgment call — because that's whatever model your session happened to open on. That's how you burn a plan's cap by 3pm and pay ceiling prices for grunt work.

The fix is one instruction: *for each task, decide the tier yourself and route it there.* Cat Wu and Thariq Shihipar of the Claude Code team put it plainly — it's better to tell a top model to **use its own judgment** about how to work than to hand it rigid rules. Simon Willison's working version (2026-07-03): *"For all tasks, use your judgment to decide an appropriate lower-power model and run that in a subagent."* Same idea, applied to a whole content operation instead of one repo.

## Two directions — both are "let the model pick the tier"

**Delegate DOWN (the default).** The orchestrator — the smart model you're talking to — does the thinking, then spins up **subagents on a cheaper model** for the high-volume, mechanical, first-draft work. Keep judgment, review, and synthesis in the main loop; push the bulk to the basement.

**Escalate UP (the Advisor Strategy).** The mirror image, from Anthropic (2026-04-09): a **cheap executor drives the whole task** and consults a top model **only when it gets stuck**. In an API harness this is a real feature — the `advisor` tool: run on Haiku or Sonnet, and it pings Opus for a short plan at the exact moments it needs frontier reasoning, then keeps going. Anthropic's own benchmark: Haiku's hard-research score more than doubled (19.7% → 41.2%) with an Opus advisor, at a fraction of Opus's cost. In a chat/Cowork session, "escalate up" is the mental rule: when a cheap subagent is spinning, hand that one subtask up a tier instead of dropping to premium for everything.

## The tier map — the whole ladder, not just "the expensive one"

| Tier | The work in THIS pack | Engine |
|------|----------------------|--------|
| **0 — Mechanical** | Transcript pulls, REST publishing, PDF/image generation, dedup, file wrangling, enrichment lookups | **Plain scripts, no model** (~$0) |
| **1 — Bulk / first draft** | Positive-mentions harvesting, first-pass article drafts, boilerplate pages, restyles, bulk social copy | **Small model in subagents** — Sonnet for anything that chains tool calls, Haiku or an open model like GLM for single-shot extraction and classification |
| **2 — Judgment** | Reputation scoring, the "earned but illegible" insight, entity disambiguation, strategy, and **writing in the subject's real voice** | **Top model** — Opus at raised effort, → the flagship (Fable) for crown-jewel work |
| **3 — Computer-use** | Logged-in publishing, browser-driven fixes, anything behind a login or a firewall | **The interactive agent on your own machine** (Cowork / browser control) |

Most of your token volume lives in tiers 0 and 1 and does not need a frontier model. Only the thin tier-2 slice — the real score, the real insight, your actual voice — earns the ceiling.

### The effort dial — a rung between the tiers (new, July 24, 2026)

Opus 5 added a per-turn reasoning-effort setting: low, medium, high, xhigh. That puts a rung on the ladder that did not exist before, and it changes the default move when a cheap tier stalls.

The old escalation was binary — the small model struggles, so jump to the flagship and pay ceiling prices for the whole remaining run. Now there is a cheaper step in between: **raise effort before you raise model.** Take the one hard sub-step to Opus at high, leave everything around it where it was, and only reach for the flagship when raised effort has actually failed a named quality check.

It cuts the other way too. Plenty of tier-2 work is judgment in name only — a scoring pass with an unambiguous rubric, a dedup call with clear rules. Drop the effort instead of dropping the model and you keep the reasoning quality you were paying for while spending less on it.

### Every scheduled job needs a fallback tier

Fable was suspended for two and a half weeks in June 2026 by an export-control order and came back July 1. Nothing was wrong with the routing table; the model was simply gone.

So: any job that runs unattended names a second engine. If the top tier is unavailable, the run drops to Opus at xhigh and says so in its output rather than stalling at 4am. A routing table with exactly one path through it is not a routing table.

## How to actually do it

- **In Cowork or Claude Code:** the agent spawns a subagent and sets the model per call (haiku/sonnet/opus/flagship). This is not a coding-only trick — it works for research, writing, scoring, and site builds just as well. You can also just *say it once* as a standing instruction: *"For substantial tasks, use your judgment to route bulk work to a cheaper model in a subagent and keep the judgment calls on the top model."*
- **In an API harness (a factory you run on a schedule):** set the executor model per tier in config, and turn on the `advisor` tool so the cheap tier can consult the top model when stuck. Route drafts to the small model; route scoring to the top model.
- **The one-line standing rule to paste into a Project or memory:**
  > For any substantial build, research, or writing task, use your own judgment to route it to the cheapest model tier that clears the quality bar. Delegate bulk and first-draft work down to a smaller model in a subagent; reserve the top model for scoring, strategy, disambiguation, and voice; escalate a stuck cheap tier up. Verify subagent output before shipping. The bar stays "holy shit, that's done."

## The decision, in one breath

Ask of each task: *does getting this wrong require taste, judgment, or my voice?* If **no** → push it down to a cheaper model in a subagent. If **yes** → keep it on the top model, and let the cheap tiers escalate up to it when they stall. That's the whole discipline.

## Worked examples — patterns first, then a real receipt

Patterns (where each tier runs):

- **Harvesting every good mention** of a client across the web → tier 1. A small model in parallel subagents sweeps the sources; the top model only ranks and interprets the shortlist.
- **A 400-article wave** for a client's topic cluster → tier 1 drafting, tier 2 editing. Drafts on a cheap model, the canonical hub and the voice pass on the top model.
- **Scoring a personal brand straight** (the KP-gated rubric) → tier 2, top model only. Never let a cheap model hand out a flattering number.
- **Writing in the subject's voice** → tier 2, flagship. This is the one thing that reliably reads as "AI" when you cheap out — so don't.

**A real receipt (2026-07-20).** Before publishing a pricing article, we ran its entire QA as three parallel **Haiku 4.5 subagents** — the $1/M model — while the flagship only orchestrated and judged: a numbers auditor re-derived all 8 cost scenarios from scratch (8/8 pass), an adversarial claims auditor checked every published claim against the raw artifacts, and a source verifier re-fetched the four primary pricing/benchmark pages. Worker total: **100,423 tokens ≈ $0.16 on Haiku, vs ≈ $1.61 had the flagship run the same passes — 90% saved on identical deliverables.** Two catches made it a teaching receipt: the *cheap* auditor caught the *orchestrator* overclaiming ("has run" where the artifact only proved "was built"), and the *flagship judge* caught the *cheap* worker mislabeling units by a factor of a million in a table whose arithmetic was otherwise correct. Delegate down, judge up top — both directions earned their keep in one run. Full receipts, token tables, and the delegate-vs-don't math on two live article programs (81% and 90% saved): blitzmetrics.com/kimi-k3-vs-claude-content-factory-math/

**Show receipts, not vibes.** When you document a run, include the token counts, the cost both ways, and what the judge caught. "Built" is not "running" — never claim a lane runs until it has a receipt. And if no worked example exists yet, run one before you publish; the example is part of the deliverable.

## Why this is the affordable half of boil-the-ocean

Boiling the ocean — full coverage, every edge case, the test, the doc, run-it-again-until-done — is only sustainable if each run is cheap. Tiering by judgment is what makes "run it again until the Definition of done passes" cost pennies instead of dollars. Route by tier and you get roughly 3× the throughput at a fraction of the cost, with no quality loss where quality matters. Cheap where it's mechanical; expensive where it's judgment; complete, always.

## Sources & links

- Simon Willison, *"Fable's judgement"* (2026-07-03) — https://simonwillison.net/2026/Jul/3/judgement/
- Anthropic, the Advisor Strategy (2026-04-09) — https://claude.com/blog/the-advisor-strategy
- Anthropic, *Create custom subagents* — https://code.claude.com/docs/en/sub-agents
- Runs beneath: all skills in this pack. Read with `boil-the-ocean` (WHAT to finish) — this file is WHICH engine finishes it.

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-31-an-unknown-flag-is-not-a-no-op -->
**July 31, 2026** (from: skill-pack-propagation daily run, July 31, 2026)

`--help` is not a safe probe. On July 31, 2026, mid-run, `python3 harvest_learnings.py --help` was
typed to check the script's interface before filing a note. The script read only the three flags it
knew (`--dry-run`, `--replay-applied`, `--dirs=`) and silently ignored the rest, so `--help` fell
through to the default action and performed a real harvest: eight source skill files rewritten, the
inbox emptied, and the published packs instantly one revision behind their own sources. Nothing
errored. The output looked exactly like a successful intentional run, and the only reason the
divergence did not ship was that the operator recognised it in the log.

The general shape: a script that MUTATES state and treats an unrecognised argument as "proceed with
the default" has inverted its own safety. Someone typing a flag the script does not know is, by
definition, unsure what it does — that is the worst possible moment to run the destructive path.
Argument parsing that only whitelists is not parsing; it is a filter with a trapdoor underneath.

The rule: every state-changing script exits non-zero on an unrecognised argument and ships a `--help`
that prints and exits 0. Never probe an unfamiliar script by guessing a flag — read its argv handling
first, or run it with the flag it documents for dry runs. Where a `--dry-run` exists, it is the probe.

Corollary on recovery: when an accidental write does happen, finish the loop rather than unwinding it.
Reverting eight source files would have left the applied/ ledger, the manifests and the live packs in
three different states; re-running propagate + republish took four minutes and left every artifact
consistent, with the lesson genuinely carried into all 13 packs.

Fixed July 31, 2026: harvest_learnings.py now rejects unknown arguments with exit 2 and prints usage
on --help/-h/help, verified against --help (exit 0), --bogus (exit 2), --dry-run and a bare run.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
