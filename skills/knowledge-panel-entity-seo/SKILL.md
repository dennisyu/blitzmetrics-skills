---
name: knowledge-panel-entity-seo
description: Run the plumbing that earns a Google Knowledge Panel — entity-clarity audit, Person schema JSON-LD with sameAs, ranked third-party corroboration, entity-collision fixes, and the KGMID claim in Search Console. Use to become the one person Google recognizes for your name and topic.
---

# Knowledge Panel / Entity SEO

**Use this when** your entity home is live and you want the box on the right of Google — plus the entity clarity underneath it that makes Google and every AI resolve you as one clear person. Step 5 of the Local Service Spotlight method.

## Inputs
- Your live entity home (yourname.com) and every profile URL you own.
- Scored proof from `positive-mentions-harvester`: press, podcasts, speaking, Wikidata candidates.
- The exact name, role, company, and primary topic locked in `personal-brand-strategist`.
- Government ID and access to your profiles — you'll need both for the claim.

## Steps
1. **Entity-clarity audit.** Search your name. Are your name, role, company, and topic identical on your site, LinkedIn, X, YouTube, podcast bios, and event pages — same headshot everywhere? List every mismatch: old titles, name variants, stray photos.
2. **Fix entity collision.** Share a name with anyone Google knows? Disambiguate: middle initial, "[Name], [Company]" phrasing, your differentiating topic in every bio. Google won't award a Panel to a name it can't resolve to one person.
3. **Person schema.** Write JSON-LD for the site head — your entity home as canonical, `sameAs` to every verified profile:

   ```json
   { "@context": "https://schema.org", "@type": "Person",
     "name": "", "jobTitle": "", "worksFor": { "@type": "Organization", "name": "" },
     "url": "https://yourname.com", "image": "",
     "sameAs": ["<LinkedIn>", "<X>", "<YouTube>", "<press/podcast profiles>"] }
   ```

4. **Build corroboration** down the signal stack below — every independent source that repeats the same facts raises Google's confidence score in you as an entity.
5. **Find the KGMID and claim.** Search your name; when a Panel appears, the share link carries your `kgmid`. Click "Claim this knowledge panel," verify through a connected profile, write a plain explanation of who you are, submit via Search Console with ID and proof. Decision typically 2–7 days.
6. **Re-audit monthly.** New mentions are new corroboration; stale titles are drift.

## Signal stack (pursue in this order)
1. Press in recognized outlets — highest authority per unit of effort.
2. Podcasts and YouTube shows with existing authority — lighthouse interviews count double.
3. Speaker pages at named events — the event's site corroborates you.
4. Wikidata entry with sourced statements — feeds the Knowledge Graph directly.
5. Association and directory profiles carrying your exact one-line bio.

## Output
- Mismatch list with exact fixes, paste-ready Person schema, ranked corroboration hit-list, and the step-by-step KGMID claim checklist.

## For DealCon — agency owners & acquirers
**If you run an agency:** the Panel is what a premium prospect sees before your first call — you stop being one vendor in a spreadsheet and become the obvious authority, which is pricing power.
**If you buy & sell companies:** a stranger-seller Googles you the night they decide which buyer to call back. A Panel with your face, role, and press wins that moment.
**Your edge:** put your differentiating topic in every bio Google reads — the Panel should say the thing only you can claim, not just a job title.

## Run on a persistent agent (Fable 5)
- **Loop to done:** loop the entity-clarity audit until the mismatch list hits zero — every profile, same name, same headshot, same one-line title — and the schema validates. A Panel is won by signals agreeing everywhere, so "most profiles fixed" is not done.
- **Self-verify:** re-search the name after every fix batch and confirm the change actually propagated before crossing it off.
- **Compound with memory:** the claim takes weeks of compounding corroboration — exactly what a persistent agent is for. Track the hit-list, KGMID status, and each month's re-audit in memory so no signal gets lost or rebuilt.
- **Log the run:** date every corroboration won — the dated trail is your evidence pack for the claim itself.

See `boil-the-ocean.md` for the full operating principles.

## Notes — Dennis's method
- This is **plumbing, not magic**. Dennis was a search engineer at Yahoo; Google resolves entities the same way — one clear identity, many independent sources agreeing.
- Consistency is the cheap win: same name, same headshot, same one-line title, everywhere. Do it before chasing press, not after.
- In 2025, Google Search Profiles require 100k followers (300k TikTok-only) **or** a Knowledge Panel. The Panel is the deal-maker's way in — authority without becoming an influencer.
- Corroboration beats volume: one talk at a named event outweighs fifty self-published posts.
- Entity collision is the silent killer for common names. Disambiguate first, or every signal you build splits between two people.
- A Panel is never "done" — Google rebuilds it from the graph continuously. Keep the sources consistent and it keeps getting richer.

## Definitive article & pairings
- Reference: https://blitzmetrics.com/knowledge-panel/ · https://blitzmetrics.com/googles-knowledge-graph/ · https://blitzmetrics.com/google-knowledge-graph-confidence-score/
- Pairs with: → ai-search-visibility → dollar-a-day-strategist

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

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

<!-- learning:2026-08-01-admin-form-save-is-not-a-save -->
**August 1, 2026** (from: igor-ivitskiy-monthly-brand-refresh)

**A WordPress admin form that returns "Post updated" has not necessarily saved your fields — re-read them.**

Creating a KG Entity record on blitzmetrics.com, the run set 7 ACF fields via JS, clicked
Publish, and got a clean `Post updated.` notice with a real post ID. Every text, url and
textarea field had silently discarded its value. Only the `true_false` toggles persisted.
Had the run trusted the success notice, it would have reported a populated registry entry
that was in fact blank — the same failure the other 34 records in that registry already had.

Adopt as standing practice:

1. **After any admin-form write, re-read the field values from the reloaded form** (or the
   public render), never the success notice. `Post updated`, HTTP 200 and a returned post ID
   all describe the *request*, not the *data*. Same rule as `DELETE /elementor/v1/cache`
   returning 200 while the page still serves stale HTML.
2. **When one field type saves and another does not, suspect the field-key contract, not
   your input.** ACF resolves values by field key and requires keys prefixed `field_`. A
   locally-registered group using bare names (`data-key="kgmid"`) fails `acf_update_value()`
   for value-bearing types. Read `data-key` on `.acf-field` before blaming the form fill.
3. **A silent write failure that predates you is a finding, not a footnote.** The empty
   fields explained why 32 of 35 entity records were blank — a registry that had looked
   populated because rows existed. Count the rows that carry *data*, not the rows.
4. **Publish the defect in the meta article.** It converts a blocked task into the most
   useful paragraph on the page, and it is how the next person finds the one-line fix.

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
