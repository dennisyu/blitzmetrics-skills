---
name: content-agent
description: The Content Agent - drop in one raw video and get back a lightly edited YouTube upload (private, for your review), a blog draft with schema, 5-10 short-clip picks, platform social posts, and an email - everything grounded in YOUR transcript and YOUR files, nothing invented, nothing published without your click.
---

# Content Agent

**Use this when** you have ONE raw recording — a talking-head video, a podcast episode, a webinar, a livestream, even a long voice note — and you want it to become a week of distribution without you touching an editing timeline. Run it weekly. This is the Content Factory's big sister: Content Factory writes the words; the Content Agent also handles the video itself and stages everything as drafts.

> **Read these first, every run:** your brand-voice document, your ideal-client file, and your links file (your real domains, offer pages, and social URLs). Everything below is grounded in those plus your transcript — and nothing else.

## The promise
One recording in. Six things out, all as **drafts for your review**:
1. A lightly edited video, uploaded to **YouTube as Private** (or staged as an upload kit).
2. A **blog post draft** (2,000–3,500 words) with the video embedded, a 3-line TL;DR, and the cleaned transcript at the bottom.
3. **5–10 short-clip picks** with timestamps, hooks, and per-platform captions.
4. **3–4 platform-native social posts** (LinkedIn · Instagram carousel script · X thread · Threads).
5. **One email** to your list, in your newsletter's voice.
6. **Schema + internal links**: JSON-LD for the post, plus 3–5 proposed internal links from your existing pages.

## Hard rules (the whole reason you can trust it)
- **Draft-only.** YouTube = Private. WordPress/GHL = Draft. Email = saved file, never sent. The agent does not publish; YOU publish. Verify the status after every upload and say what you verified.
- **Nothing invented.** Every claim, quote, name, number, and link comes from your transcript, your knowledge-base files, or a page actually fetched and confirmed live. If a link isn't in your files and doesn't resolve when checked, leave it out and say so.
- **Quotes are verbatim** from the transcript. Image/thumbnail captions describe only what is literally in frame.
- **Your voice, not AI voice.** Use the brand-voice file. Style gate: no "not just X, but Y" constructions, H2s start with verbs where natural, no sentences ending in prepositions, no em-dash soup, TL;DR liftable word-for-word. Run the gate as a **mechanical final pass** AFTER all edits and expansions — violations sneak in precisely when you lengthen or rework a draft.
- **Re-ground every file against `transcript.md`**, never against earlier drafts — one imprecise word in an early file otherwise spreads to all of them. Before handing over, spot-check three claims and every quote directly against the transcript.
- **Log every run.** Append one line per video to `Outputs/processing-log.md`: date · source file · what shipped · what's waiting on you. Never process the same video twice — check this log first.

## Folder convention
Work from three folders — **Knowledge Base** (voice, ideal client, links), **Raw** (new recordings go here), **Outputs** (everything produced). Google Drive or local, same names. New video = any file in Raw not yet in the processing log.

## Inputs
- One raw recording from Raw: a video (best), audio, a YouTube link to something already uploaded — or even just a transcript or long text (the written five still ship).
- Your knowledge-base files: brand-voice, ideal-client, links file.
- Optional: a Descript account (Free covers the first full run) or your own editor — the agent never blocks on tooling.
- Optional: WordPress/GHL access for draft staging — paste-ready HTML works without it.

