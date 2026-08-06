---
name: "geo-visibility-audit"
description: "Measure how AI models actually see a person or brand — query ChatGPT, Gemini, Perplexity and Claude live, score identity vs discovery presence, name every citing source, and produce the weekly MAA GEO block. Use when asked for GEO rankings, AI citations, LLM visibility, AI share of voice, 'are we showing up in ChatGPT', or when a weekly MAA needs a GEO section. Also use to troubleshoot why Ahrefs Brand Radar or a mentions database reports zero for a person's name."
---

# GEO Visibility Audit

**Use this when** someone asks how a client shows up in AI answers — or when a weekly MAA needs its GEO block. Runs for a person, a company, or both at once. Takes about 15 minutes of tool time.

**The core insight this skill exists to encode:** indexed AI-citation tools cannot see individuals. They sample prompts by search volume, and a person's name has almost none. Reporting their zero as a finding is a measurement artefact. **You must query the engines live.**

## Inputs

- The person's name, plus every spelling and transliteration they use (Paul/Pavlo, diacritics, maiden names).
- Their owned properties: personal domain, company domain, community/event domain.
- Their claimed positioning — what they *want* to be known for. Get this from the `personal-brand-strategist` brief if one exists.
- Their buy box: who hires them, for what, where. This is what generates the discovery prompts.

## The method

### 1. Build the prompt ladder — two tiers, always

The whole audit turns on separating these. → `references/prompt-ladder.md`

**Known-item tier** — the prompt names the person or their company. Tests whether the entity exists in the model and is described correctly.
- "Who is {name}?"
- "Who is the CEO of {company}?"
- "Who runs {community/event}?"
- "Is {company} any good? What do reviews say?"

**Discovery tier** — the prompt describes a *need*. Tests whether they get recommended to a stranger. This is where the money is.
- "Best {category} agency in {geo}"
- "Top {category} experts to follow in {year}"
- "Who are the top {category} speakers in {geo}?"
- One long, high-intent buyer question written in the voice of their actual buyer, with revenue, platform and constraint named.

Minimum 4 known-item and 5 discovery. Run known-item across **all four engines**; discovery can be ChatGPT-led with one Perplexity long-tail.

### 2. Query the engines live, capture the sources

Exact working calls in `references/tool-recipes.md`. Summary:
- **ChatGPT** — `ai_optimization_chat_gpt_scraper`, `force_web_search: true`. Returns `sources[]` with domain + title, and `brand_entities[]` which tells you how the model *categorises* the person. Set `location_name` to their market.
- **Gemini / Perplexity / Claude** — `ai_optimization_llm_response`, `web_search: true`. Perplexity returns the richest citation list; Gemini returns grounding annotations mapped to specific sentences.

Record for every prompt: engine, named yes/no, every source domain, and who won instead when they lost. **The losers' source pages are the action list** — the model just told you which directory it shops at.

### 3. Score it

| Metric | How |
|---|---|
| Engines recognising | of 4, on the identity prompt |
| Distinct citing domains | unique domains across all answers |
| Citation instances | total source links returned |
| Third-party share | citations not on an owned domain ÷ total |
| Known-item won | x of n |
| Discovery won | x of n |
| Claim consistency | for each claim, how many of 4 engines surfaced it |

Third-party share is the one to watch. An answer sourced only from the client's own site reads as self-assertion and is fragile. Corroboration is what makes an entity durable.

### 4. Cross-check the link profile — and filter spam before you report it

Pull referring domains with `is_spam` in the select and **report the clean count, never the raw count.** Link-farm blasts arrive automatically once a domain starts ranking; a raw "+23 referring domains this week" can be 23 spam domains and zero real ones. → `references/tool-recipes.md`

Then check that the clean domains and the citing domains are the same names. When they are, you can show the causal chain end to end: placement → link → citation. That is the most persuasive thing in the whole report.

### 5. Write it up

Report structure and the MAA block in `references/report-template.md`. Build the visual report with the `dataviz` skill — validate the palette, never eyeball it.

## Output

- HTML report, self-contained, light + dark, hover tooltips, table view behind every chart.
- A GEO block for the weekly MAA (6 lines, pasteable).
- An action list where every item names the specific page or directory to get onto, taken from the losing answers.

## Definition of done

- Every engine queried live in this run — no numbers carried over from last week without a re-run.
- Every citing domain named. "15 domains" without the list is not a finding.
- Every discovery loss names who won and which source page the model used.
- Spam-filtered link numbers, with the raw number shown beside it so nobody thinks we hid it.
- At least one item in the action list is something the client can do this week.

## Troubleshooting — read this before reporting a zero

| Symptom | Cause | Do this |
|---|---|---|
| Ahrefs `site-explorer-ai-responses-count` returns 0 for a personal domain | Ahrefs replays a fixed prompt panel sampled by ask-volume. A person's name has none. | Query live. Report the live result; note the index gap rather than the zero. |
| `Missing addon: Brand Radar ["Chatgpt"]` | Per-engine paid add-on. | Note it, price it, move on. It would still be volume-sampled. |
| Mentions database returns nonsense for a name | Keyword databases word-match. "Dennis Yu" matched *Yu Yu Hakusho* and Dennis Trillo. | Never use keyword-matched mention data for people. Live query only. |
| Model returns a different person with the same name | Real name collision. | Add a disambiguator to the prompt ("the ecommerce consultant"), and flag it — it is a Knowledge Panel risk worth its own action. |
| Model describes them accurately but cites only their own site | No corroboration yet. | This is the finding. Third-party share is the metric; the action is placements, not more self-published articles. |

## Field lessons

- **Publishing volume does not create citations.** One client published 299 articles on his personal domain and the indexed AI citation count stayed at zero, while his company site — with a Clutch profile and a Trustpilot page — earned 11. Directory and review presence beats owned-content volume for discovery-tier prompts, every time.
- **The losing answer is more useful than the winning one.** A win tells you it worked. A loss hands you the exact URL of the roundup page the model reads.
- **Check every language and spelling the person lives in.** An English-only audit of a non-English person measures your search, not their authority.
- **Our own knowledge-base articles get cited.** Once a client has a page on blitzmetrics.com, Perplexity started using it as a corroborating source. Publishing the client's knowledge base is itself a GEO placement — say so in the report.
- **Never criticise the previous week's report to make this week's look better.** Show what the older method could not see, then hand over the method that can.

## Pairs with

← `personal-brand-strategist` (what they claim) · ← `positive-mentions-harvester` (the proof to place)
→ `dataviz` (build the charts) → the weekly MAA thread.
