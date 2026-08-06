---
name: definitive-article-writer
description: Write the ONE canonical page that owns a topic or a person's name — comprehensive, source-linked, structured so Google ranks it and AI quotes it, with every thin post orbiting it. Use instead of publishing competing posts.
---

# Definitive Article Writer

**Use this when** you want to own a topic — or a person's name — in Google and in AI answers. One comprehensive canonical page beats a dozen thin blog posts, because humans and machines both cite the page that settles the question. Step 9 of the Local Service Spotlight method.

## Inputs
- The topic or person, plus every fact you can prove: numbers, dates, names, clients, quotes, media.
- The mined transcript from `content-factory` stage 2, if the article starts from a recording.
- Your proof inventory from `positive-mentions-harvester` — third-party corroboration to cite.
- Every existing page on the subject — yours and competitors' — so you know what to absorb and what to beat.

## Steps
1. **Audit first.** If a canonical hub already exists on your site, improve it. Never publish a second page on the same topic — that's content vandalism; you'd split your own authority.
2. **Outline every question** a prospect, buyer, journalist, or AI could ask about the subject. Definitive means nothing left to ask. Boil the ocean — good enough is not enough.
3. **Write facts, not fluff.** Open with a 2–3 sentence plain-language summary — who, what, why it matters — because that's the block AI lifts verbatim. Every claim carries a number, a name, or a source link. Publish nothing you couldn't defend in diligence.
4. **Structure for machines.** H2s phrased as the questions people actually ask. Schema markup (Person, Article, FAQ). The entity's name spelled identically everywhere. A stable URL that never changes.
5. **Build the orbit.** Internal-link every related thin post INTO this page; link this page out to its sources and sibling hubs. Thin posts orbit the hub — they feed it, never compete with it.
6. **Make it the target.** Every clip, social post, podcast show-note, bio, and profile points at this URL. One topic, one URL — the Task Library principle.

## Anatomy — what's on the page, in order
- Plain-language summary (2–3 sentences a machine can quote).
- The facts: numbers, dates, names, each tied to its source.
- The story and strongest quotes from the recording.
- Embedded media — the interview or talk this came from.
- FAQ — the questions you outlined, answered directly.
- Links out to sources, across to sibling hubs.
A definitive article is a facts/SOP hub, not an essay. If a section doesn't inform or prove, cut it.

## Why AI quotes it
- AI engines lift the page that states facts plainly, with consistent entity spelling and sourced numbers.
- Corroboration decides ties: your harvested mentions (step 2) and entity plumbing (step 5) confirm what this page claims.
- A stable URL accumulates citations; a renamed one starts over. Pick the URL once.

## Failure modes — what kills a definitive article
- Publishing a second post on the same topic because writing fresh feels easier than improving the hub.
- Adjectives instead of numbers. "Leading expert" proves nothing; "110+ locations, $310M+" does — that's how you describe Zach Peyton.
- Changing the URL or title to chase keywords — you reset your own authority to zero.
- Letting it go stale. The hub is living: every new recording, deal, or mention updates it.

## Output
- One canonical, source-linked, schema-marked article at a stable URL — the page Google ranks and AI quotes for this subject.
- The orbit list: existing posts to re-link into the hub, plus every clip and profile that should point here.

## For DealCon — agency owners & acquirers
**If you run an agency:** the definitive article on your niche is what prospects read before the sales call — it pre-sells you as the documented authority, justifies premium pricing, and becomes a productized deliverable you can sell to every client.
**If you buy & sell companies:** a definitive article on you-as-acquirer — thesis, buy box, closed deals, references — is what sellers and brokers find before they reply; that's off-market deal flow. Post-close, write one per acquired brand so its authority survives the transition.
**Your edge:** name the topic where you hold facts no competitor can publish — your deal count, your niche data, your named clients. Write that page before someone adjacent to you does.