## Steps
1. **Intake.** List Raw, diff against the processing log, pick the newest unprocessed recording. Confirm: "Processing [filename] — right one?" Load the knowledge base. Keep outputs in the video's language unless told otherwise.
2. **Light edit — pick the path you have, never block on tooling:**
   - **Descript** (account / connector available): create a project from the raw file, then run exactly: *"Apply Studio Sound to the whole composition, remove filler words conservatively so it still sounds human, remove silences over 2 seconds, and render/export the result."* Nothing fancier. Then report receipts: fillers removed, trims made, before/after duration. **Zero fillers found = zero removed is a valid result — never invent work.** (Measured reality from our own runs: a 1-minute video edits in ~4 minutes for ~9 AI credits; a full HOUR of raw video edited in ~13 minutes for **49 credits** — 35 fillers and 15m39s of dead air removed, 59:48→42:21. Descript's free plan covers a first full run but watermarks video exports — fine for testing, not publishing.)
   - **Your own tool** (CapCut, Final Cut, etc.): use the 3-line edit checklist (filler pass · silence trim · loudness normalize) and continue with the raw file meanwhile.
   - **No tool:** proceed with the raw video unedited and say so — a real upload this week beats a perfect one next month.
3. **Transcript.** Export from Descript; or pull auto-captions if already on YouTube; or work from a transcript provided. Save `Outputs/<video-slug>/transcript.md` (timestamped where available).
4. **Target keyword.** From the transcript's strongest theme + your positioning: one keyword you can actually win (specific beats glamorous). One line of why.
5. **Blog draft.** Restructure the transcript into an article in your voice: hook open, H2/H3s, verbatim quote callouts, 3-line TL;DR up top, key takeaways, video embed placeholder, cleaned transcript at the bottom. Wire in your offer/lead-magnet link FROM YOUR LINKS FILE. Passes in this order: outline → draft → expand → tighten → style gate LAST.
6. **YouTube upload package.** SEO title (≤70 chars, keyword-front), description opening with the meta title + 2-line meta description, then summary + timestamped chapters + verified links, then transcript excerpt. Tags. Thumbnail brief: 3 concepts, each = frame-grab suggestion + ≤4 overlay words. Upload **as Private** — via YouTube Studio in your signed-in browser, or the one-screen upload kit (`youtube-upload.md`) if you'd rather click yourself. Never public.
7. **Clips plan.** Scan for 5–10 self-contained 30–60s moments; score each: hook-in-1.5s · stands alone · quotable. For each: timestamps, the hook line, and captions for Shorts / Reels / TikTok / LinkedIn in that platform's tone.
8. **Social + email.** LinkedIn post (200–300 words), Instagram carousel script (5–7 slides), X thread (6–10), Threads one-liner — each pointing to the blog post. Email (200–400 words) in your newsletter format: headline takeaway, one verbatim quote, one link.
9. **Schema + internal links.** JSON-LD (BlogPosting + Person + VideoObject) for the post. Crawl your site for 3–5 real pages that should link to the new post; propose natural anchors; touch nothing until approved.
10. **Stage drafts + hand over.** WordPress/GHL draft if connected (verify "draft" in the response); otherwise paste-ready HTML. Save everything to `Outputs/<video-slug>/`. Update the log. Close with the review list: "3 things to approve: YouTube (private) → publish · blog draft → publish · email → send."

## Output
- `Outputs/<video-slug>/` with: `transcript.md` · `blog-post.md` (+ `.html`) · `youtube-upload.md` · `clips-plan.md` · `social-posts.md` · `email.md` · `schema.json` · `internal-links.md`.
- The lightly edited video on YouTube as **Private** (or the upload kit), with receipts: what changed, before/after duration.
- The WordPress/GHL draft if connected — status verified as "draft" and said so.
- One appended line in `Outputs/processing-log.md`.

## Definition of done
- You can review everything in under 30 minutes and publish with clicks, not edits.
- Zero invented facts, quotes, links, or offers — three claims spot-checked against the transcript before handover.
- YouTube is Private, blog is Draft — verified and stated.
- Every asset points home (blog ← video ← clips ← social ← email), in your voice, in your language.
- The log line exists. Next week's run knows what this week did.

## Notes
- Weekly rhythm: record once → drop it in Raw → run this agent → review over coffee → publish. 52 recordings a year becomes 52 posts, ~500 shorts, ~150 social posts, 52 emails.
- What the edit does NOT do (say it out loud, it prevents heartbreak): no b-roll, no music, no burned-in captions, no jump-cut style, no color grade, no auto-thumbnails. It gets a raw recording over the publish line; it is not a video editor with bells and whistles.
- Model note: plans on the big model, drafts on the fast one (see model-judgment). No special setup.

## Pairs with
→ content-factory (words-only weeks) → video-repurposing-agent (this is record-side; that watches the channel publish-side — the full loop) → definitive-article-writer (when a video deserves the canonical page) → dollar-a-day-strategist (put $1/day behind the winner) → recursive-self-improvement-qa (grade the run, better next week)

---
*Built by Dennis Yu (BlitzMetrics / Local Service Spotlight). Reads your brand-voice + ideal-client + links files so everything sounds like you and points home. Draft-only by design: the agent prepares, you publish.*

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:ghl-mcp-truth-2026-07-27 -->
**July 27, 2026**

HighLevel's official MCP (https://services.leadconnectorhq.com/mcp/, Private Integration Token
auth) exposes 36 tools — contacts, conversations, opportunities, payments, calendars, forms,
social posts, blog posts, email templates. It does NOT expose funnels or landing pages, and the
underlying REST Funnels API is read-only (list funnels / list pages / count pages only). There is
no create or update endpoint in any version.

