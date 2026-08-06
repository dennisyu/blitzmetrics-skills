---
name: security-audit
description: Continuously verify that a website is still the site you published — no injected spam, no rogue admin, no hidden plugin, no different page served to Googlebot than to humans. Use to stand up monitoring on a new property, to run a point-in-time compromise check, to investigate a "my site looks hacked" report, or as the daily read-only sweep across a network of sites. Read-only by default; it finds and proves, it does not clean.
author: Dennis Yu — BlitzMetrics / Local Service Spotlight
references:
  - https://localservicespotlight.com/security-audit/
  - DealCon-Skills/evidence-verification.md
  - DealCon-Skills/seo-audit.md
  - DealCon-Skills/client-access-checklist.md
  - Fleet-Security-2026-07-27/README.md
  - Sigrun-SOMBA/security/monitor.py
---

# Security Audit

**Use this when** you are responsible for a site staying the site you published — which, on
a managed network, is every day, not the day someone complains.

This skill exists because of a specific pattern we kept losing to: **we found out from the
outside.** A first-degree LinkedIn connection messaged at 6:19am asking whether we had been
hacked. A Search Console email about video markup turned out to be three sites serving a spam
storefront. A client forwarded a newsletter about a WordPress vulnerability and asked whether
it affected his sites — it did, and the sweep that question triggered found more. Every one of those was discoverable from outside, for free, with no
credentials, on any morning before it was reported to us.

## The one idea

**A site is compromised the moment it stops matching its own baseline — not the moment
somebody notices.**

So the job is not "look for malware." Malware you have never seen is invisible to you. The
job is to **write down what the site is when it is known-good, and then diff it every day.**
A new external script domain is suspicious whether or not you recognise the payload. A new
admin user is suspicious whether or not you know what they did.

---

## The seven checks

All read-only. All runnable against any WordPress property with a REST endpoint and an
application password. Six can run credential-free from outside.

| # | Check | What a failure looks like |
|---|---|---|
| 1 | **External resource inventory** | A script, iframe or link to a domain that was not in yesterday's baseline |
| 2 | **Spam-injection markers** | Known link-spam domains, casino/pharma keyword blocks, hidden-link patterns in the rendered HTML |
| 3 | **Users** | A new account, or an existing account whose role escalated |
| 4 | **Plugins** | A new or removed plugin, a status flip, a version *downgrade*, or a version that is not a real published release |
| 5 | **Reachability** | A critical page that stopped returning 200 |
| 6 | **Cloak check** | The page served to Googlebot differs from the page served to a human |
| 7 | **Did checks 3 and 4 actually run?** | An unreadable REST endpoint, an unparseable 200, or an empty baseline |

### Check 7 is the one that makes the other six trustworthy
An endpoint that 403s and a site with zero plugins produce the same empty list. Without a
guard, "we could not read the plugin list" silently renders as "no plugins changed" — the
monitor reports **clean** on the day it went blind. So: an unreadable endpoint is its own
ALERT, naming the real cause, and that half of the diff is **SKIPPED** — never reported as
mass deletion, and never allowed to pass as clean.

This generalises past security. *Any* check whose failure mode resembles its success mode
needs a third state.

---

## Three states, never two

The hardest bug in this whole skill is the two-valued answer. When the monitor asked
wordpress.org "what versions of this plugin exist?", a `None` reply meant two opposite
things: **the plugin is premium and not listed there** (fine, forever) and **wordpress.org
did not answer** (a real blind spot). Both printed the same alert line, so a paid plugin
alerted every single morning — and an alert that fires every morning is an alert nobody
reads.

The fix is the shape, not the wording:

- **NOT_LISTED** — a definitive answer (404, or a 200 whose body is `false`). Advances the
  baseline, logged as INFO, and states plainly that the version was *not verified upstream*.
- **UNREACHABLE** — timeout, 5xx, unparseable. Still ALERTs, names the upstream service
  rather than accusing the plugin, and retries with backoff so one network blip cannot
  manufacture a security alert.
- **A real version set** — compare normally.

And delete the hand-maintained exception list. We had a `PREMIUM_SLUGS` constant listing
which plugins to excuse; hand-maintained lists drift behind the thing they describe.
wordpress.org answers the question itself, so ask it.

---

## Prove the monitor can fail

A check that cannot fail is not a check. Before you trust a clean result, run **live negative
tests** against the real baseline in memory (never writing to the baseline file):

- control → expect 0 alerts
- inject a rogue admin → expect exactly 1
- remove a plugin → expect exactly 1
- tamper a version → expect exactly 1

Only then is "clean" an earned result. When we did this the first time, the test suite went
from 55 to 116 assertions and immediately caught a defect the live path would never have
reached: the new retry branch called `time.sleep()` and `time` was never imported — code that
only executes during a wordpress.org outage, which is exactly when the monitor matters most.

---

## What the real incidents taught

