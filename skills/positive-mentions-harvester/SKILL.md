---
name: positive-mentions-harvester
description: Find, verify, and score every good thing the market already says about you — podcasts, testimonials, press, speaking, client results, reviews, unprompted shoutouts — on a 30-point authority scale, into a ranked proof library that feeds your site, Knowledge Panel, and Dollar-a-Day boosts. Run right after your positioning brief.
---

# Positive Mentions Harvester

**Use this when** you have your positioning brief and need the receipts. Most founders sit on years of proof they never collected; this skill harvests it systematically. Step 2 of the Local Service Spotlight method.

## Inputs
- Positioning brief from `personal-brand-strategist` — proof gets scored against the buy box, not your ego.
- Your profile links: LinkedIn, X, Instagram, YouTube, your site, podcast directories.
- Names of clients, podcasts, events, and people who have referenced you — spelled correctly, so search actually finds them.
- Screenshots, transcripts, testimonials, thank-you emails you already have. Paste everything; thin inputs make a thin library.

## Steps
1. **Sweep every source.** Search the web and the supplied links for podcast appearances, press quotes, speaking listings, testimonials, reviews, client results, and unprompted social shoutouts. Search your name against every client, event, and topic in the brief.
2. **Capture each mention in full:** the exact quote or claim · who said it · where, with link · date · format (video, audio, text) · why it carries weight.
3. **Score each mention on the 30-Point Authority Scale** (below). No gut calls — the rubric keeps the library honest.
4. **Rank the library, highest score first.** Flag the top 10 — these become the homepage proof wall, the Knowledge Panel corroboration, and the first Dollar-a-Day boosts.
5. **Flag every lighthouse mention.** One quote from a marquee name you're tied to outranks ten generic compliments — their authority reflects onto you.
6. **Log the silence.** Buy-box claims with zero proof go straight to `reputation-gap-analyzer` as the gap list.

## The 30-Point Authority Scale
| Dimension | Points | What earns them |
|---|---|---|
| Source authority | 0–10 | Who said it and who listens to them — a lighthouse name or national outlet maxes this |
| Specificity | 0–10 | Numbers, names, outcomes ("took us past 300 customers") beat adjectives ("great guy") |
| Buy-box relevance | 0–10 | Whether the mention sells the exact deals you want next |

- **24–30:** lead with it — homepage, pinned posts, first boosts.
- **15–23:** supporting proof — topic pages, follow-up sequences.
- **Under 15:** archive it. Weak proof dilutes strong proof.

## Output
- Scored proof table: quote, source, link, date, format, why it carries weight, 30-point score.
- Top-10 shortlist, ranked — raw material for the entity home, the Knowledge Panel, and Dollar-a-Day.
- Lighthouse list: the marquee names already on record about you.
- Gap list: buy-box claims with no proof yet, handed to `reputation-gap-analyzer`.

## Worked examples
- **Dennis's public tracker:** 236+ podcast appearances logged in one place at dennisyu.com/podcast-appearances — proof compounds when you track it; it rots when you scatter it across old links.
- **Cam Hazzard:** harvested testimonials became the wall on camhazzard.com. The proof existed for years; collecting it was the work.
- **Marko Sipila — HVAC Quote:** phone-shot conference interviews became a proof library, repurposed and boosted at $1/day, on the way to 300+ customers.

## For DealCon — agency owners & acquirers
**If you run an agency:** every harvested mention is a closing asset — the prospect who Googles you finds third parties vouching instead of you selling. A documented proof library also transfers in a sale; reputation that lives only in your head doesn't.
**If you buy & sell companies:** every mention is a relationship thread — the podcast host, the quoted client, the event organizer are warm paths to off-market deals. Harvest the proof AND the people.
**Your edge:** the mentions scoring highest on buy-box relevance reveal what the market already believes only about you — amplify that, not the generic praise.

## Run on a persistent agent (Fable 5)
- **Loop to done:** keep sweeping until new searches stop surfacing mentions — every client, event, and topic in the brief, not the first page of results. A 90% harvest produces a gap list you can't trust.
- **Self-verify:** no mention enters the library without quote, source, link, date, format, and its 30-point score — rubric only, no gut calls.
- **Compound with memory:** read the brief from `personal-brand-strategist` and the existing proof library first; append and re-score the deltas instead of rebuilding, so the monthly rerun takes minutes.
- **Log the run:** record what each sweep found and missed — that meta-article sharpens next month's search list.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- The more material you paste in, the better this gets. Boil the ocean: every podcast, every event, every thank-you email.
- Score against the buy box, not your ego — a flattering mention that attracts the wrong deal scores low.
- Lighthouse mentions are the priority output: they become the pieces you boost first with Dollar-a-Day.
- Run this monthly. New proof appears constantly; re-score so the library stays current, like the public tracker does.

## Definitive article & pairings
- Reference: Authority tracker — https://dennisyu.com/podcast-appearances/ ; Knowledge Panel corroboration — https://blitzmetrics.com/knowledge-panel/
- Pairs with: personal-brand-strategist → **this skill** → reputation-gap-analyzer

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

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