Consequence for every agent that touches a CRM: never promise to "build the funnel page." Write
the page to the client's own WordPress site as a draft and hand over paste-ready copy for their
page template. This is also the only route that works for clients not on the coach's platform.

Send safety: conversations_send-a-new-message is a REAL send — never call it on a scheduled run.
emails_create-template is the safe way to stage a daily email.

<!-- learning:2026-07-29-edit-the-generator-not-the-page -->
**July 29, 2026** (from: applying the SEO-tree block across 13 surfaces on 6 domains, July 29, 2026)

### Before editing any live page, ask what regenerates it

Twelve pages needed the same block. Two of them — `localservicespotlight.com/skill-packs/` and
`/asset-tracker/` — are rebuilt from scratch by their own Python generators on a schedule.
Editing those live would have looked like a clean success: HTTP 200, block in the rendered DOM,
verification green. The next scheduled rebuild would have erased it, silently, and the job that
erased it would still have reported success.

So the work split three ways and each page went through exactly one owner: generated pages got
the block added to their generator, plain pages through REST, base64 payload pages by decoding,
inserting, re-encoding. One owner per file, always.

**Rules:**

1. **Establish the owner before the edit.** Search the project for the page's slug. If a script
   writes it, that script is the only thing allowed to write it.
2. **Two writers on one artifact is a bug even when both succeed.** The loser is whoever ran
   first, and nobody finds out until a reader notices something missing weeks later.
3. **When a live page and a local template have drifted, do NOT "restore" from the template.**
   Our trunk page had picked up three hand-added blocks since its last build; republishing the
   template would have deleted all three. Diff first, then make surgical marker-guarded edits.
4. **Every surgical edit replaces exactly once and raises on zero matches.** A `sub_once()` that
   throws when its anchor is gone turns silent drift into a loud failure the same morning.
5. **Mark generated blocks with a data attribute, not a comment.** `data-system-tree="<node>"`
   survives every filter WordPress runs over content, and gives the checker something exact to
   assert and the updater something exact to replace.

Learned July 29, 2026.

<!-- learning:2026-08-03-the-message-about-the-artifact-drifts-faster-than-the-artifact -->
**August 3, 2026** (from: somba-skill-weekly-update — first run under the "tell all ~100 members, not one" mandate; found the pack current and every sentence describing it stale)

### The message about the artifact drifts faster than the artifact

The SOMBA skill pack was in perfect shape. `skill-pack-propagation` had rebuilt it every morning,
the daily verifiers were green, the zip on sigrun.com matched the zip on disk. Three new agents had
shipped that week and eleven more had absorbed 51 field lessons. The artifact was flawless.

Every sentence describing it was wrong.

The library held **22 agents**. Five separate member-facing surfaces said **nineteen**, or twelve, or
seventeen, or ten:

