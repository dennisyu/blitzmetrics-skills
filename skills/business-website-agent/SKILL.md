---
name: business-website-agent
description: Build your company's entity home — your company name as the domain, a facts-first site with real service pages and consistent NAP (name, address, phone), structured so Google and AI treat it as the source of truth about the company. Use to create or audit a company website.
---

# Business Website Agent

*Part of the Local Service Spotlight Agent Skill Pack — Company Edition.*

**Use this when** you're ready to build (or fix) the authoritative URL about your company — the facts page that every profile, directory, review platform, and press mention points back to. Step 4 of the Local Service Spotlight method.

## Inputs
- Positioning brief from `business-brand-strategist`: ideal customers, one-sentence differentiation, top-5 proof points.
- Scored proof from `positive-mentions-harvester` and the 30-day plan from `reputation-gap-analyzer`.
- Real numbers (years, jobs, locations, reviews), the exact NAP — name, address, phone — one logo and one crew photo set, every profile URL the company owns.

## Build pipeline (Dennis's order — don't skip steps)
1. **Research and disambiguate.** Google the company name. List every same-name or similar-name business and what makes yours unmistakable — category, city, people. Google must be able to tell you apart before it will trust your page.
2. **Register the company name as the domain.** yourcompany.com, exactly as the name reads on your Google Business Profile. Taken? Add the city or the trade — never a pun.
3. **Generate the site** on the standard template below.
4. **Wire DNS** and confirm the site resolves on https.
5. **Publish**, then run `knowledge-panel-entity-seo` the same day.

## Homepage structure (this exact order)
1. **Hero** — company name, your one-sentence differentiation, two CTAs (call, request a quote), and an authority image: your crew on a real job, not stock.
2. **Stats bar** — 4 real, provable numbers: years in business, jobs completed, review count, coverage area. HVAC Quote leads with 300+ customers, not "passionate about service."
3. **Our Story** — factual company arc with dates, founders, and milestones, written so AI can quote it.
4. **What We Do** — service cards aimed at your ideal customers, each linking to a full service page — not every job you've ever taken.
5. **Featured proof** — your single best case study, local-press hit, or customer video, embedded.
6. **What Customers Are Saying** — reviews and testimonials with name, job type, and a link to where each was said (Google, Yelp, industry platform).
7. **Licenses, awards & affiliations** — real credentials, certifications, and association logos only, each linked.
8. **Contact** — the exact NAP, hours, and service area, plus every profile you own, mirrored exactly in LocalBusiness schema `sameAs`.

## Copy rules
- Facts page, not a sales page. Every claim links to its source; funnels live elsewhere.
- No adjective without a receipt. "Award-winning" needs the award, the year, the link.
- NAP identical, character for character, across the site, the Google Business Profile, and every directory — mismatches erode the entity.
- Flag anything unconfirmed during drafting — it does not ship.
- Write for the machine that will quote you: clean headings, alt text, descriptive links.

## Steps
1. Draft the homepage and one page per core service from the brief and scored proof only.
2. Build on the template — one homepage, eight sections, nothing exotic.
3. Wire Organization + LocalBusiness schema JSON-LD: your site as canonical home, `sameAs` to every profile and directory.
4. Add About, Reviews, Service-area, Gallery, and Contact pages; publish an accessibility statement in the footer (WCAG 2.2 AA target, honest conformance status, monitored contact email, dated — per the BlitzMetrics accessibility-statement standard).
5. Publish and hand off to `knowledge-panel-entity-seo`.

## Output
- Draft homepage and service-page copy with every claim sourced, then a live site at yourcompany.com with schema wired and NAP consistent everywhere.

## For marketing managers & owners
**If you're the marketing manager:** this is the site brief, copy deck, and schema spec in one — hand it to any builder, or run it yourself, without an agency discovery phase.
**If you own the business:** the site is where customers, commercial clients, and future hires verify you before they call — facts they can check close more work than slogans they can't.
**Your edge:** the hero headline is your differentiation sentence — the guarantee, specialty, or coverage no competitor in your market could claim; if it could sit on their site, rewrite it until it can't.

## Run on a persistent agent (Fable 5)
- **Loop to done:** run the whole pipeline — research, domain, build, DNS, publish — and loop until the site resolves on https with all eight sections, schema wired, NAP consistent, and every claim sourced. Draft copy is the midpoint, not the output.
- **Self-verify:** audit your own page against the copy rules before handoff — no adjective without a receipt, nothing unconfirmed ships, `sameAs` mirrors the Contact section exactly.
- **Compound with memory:** build from the stored brief, proof library, and 30-day plan — never re-interview the owner for facts the chain already holds.
- **Log the run:** record what the template needed that the inputs didn't supply — that's the upstream fix for the next build.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- COMPANY NAME = the domain. The entity home is the URL Google treats as authoritative about the business; everything else — GBP, directories, socials — orbits it and links back.
- The homepage is the most authoritative set of **facts** about the company, each tied to a source. Not a "call now" carousel.
- One logo, one NAP, one crew photo set everywhere — site, Google Business Profile, directories. Variants create entity confusion that Step 5 then has to undo.
- In Content Factory terms this is core plumbing: the hub your tracking, retargeting, and every definitive article hang off.
- Boil the ocean on proof, not on design. The template is fixed so your facts do the work.

## Definitive article & pairings
- Reference: https://blitzmetrics.com/knowledge-panel/ · https://blitzmetrics.com/task-library/
- Pairs with: → knowledge-panel-entity-seo → ai-search-visibility

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
