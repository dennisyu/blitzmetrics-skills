---
name: reputation-gap-analyzer
description: Compare the reputation you HAVE (scored proof) against the reputation you NEED for your buy box, then run Metrics → Analysis → Action to ship a dated 30-day plan of content, proof, and boosts that closes the gap. Run after harvesting proof.
---

# Reputation Gap Analyzer

**Use this when** you hold the positioning brief and the scored proof library and need to know exactly what to fix first. Step 3 of the Local Service Spotlight method — MAA (Metrics → Analysis → Action) applied to your own name.

## Inputs
- Positioning brief from `personal-brand-strategist` — buy box, passion, differentiation.
- Scored proof library from `positive-mentions-harvester` — including the lighthouse list and gap list.
- Your next 30 days: real availability, events you'll attend, interviews you can book. The plan has to survive your calendar.
- Optional: 2–3 peers who currently win the deals you want — their public reputation is the benchmark you're closing against.

## Steps
1. **Metrics — score what you have.** Map every scored mention against each buy-box claim. Some claims will have stacked proof; others will be silent. The silence is the finding.
2. **Metrics — define what you need.** For the deals you want, write the 3–5 things the other side must believe before they call. That's the reputation requirement — not a vanity wish list.
3. **Analysis — diagnose each gap.** Every gap has one of three causes: you never said it publicly, you said it but never captured proof, or the proof exists but is buried and unfindable. Each cause has a different fix.
4. **Pick 3 gaps and 3 strengths.** Three claims that need proof, three strengths already working that you're under-leveraging. More than that and nothing ships in 30 days.
5. **Action — build the dated 30-day plan.** Repurpose before you create: one lighthouse interview, cut into clips, closes most gaps faster than net-new writing. Every action gets a date, an asset, and a destination — site page, post, or boost.
6. **Schedule the re-measure.** Day 30: rerun the harvester, re-score, compare. MAA is a loop, not a report.

## Output
- Gap map: each buy-box claim with proof you have vs. proof you need.
- 3 gaps with their diagnosed cause; 3 strengths to amplify.
- Dated 30-day plan: action, asset, destination — content + proof + boosts, no filler.
- Handoff notes: which actions feed `personal-brand-website-agent`, which feed `dollar-a-day-strategist`.

## The 30-day plan shape
- **Days 1–7 — plumbing + capture:** confirm tracking is in place; record the lighthouse interviews that hit the biggest gap; ask directly for the missing testimonials.
- **Days 8–14 — publish:** cut interviews into clips, post natively everywhere, put the strongest new proof on your entity home.
- **Days 15–21 — promote:** Dollar-a-Day on the proven pieces — $1/day × 7 per clip, kill the bottom 90%.
- **Days 22–30 — perform:** read the metrics, put $30/30 days behind winners, book the next round of interviews.

## Worked examples
- **Marko Sipila — HVAC Quote:** gap = HVAC owners had never heard of him; cause = no proof in their world; action = phone-shot conference interviews, repurposed, $1/day. Result: 300+ customers.
- **Harry Gold — Overdrive Interactive:** the gap wasn't proof — decades of it existed — it was findability. One Zoom interview became harryjgold.com.
- **George Paladichuk — NaiL AI:** wanted to own AI in roofing before anyone else claimed it; the analysis said move now; the podcast made him the reference point.
- **Dennis's loop:** 236+ tracked podcast appearances didn't happen by accident — each MAA cycle booked the next round.

## For DealCon — agency owners & acquirers
**If you run an agency:** the gap between how you're known and the clients you want is why you're stuck in referral roulette — close it and the right clients arrive pre-sold at premium prices, and the documented reputation makes the agency itself more sellable.
**If you buy & sell companies:** sellers and LPs diligence you before the first call — every gap they find is friction on terms; every gap you close first is leverage. Post-close, run this on the acquired company: amplifying proof that already exists is the cheapest EBITDA lift available.
**Your edge:** the analysis names the ONE claim that, proven publicly in 30 days, moves your specific pipeline — do that one first, not the easy ones.

## Run on a persistent agent (Fable 5)
- **Loop to done:** not finished until every buy-box claim is mapped and every plan item carries a date, an asset, and a destination — "build awareness" gets rejected by your own QA pass, not by Dennis.
- **Self-verify:** check the 30-day plan against the stated calendar before delivering; a plan that ignores real availability fails its own definition.
- **Compound with memory:** pull the brief and scored library from the upstream skills; on day 30, diff against the prior gap map instead of re-deriving it — MAA is a loop, and memory is what makes it one.
- **Log the run:** each cycle's gap-map delta is the meta-article — dated proof the reputation is actually moving.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- MAA is the engine: metrics say what's missing, analysis says why, action closes it. Skip analysis and you'll make content nobody needed.
- Amplify what's working before you fix what isn't — winners hand off straight to `dollar-a-day-strategist`.
- Gaps close fastest by interviewing your lighthouse and repurposing the result (the `content-factory` pattern), not by writing from scratch.
- "Build awareness" is not an action. A date, an asset, a destination — or it doesn't go on the plan.

