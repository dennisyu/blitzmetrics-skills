---
name: ai-search-visibility
description: Control how ChatGPT, Perplexity, and Google AI Overviews describe you when a buyer, seller, or client researches you — audit the answers, trace them to sources, feed the AIs your canonical facts. Use to win the AI first impression before any deal conversation.
---

# AI Search Visibility

**Use this when** you want AI to give the right answer about you — because buyers, sellers, and premium clients now ask ChatGPT before they ever reply to your email. Step 6 of the Local Service Spotlight method.

## Inputs
- Your name, niche, entity home, and every profile URL.
- Entity-clarity findings and Person schema from `knowledge-panel-entity-seo`.
- Your differentiation sentence and top-5 proof points from `personal-brand-strategist`.
- Prior test-grid answers, if you've run this before — you'll diff against them.

## The buyer's test grid (run verbatim)
| Who's asking | What they type | What you need back |
|---|---|---|
| Premium client | "Who is [your name]?" | Your differentiation plus two proof points |
| Seller vetting a buyer | "[your name] [company] acquisitions" | Your buy box and deal history, accurate |
| Anyone in your niche | "Best [niche] expert for [buy box]" | You, named, your entity home cited |
| Skeptic | "Is [your name] legit?" | Third-party proof, not your own claims |
| Podcast host | "[your name] interviews" | Your featured interview and core topics |

## Where the answers come from
- **ChatGPT** — training data plus live browsing; your entity home and high-authority mentions feed it.
- **Perplexity** — live retrieval with cited URLs; it quotes specific pages, so your definitive article matters most here.
- **Google AI Overviews** — the Knowledge Graph plus top-ranked pages; everything you fixed in Step 5 compounds here.

## Steps
1. Run the grid in all three engines. Paste raw answers — no cleanup, no cherry-picking.
2. Mark every line **thin, missing, or wrong**. Wrong includes stale titles and another person's facts bleeding in — entity collision surfacing in AI.
3. Trace each weakness to its source: the page, profile, mention, or schema field the model is reading — or can't find.
4. Check for a **definitive article** on your topic. No canonical page means the models improvise; hand that gap to `definitive-article-writer`.
5. Produce **5 ranked actions**: a page to strengthen, a mention to earn, a fact to add to the entity home, an inconsistency to clean, an article to write.
6. Re-test in 30 days and diff. This is MAA: metrics (the grid) → analysis (the trace) → action (the five fixes).

## Output
- Verbatim current-state AI answers, a gap list traced to specific sources, and 5 ranked actions to make AI describe you the way you want for deals.

## For DealCon — agency owners & acquirers
**If you run an agency:** when a prospect asks AI "who should run marketing for my [industry] business" and you're the named answer, the call starts closed — inbound at premium pricing.
**If you buy & sell companies:** sellers vet acquirers in ChatGPT now. When AI states your buy box and closed deals accurately, qualified sellers self-select toward you — off-market deal flow.
**Your edge:** name the one question in your niche you must be the answer to, then aim all five fixes at that single question.

## Run on a persistent agent (Fable 5)
- **Loop to done:** run the full grid in all three engines, verbatim, every time — and loop until every thin, missing, or wrong line is traced to a specific source and covered by one of the 5 ranked actions.
- **Self-verify:** paste raw answers, no cherry-picking, then grade them against the differentiation sentence and proof points held in memory.
- **Compound with memory:** store each run's verbatim answers so the 30-day re-test is a diff, not a fresh audit — the trend across runs is the real metric.
- **Log the run:** the before/after diff is the meta-article — and the proof a client or counterparty can check.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- Same engine as the Knowledge Panel: **clear entity + agreeing sources**. Fix it for Google and you largely fix it for the AIs that read Google's view of you.
- AI quotes canonical pages. ONE definitive article per topic; thin posts orbit it and link back. Competing with your own hub is content vandalism.
- Specificity survives the model. Zach Peyton's facts — Superior Fence & Rail, largest US fence franchise, 110+ locations, $310M+ — get repeated verbatim. Vague bios get paraphrased into mush.
- George Paladichuk built NaiL AI so that when roofers ask AI about AI, he is the named answer. Pick your question and own it the same way.
- Don't argue with the output — fix the sources. Models repeat what the web agrees on about you.
- Run this before every raise, listing, or launch. The answer changes as the web changes — know it before your counterparty does.