## Run on a persistent agent (Fable 5)
- **Loop to done:** outline every question, then loop until none are left unanswered — definitive means nothing left to ask. Walk the anatomy top to bottom: summary, sourced facts, media, FAQ, orbit links.
- **Self-verify:** run the failure modes as a checklist on your own draft — no second post on the topic, no adjective without a number, URL stable, nothing stale.
- **Compound with memory:** check memory and the site for an existing hub FIRST — improve it, never duplicate it — and carry the orbit list forward so every new asset points home.
- **Log the run:** note which questions the inputs couldn't answer — that's next month's capture list for `content-factory`.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- Harry Gold's harryjgold.com started as one Zoom interview — one capture, one canonical hub, everything else orbits it. Dennis's podcast-appearances page runs the same play: 236+ appearances tracked on one URL that every episode links back to.
- George Paladichuk's NaiL AI shows the niche version: own the definitive page on one tight topic — AI for roofing — and the category cites you by default.
- Write for the diligence reader. Facts with sources survive a buyer's scrutiny and an AI's retrieval; adjectives survive neither.
- One URL per task or topic is the backbone of the BlitzMetrics Task Library — and each agent's own documentation is itself a definitive article (see `recursive-self-improvement-qa`).

## Definitive article & pairings
- Reference: https://blitzmetrics.com/definitive-article-guide/ · https://dennisyu.com/podcast-appearances/
- Pairs with: content-factory → **definitive-article-writer** → recursive-self-improvement-qa

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-19-backdated-content-contradiction -->
**July 19, 2026** (from: michaelkrigsman.com QA run (filed into the loop by skill-pack-propagation 2026-07-19))

Never backdate WordPress posts below the visible byline. On the Krigsman build, rendered
byline dates and the WP/schema datePublished diverged on 8 of 16 articles by up to 9
months — a self-contradiction any journalist or Google can see, and an EEAT risk. The
honest scheme: set the visible byline to "Episode NNN, recorded {air date}" and set
datePublished to the REAL publish date. Air date and publish date are different facts;
show both truthfully rather than forcing datePublished to match a backdated byline.

<!-- learning:2026-07-19-repurposed-article-disclosure-sweep -->
**July 19, 2026** (from: michaelkrigsman.com QA run (filed into the loop by skill-pack-propagation 2026-07-19))

When repurposing podcast or show episodes into articles, ALWAYS check each source episode
for an underwriter/sponsor block and mirror that disclosure in the article deck. On the
Krigsman build, 6 of 16 articles covered underwritten episodes with no disclosure —
including 3 underwritten by the exact sponsor (Gartner) the client engagement centers on.
Both the episode page and its /transcript page carry the underwriter block, so check both.
Undisclosed sponsorship in a repurposed piece is an EEAT and trust liability; the fix is a
one-line disclosure in the deck, not a rewrite.