## Definitive article & pairings
- Reference: Content Factory (MAA engine) — https://blitzmetrics.com/content-factory/ ; Boil the Ocean — https://blitzmetrics.com/always-boil-the-ocean-because-good-enough-is-not-enough/
- Pairs with: positive-mentions-harvester → **this skill** → personal-brand-website-agent

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-19-sitemap-bio-count-not-guest-count -->
**July 19, 2026** (from: michaelkrigsman.com QA run (filed into the loop by skill-pack-propagation 2026-07-19))

A /bio/ sitemap count is not a guest count. The Krigsman parse (569) swept in the host's
own bio, a staff bio, a brand page, and a dummy test page, inflating the real figure.
On any client-facing surface, publish "more than N" FLOORS, never a raw sitemap count —
raw counts include non-guest URLs and will overstate. Before quoting a count, subtract
host/staff/brand/test pages, then round DOWN to a defensible floor.

<!-- learning:2026-07-27-audit-for-the-absence-and-report-counts -->
**July 27, 2026** (from: cxotalk-weekly-maa run)

### Answer a client's site complaint by auditing for the ABSENCE, and report what you found missing

The client asked us to "make sure the Person schema lists my job title as Industry Analyst,"
after twice complaining that he is labeled a journalist.

The lazy answer is to set the field and reply "done." The useful answer came from checking
whether the complaint was even about our surface: the homepage schema **already** said
`"jobTitle": "Industry Analyst"`, and the string "Journalist" appeared **zero times**
anywhere on the site — copy or markup, every page. The label he was seeing was Google's own
Knowledge Panel title, which his support request already targets. Telling him "our site
isn't the source of that" was worth more than any edit.

Same pass, same technique, on a second standing request (remove a co-founder he'd fallen
out with): 0 occurrences site-wide, so that commitment was already satisfied on the
website — and it surfaced that the *actual* remaining surface is the Wikidata item, which
nobody had touched.

**Rule:** when a client reports a wrong fact about their brand, grep every owned surface for
the offending string *and* the desired string before changing anything. Report the counts.
"It appears 0 times on your site, here's where it actually comes from" is a better
deliverable than a silent fix, and it usually relocates the work to the surface that's
really broken.

**Corollary found the same way:** a `@graph` whose `Person` node is a bare `@id` reference
to another page is a *valid, standard* pattern (Yoast and RankMath both do it) — do NOT
report it as a bug. Report it accurately: Google doesn't reliably dereference cross-document
`@id`s, so the ProfilePage ranking for the person's name never states the job title in its
own markup. Recommend inlining `name` + `jobTitle` + `sameAs`. The credibility cost of
calling a normal pattern "broken" is higher than the fix is worth.
Learned July 27, 2026.

<!-- learning:2026-07-29-audit-the-name-in-every-language-they-live-in -->
**July 29, 2026** (from: jagodapasko.com second pass, July 29, 2026)

On **July 29, 2026** a client's audit from six weeks earlier recorded **2 proof items, 24
authority points, 0 power proof**, and described her third-party footprint as very thin. A
single afternoon of searching found national television coverage on two networks, a
broadcast documentary segment, three long-form interviews on three independent channels,
and a verified fundraiser documenting 210+ evacuations. None of it was hidden. All of it
was in **Polish**, and most of it lived on other people's channels rather than her own.

**A proof library built from English-language search of a non-English person is a
measurement artefact, not a finding.** So before scoring anyone's authority:

1. Search the name in **every language the person has lived and worked in**, including with
   and without diacritics, and search their brand or company name separately.
2. Search for the *events* as well as the person — the coverage may name the work rather
   than the individual, and their own outbound links (a fundraiser page, a media page, a
   LinkedIn post) often point straight at press that no name-search returns.
3. Treat "third-party footprint is thin" as a **hypothesis that must survive a
   native-language search**, never as a conclusion from an English result set. Say which
   languages were searched, so the next run can see the gap instead of inheriting it.
4. Verify every video with oEmbed before publishing it — it returns the exact title, the
   real channel, and whether the thing is still public. Titles get paraphrased from memory
   otherwise, and paraphrasing someone else's video title onto a client's press page is how
   a credibility asset turns into an error.

**Reject search summaries that conflict with primary sources.** One auto-generated summary
in this run asserted the client had been "a TV director turned brain-injury recovery
mentor." It was a different person with a similar name, and it contradicted a verified
twenty-year finance career. A name collision inside a research tool will happily produce
fluent, specific, false biography — check every claim against a source that names the
person unambiguously before it reaches a published page.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
