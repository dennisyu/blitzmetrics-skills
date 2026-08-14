---
name: grokipedia-authority
description: Win a Grokipedia page for a person, company, podcast, or book — and keep it accurate. Scores whether Grok can already write and SOURCE a page (readiness), hardens the citable proof, submits through the Suggest-Article flow in a disciplined drip, then monitors and corrects. Runs as a STANDALONE MONTHLY agent because notability accrues on a monthly rhythm, not a weekly one. Step 6b of the Local Service Spotlight method — the AI-encyclopedia sibling of ai-search-visibility.
---

# Grokipedia Authority

**Use this when** you want your people, clients, companies, podcasts, and books to have a Grokipedia page — xAI's AI-generated encyclopedia — and you want it done at scale, honestly, without getting flagged for spam.

Grokipedia is not Wikipedia. You don't write the page; **Grok does**, by scraping the open web. It builds a page when it can (a) pin down *one* clearly-identified entity and (b) back every claim with independent, citable sources that clear a lenient-but-real notability bar. That means a Grokipedia page is the **external validation of your entity-home work**: you graduate to a page when your online legibility finally catches up to your earned credibility. This skill decides who's ready, makes the ones who aren't ready ready, and submits the ones who are.

## Why this is a STANDALONE MONTHLY agent (not part of the weekly fleet audit)
Read this before you wire the schedule — the cadence is a deliberate design choice, and the same reasoning is printed on every skill-pack landing page so clients understand it too.

- **Notability moves monthly, not weekly.** The inputs that flip a "not yet" into a "ready" — a new press hit, a published book with an ISBN, an award, a podcast season, a Wikidata item — land on a monthly-or-slower rhythm. Re-scoring weekly burns tokens and Grok's patience to watch a needle that hasn't moved.
- **Submission must be rationed.** Grok penalizes duplicate and thin submissions. A monthly capped drip (top ~3 newly-ready entities per run) keeps the account clean; a weekly firehose gets it flagged. Discipline is the product.
- **It's a different job from the weekly audit.** The weekly fleet audit is *maintenance* (health, SEO, RankMath, interlinking). Grokipedia is *promotion of an entity to an encyclopedia* — a distinct pipeline with its own registry, its own drip cap, and its own human-gated write (a submission on your X/Grok identity). Bolting it onto the weekly job would blur two jobs and make both harder to reason about.
- **It mirrors what already works.** Our weekly-fleet-wikidata-audit already proved the pattern for the *harder* bar (Wikidata): read a registry, drip-create 1–2/run with independent references, never mass-create. Grokipedia is the lower-bar cousin, so it gets the same discipline on a monthly clock.

One agent, one clock, one registry, one drip cap. That is why it stands alone.

## What agent kicks this off, and what skills it's tied to
The **Grokipedia Authority agent** kicks off **monthly** (1st of the month). It doesn't work in isolation — it stands on the skills before it in the method and feeds the one beside it:

- **personal-brand-website-agent** → the entity home. Grok's #1 citable source is a live site at your name with Person schema. No entity home, no page. This skill *requires* that one.
- **knowledge-panel-entity-seo** → the schema + entity disambiguation. The same Person/Organization JSON-LD that earns a Google Knowledge Panel is what lets Grok pin the right entity and dodge namesakes.
- **positive-mentions-harvester** → the proof. Third-party mentions, press, podcast spots and awards are the independent sources Grok verifies against.
- **definitive-article-writer** → citable facts. When Grok gets a date or a claim wrong, the fix is to publish the correct fact somewhere Grok can read it (usually the entity home), then submit an edit.
- **ai-search-visibility** → the sibling. That skill makes ChatGPT/Perplexity/Google-AI describe you correctly; this one does the same job for the AI encyclopedia. Run them together.

## Inputs
- A roster with, per entity: name (proper diacritics), niche, country, entity-home URL, socials, and any independent proof (press, books w/ ISBN, awards, academic records, notable roles).
- The readiness inputs you already have from the audit: entity-home liveness + domain type, Ahrefs DR, proof band, and a notability/namesake triage (who shares your name in the knowledge graph).
- A logged-in grokipedia.com (X/Grok) session for submissions, and dashboard/publish credentials for reporting.

