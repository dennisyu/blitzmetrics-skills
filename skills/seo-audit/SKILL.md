---
name: seo-audit
description: Run a full technical + content + authority SEO audit on any site and score it out of 100 on the seven-component BlitzMetrics SEO & Growth rubric, with every finding tied to a URL a stranger can open. Use when a client asks "how is my SEO", when a site is about to be rebuilt, when a monthly re-audit is due, or before promising anyone a ranking outcome. Produces a dated score, a delta against the last run, and a fix list ordered by cost-to-fix — not a list of everything that is wrong.
author: Dennis Yu — BlitzMetrics / Local Service Spotlight
references:
  - https://blitzmetrics.com/quickaudit/
  - https://blitzmetrics.com/website-qa-audit/
  - https://blitzmetrics.com/seo-tree/
  - https://dennisyu.com/seo-audits/
  - DealCon-Skills/weekly-brand-maa.md
  - DealCon-Skills/evidence-verification.md
  - DealCon-Skills/client-access-checklist.md
---

# SEO Audit

**Use this when** you need to say something true and defensible about a site's search
performance — to a client, in a pitch, in a monthly tracker, or to yourself before you
promise anyone a result.

An SEO audit is not a crawl dump. A crawl tool produces 400 issues sorted by its own
severity guess; that is a data export, not an audit. An audit is a **judgement**: this is
where the site stands, this is what is costing the most, this is the order to fix it, and
here is the number so next month can be compared to this month.

## The one idea

**Every finding names a URL, and every score component moves for a reason you can point at.**

A score with no evidence under it is a vibe with a number attached. If you say Technical is
55, you must be able to open the four things that made it 55. This is what makes the monthly
re-audit possible at all: next month you are not re-forming an opinion, you are checking
whether those four specific things changed.

---

## The rubric — seven components, 100 points

These weights are the standing BlitzMetrics SEO & Growth score. They live **here** and
nowhere else. Any job that needs them reads this file. (Until 2026-08-02 they existed only
inside one scheduled task's parameter block, which meant no other audit could be compared to
it and nobody could find the definition — the exact failure this file exists to end.)

| # | Component | Weight | What it measures |
|---|---|---|---|
| 1 | **Technical** | 18% | Indexability, crawl access, sitemaps, robots.txt, status codes, redirects, HTTPS, Core Web Vitals, mobile rendering |
| 2 | **On-Page & Schema** | 16% | Titles, H1s, meta descriptions, internal linking, JSON-LD structured data, canonicals |
| 3 | **Content & Keywords** | 18% | Coverage of the money terms, depth on category/service pages, cannibalisation, thin pages |
| 4 | **Authority** | 14% | Referring domains, link quality and growth, brand mentions, Domain Rating trend |
| 5 | **Local** | 12% | Google Business Profile completeness, NAP consistency, local pack presence, reviews, location pages |
| 6 | **AI Search Readiness** | 12% | Whether AI crawlers are allowed, entity clarity, schema an LLM can parse, citability, Knowledge Panel/Wikidata presence |
| 7 | **Conversion** | 10% | Does the traffic have somewhere to go — offer clarity, forms, calls, tracking that proves it |

Score each component 0–100 on its own, then weight. Report the weighted total **and the
seven raw components**, because the total hides which lever to pull.

**Never report a component you did not check.** Score it `UNKNOWN` and say what access you
need. A component scored 0 because nobody looked reads identically to a component scored 0
because the site is broken — see `evidence-verification.md`, Part 4.