## Definitive article & pairings
- Reference: https://blitzmetrics.com/definitive-article-guide/ · https://blitzmetrics.com/how-my-ai-agents-document-and-improve-themselves-meta-articles-definitive-articles/
- Pairs with: → dollar-a-day-strategist → content-factory → definitive-article-writer

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-20-ahrefs-free-dr-endpoint-auth-deadline -->
**July 20, 2026** (from: anthony-hilb-seo-tracker (weekly-brand-maa) — refiled from a stray root note by skill-pack-propagation on July 21, 2026)

Ahrefs' free Domain Rating endpoint stops accepting unauthenticated calls on August 1, 2026.
> **⚠ RESOLVED August 3, 2026 — read this first: use `site-explorer-domain-rating`, always.**
> Everything in this section down to "Rules for any skill that pulls Ahrefs Domain Rating" is
> the historical record of a deprecation that no longer needs tracking. Do not act on the dates.

The `public-domain-rating-free` MCP call still returns the normal DR value today but now
carries a deprecation warning: "Unauthenticated access to this endpoint will be removed on
2026-08-01. Requests will require a free API key." Every weekly/monthly tracker that pulls DR
(anthony-hilb, wtp, trenton-sandler, cxotalk, family-law, somba, and any future tracker) will
start erroring from August if its call path is unauthenticated.

Rules for any skill that pulls Ahrefs Domain Rating:

**RESOLVED — August 3, 2026. Use `site-explorer-domain-rating`. Always.** There is no date left to
track and no key to register. The three dated rules below are superseded, kept only as the record.

Why the free endpoint was retired from our skills rather than migrated:

- **We already hold the key.** The workspace MCP authenticates with a paid Lite key
  (`subscription-info-limits-and-usage` returns real workspace data, so auth demonstrably works).
  The "free API key" in Ahrefs' warning is for callers who hold no key at all. Registering a second
  one would have added a credential to manage in exchange for nothing.
- **Identical numbers.** Verified August 3, 2026 across two domains: anthonyhilb.com returned DR 10
  from both endpoints, michaelkrigsman.com DR 1.0 from both.
- **The authenticated endpoint is MORE accurate.** `public-domain-rating-free` lags the authenticated
  series by about a day, which is exactly what put a wrong DR 11 into the anthony-hilb 2026-07-20
  snapshot. Switching removes a known defect; it is not merely deprecation-proofing.
- **Cost is not a constraint.** ~50 units per call against a 100,000/month Lite allowance. For many
  domains at once, `batch-analysis` takes up to 100 targets in ONE call at ~18 units each, verified
  to return DR values identical to the single endpoint.

**The meta-lesson, which is the part worth keeping.** This block carried a hard-coded vendor date into
six skill files, and only ONE of them ever received the July 27 correction from August 1 to August 10.
The other five still read "Until August 1, 2026" on August 3 — a deadline that was both wrong and
already expired, still instructing agents to prefer the dying endpoint. A conditional written around a
vendor's date has to be re-verified in every copy, forever; an unconditional instruction needs nothing.
**Prefer the instruction that cannot go stale over the one that is merely correct today** — and when a
correction lands, grep for the other copies in the same breath. Same shape as the "a standing contract
recorded in one file is not a standing contract" rule in `Skill-Learnings/README.md`.

Superseded, retained as the record:
1. ~~Until August 2026 keep using `public-domain-rating-free` first — it works and costs 0 units.~~
2. ~~If it errors, fall back once to `site-explorer-domain-rating` and state the switch in the report.~~
3. ~~Permanent fix: register a free API key (about a 5-minute setup).~~

Learned July 20, 2026. Resolved August 3, 2026.

<!-- learning:2026-07-27-serp-depth-needs-max-crawl-pages -->
**July 27, 2026** (from: cxotalk-weekly-maa run)