## The rules — non-negotiable
- **Never mass-submit; respect the rate limit.** Grokipedia's Suggest-Article is rate-limited to ~1 request per 600 seconds (10 min) after a small burst — bursting returns "Rate limit exceeded: max 1 requests per 600 seconds." Submit ONE at a time, spaced ≥11 min (the `grokipedia-drip` scheduled task paces this automatically), a few of the strongest per cycle. A thin or duplicate submission costs you more than a slow rollout.
- **Disambiguate or don't submit.** If a different, established person owns the name in the knowledge graph and you have no strong anchor (name-domain + niche + location), build the anchor first. A merged/confused page is worse than no page.
- **One citable fact per claim.** Grok verifies against the open web. If it isn't published somewhere Grok can read, it isn't a fact yet — publish it on the entity home first (this is the definitive-article-writer handoff).
- **Person ≠ company ≠ podcast ≠ book.** Submit them as separate, interlinked entities. Grok rejects a company page that looks like a duplicate of its founder.
- **Honesty over coverage.** A "ready" call must be defensible. Better to hold a member at "nearly" for a month than to submit and get rejected.

## Steps (the monthly pipeline)
1. **Score readiness.** For every entity compute a 0–100 Grokipedia Readiness Score: identity/20 (can Grok pin one entity?) + entity_home/30 (live, schema'd, citable) + corroboration/30 (independent sources) + authority/20 (DR + active social). Route each to a status: **live** (page exists → monitor), **ready** (submit now), **nearly** (one fixable gap), **build** (entity home/proof first), **hold** (namesake/identity unresolved).
2. **Detect existing pages.** Check grokipedia.com/page/&lt;Name&gt; (diacritic-sensitive — check the proper spelling AND an ASCII-folded fallback). A real page returns HTTP 200 with og:title "Name — Grokipedia"; a missing one returns 404 "Article Not Found." Anyone already LIVE skips submission and goes to monitor.
3. **Harden sources** for the "nearly" band: publish the missing facts on the entity home, point pending nameservers so the home goes live, and surface 1–2 independent proofs. This is where most of the value is — it improves the Knowledge Panel and AI-search at the same time.
4. **Submit the drip** (top ~3 ready, by score): on grokipedia.com, use Suggest Article. Paste the one-line notability rationale, the entity type, and the source list from the entity's submission package. Submit the person first; once it lands, create each ecosystem entity (company/podcast/book) and interlink.
5. **Monitor & correct** the LIVE pages: read the page, list factual errors, and submit edit-suggestions — each backed by a citable URL (usually the entity home). Small errors compound; fix them.
6. **Report.** Write each entity's status (score, action, page URL) to its dashboard and to the registry, append a dated changelog line, and draft the summary email. Never publish silently.

## Output
- A per-entity registry (status · score · action · page URL · ecosystem) + a ranked human-readable report.
- A ready-to-paste Suggest-Article package for every "ready"/"nearly" entity.
- Submitted drip (≤3), monitored corrections, and updated dashboards — with a human-steps list for anything gated (a login, a nameserver, a source that has to be created).

## For DealCon — agency owners & acquirers
Grokipedia pages are a productized authority add-on with near-zero delivery cost: the readiness engine and submission packages are automated, and the same source-hardening that wins the page also lifts the client's Knowledge Panel and AI-search answers. Sell it as "own your name in the AI encyclopedia," priced as a quarterly authority retainer. The monthly cadence *is* the deliverable cadence — one clean report a month showing who graduated.

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-08-01-a-resolved-flag-must-be-retired-at-the-source -->
**August 1, 2026** (from: grokipedia-readiness)

**August 1, 2026** (from: grokipedia-readiness)

When research clears a warning, retire the warning where it lives. A resolution written somewhere
else is a second opinion, and the code keeps reading the first one.

On June 30 the Wikidata triage filed Claudia Witticke as a namesake trap: `Q133434182` looked like
a near-empty "seamstress" stub that could not be confirmed as hers. On July 27 a rotation check
disproved it — following the item's `GND 1268215171` to the DNB record gives *Witticke, Claudia /
Land Italien / Beruf Näherin / Gründerin von "Leidenschaft Nähen"*, and "Leidenschaft Nähen" is
the exact brand on her own domain. The rotation wrote that up correctly and promoted her to
tier A. It did not delete the trap entry.

So for five weeks the same file asserted both things at once, and the engine believed the older
one. The cost was not cosmetic:

- identity scored 14/20 instead of 20/20, dropping her from **92.4 to 86.4**
- she carried a `namesake-collision` flag, which under the standing *disambiguate or don't* rule
  meant the monthly drip would skip her — indefinitely, and for a reason that had already been
  disproved

A stale warning is worse than a missing one, because it is load-bearing. Nobody re-examines a
member the file says is unsafe to touch.

Two fixes, and the second is the one that generalises:

1. Retire the entry at the source. Move it to a `namesake_resolved` key with the evidence and the
   date, so the history survives without the live list lying.
2. Make the contradiction self-detecting. A trap says "the only match for this name is someone
   else"; a tier-A entry says "this member has an item". If both name the **same qid**, they cannot
   both be true. The engine now resolves that in favour of the newer evidence, prints
   `[STALE-TRAP]`, and a unit test fails until the underlying file is cleaned.

The general rule: when two records in one system disagree about the same identifier, that is a
detectable condition, not a judgement call. Write the check. Silent contradictions get obeyed by
whichever code path happens to read first, and the loudest possible failure is cheaper than a
member who quietly never ships.

A corollary found in the same file: the rotation note also recorded that the roster's niche and
country for her were wrong ("Style / image coaching, AT" for a sewing author in South Tyrol,
Italy). That was flagged and not actioned either — and it would have shipped a false claim about a
real person into an encyclopedia. **A note that says "X is wrong and should be corrected" is not a
correction.** Either fix it in the same run or file it where something will fail until it is fixed.

<!-- learning:2026-08-01-confirmation-screen-is-not-confirmation -->
**August 1, 2026** (from: grokipedia-readiness)

**August 1, 2026** (from: grokipedia-readiness)

A confirmation screen is a rendering decision. It is not evidence that the write happened.
When a submission matters, read the response the server actually sent.

Grokipedia's Suggest-Article modal has two failure modes that look identical on screen:

| What happened | What the screen showed |
|---|---|
| Rate-limited, nothing created | modal clears, empty form, no error |
| Submitted successfully | modal clears, empty form, no error |
| Submitted successfully | "Thank you!" screen |

The July 4 run recorded that exceeding the rate limit returns a visible
`Rate limit exceeded: max 1 requests per 600 seconds`. On August 1 it returned nothing at all —
the form just reset. So the note that was written to prevent a misdiagnosis became the cause of
one: the first Witticke attempt looked exactly like the successful Nichterl attempt that preceded
it, except Nichterl had shown the Thank-you screen and Witticke had not.

Guessing in either direction is expensive. Assume failure and you re-submit, and duplicates are
the one thing this job must not produce — the July run already left two identical
`Annelie Salminen (writer)` rows in the activity log. Assume success and the member silently never
gets submitted at all, and nobody notices until the next monthly run.

The resolution is to stop reading the UI. Wrap `window.fetch` before clicking Submit and capture
the POST body:

```js
if (!window.__hooked) {
  window.__cap = []; const of = window.fetch;
  window.fetch = async function (...a) {
    const r = await of.apply(this, a);
    if ((a[1] && a[1].method) === 'POST') {
      const c = r.clone(); window.__cap.push({ s: r.status, b: (await c.text()).slice(0, 300) });
    }
    return r;
  };
  window.__hooked = 1;
}
```

`{"success":true,"id":"<uuid>"}` is the fact. Everything else is decoration. Attempts 1 and 2
produced no POST at all; attempt 3 returned success and the Article Requests counter moved
106 → 107 with exactly one new row.

Two general rules fall out of this:

1. **Verify a write at the layer that performed it**, not the layer that reports it. This is the
   same shape as the Elementor lesson (a 200 on the REST write is not a live render) and the
   scheduled-task lesson (a draft is not staged until a re-fetch confirms it).
2. **A documented gotcha has a shelf life.** It describes a third-party system on the day it was
   written. When a run's behaviour contradicts the note, the note is the thing to re-check first —
   and then to correct in place, so the next run inherits the truth rather than the fossil.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
