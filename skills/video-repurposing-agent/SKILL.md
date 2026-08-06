---
name: video-repurposing-agent
description: Watch a YouTube channel every day, judge which new videos deserve repurposing, and turn the winners into published articles on the right site (personal brand, company, or both) — written to BlitzMetrics standards, graded to A- by jennifer, cross-linked per the Content Factory hub rules. Use when a client or member has a YouTube channel and wants it feeding their sites without anyone watching the uploads page.
---

# Video Repurposing Agent — the daily channel watchdog

**Use this when** someone records on YouTube but their websites don't know it. This agent closes that gap on a schedule: every day it checks the channel, triages anything new, and moves the worthwhile videos through transcript → article(s) → grade → publish → cross-link. One recording becomes site equity the same week it was uploaded.

Built July 20, 2026 by merging Daniel Goodrich's Repurposing Suite v0.2 (the YouTube Data API watch loop, effort routing, and grader caps he validated on Escape Fitness LIFTS — 247 episodes inventoried, first article graded A- for 251 API units) into the Content Factory method. Daniel's grader was already scoring "per Jennifer rubric," so the two systems merged without a seam.

## The client card (fill once, reuse every run)
One block per client/member — keep it in the project or a `client.json`:
- **Channel URL** (and channel_id once resolved — cache it).
- **Sites**: personal-brand site URL, company site URL, or both. Each with its publish mode: `draft` (self-serve members — they click publish) or `live` (managed — we publish via the site's Application Password; see blitzmetrics.com/application-passwords/).
- **Voice + context files**: brand-voice doc, ideal-client file, links file (real domains, offer pages) — read them every run; never invent a link or offer.
- **Network entities**: name → URL map of the people, companies, and partners this client is tied to.
- **Extra banned words** (client-specific), batch cap per run (default 3), and the hub URLs nothing may compete with.
- Never store credentials in the card. Secrets live in the OS keychain or `.credentials.json`, and never appear in chat, reports, or output files.

## Step 1 — Daily watch (the part that runs before anyone is awake)
- First run: pull the channel's full uploads playlist and write `inventory.json` (id, title, publishedAt, duration, views, thumbnail, status per video).
- Every run after: poll newest-first and STOP at the first video already in the inventory — append only what's new. Log "0 new videos" as a valid result; never invent work.
- How to read the channel, in order of preference: (1) YouTube Data API — playlistItems.list + videos.list, 1 unit per 50 videos, if API credentials exist; (2) keyless — the channel's public uploads page or RSS (`/feeds/videos.xml?channel_id=`) — fine for daily new-video detection with zero setup.
- Schedule it off-peak (our standard: ~4am local, one run per client per day). Say in the log which read path ran.

## Step 2 — Triage: is this video worth repurposing, and how hard?
Score each new video against the client's GCT (Goals · Content · Targeting) and decide out loud:

| Tier | When | Article shape | Cross-links | Revision budget → target grade |
|---|---|---|---|---|
| **SKIP** | Off-topic for the GCT, duplicate of an existing article's ground, under ~2 minutes with no standalone claim, or pure promo | Log the reason, mark `skipped` — that IS the deliverable for this video | — | — |
| **LIGHT** | One reusable idea; short clip or single-point video | 600–1,000 words, embed only | 1–2 | 1 → B |
| **MODERATE** | Solid episode; one clear theme | 1,000–1,500 words + diagram if it strengthens the point | 2–3 | 2 → B+ |
| **STRONG** | Signature content: named guests, real numbers, a framework, a story only this client can tell | 1,500+ words + required SVG diagram | 3–5 | 3 → A- |

A 1-hour STRONG video may carry more than one article: if the transcript yields two distinct GCT-worthy themes with 6+ subtopics each, ship separate articles on separate hubs — never two pages on the same topic (that's content vandalism, competing with yourself).

## Step 3 — NEW vs ENHANCE (search before writing)
Before drafting, search the destination site (site: search + the site's own search) for the video's topic:
- **No live article owns it** → write NEW.
- **A live article already owns it** → ENHANCE: embed the video there, add the new material as sections, refresh the date — and log "enhanced X" instead of shipping a competitor page.
- **A thin/stub page holds the slug** → rebuild it in place.

## Step 4 — Destination and point of view
- **Personal-brand site** → first person, the owner's voice ("I"), relationship context by name. WordPress author = the person, never admin.
- **Company site** → third person; the subject is the company or featured guest.
- **Both** (only when both POVs have real material): two different articles — the personal cut (what I learned/did) and the company cut (what the company/guest delivered) — cross-linked to each other, each pointing at its own site's hub. Different angles, never the same article twice.
- The agent decides and states the routing + one-line reason in the run report.

## Step 5 — Transcript
In order of preference: the video's caption track (prefer a manually-uploaded track over auto-generated; API path: captions.list → captions.download, ~250 units per video — a 10,000-unit free day covers ~39 articles); the client's own transcript or Descript export; auto-captions scraped from the public player. Clean it: strip timestamps, cut filler, fix proper nouns against the client's known entities. Quotes used in the article stay verbatim.

## Step 6 — Write, link, illustrate
Hand the cleaned transcript + client card to `definitive-article-writer` (Brandon) with the tier's spec. Non-negotiables:
- Embed the source video at the top with one sentence of provenance; answer the article's question in the first paragraph.
- 6–12 verb-led H2s for a long video; paragraphs ≤5 lines; preserve real quotes (E-E-A-T Experience).
- **Entity Linking Decision Tree** — route every named entity: in-network person → their personal-brand site; in-network company → their site; out-of-network person/company or any tool/concept → the BlitzMetrics article on it, else plain text; Dennis Yu → dennisyu.com. Anchor text 3–6 descriptive words; link each entity on first mention only; 3+ in-network links on STRONG.
- Every article links UP to its hub (Content Factory rule) and sideways to 2–3 sibling articles; when we run both sites, link across them.
- Featured image = the video's own maxres thumbnail (`i.ytimg.com/vi/{id}/maxresdefault.jpg`) — a real frame, never a text-only card and never stock (blog-card thumbnails standard).
- Evergreen: no dates-as-news, no limited-time promos.

## Step 7 — Grade to done, then publish
- Hand the draft to `jennifer`. **A- is the publish bar — never iterate past A-** (an A is reserved for world-class national-publication journalism). Revise within the tier's budget; below a C after budget, stop and flag for a human with the penalty list.
- Publish per site mode: `live` → post via the site's Application Password (REST, full browser User-Agent), then verify the URL with a cache-busted fetch and confirm the images render; `draft` → stage the post + a one-line morning note ("ready to publish: [title]").
- Mark the video `published` / `staged` / `enhanced` in `inventory.json` with the article URL.

## Step 8 — Report
Append one run report: videos found / skipped (with reasons) / articles shipped (grade, tier, destination, URL) / enhancements / API units used / anything a human must do. Post client-relevant results to the client's Basecamp thread. If the run taught something, file a Skill-Learnings note — that's how this skill stays alive.

## Output
- `inventory.json` — the channel's full state, every video accounted for.
- Published or staged article(s), graded A-/tier target, cross-linked, real-thumbnail featured images.
- A run report a human can read in 30 seconds, plus the log line that stops tomorrow's run from repeating today's work.

## Run on a persistent agent (Fable 5)
- **Loop to done:** a video isn't "processed" at the draft — loop until graded, published/staged, cross-linked, inventoried, reported.
- **Self-verify:** re-fetch every published URL cache-busted; grep the live HTML for the embed and the links you claim are there.
- **Compound with memory:** the inventory watermark, the client card, and the hub map make run 100 cheaper than run 1.
- **Know when to stop:** SKIP is a first-class verdict, zero-new-videos is a clean run, and A- terminates revision. Agents that can't stop are as broken as agents that can't start.

## Notes — Dennis's method
- The proof pattern is Marko Sipila's: phone-shot conference interviews → HVAC Quote's YouTube → repurposed articles → $1/day behind winners → 300+ customers. This agent is that loop with the human watching removed.
- Daniel Goodrich proved the watch-loop economics on Escape Fitness (May 2026): 247 episodes inventoried, transcript via the captions API, first article A- in two revisions, 251 of 10,000 free daily units. His three-skill split (orchestrator / writer / grader) is preserved here as steps 1–5 / 6 / 7.
- One credential can serve a whole managed fleet: clients invite a shared BlitzMetrics access email as YouTube Studio collaborator (Editor), and the same OAuth token reads captions on every channel. Members installing self-serve skip OAuth entirely — the keyless path runs day one.
- Pair the output with `dollar-a-day-strategist`: the article that wins organically is the one that earns the $1/day.

## Definitive article & pairings
- Reference: blitzmetrics.com/inventory-youtube-channel/ · blitzmetrics.com/blog-posting-guidelines/ · blitzmetrics.com/content-factory/ · blitzmetrics.com/application-passwords/
- Pairs with: **video-repurposing-agent** → definitive-article-writer → jennifer → dollar-a-day-strategist → recursive-self-improvement-qa