### DataForSEO `depth` alone does NOT go past page 1 — you need `max_crawl_pages`

Checking whether michaelkrigsman.com still ranked for "michael krigsman":

```
serp_organic_live_advanced { keyword, location_name, language_code, depth: 30 }
```

returned **9 organic results** and no michaelkrigsman.com. Combined with a live Chrome
render that also didn't show it, the obvious read was "the entity home dropped off page
one." That would have been the report's headline — and it would have been wrong.

`depth` sets how many results to *return*; `max_crawl_pages` (default **1**) sets how many
SERP pages to *crawl*. Re-running with `max_crawl_pages: 4` returned 21 results and showed
**four** michaelkrigsman.com URLs — homepage at rank_group 7, `/about/` 9, `/home/` 12,
`/connect/` 14. The real story was the opposite of the false one: the site went from 1
ranking URL to 4.

**Rules:**

1. Any "did we lose a ranking?" check must pass `max_crawl_pages` ≥ 3. `depth` alone is a
   page-1 query, no matter how large you set it.
2. Never report a disappearance from a single SERP pull. Two pulls one minute apart
   genuinely disagreed on this keyword (one had the homepage at #7, the other didn't have
   the domain at all). Volatility at the page-1/page-2 boundary is real — report
   "contested foothold," with both observations, rather than a clean win or loss.
3. A logged-in browser render is a *third* opinion, not a tiebreaker. Personalization makes
   it systematically different from a clean datacenter pull; prior runs quoted "#8 clean /
   #3 browser" for the same query on the same day.

Severity note: this nearly reported a client's site as having fallen out of the SERP
entirely. Learned July 27, 2026.

<!-- learning:2026-07-29-a-redirect-you-ship-is-a-redirect-you-own -->
**July 29, 2026** (from: SEO-tree link audit, July 29, 2026)

### A URL you ship inside a skill pack is a URL you have to keep alive

Our own published packs told every installer's agent to read
`localservicespotlight.com/ai-agent-application-password/` for login-free publishing. That URL
had become a **double 301** — one hop to a renamed article, a second hop to its current home.
It still resolved, so nothing complained. It was sitting in `boil-the-ocean.md` and
`video-repurposing-agent.md` across four public packs, in two generators, in the daily
checklist, in the project's own CLAUDE.md, and on the trunk page of the whole system.

A redirect chain is not a broken link, which is exactly why it survives: every check passes,
every page loads, and the crawler quietly discounts the destination. Sixteen references were
repointed at the final URL, at the source, so the next rebuild ships the fix to everyone.

**Rules:**

1. **Cite the URL that answers 200, never a URL that answers 301.** Follow every external link
   you are about to write into a skill file, and record where it ends up, not where you started.
2. **A URL inside a downloadable pack is published surface area.** It reaches people you cannot
   email later. Treat a link in a shipped skill file with the same care as a link on a page.
3. **Fix at the source, then let propagation do the distribution.** Editing a live page fixes
   one copy; editing the skill file fixes every copy on the next run.
4. **Add the dead URL to the checker, not just to your memory.** `verify_link_graph.py` now
   fails if any node reintroduces it and if any node sits behind a redirect hop at all.
5. **A short URL does not need a redirect plugin.** WordPress core's
   `redirect_guess_404_permalink` 301s an unmatched path to the single post whose slug it
   prefixes, so `/persistent` reaches `/persistent-agents/` for free. Do NOT publish a stub page
   on the short slug to fake this — a thin page that competes with the article is the exact
   content-vandalism the definitive-article standard exists to prevent. Assert the short URL's
   final destination on every run, because the guess turns into a 404 the day a second matching
   slug ships.

Learned July 29, 2026.

<!-- learning:2026-07-29-a-check-that-cannot-fail-is-not-a-check -->
**July 29, 2026** (from: redirect-chain audit, July 29, 2026)

### A check built on a branch that can never run reports perfect health forever