| Surface | What it said | Why it was wrong |
|---|---|---|
| `agents_status.json` note + 2 news items | "Your Agent Library is NINETEEN agents" | hand-typed |
| `somba_theme.AGENTS` | a hand-typed roster of **12** | fed every member's dashboard grid — ten shipped agents were invisible on ~100 dashboards |
| `build_agents.py` | `Agent {n} of 10` | live pages literally read **"Agent 21 of 10"** on 21 pages |
| `_publish/build_delivery_summary_page.py` | "all seventeen agents" ×3 | written when it was seventeen |
| `docs/agents/README.md` | "The team (17 agents)" | mechanism derived, output never regenerated |

Nothing failed. Nothing could. **A hand-maintained number has no way to know it is wrong**, and the
job that was supposed to announce the changes — `patch_news.py` — carried a hand-typed news list and a
hard-coded `TODAY_H = "20 Jul 2026"`. It was not a script; it was a document that had to be edited by
hand before every run. It had sat unedited for two weeks while the thing it describes was rebuilt
daily.

**The rule: the pipeline that MAINTAINS an artifact and the copy that DESCRIBES it decay at different
rates, and only one of them has a test.** We had built real machinery around the artifact — hash
manifests, coverage gates that hard-fail when `skills/` and `ORDER` disagree, three daily verifiers,
a link-graph checker. Zero of it looked at the sentences. So the pack could not go stale and the story
about the pack could not stay fresh, and the daily report was green throughout.

Everything now derives from `agents_manifest.json`: the roster, the counts, the "Agent N of M", the
prose in the delivery page, and the news items themselves — which are produced by diffing today's pack
zip against the dated backup from seven days ago and resolving each changed skill's own
`<!-- learning:ID -->` markers to their note titles. The generator has no list to edit.

### Corollary — a guard that compares a thing to itself cannot see consistent error

`dash_weekly.py` already had a guard for exactly this: it asserted that no two visible news items
claimed different Agent-Library counts. It passed, twice over. First because it matched **one
phrasing** — "Agent Library is N agents" — and the worst offender read "arranges all nineteen into six
departments." Second, and more importantly, because **all three stale claims agreed with each other.**
A set of items that are consistently wrong is precisely what self-comparison is blind to. The guard now
compares the message against `agents_manifest.json` — the artifact — and fails on any count that is not
today's, in any phrasing, spelled or numeric.

Same shape as the 2026-08-01 mirror finding (a weekly check of a daily source comparing the source to
its own snapshot rather than to the clock). **Guards must terminate at something outside the system
they are guarding.**

### Corollary — a checker that fires on correct behaviour is worse than no checker

The verifier written for this run failed three times before it was right, and all three were the
checker's fault, not the surfaces':

1. It looked for `<script id="vault">`; the real payload is `<template id="smb-vault">`.
2. It flagged the niche "Coaching" as a member-data leak. It is Sigrun's own nav — "My Coaching
   Philosophy" — on every page of the site. Fixed by subtracting terms that also appear on a public
   control page, so the check discriminates member data from site chrome.
3. It asserted "the agent library links 22 agents" against an anonymous fetch of a **password-gated**
   page, and then against the outer HTML of a page that ships its whole body inside a base64
   `data:text/html` iframe. Both times it read 0 of 22 and reported failure about a healthy page.

Three red lines on a green system. Ship that and the next person learns to skim past red. **Before
believing a failure, reproduce the thing the checker claims to have read** — and when a surface is
gated or encoded, the check has to unlock and decode it, or it is asserting against a login form.

### Corollary — verify the whole sequence, not the step you touched

Rebuilding the bundle made the published zip stale by two bytes. Republishing it made the
`/skill-packs/` directory stale, because that directory is written by two *further* scripts
(`update_index_packs.py`, `build_skillpacks_index.py --publish`) that run after the republisher. Only
`verify_directory_and_somba.py` caught it. **When you re-run one stage of a pipeline by hand, you have
re-run one stage of a pipeline by hand** — the stages downstream of it are now describing the state you
just replaced.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
