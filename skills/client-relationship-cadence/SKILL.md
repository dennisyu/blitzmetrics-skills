---
name: client-relationship-cadence
description: The canonical SOP for recurring client-relationship agents that are NOT a scored metrics loop — monthly/weekly jobs whose real work is checking for replies/approvals since last run, doing exactly one safe incremental improvement, and keeping a human relationship warm without spamming it. Use this instead of weekly-brand-maa.md when the entity isn't being scored against a Personal Brand Score or SOW milestones — it's a person or small client you're quietly maintaining momentum with. Each scheduled agent passes a PARAMETERS block and follows this file.
author: Dennis Yu — Local Service Spotlight
references:
  - weekly-brand-maa.md (the sibling SOP for scored metrics-loop agents — use that one instead if the entity has a Personal Brand Score, SOW targets, or a metrics baseline to track)
  - boil-the-ocean.md
  - recursive-self-improvement-qa.md
  - https://blitzmetrics.com/meta-article-prompt/
---

# Client Relationship Cadence — canonical SOP

**Use this when** a scheduled agent's real job is relationship maintenance, not metrics tracking: a monthly brand-refresh check-in on a friend/peer (no scored rubric), or a client project still mid-build where you're waiting on THEM (logins, approvals, content sign-off) between runs. The two current examples are `igor-ivitskiy-monthly-brand-refresh` (monthly relationship refresh + content update) and `junks-above-daily-progress` (weekly client-project cadence pending a handoff meeting) — different cadences, same shape. Never improvise the method — if something's missing, flag it and propose the fix back into this file (see `recursive-self-improvement-qa`).

## PARAMETERS the caller provides
```
entity_name:        # the person or client
context_docs:       # absolute path(s) to read FIRST — canonical brief, project plan, "easy checklist", baseline notes
comms_channels:      # where to check for replies/approvals since last run — email thread id/search terms, Basecamp project + thread URLs
approval_gate:       # what specifically needs their sign-off before it goes live (e.g. "draft posts 498/499", "GoDaddy login", "Instagram photo permission") and what to do the moment each one arrives
safe_increment_policy: # what "one incremental improvement needing no new access" is allowed to touch this run (e.g. repurpose existing public material into a draft post, fix one Yoast title, tidy one QA item) — and what's explicitly off-limits (never enter passwords into a login form, never publish new content without review, never permanently delete data)
notify_rule:         # when to post/reply vs. stay quiet (e.g. "only if something material changed"; "one friendly nudge if no checklist progress in 7+ days AND no nudge sent in the past 14 days")
state_file:          # where the running "state of the project" note lives — update it every run, don't just append noise
voice:               # tone to write in (e.g. entity's own casual voice for client-facing drafts; Dennis's direct voice for outreach email)
```

## STEP 0 — Load context
Read every file in `context_docs` (there is no memory between runs — the docs + the last state note ARE the memory). Read the current `state_file` if it exists to see what happened last run.

## STEP 1 — Check for movement since last run
Search `comms_channels` (Gmail thread, Basecamp project/thread) for anything new: replies, approvals, completed checklist items, sent credentials. For each item found:
- **An approval arrived** → execute exactly what was approved (e.g. publish the specific posts that were greenlit), nothing more.
- **Credentials arrived that violate `safe_increment_policy`** (e.g. a password sent in plain text) → do NOT use them to log in. Flag it to Dennis as top priority instead. Never enter a password into a login form on the entity's behalf.
- **Nothing new** → say so plainly and move to Step 2.