Two scripts written the same day counted redirect hops like this:

    try:
        r = urllib.request.urlopen(req)      # HEAD
        return hops, r.status
    except urllib.error.HTTPError as e:      # <-- catch the 301 here
        ...follow Location, hops += 1

That `except` can never fire. `urlopen` installs `HTTPRedirectHandler` by default and follows
301/302 transparently, returning the FINAL response. So the counter returned **0 hops for every
URL on earth** — including one we had already proved by hand was a double 301. The first audit
printed "34 rules · 0 chained" and read as good news.

Fixing the counter turned that into: 6 chains on one site, 18 on another, one self-redirecting
rule with 12,190 hits looping forever, and the busiest rule on the site (829,576 hits) throwing
away a trailing slash and buying a second hop on every single request.

**Rules:**

1. **Before trusting a checker, make it fail on purpose.** Feed it a case you KNOW is bad. If it
   passes, the checker is broken — not the world. Both scripts now call a `selftest()` that
   fetches a URL known to redirect and aborts the whole run if it measures zero hops.
2. **Any library call with "convenience" behaviour is a checker's enemy.** Following redirects,
   retrying, normalising, caching: all of it hides the exact signal a verifier exists to see.
   Measure at the lowest level that still answers the question.
3. **A `try/except` around a network call deserves the same scrutiny as the happy path.** An
   `except` clause that cannot be reached is dead code that looks like diligence.
4. **Zero is a suspicious answer.** Zero orphans, zero chains, zero errors on the first run of a
   brand-new check almost always means the check is not wired to anything. Confirm one true
   positive exists before believing the zero.

Learned July 29, 2026.

<!-- learning:2026-07-29-read-the-plugin-source-before-writing-to-its-table -->
**July 29, 2026** (from: collapsing 24 redirect chains across localservicespotlight.com + dennisyu.com, July 29, 2026)

### When a plugin's REST API is undocumented, download the plugin and read it

Two redirect tables needed surgical edits and neither API was documented in a way that answered
the only question that mattered: *what happens to the fields I do not send?* Guessing against a
live table with 34 and 192 rules on it was not acceptable, and probing by trial risked detaching
real redirects carrying thousands of hits.

So both plugins were downloaded from the wordpress.org repo at the exact installed version and
read. Ten minutes, and it turned two unknowns into contracts:

- **RankMath Redirections** has no route that LISTS redirections. The read path is
  `status/exportSettings` (redirections ride along in the export). The write path is
  `updateRedirection`, which is really the post-metabox save handler: it rebuilds the rule from
  `(redirection_id, url_to, sources, header_code)`. **Omit `redirectionSources` and the source is
  rebuilt EMPTY**, silently detaching the rule from the URL it exists to catch. It also rejects an
  empty `objectID`, which a standalone rule does not have — pass an id matching no post, because
  a real one makes that post's metabox claim it owns a redirect.
- **Redirection plugin** (`redirection/v1/redirect`) sanitises the whole payload and then does a
  full row `UPDATE`. A partial patch drops every field you left out. The payload has to be the
  GET item echoed back with only the target changed — and `hits` / `last_access` must be OMITTED,
  because the sanitiser maps them onto `last_count` / `last_access` and rewrites the counters.
- Its import path is safe but useless for repairs: `set_redirections()` skips any row whose
  source already matches an existing rule, so re-importing corrected copies changes nothing.

**Rules:**

1. **Read the source before the first write, not after the first surprise.** `curl` the versioned
   zip from wordpress.org, unzip, read the sanitiser and the update method. Cheaper than one bad
   write to a production table.
2. **Find out whether update means PATCH or REPLACE.** If the model sanitises into a fresh array
   and calls `$wpdb->update` with it, every field you omit is erased.
3. **Audit every redirect engine a site has, not the first one you find.** dennisyu.com runs
   RankMath Redirections AND the Redirection plugin at once. `X-Redirect-By` proved the plugin
   wins; fixing the RankMath copies changed nothing a visitor could see — 2 of 13 "fixes" held
   and the rest still measured 3-4 hops. **`X-Redirect-By` on the response is the ground truth
   for who is actually in charge.**