### AI Search Readiness is the one people skip
It is the component most sites fail worst and know least about. Start with `robots.txt`:
count how many AI and image crawlers are blocked (`GPTBot`, `OAI-SearchBot`, `ClaudeBot`,
`PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `GoogleOther-Image`,
`facebookexternalhit`). One real client was blocking **40+** of them while paying for content
marketing — invisible to every AI assistant their buyers were asking, and nobody had opened
the file.

---

## How to run it

1. **Get access first, or say plainly that you did not have it.** Search Console before
   anything else — see `client-access-checklist.md`. An audit without GSC is an outside-in
   audit and must be labelled as one. It is still worth doing; it is not worth pretending.
2. **Crawl what a stranger gets.** Anonymous, cache-busted, no cookies. Then crawl again as
   Googlebot. If those two differ, stop the audit and open a security incident — see
   *Cloaking*, below.
3. **Pull the numbers.** Domain Rating, organic traffic and value, keyword counts by
   position band, top pages, referring domains, and the same set for 3–6 competitors. The
   competitor set is what turns "2,094 visits/mo" into "2,094 against a peer at 24,833."
4. **Score the seven components**, each against its own evidence list.
5. **Delta it.** Against last month, and against the original baseline. Arrows, not prose.
6. **Order the fix list by cost-to-fix, not by severity.** A 5-minute robots.txt edit that
   unblocks every AI crawler outranks a 6-week content programme, even if the content
   programme is "more important."
7. **Write the one-page visual report.** Score then vs now, the traffic table, what shipped,
   what is still open, top three next actions. One page. The 40-page audit is read by nobody.

---

## Traps that have actually bitten us

Each of these produced a wrong finding in a real client audit before it became a rule.

### Decode XML entities before fetching sitemap children
A sitemap index returned 200 and listed five child sitemaps; all five fetched as **404, zero
bytes**. The obvious read was that the client's sitemap fix was cosmetic. The child URLs
contained `&amp;` — fetching the raw, un-decoded string requested a URL that does not exist.
The sitemaps were fine. **Decode entities before you request the URL**, and treat "all N
children failed identically" as a smell about your fetcher, not the site.

### A parameter that names a missing data source has an expiry date
An audit's parameters said `gsc_property: not configured`. The run believed it and wrote
"No Google Search Console property is configured" into a client-facing report as a finding
with an owner — while a teammate had been posting GSC data weekly in the client's own
Basecamp thread. **Check the client's channel before you report a data source as missing.**
Configuration facts go stale between the day a task is written and the day it runs.

### An empty result from a cross-origin fetch is not an empty result
Five in-page `fetch` calls to a search endpoint returned zero results and the conclusion was
"no history exists." They had failed silently on same-origin policy. **A search that returns
nothing and a search that never ran look identical.** Prove the fetch can succeed at all —
run a control query you know has hits — before you report an absence.

### A client-rendered shell is not a thin page
A plain HTTP fetch of a JS-rendered site returns a near-empty body. Score that as "no
content" and you have audited your own fetcher. If the static fetch returns a shell, render
it in a browser before scoring On-Page or Content.

### Cloaking: check what Googlebot sees, every time
On 2026-07-27, three sites on one host returned **HTTP 500 to every human and HTTP 200 with a
spam storefront to Googlebot**, plus a fake 1,733-URL sitemap regenerated per request. From
the human side the sites looked merely broken. This check costs one extra request and is the
difference between "site is down" and "site is compromised and feeding spam to Google."
Divergence between the human render and the bot render is a **security finding**, not an SEO
finding — hand it to `security-audit.md` and do not publish anything to that site.

---

## What you deliver

- A dated one-page report: weighted score, seven components, delta arrows vs last run.
- A findings table where **every row has a URL** and a cost-to-fix estimate.
- A "what shipped since last time" section — this is what makes the client believe the next one.
- An explicit list of what you could not check and what access would fix that.

## Definition of done
- Every score component traces to evidence a stranger can open.
- Anything unchecked says `UNKNOWN`, never 0.
- The human render and the bot render were compared.
- The fix list is ordered by cost-to-fix and the top item is doable this week.
- The report is one page, and the numbers on it can be recomputed next month the same way.

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-08-01-decode-xml-entities-before-fetching-sitemap-children -->
**August 1, 2026** (from: wtp-monthly-seo-reaudit run (Western Trading Post, first tracked run))

### Decode XML entities before fetching sitemap child URLs — or you will report a healthy sitemap as dead

Checking whether a client's `/sitemap.xml` fix had shipped, the index at `/xmlsitemap.php`
returned 200 and listed five child sitemaps. Fetching each child returned **404 with zero
bytes, all five**. The obvious read was that the sitemap fix was cosmetic — index alive,
every child dead, zero URLs discoverable by Google. That was about to be the report's
headline finding, and it was completely wrong.

`<loc>` values are XML-escaped. The real URL is `?type=pages&page=1`; the sitemap contains
`?type=pages&amp;page=1`. Fetching the raw captured string sends a literal `&amp;`, the
parameters break, and the server 404s. Decoding entities first, all five children return
**200 with 4,516 URLs**.

**Rules:**

1. **Always entity-decode `<loc>` values before fetching them** — `&amp; &lt; &gt; &quot; &apos;`.
   This bites hardest on sitemaps with query-string pagination, which is the norm on
   BigCommerce, Shopify and most hosted carts.
2. **A 100% failure rate across every child is a smell, not a finding.** Real breakage is
   usually partial. When every single item in a set fails identically, suspect the harness
   before the target — the same instinct that `max_crawl_pages` taught on the SERP side.
3. **Never report an infrastructure catastrophe from a single method.** Confirm with a second
   path (browser navigation to one child URL, or Search Console's sitemap report) before
   telling a client their sitemap is dead. The credibility cost of a false alarm this size is
   far higher than the minute it takes to check.

Same run, same discipline, two more times: a robots.txt parser that reported "zero crawlers
blocked" was **prove-red tested against a synthetic blocking file first** (it correctly caught
2/2) before its zero on the live file was trusted, and cross-checked against a raw count of
bare `Disallow: /` lines. And a **+46% referring-domain jump** — exactly the shape of a
mode/measurement artifact — was confirmed as real by pulling `refdomains-history` and seeing a
steady 13-week climb before it was narrated as growth.

**General form of all three: when a check returns the answer you were hoping for, or an answer
too dramatic to be ordinary, make it prove itself before it reaches the client.**

Learned August 1, 2026.

<!-- learning:2026-08-01-read-the-channel-before-reporting-a-missing-data-source -->
**August 1, 2026** (from: wtp-monthly-seo-reaudit run (Western Trading Post) — GSC reported as "not configured" while a teammate posted GSC data weekly in the same thread)

### A task parameter that names a missing data source is a claim with an expiry date — check the client's own channel first

This monthly audit's parameters said `gsc_property: not configured — Ahrefs + direct crawl only`. The run
believed it, wrote "**No Google Search Console property is configured**" into the client-facing report as a
finding with an owner, and listed "get GSC verified" as an action.

Then the run opened the client's Basecamp thread to post — and found our own operations teammate posting
**Search Console data in that thread every single week**: ~120K impressions, 3.5% CTR, average position 8.4,
top queries with click and impression counts. The property existed. It had existed the whole time.

Two costs, and the second is worse than the first:

1. We nearly asked a client for access they had already granted — the exact move that burns an ask and makes
   the retainer look inattentive.
2. **We did the analysis without the best data we had.** Ahrefs estimates rankings; Search Console reports
   what actually happened. The GSC query table turned out to contain the single most valuable finding of the
   engagement — 4,419 monthly impressions on one dead craftsman's name, landing on a sold lot page. That
   insight was sitting in a teammate's weekly report for six weeks and the "authoritative" monthly audit
   never opened it.

**Rules:**

1. **Before reporting any data source as missing or unavailable, read the client's own channel** — the
   Basecamp thread, the shared drive, the weekly report someone else files. A per-client agent's parameters
   are a snapshot of what was true when the task was written; access changes and nobody edits the task.
2. **When you find the parameters wrong, fix the parameters, not just the report.** File it as an ask against
   *yourself* in the ledger. A correction that lives only in one month's write-up gets re-derived — and
   re-published as a false finding — next month.
3. **Sibling reporting is a data source, not just context.** The existing 2026-07-20 learning already says
   "check sibling scheduled tasks' outputs before declaring a metric blocked." Extend it: check what *humans*
   on the account are already reporting, in the channel you are about to post into. Read the channel before
   you write to it.
4. Corollary on credit: when you use a teammate's numbers, say whose they are. The client should see one team,
   and the teammate should see their work being built on rather than quietly re-derived.

This is the same family as the 2026-07-31 lesson that "blocked is a claim that needs evidence" — but a rung
earlier. There, a real blocker was misdiagnosed. Here, a **non-existent** blocker was inherited from a config
file and published without anyone testing it once.

Learned August 1, 2026.

<!-- learning:2026-08-02-same-origin-required-before-trusting-an-empty-search -->
**August 2, 2026** (from: WTP auction-tracking investigation — five Basecamp searches returned zero because they ran cross-origin from a client site)

### An in-page `fetch` to another origin fails silently — and an empty search result looks exactly like "no history exists"

Asked to mine years of Basecamp history for prior conversations about a client's auction platform, the run
issued five in-page `fetch` calls to Basecamp's search endpoint and got **zero results for every query**. The
obvious conclusion was that the team had never discussed it.

The tab was sitting on `auction.westerntradingpost.com`. Every one of those fetches was cross-origin and was
rejected by the browser before it left. The catch block swallowed it. Zero results was never an answer about
Basecamp; it was an answer about CORS.

Run properly, the same searches returned 11 hits, and the history contained the single most valuable fact of
the whole investigation: the client's tag stack was **already installed** on the auction platform, and a
9-month-old access request had dissolved into an unrecorded phone call.

**Rules:**

1. **Check `location.host` before trusting any in-page `fetch` result.** If you are not on the origin you are
   querying, the result is meaningless. Navigate first, then query.
2. **A search that returns zero needs a positive control before you report "nothing exists."** Run a query you
   *know* has hits through the identical code path. If the control also returns zero, the harness is broken,
   not the archive. This is the same prove-red discipline used for the robots.txt parser — extend it to every
   negative finding, because a negative finding is the easiest kind to fake.
3. **A second failure mode stacked on the first here:** even same-origin, Basecamp's search results are
   client-rendered, so `fetch` + `DOMParser` returned a shell with zero result anchors while the live page
   showed 53. When a fetch of a modern web app returns structurally empty results, read the **rendered DOM**
   after navigation instead. Two different mechanisms, one identical symptom: a confident, wrong "nothing
   found."
4. **"No prior discussion" is a claim about an archive, and archives are exactly where an agent's memory
   advantage lives.** Getting it wrong does not just lose a fact — it wastes the institutional knowledge the
   client already paid for, and re-asks colleagues questions they answered months ago.

Learned August 2, 2026.

<!-- learning:2026-08-03-a-capability-with-no-skill-file-cannot-propagate -->
**August 3, 2026** (from: SEO-audit discoverability + security-audit generalization build — 49 published SEO audits with no hub, a rubric that lived inside one task's parameters, and a jammed harvest queue that turned out to be the same problem)

### A capability with no skill file cannot propagate, cannot be taught, and cannot absorb its own lessons

Dennis asked to be "clearly known for doing SEO audits." The assumption going in was that
this was a marketing problem — write something, publish it. It was not. An inventory of our
own properties found **49 published SEO audits** already live, plus 341 audit-family URLs
across three domains. The work existed. What did not exist was any way to see it as a body
of work: **no hub page, 38 of the 49 with zero inbound links from any sibling audit, 35 with
zero outbound links.** Forty-nine deliverables, each an island.

The root cause was one level deeper than the missing page. There was **no `seo-audit` skill
file.** The seven-component SEO & Growth rubric — the thing that makes two audits
comparable — existed only inside the parameter block of a single scheduled task
(`wtp-monthly-seo-reaudit`). One job could score a site. Nothing else could, because there
was nowhere else to read the definition from.

And that had a visible symptom nobody had connected to it: **three learning notes had been
jammed in the harvest inbox since the previous day, all naming `seo-audit`**, all
unresolvable, aging toward the stale-queue gate. The morning run reported them as a queue
defect. They were not a queue defect. They were the loop correctly reporting that a skill
our own runs believed in did not exist. **A jammed learning note is a missing-capability
alarm, not a filing error.** Creating the skill cleared all three on the next run.

Same shape on the security side: seven real checks, a 116-assertion test suite, and a
track record of caught compromises — all of it existing only as one client site's
`monitor.py`. Nothing generalized to the network because there was no file to generalize
*into*.

**The rule:** when you find yourself doing something well and repeatedly, check whether it
has a canonical skill file. If it does not, that is the deliverable — before the landing
page, before the marketing. The file is what lets the capability propagate to every pack,
teach itself to the next agent, and accumulate lessons. Publishing a page about a
capability with no skill file behind it produces a claim; publishing the skill produces a
system.

**Second-order effect worth expecting:** adding two mandated skills tripped every coverage
gate that had been built in the preceding days — the SOMBA orphan check, the numbering
lists, the count derivations. All of them fired correctly and named exactly what to edit.
Ten registration points across three builders, caught by gates rather than by users. That
is what those gates are for, and a day where several fire at once is a good day, not a
messy one.

### Corollary — measure your own work before describing it

Before writing a word of the hub page, the 49 audits were fetched anonymously and measured:
status, transfer size, time to last byte, inbound and outbound sibling links, `h1`, meta
description, JSON-LD. That is our own `seo-audit` skill run against our own SEO audits, and
it produced the specific numbers the page and this note are built on — including one page
taking **9.9 seconds** to load and three returning **403 to every programmatic client**
(browser-verified fine, so: invisible to AI crawlers, visible to humans).

Running the skill on yourself first is not a nice touch. It is how you find out whether the
claim you are about to publish is true.

<!-- learning:2026-08-03-a-compromised-site-must-not-outscore-a-clean-one -->
**August 3, 2026** (from: weekly-fleet-hub-audit v2, fleet-wide proof enrichment)

### Rankings are evidence about *someone's* work — check whose before you score them

The fleet scoreboard rates every site on PROVE: Domain Rating, organic traffic, and the
breadth of keywords it ranks for. On August 3, 2026 the two sites whose keyword breadth
looked strongest were **philmershon.com (15 ranking keywords)** and
**theathletespotlight.com (5)**. Both readings were the attacker's, not the client's.

Pulling the keywords themselves rather than the count showed philmershon.com — a speaker
coach — ranking for `hollymoviehd`, `borat thong`, `nintendo store`, `jupiter 125 black
colour`, `silver aranjanam for baby boy`. Fourteen of its fifteen keywords were junk. On
theathletespotlight.com it was five of five: `activa 6g best colour`, `bici decathlon`,
`charola de unicel`. Selecting `best_position_url` alongside the keyword named the cause —
every junk term ranked on an injected path:

    /product-similar-image/?<digits>
    /product/category/<digits>
    /shop/manufacturer-site?&transition=top<digits>

with a per-site numeric suffix (`…1310` on one, `…1760` on the other): one kit, two of our
sites. Uncorrected, philmershon.com scored **impact 40**; netting the injected rankings out
drops it to **21** — an eight-point BIS swing. A compromised site was being rewarded for
being compromised, and would have been reported as a fleet-best performer.

**Rules:**

1. **Never score a ranking you have not attributed to a URL.** `org_keywords` is a count of
   things Google associates with the domain, not a count of the client's wins. Select
   `best_position_url` and read the paths before any keyword number reaches a score or a
   report.
2. **Net hostile rankings out of the score and raise them as an action instead.** Traffic
   attributed to injected URLs gets discounted in the same proportion. Infection is a
   dispatch item, never a credit.
3. **Judge the keywords by fit with the person, not by how spammy they look.** `nintendo
   store` is a fine keyword — for a games retailer. The tell is a *speaker coach* ranking
   for it. The GCT already states who each site is for; compare against that.
4. **A clean sitemap and a clean REST API do not mean a clean site.** Both sites' sitemaps
   and post lists were entirely legitimate, and their real content is real. The injection
   lives beside WordPress, in URL space the CMS never enumerates — so any check that walks
   the sitemap or `/wp-json/wp/v2/posts` is structurally unable to find it. What Google has
   indexed is a separate source of truth from what the CMS will admit to.
5. **404 today does not mean clean.** These URLs now return 404 to human and Googlebot
   alike from a datacenter IP, while still ranking. That is consistent with cleaned-but-
   still-indexed *and* with a cloak keyed to something the probe can't reproduce. Say which
   of those you have ruled out; removal still has to be requested in Search Console either
   way, because the junk keeps ranking after the files are gone.

Companion to the same day's `classify-the-metric-dont-just-count-it` (referring domains,
same disease one metric over): fleet median referring domains is 368 against a median of
**26 dofollow**, because a `.shop`/`.store` link-spam blast hits every site daily. Report
`refdomains_dofollow`; `refdomains` is noise. billybatt.com reads as 324 referring domains
and is actually **2 dofollow, both of them ours** — the authority problem the number
appears to have solved is entirely intact. Ahrefs exposes an `is_spam` flag; use it.

Learned August 3, 2026.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