<!-- learning:2026-07-20-a-minus-terminator-and-entity-linking -->
**July 20, 2026** (from: Daniel Goodrich's blog-grader (validated May 28, 2026 on Escape Fitness, grading "per Jennifer rubric") merged into jennifer + the writer chain)

Two rules from the production grader loop, July 20, 2026. First, the A- terminator: A- is the publish bar — when a draft grades A-, it is DONE; never revise past it (an A is reserved for world-class national-publication journalism, and chasing it is how agents fall into infinite revision loops). Revision budgets before human escalation: 3 rounds for a definitive/STRONG piece, 2 for a standard article, 1 for a short post. Second, route every named entity through the Entity Linking Decision Tree: a person in the network links to their personal-brand site; a company in the network links to its site; anything out-of-network — people, tools, concepts — links to the BlitzMetrics article on that topic, else stays plain text; anchor text is 3–6 descriptive words; each entity links on first mention only, never twice. On a personal-brand site write first person in the owner's voice; on a company site write third person — a POV mismatch caps the grade at B.

<!-- learning:2026-07-28-a-number-about-an-artifact-belongs-to-the-artifact -->
**July 28, 2026** (from: skill-pack-propagation daily run, July 28, 2026)

### A number about an artifact belongs to the artifact — derive counts, never type them

Bringing one pack onto the pipeline surfaced the same defect in six places at once, all of them
a human-typed number describing a file:

- the directory advertised **"18 skills"** for downloads that contained 19, **"17 agents"** for
  a 19-agent library, and a card literally named **"Task Library (246 SOPs)"** beside a badge
  reading 247;
- the member library page said **"17 AI agents"** in its hero and **"all ten skills"** in its
  download section — the "ten" had been wrong since the pack passed 10 in early July;
- the pack's own `README.md`, the first file anyone opens, opened with **"Thirteen installable
  agents"** while shipping 16;
- the copy-paste installer prompt members actually paste into Claude listed **10 of 17 agents**,
  so anyone following it hired a team two-thirds the size of the one they downloaded.

None of this was noticed, because nothing compares a sentence to a zip.

**Rules:**

1. **Derive every count at render time from the artifact.** Read the pack's `VERSION.txt`
   (or count its members) and print that. A count in a source file is a claim; a count read
   from the zip is a fact. Use the SAME key (`Skills: N`) in every pack's VERSION.txt so one
   parser serves all of them.
2. **Never bake a number into a label.** "Task Library (246 SOPs)" goes stale on the next run;
   "Task Library" plus a derived badge never does.
3. **Generate the README from the same list that builds the zip.** A README that can disagree
   with its own package eventually will, and it is the first thing the customer reads.
4. **Generate any prompt you ask people to paste.** It is not documentation, it is the product.
5. **Check coverage in BOTH directions.** The library builder validated "every slug in `order`
   exists as a file" and never "every file appears in `order`" — so a new skill got no card, no
   link and no install zip, silently. The gap is always the direction nobody checks.
6. If you must keep a literal, make the run FAIL when it stops matching. A replacement that can
   silently match nothing is not a replacement, it is a wish.

Learned July 28, 2026.

<!-- learning:2026-07-29-a-catalogue-is-not-a-graph -->
**July 29, 2026** (from: SEO-tree link audit across the 13 agent/skill surfaces, July 29, 2026)

### Being listed in the catalogue is not the same as being connected to the tree

Every one of our 13 published agent/skill pages was live, current, and listed on the master
directory. An actual link audit — pull each page's rendered DOM, decode any base64 payload,
extract links to the other twelve — found the graph full of holes:

- `aibuilderspotlight.com/skill-pack` and `dunkerspotlight.com/set-up-claude` linked **nothing
  at all**. Both dead ends.
- `sigrun.com/somba-agents` linked exactly one page — a partner's members' area with no route
  back into the system it belongs to.
- `blitzmetrics.com/task-library-dashboard`, the 239-skill page, linked neither the packs that
  contain those skills nor the agents that run them.
- `localservicespotlight.com/business-authority-pack` linked only its sibling pack — no path up.

None of this was visible in any report, because everything that existed was checked and
everything that was checked was fine. Publishing a page and connecting a page are two different
jobs, and only the first one had an owner.

**Rules:**

1. **Define the link tree in ONE file and render it from there.** Ours is
   `System-Hub/system_tree.py`: every node's rung, its sibling, and the block that draws the
   ladder. A tree that lives in twelve page bodies is twelve chances to drift.
2. **Put the whole ladder on every node with "you are here" marked.** A reader or a crawler
   landing on any leaf should be able to see the entire structure and their position in it
   without a back button. One shared block does this; twelve bespoke "related links" do not.
3. **Link one sibling each, arranged as a closed ring.** Every pack surface reachable from
   every other, and no two pages pointing at each other — reciprocal pairs read as link
   exchange, and a full mesh makes every page look identical.
4. **Verify links in the LIVE DOM, decoding payloads first.** Several of these pages render
   their whole UI from a base64 `data:text/html` iframe. A link check that reads only
   `post_content` sees an empty page and passes it.
5. **A gated page is verified by authenticated read-back, never a public GET.** A public fetch
   of a member-password page returns the password form; asserting against that certifies a
   broken publish as green.
6. **If nothing asserts a relationship, the relationship will rot.** Write the check the same
   day you build the structure — `verify_link_graph.py`, wired into the daily checklist,
   non-zero exit on any orphan, dead end, missing rung or redirect chain.

Learned July 29, 2026.

<!-- learning:2026-07-29-a-plugin-namespace-can-be-blocked-while-wp-v2-is-fine -->
**July 29, 2026** (from: publishing blitzmetrics.com/persistent-agents/, July 29, 2026)

### A plugin's REST namespace can be blocked while wp/v2 works perfectly

Setting the SEO title and meta description on a new blitzmetrics.com article returned **403** on
every POST to `/wp-json/rankmath/v1/updateMeta` and `/updateRedirection` — while POSTs to
`/wp-json/wp/v2/posts/<id>` on the same host, same Application Password, same full browser
header set, returned 200 all day. Probed both ways, JSON body and form-encoded, GET vs POST:
`GET /wp-json/rankmath/v1/` is 200, every POST under it is 403, and the body is the host's own
styled 403 page rather than a WordPress JSON error. That is a WAF rule scoped to a namespace,
not a broken credential and not a capability problem.

The second trap was worse. RankMath does not register `rank_math_title` /
`rank_math_description` with `show_in_rest`, so writing them through wp/v2's `meta` field
returns **HTTP 200 and stores nothing**. Reading the post back with `context=edit` shows `meta:
{}`. A publish job that trusts the 200 reports the SEO as set forever.

**Rules:**

1. **Diagnose a 403 by namespace and method before blaming the credential.** `GET
   /wp-json/<ns>/` plus a no-op POST tells you in two calls whether it is auth, capability, or
   an edge rule. Twelve days were once lost calling a WAF rule a broken app password.
2. **After any meta write, read it back.** If the field comes back empty, the write was
   accepted and discarded. A 200 is a receipt for a request, not evidence of a change.
3. **Know the fallbacks before you need them.** RankMath derives the meta description from the
   post excerpt and the SEO title from the post title when its own fields are empty — both
   writable through plain wp/v2. Setting `excerpt` produced the exact intended
   `<meta name="description">` in the rendered head. Verify in the head, not the API response.
4. **On WP Engine, purge before you verify.** `POST /wp-json/wpe/cache-plugin/v1/clear_all_caches`.
   A page trashed through the API kept returning 200 to an anonymous fetch until the cache was
   cleared, which reads exactly like a failed delete and invites a second, wrong repair.

Learned July 29, 2026.

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

<!-- learning:2026-08-02-a-row-in-a-table-is-not-a-page -->
**August 2, 2026** (from: grokipedia-fleet)

**August 2, 2026** (from: grokipedia-fleet)

We had 24 skills and nowhere to send someone who asked what one of them was.

Each skill existed in three places — a markdown file in the repo, a file inside every pack
zip, and a single row in a table on `/skill-packs/`. All three are real. None of them is a
page. There was no URL for "what is evidence-verification and why would I run it," which
means there was nothing for a search engine to rank, nothing for an AI assistant to cite,
and nothing to link to in a client email.

That is the same mistake we diagnose in clients every week. A capability that exists but has
no citable address does not exist to anything that reads the web.

Fixed by generating one page per skill from the master `.md` files — 24 pages at
`/skills-<slug>/`, each carrying the same five-rung ladder block as the rest of the system
tree, each linking up to the pack directory and across to the Task Library.

Three things worth carrying forward:

**Generate, never hand-write.** The pages are built from the skill files that already exist,
so a skill and its page cannot describe different things. The moment someone edits a page in
wp-admin, the next run overwrites it and nobody finds out for weeks. Say GENERATOR-OWNED in
the file header, and mean it.

**A new tier of pages needs a new line in the verifier, the same day.** Twenty-four pages went
live at once, entirely outside the daily link-graph check. That is precisely how
`aibuilderspotlight.com/skill-pack` linked to nothing for weeks inside green reports. The
verifier now checks that every master skill on disk has a page linked from the directory, and
samples three live pages per run on a rotating index so all of them get covered over time.

**A page tier needs a line in the runner too, or it becomes a slower clock than its source.**
The daily job rewrites the master skill files every morning. Without a regeneration step the
published pages would keep describing whatever the skill said the day they were generated,
while the directory printed a fresh "last updated" date next to them — a stale page wearing a
current timestamp, which is worse than an obviously old one. This is the third time the same
defect has appeared in this system (Dorine's mirror pack, the cloud runtime mirror, now the
skill pages). **Any artifact derived from a source that changes daily needs its own step in
the daily job.** Look for the pattern rather than waiting to be bitten by it a fourth time.

One smaller thing, worth its own note: the page generator imported `propagate_all_packs` just
to read its `MANDATED` list. That module parses `sys.argv` at import time, so the generator's
own argument errors came out under the propagator's name and usage text. **Never import a
module that acts at import time in order to read one constant from it** — parse the constant
out of the source instead.

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