4. **Never auto-rewrite a regex rule.** Its source is a pattern, not a URL, so hops cannot be
   measured, and its target may contain capture groups. Report it and stop.
5. **A rule pointing at itself is a live infinite loop, not a chain.** Detect "never lands after
   N hops" as its own class and never auto-repair it — the correct destination is an editorial
   decision. One such rule had taken 12,190 hits.
6. **Check the trailing slash on high-volume rules.** A target of `/$1` where WordPress canonical
   wants `/$1/` costs an extra 301 on every request. On the busiest rule on the site that was
   829,576 requests each paying for a hop nobody needed.

Learned July 29, 2026.

<!-- learning:2026-08-03-prefer-the-instruction-that-cannot-go-stale -->
**August 3, 2026** (from: Ahrefs free-DR deprecation follow-up after the anthony-hilb-seo-tracker run)

### A conditional built on a vendor's date rots in every copy except the one you corrected

The anthony-hilb report flagged that Ahrefs' `public-domain-rating-free` endpoint stops accepting
unauthenticated calls on August 10, 2026 — seven days out, and the date of the tracker's own next
run — and recommended a "5-minute free API key registration." Chasing that down produced two
findings, and the second is the one that generalises.

**1. The registration was never necessary, and checking took one call.** The workspace MCP already
authenticates with a paid Lite key. The "free API key" in Ahrefs' warning is aimed at callers who
hold no key at all. `site-explorer-domain-rating` returns the identical number on the key we already
have — verified across two domains the same day (anthonyhilb.com DR 10 from both endpoints,
michaelkrigsman.com DR 1.0 from both) — for ~50 units against a 100,000/month allowance. It is also
*more accurate*: the free endpoint lags the authenticated series by about a day, which is precisely
what wrote a wrong DR 11 into the 2026-07-20 snapshot. So the "deprecation fix" was really a defect
fix that had been available all along.

**Rule: before scheduling work to satisfy a vendor's new requirement, check whether the credential
you already hold satisfies it.** A deprecation notice describes the vendor's default caller, not
your setup.

**2. The instruction had already rotted in five of six copies.** The block telling agents to prefer
the free endpoint lived in six skill files. On July 27 the cutoff moved from August 1 to August 10,
and exactly ONE file — `weekly-brand-maa.md` — received the correction. On August 3 the other five
still read *"Until August 1, 2026 keep using `public-domain-rating-free` first"*: a deadline that was
both wrong and two days expired, still actively instructing agents toward the dying endpoint. Nobody
noticed, because each file was individually plausible and nothing compares them.

The fix was not to propagate the new date. It was to **delete the date**: the rule is now
unconditional — *use `site-explorer-domain-rating`, always* — with the dated version struck through
beneath it as the record, plus a pointer at the top of the section so an agent reading top-to-bottom
cannot hit the stale narrative first.

**Rules:**

1. **Prefer the instruction that cannot go stale over the one that is merely correct today.** "Use X"
   survives indefinitely. "Use X until DATE, then Y" is a maintenance obligation in every copy,
   forever, and it fails silently and invisibly — an expired conditional reads exactly like a live one.
2. **When a correction lands on a duplicated instruction, grep for the other copies in the same
   breath.** This is the same shape as the standing rule in `Skill-Learnings/README.md` that "a
   standing contract recorded in one file is not a standing contract," and the same shape as the
   July 29→31 gap between a rebuild gate being learned and the runner being changed. Three
   independent recurrences means the default is wrong: assume duplication until a grep proves
   otherwise.
3. **A date copied out of a vendor's warning is the least durable thing in a skill file.** Where one
   must be written down, write it as "as of <Month D, YYYY> the API said X" so the staleness is
   visible on the page — and pair it with a dateless instruction that stays correct if nobody ever
   revisits it.
4. **Check the whole fleet of callers, not the one that surfaced the problem.** Of 31 scheduled task
   prompts, only two named the dying endpoint and two others were already on the authenticated one.
   Grepping the mirrored prompt set answered in one call what would otherwise have been six file
   reads and a guess.

Learned August 3, 2026.