**A hidden plugin is not in the plugin list, by design.** One backdoor shipped as "Web Media
Optimizer" and filtered *itself* out of `all_plugins`, stripped its own action links, and
removed itself from update checks. A clean plugin audit meant nothing. It was found by
requesting its file path directly and comparing the status code against a control path that
should not exist: real file → 200, control → 307. **Probe for the thing, do not ask the list.**

**Payload and repair are two halves.** The same compromise had a dropper in `mu-plugins/`
and a hidden fake plugin. Removing one and declaring victory is how a backdoor self-heals.

**Cloaking is invisible from a browser.** Three sites answered 500 to humans and 200 with a
spam storefront to Googlebot. Nobody clicking around would ever see it.

**Not every scare is an incident, and saying so is the deliverable.** A "lickfix malware"
report turned out to be a Cloudflare bot-challenge interstitial. Sixteen independent checks
came back clean and the honest answer was *no active malware*. An audit that can only
conclude "compromised" is not an audit.

**Rate-limit yourself.** Chained manual runs against one host earned a 429 that got logged as
an ALERT. Space runs out, and annotate self-inflicted noise in the log immediately so nobody
reads it as an incident six weeks later.

---

## Running it across a network

1. **Baseline every property** the day you take it on. No baseline, no monitoring — and say
   so out loud rather than implying coverage you do not have.
2. **Run daily, read-only, from a residential IP** with a full browser User-Agent. Datacenter
   IPs and minimal UAs get edge-blocked and you will audit the WAF instead of the site.
3. **Alert on change, log on clean.** The log is the evidence that the quiet days were checked.
4. **Never auto-remediate.** Writing to a compromised site destroys evidence and usually does
   not reach the interceptor anyway. Diagnose fully, package the fix, hand it to a human with
   host access.
5. **Count what you do not cover.** If the network is 198 sites and you can enumerate 49, the
   report says 49 of 198 — not "the fleet is clean."

## Definition of done
- Every monitored property has a dated known-good baseline in version control.
- Every check has a third state for "could not determine."
- The negative tests pass — the monitor demonstrably catches a planted change.
- The uncovered count is stated in every report.
- No cleaning was performed by the audit itself.

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-08-02-one-message-for-two-opposite-facts -->
**August 2, 2026** (from: sigrun.com security monitor — a paid plugin alerted every morning forever because "not listed" and "unreachable" printed the same line)

### When one code path can produce a message for two opposite facts, the message is wrong in both cases

The sigrun.com monitor verifies each plugin version against api.wordpress.org. Its lookup returned `None` for
two situations that have nothing in common:

- **wordpress.org answered, and it does not distribute this plugin** — true of every paid add-on (Elementor
  Pro, Yoast Premium, WPConsent Premium) and of the site's own custom plugin.
- **wordpress.org could not be reached at all** — a timeout, a 5xx, a WAF interstitial.

Both printed `upstream UNVERIFIABLE ... lookup failed`. One sentence, two opposite meanings, and the failure
runs in both directions:

1. **It never clears.** A paid plugin nobody had hand-added to the `PREMIUM_SLUGS` allowlist alerted every
   single morning, forever, and the only way to silence it was for a human to edit a hardcoded set. That is
   alert fatigue attached to a scheduled job. This monitor exists to catch the next infection on day one — and a daily alert everyone learns to skim rebuilds the exact condition it was built to remove.
2. **It hides the real thing.** During a wordpress.org outage, every ordinary plugin bump prints that same
   "UNVERIFIABLE" line. A genuinely tampered plugin folder arriving in that window would have been visually
   identical to the routine noise. The one line a human most needs to trust said the same thing whether the
   news was "nothing to see" or "someone edited your plugins."

**Rules:**

1. **Distinguish "answered no" from "did not answer."** A 404 is data. A timeout is the absence of data. Any
   function that collapses them into one return value has thrown away the more important half. Return a
   three-state result, not a nullable one.
2. **A hand-maintained allowlist is a clock that runs slower than the thing it describes.** `PREMIUM_SLUGS`
   had two entries and the site had four unlisted plugins. Derive the answer from the authority (wordpress.org
   already knows) instead of restating it locally.
3. **Retry before you alarm; vary time before you vary anything else.** A one-second network blip should not
   be able to manufacture a security alert. Backoff-retry the unreachable case, then report it.
4. **Dispatch on type and fail CLOSED.** The sentinel chain `if known is UNREACHABLE ... elif nv in known`
   would substring-match on a sentinel (`"1.1" in "NOT_LISTED"`) or raise `TypeError` on `None` if identity
   ever missed. Check the *shape* of the good case first and let everything unexpected fall through to the
   alert branch — a security check must never be able to pass by accident.
5. **Test the path that only runs during the emergency.** The new retry code called `time.sleep()` with `time`
   unimported. It executes only when wordpress.org is down — i.e. only when the monitor matters — so no live
   run would ever have caught it. Any branch that fires only under failure conditions needs a test that
   simulates those conditions, because production will never rehearse it for you.
6. **Prove red before you trust green.** Reconstructing the pre-change code and running the new suite against
   it produced 17 failures and a `TypeError`. Without that step, 116 passing assertions prove only that the
   tests agree with the code that was just written.

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