## STEP 2 — One safe increment
Do exactly ONE incremental improvement that fits `safe_increment_policy` and needs no new access — draft-only for anything public-facing unless it was already pre-approved. Prefer real, repurposable material (the entity's own site, public press, existing reviews) over generic filler. Then QA whatever you touched (fetch the live pages, check nav/contact info/schema still parse) before moving on.

## STEP 2.5 — Put the ask where it can be tracked, and OWN the chase

**Standing since August 1, 2026 (Dennis).** *"I want it so there's no follow-up on me."* An ask that lives in an email thread has no owner, no state and no due date — it survives only as long as someone remembers it. Two of these agents had been staging email drafts for months and calling that follow-up. It isn't; it's a notification.

**Every ask goes in the client's Basecamp project as a to-do, assigned to the person who has to do it, including the client.** Not a message, not a bullet in a status post, not an email paragraph. A to-do has an owner and a state; everything else is prose.

- **Give the client access on day one.** A client-visible to-do that the client cannot see is worse than no to-do, because it looks done from the inside. Convention: project named `Google Knowledge Panel: <Name>`, tools = message board + todoset, internal team + the client as a **Client** (not Team), one client-visible list for their asks and one internal list for ours. Basecamp gotchas are in [[basecamp-lexxy-editor-gotcha]] — in particular, client visibility on a message cannot be set until the project actually has a client, so **add the client before you post**.
- **Assign to the real owner, not the nearest human.** Rotating a password on the *client's own site* is the client's to-do, not ops'. A PHP fix is a developer's, not a VA's. Routing work to whoever is closest is how one person becomes the bottleneck for every client.
- **When you must route through ops, make it a routing job, not a research job.** Title it with the verb and the time cost — "Route X to someone with file access (2 min)" — and carry the full spec so the person who receives it needs no context from anyone.
- **Bundle defects by owner, not by discovery date.** Four separate small fixes in one codebase is one trip for one person, not four to-dos on four days.

**Then chase it.** The next run re-reads every open to-do and decides whether reality moved, **by checking the artifact rather than the reply** — an unanswered to-do whose work is visibly done should be closed, not nudged. For what is genuinely still open, post one consolidated comment on the to-do and escalate on a written schedule: run 1 friendly nudge · run 2 nudge naming the cost in their terms · run 3 hand it to the human with the exact ask. **Write the next escalation date into `state_file`** — the next run is a different session with no memory of the promise, so an undated intention is not a mechanism (see the twelve-day Christine gap in [[blocked-work-becomes-muzamil-todo]]).

Escalating to the principal is the *last* rung, not the first. If a run ends with "Dennis needs to chase this," ask first whether an agent could have checked it, an owner could have been named, or a date could have been set instead.

## STEP 3 — Notify per `notify_rule`
Most runs should NOT generate a client-facing message — only post/reply when something material happened (an approval was executed, a real update shipped) or the specific nudge condition in `notify_rule` is met. Silence is a valid, correct outcome for this step; don't manufacture an update to justify the run. Internal-only notes (to Dennis) can be more frequent than client-facing ones.

## STEP 4 — Update state and log
Overwrite/update `state_file` with a short "state of the project" summary: what's approved, what's still pending from the entity, what was shipped this run, what the next milestone is. This is what the NEXT run (and any human who opens the file) reads first — keep it current, not additive noise.

## STEP 5 — Report back
Tell Dennis, concisely: what moved, what you did, what's still waiting on the entity, and anything ambiguous or broken (don't guess silently — flag it). Per the standing continuous-enhancement policy: act first, then inform; never silently change things without reporting exactly what changed.

## NON-NEGOTIABLES
- Never enter a password into any login form, even one the entity sent you directly.
- Never publish new client-facing content without the approval gate being satisfied, unless the run's own policy explicitly pre-approves a category of change.
- Never spam the relationship — an unnecessary update is worse than no update.
- Every fact you report has a verifiable source (a real reply, a real page fetch) — never fabricate progress.

## Currently called by
- `igor-ivitskiy-monthly-brand-refresh` — monthly cadence, comms_channels = Gmail thread `19929d6921b94285`, approval_gate = n/a (BlitzMetrics-owned article, no client sign-off needed, but WP auth is currently broken — see `blitzmetrics-app-password-broken` — use the Chrome+nonce method), safe_increment_policy = append a dated Update section, never rewrite the original narrative.
- `junks-above-daily-progress` — weekly cadence until handoff meeting, comms_channels = Gmail thread "this is Dennis Yu" with uhhroland@gmail.com + Basecamp project 47842096, approval_gate = the "Easy Checklist for Roland" items (hosting login, admin-email confirm, Google access, Instagram permission, public email confirm) plus the two draft posts (498/499), safe_increment_policy = one repurposed draft or one QA fix per run, no visual overhaul, no publishing without Roland's OK, never enter his GoDaddy password.

## See also
`weekly-brand-maa.md` (the scored-metrics sibling SOP) · `boil-the-ocean.md` (operating principles) · `recursive-self-improvement-qa.md` (loop this run before moving on — propose fixes back into this file when you had to guess)

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-27-dont-retro-charge-silence-when-bootstrapping-a-ledger -->
**July 27, 2026** (from: cxotalk-weekly-maa run)

### Bootstrapping an ASK-LEDGER retroactively: don't retro-charge silence

STEP 6.7 has required `ASK-LEDGER.md` since July 24, 2026, but this client's ledger didn't
exist and had to be back-filled from three prior reports. Two judgment calls keep a
back-filled counter honest, and should be the default whenever a ledger is created late:

1. **Start counting at the first run that had the SOP's discipline available**, not at the
   ask's original date. Charging someone four misses for a period when nobody was tracking
   misses produces a number that feels like an accusation and can't be defended.
2. **Collapse bunched runs into one window.** This task fired 7/17, 7/19 and 7/20 — three
   times in four days. Counting each as a separate miss would have put a client at Rung 4
   ("recommend off-channel contact") for going quiet over a weekend. One window, one count.

The payoff of doing it honestly: the finished ledger showed that **two of the three
highest-count asks were ours or ops', not the client's** — the delivery-channel param and a
GA4/GSC request nobody had chased. A ledger that inflates client counts hides our own drift.
Learned July 27, 2026.

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

<!-- learning:2026-08-01-asks-belong-in-a-tracker-with-an-owner -->
**August 1, 2026** (from: igor-ivitskiy-monthly-brand-refresh)

**An ask staged in an email draft is a notification, not follow-up. Put it in the tracker, assign an owner, and chase it yourself.**

Dennis, August 1, 2026: *"I want it so there's no follow-up on me... all the operations and
follow-up and messaging and communication should be handled by agents."* The Igor run had done
what these agents always did — staged a beautiful Gmail draft carrying three client asks — and
that pattern quietly makes the principal the routing layer for every client.

Rules to adopt:

1. **Every ask becomes a to-do with an owner**, in the client's project. Prose in a message,
   a bullet in a status post, or a paragraph in an email all share the same defect: no owner,
   no state, no date. Only a to-do can be closed.
2. **Invite the client before you write to them.** A client-visible list the client cannot
   reach looks complete from the inside — the worst failure mode, because it reports green.
   On Basecamp, client visibility on a message literally cannot be toggled until the project
   has a client, so the order is: enable clients → add them → post → flip visibility.
3. **Assign to the true owner, not the nearest human.** Rotating a password on the *client's
   own* site is the client's job. A PHP fix is a developer's, not a VA's. Defaulting to
   "assign it to ops" is exactly how one person becomes everyone's bottleneck — the thing
   this rule exists to prevent.
4. **Where routing through ops is unavoidable, ship a routing job, not a research job.** Put
   the verb and the time cost in the title ("Route X to someone with file access — 2 min") and
   carry the whole spec, so the receiver needs no context from anyone.
5. **Bundle by owner, not by discovery date.** Four defects in one codebase is one trip.
6. **Chase by checking the artifact, not the reply.** Next run, re-read every open to-do and
   verify against reality — did the page change, did the score move — then close what is done
   and escalate what is not, on a date written into the state file. The next run has no memory
   of your intention; only the date survives.

<!-- learning:2026-08-02-automate-for-the-cohort-not-the-pilot -->
**August 2, 2026** (from: somba-skill-weekly-update)

**August 2, 2026** (from: somba-skill-weekly-update)

We had automated weekly delivery for one member out of roughly a hundred, and left the other
ninety-nine on a hand-written page that had not been updated in two weeks.

Dorine Holman was an early pilot. Building her a personal mirror folder, a personal checker
script, a line in the propagator, and a dedicated Monday job was the right way to prove the
idea worked. What went wrong is that it stayed that way after it worked. An audit found her
folder holds **21 skill files, every one byte-identical** to the shared source — a full private
copy of something everybody already receives.

Meanwhile the surface all 100 members actually read carried news items typed by hand into
`patch_news.py`, with a hard-coded date string frozen at 20 Jul. So the effort was exactly
inverted: **automated and current for one person, manual and stale for everyone.**

Dennis's question was the right one — "are we doing something special for her? We should do
things in a central, solvable way and less one-offs." The rewrite serves everyone through the
dashboard and Agent Library they already have. Same work, roughly a hundred times the audience.

Three things to carry forward:

**A pilot has an exit condition, and it should be written down when the pilot starts.** "Prove
it with one member, then generalise" is a good plan. "Prove it with one member" alone becomes
permanent infrastructure with an audience of one, and nobody notices because it keeps working.
When you build for a single person to test something, write the graduation step into the job
itself.

**Count the audience of every automation you own.** If a scheduled job serves one member of a
cohort, that is either a deliberate bespoke engagement or an un-generalised pilot. Both are
fine; not knowing which is not. The tell here was cheap: one folder, 21 identical files.

**Check the direction of the asymmetry.** The individual got the generated, always-current
version and the group got the hand-maintained one. That is worth looking for elsewhere — the
effort usually flows to whoever asked most recently, not to wherever it does the most good.

Guard added: the rewritten job now says plainly that if something is worth telling one member it
is worth telling all of them, and that no member-specific branch may be added to the pipeline.
The one-off that remains — Dorine's mirror folder — is left in place on purpose, because
deleting a real person's synced files is a decision for a human, not a cleanup. But it is
frozen: not extended, and no second member's mirror gets created beside it.
