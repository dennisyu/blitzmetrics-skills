---
name: weekly-brand-maa
description: The canonical weekly MAA (Metrics → Analysis → Action) SOP every per-client brand agent runs. One source of truth for the MAA discipline, the Personal Brand Score, safe site-update policy, and delivery format. Each scheduled agent passes a PARAMETERS block and follows this file. Improve the method here once and every agent inherits it.
author: Dennis Yu — Local Service Spotlight
references:
  - TaskLibrary/skills/strategy-measurement/maa-cycle-metrics-analysis-action.md
  - TaskLibrary/skills/strategy-measurement/submit-weekly-maa-report-every-friday.md
  - https://blitzmetrics.com/maa/
  - https://blitzmetrics.com/personal-brand-score/
---

# Weekly Brand MAA — canonical SOP

**Use this when** a scheduled per-client agent runs its weekly report. The calling task supplies a PARAMETERS block; you execute the steps below using those parameters. This file is the single source of truth for the MAA discipline so the per-client agents stay thin and consistent. Never improvise the method — deviations are data; if something's missing, flag it and (per `recursive-self-improvement-qa`) propose the fix back into this file.

## PARAMETERS the caller provides
```
entity_name:        # e.g. "Trenton Sandler"  | or a roster file for agency mode
mode:               # personal-brand | agency-roster
depth:              # full | tracker-lite
canonical_brief:    # absolute path to the verified-facts brief (read FIRST). For agency-roster: the roster YAML.
domains:            # entity-home + owned domains (Ahrefs target; mode=subdomains)
handles:            # social handles to read live (YouTube/IG/TikTok/X/LinkedIn)
gsc_property:       # GSC URL-prefix property if verified (authoritative search signal)
baseline_path:      # prior snapshots/reports dir for week-over-week + vs-baseline deltas
site_update_policy: # additive-auto | stage-only | none
brand_score:        # on | off
delivery:           # basecamp_url | gmail_draft:<addr> | file_only   (always ALSO save a file copy)
report_dir:         # where to save the dated report + log
extra_steps:        # optional entity-unique steps (e.g. disavow append, content repurposing, target-keyword list)
escalate_rule:      # optional — a plain-language watch condition + what counts as "escalate" (e.g. "if organic traffic declines 3 consecutive weekly checks, say so explicitly to Dennis at the top of the report, don't bury it in Analysis")
context_channels:   # optional — other threads/boards to read for context before writing the report (e.g. a partner team's own Basecamp thread or weekly report), when the entity has its own people/agents also reporting
```

All 7 personal-brand/agency-roster client agents below call this file rather than re-deriving the loop. Ahrefs MCP tools referenced throughout are server `mcp__ea56e910-0a35-4107-aeee-16d873278687__*` (load via ToolSearch on first use each run).

## Currently called by (update this list when you retrofit or retire a caller)
- `trenton-sandler-weekly-maa` — mode=personal-brand, depth=full, site_update_policy=additive-auto, escalate_rule set. **Cadence changed weekly → twice monthly (1st + 15th) on 2026-07-31 per Dennis** (the task ID still says "weekly"; renaming it would break its run history, so the ID is now cosmetic — same situation as cxotalk's `delivery` param above).
- `cxotalk-weekly-maa` — mode=personal-brand, depth=tracker-lite (SOW-milestone framing instead of brand_score); client comms live in Basecamp bucket 48001656 / message 10075591082 (client-visible), redirected there by ops 7/17. **Resolved 7/27:** the `delivery` param still literally says `gmail_draft:mkrigsman@cxotalk.com`, but STEP 6.6 makes the weekly Basecamp post happen regardless, so the param is now cosmetic — the run posts to Basecamp and stages the internal Gmail draft to Dennis. Updating the param only removes a standing deviation note.
- `kingdom-broker-friday-maa` — mode=agency-roster (multi-client CRM/GBP/ads roster)
- `family-law-leaderboard-weekly-checkin` — mode=personal-brand, depth=tracker-lite, escalate_rule + context_channels set (reads the implementing team's own Basecamp thread)
- `anthony-hilb-seo-tracker` — mode=personal-brand, depth=tracker-lite, brand_score=off
- `wtp-monthly-seo-reaudit` — mode=personal-brand, depth=tracker-lite, brand_score=off, site_update_policy=none
- `somba-weekly-maa` — mode=personal-brand (agency-roster-flavored: one call fans out to ~78 members), delivery is bespoke (Elementor dashboard blob, not Basecamp/Gmail) — this file supplies the MAA/Funnel *methodology* only; see `somba-weekly-maa`'s own SKILL.md for the Sigrun-specific publish mechanics, which are legitimately unique and should stay there.

Two more client cadence agents (`igor-ivitskiy-monthly-brand-refresh`, `junks-above-daily-progress`) are a different shape — relationship-maintenance + approval-gated site work, not a scored metrics loop — and call `client-relationship-cadence.md` instead. Don't force them onto this file; see that SOP.

## STEP 0 — Load context
Read `canonical_brief` (verified facts, IDs, handles, publish recipe) and the newest file in `baseline_path` (last week's numbers). If you discover a NEW verified fact, update the brief. There is no memory between runs — the brief + last report ARE the memory.
- **If `baseline_path` is empty (first run):** check whether the calling task's `extra_steps` embeds an original baseline (numbers gathered when the account was first audited/onboarded, before this scheduled agent existed) — use that as the week-over-week comparison point instead of skipping deltas. Say explicitly in the report that this is the first tracked run and that it becomes the new baseline going forward.
- **Duplicate/same-day re-trigger guard:** if `report_dir` already contains a report dated TODAY, this is a re-trigger (manual "Run now", permission pre-approval click, or scheduler hiccup) — do NOT re-run the metrics loop and NEVER deliver twice. Instead: verify the earlier run completed every step (report file, log line, brief update, and the draft/post — confirm the draft is still DRAFT, or was legitimately sent by Dennis; check the thread for client replies while you're there), fix only what's genuinely missing, append anything new as a dated addendum to today's report, and stop. A duplicate client-facing send is worse than a skipped run. (Added 2026-07-17 after the cxotalk evening re-trigger — the verify path also caught the client's same-day reply and a channel-change instruction that would otherwise have waited a week.)

## STEP 1 — METRICS (business first, then diagnostics)
Pull only what the parameters enable; note any source that's unavailable rather than guessing.
- **Audience (live):** read current follower/subscriber counts for each handle (Chrome JS from page data; Google snippet if walled). Record values + week-over-week deltas.
- **Authority/SEO (Ahrefs MCP, target = domains, mode=subdomains, today):** domain-rating, site-explorer-metrics (org_keywords, org_traffic), top-pages, backlinks-stats, referring-domains (flag NEW domains; legit vs spam). Site Explorer's `date` param rejects future/today's dates on some plans — if you get `"bad date"`, step back 1-2 days until it resolves.
- **Brand Radar / AI-citation tools specifically:** these need either a saved `report_id` (a Brand Radar project already configured in the Ahrefs dashboard) or `prompts: "ahrefs"` premade prompts — and even then, each `data_source` (chatgpt, google_ai_overviews, grok, etc.) is a separate paid add-on that hard-errors (`Missing addon: Brand Radar [...]`) rather than degrading gracefully if the workspace's plan doesn't include it. Before spending calls on Brand Radar, call `subscription-info-limits-and-usage` (free, no units) to check the plan tier. If the addon's missing, don't retry with different data_source combos — note the gap plainly (per Step 6.5) and move on.
- **Fetching BlitzMetrics-fleet or other Cloudflare-protected client sites:** raw `curl`/bash fetches return bot-challenge 403s ("Just a moment...") even for plain static pages like sitemaps. Default straight to Chrome MCP (`navigate` + `get_page_text`, or `browser_batch`) for any client-site check — don't burn a round-trip discovering the 403 first.
- **Search Console (AUTHORITATIVE when gsc_property set):** clicks, impressions, avg CTR, avg position, top queries + top pages (last 28 days, W-o-W). Use as the primary search-presence signal; fall back to Ahrefs estimates only if GSC isn't reachable.
- **Agency-roster mode also pulls business outcomes**, per client, comparing the prior 7 days vs. the 7 before that: GA4/Google Ads/CallRail via the Windsor.ai MCP (sessions by channel, conversions, top landing pages, booked-call count by source, ad spend + conversions); GBP rank grid via the Local Falcon MCP (grid average rank, % top 3, % top 10, best/worst points) if a campaign_id is configured; CRM jobs via whatever `crm.access_method` the roster specifies (`api` = call it directly, `csv` = read the newest file in the configured dropbox path, `chrome` = log in via Claude in Chrome and pull the last-7-days report, `unknown` = skip and flag, ask Dennis to confirm). Skip+flag any connector that isn't installed or configured — never abort the whole run over one missing source; note it as an explicit action item ("Connect X — Dennis, by next Friday").
- **New results/press + Brand SERP:** new mentions (past week), new content the entity published, and whether a Knowledge Panel renders and the entity-home ranks for the entity's name.
- **If `context_channels` is set:** before writing Analysis, read those threads/boards too (e.g. a partner team's own weekly report or Basecamp thread) so you're reacting to what they already said, not duplicating or contradicting it.

## STEP 2 — ANALYSIS (the "why" — 10x more important than metrics)
For each meaningful change, explain WHY, tied to the entity's goals (own the entity, trigger a Knowledge Panel, grow audience, monetize). Never optimize to a single metric — name the counterbalancing metric (publishing volume vs. indexation; followers vs. owned traffic). In agency-roster mode, correlate digital cause to business outcome in dollars ("calls down 18% because the Plano page fell #4→#9 after the core update ≈ 6 lost jobs at $X = $Y"). If nothing moved, explain what's gating it. If the data looks wrong, say so — don't smooth it over.
- **If `escalate_rule` is set:** check it explicitly every run (e.g. "organic traffic down 3 consecutive weekly checks"). If it trips, put the escalation as the FIRST line of the report, addressed to Dennis by name, not folded into the middle of Analysis — the whole point of the rule is that it doesn't get missed.

## STEP 3 — ACTION (2–3 specific, assigned, due-dated items for next week)
Concrete and verifiable, each with an owner and a due day. Prefer "publish the rewritten /ac-repair-plano/ page by Tue — Eric" over "improve SEO." Tie every action to a goal from Step 2.

## STEP 4 — SAFE SITE UPDATES (governed by site_update_policy)
- `additive-auto`: if logged in (check /wp-admin first; fleet WAF blocks Basic Auth → use cookie + X-WP-Nonce from window.wpApiSettings.nonce), apply low-risk additive updates only: add a new legit mention to /media/ + Person sameAs; refresh stats; publish a substantive repurposed SEO article (entity as author, verified content only, link to source, internal-link the cluster); set Rank Math title/desc where missing. Validate render after.
- `stage-only`: write the changes as drafts/to-dos in `report_dir`; note that a wp-admin login is needed.
- `none`: skip (tracker-lite).
- Structural changes (layout/nav/schema overhaul): ALWAYS stage for human review, never auto-apply.
- New spam backlinks: append to the entity's disavow.txt if `extra_steps` names one.

## STEP 5 — PERSONAL BRAND SCORE (when brand_score = on)
Re-score the 100-pt rubric: Entity Home 20, Knowledge Panel 15, Search Presence 15, Content 15, Audience 15, Schema 10, Social 10 (https://blitzmetrics.com/personal-brand-score/). Show total + per-component vs last week.

## STEP 6 — DELIVER
1. Save the report to `report_dir`/MAA-YYYY-MM-DD.md and append a one-line entry to MAA-LOG.md (create if missing). ALWAYS keep the file copy regardless of channel.
2. Deliver per `delivery`: post to the Basecamp thread via Claude in Chrome (Dennis stays logged in; verify the post appeared) OR create a Gmail draft to the given address OR file_only. If a Basecamp URL is configured but unreachable, fall back to a Gmail draft and note it.
   - **Basecamp two-thread rule (added 2026-07-19, Dennis's explicit instruction):** most client projects have both a client-visible thread and a separate internal-only "Updates" thread. Default to internal. Only post to the client-visible thread when the update is genuinely interesting/noteworthy to the client (a real win or milestone) — routine no-change verification passes, internal process/incident notes, and anything with internal-only commentary always go to the internal thread, never client-visible. Confirm which kind of thread you're looking at via Basecamp's "The client can see this" banner, don't assume from the thread name.
   - **Gmail-draft delivery is DRAFT-ONLY, always — no exceptions.** Use the draft-creation tool; never a send-message tool. This applies even when the configured recipient is Dennis himself — a scheduled/autonomous run never has standing to put a message in someone's inbox unreviewed. Before marking this step done, re-fetch the message (search_threads/list_drafts/get_message) and confirm its label is DRAFT, not SENT, and that the To: field matches the `delivery` parameter's address exactly. Pulling the entity's own contact info (athlete/client personal email) out of the canonical brief instead of the configured fallback address is a real, observed failure mode (2026-07-17, Trenton Sandler run: a report meant for `gmail_draft:dennis@blitzmetrics.com` was instead fully SENT to the athlete's personal address + a teammate, skipping Dennis's review entirely) — not a hypothetical one. If you ever discover a prior run sent instead of drafted, do not attempt to unsend or delete it; flag it plainly at the top of the next report and let Dennis decide on any follow-up.
   - **Agency-roster mode:** deliver per-client (one Basecamp post per client with a `basecamp.project_url` configured; skip+flag clients without one) AND always send one combined summary email to YOUR OWN inbox (the owner address configured for this agent — this skill ships in public packs, so it must never carry someone else's address) with one bullet per client — headline metric delta, biggest action, link to that client's Basecamp post or a note that posting was skipped. Never put internal-only figures (EBITDA, valuation, exit plans) in a client-facing Basecamp post — those stay in the Dennis-only summary email.
3. Keep it tight: lead with business metrics + the 2–3 actions; diagnostics below. Plain English, encouraging, honest. Client-facing posts never include internal commentary (EBITDA, valuation, exit) — that goes only to Dennis.
4. Run `extra_steps` (entity-unique work like content repurposing) where provided.
5. If a connector or login needed this run isn't working, don't retry in bursts (WAF risk) — save what you have, note the gap plainly in the report, and say what Dennis needs to do to unblock next run.

## REPORT FORMAT (personal-brand)
```
{ENTITY} — WEEKLY MAA REPORT — {date}
★ Personal Brand Score: {n}/100 ({Δ})       (omit if brand_score off)
METRICS: {audience w/ deltas} | DR {dr}; keywords {kw}; organic traffic {t}; new backlinks {legit}/{spam}; new mentions {list}; new content {list}; Brand SERP {KP? ranks for name?}.
ANALYSIS: {why, tied to goals; counterbalancing metric}.
ACTION: 1) … 2) … 3) …
WHAT WE DID: {updates/articles/disavow}.
WHAT WE NEED FROM {ENTITY}: {footage, login, approval}.
```
Agency-roster mode uses the METRICS → ANALYSIS → ACTIONS sections per client (top-of-funnel + bottom-of-funnel + leading indicators), 500–800 words each, Basecamp-ready.

## STEP 6.6 — DELIVERY IS NOT OPTIONAL (added 2026-07-24, Dennis's explicit instruction)

"Update Basecamp every week with what's going on without needing me to initiate." A run that gathered
perfect metrics and didn't land in the channel is a failed run. Three rules make delivery self-healing:

1. **Post-always.** The weekly post goes up whether or not anything changed, whether or not the client
   replied, whether or not the news is good. "Nothing moved and here's why" IS the update — silence from
   our side is indistinguishable from a dead agent, which is exactly the failure the client just had.
2. **Verify, then trust nothing.** After posting, re-fetch the thread and confirm your comment is present
   server-side (fresh navigation, not the optimistic in-page render). Only then mark delivery done.
   **Degradation banners can be stale** — Basecamp rendered a "database is in read-only mode" banner on
   2026-07-24 while the status page read all-operational and the post in fact succeeded. Never let a
   banner alone stop you: check the vendor status page, then ATTEMPT the post and let the attempt be the
   verdict. Only a failed attempt is a real outage.
3. **Queue, never drop.** If the post genuinely fails, write the exact post body to
   `report_dir`/UNPOSTED/YYYY-MM-DD.md, note the failure in the report, and send the Gmail draft fallback.
   **At STEP 0 of every subsequent run, check UNPOSTED/ first** — if anything is queued, post it (labeled
   with its original date) before the current week's report, then delete the queued file. A skipped post
   must resurface by itself; it may never depend on a human remembering.

Also: **re-confirm the destination every run.** Ops rotates Basecamp threads (`Updates (Continuation-N)` →
`N+1`) with only a pointer comment. Before posting, verify the configured thread is still the active one and
that its "The client can see this" banner matches the intended audience — visibility does not carry over to
the successor thread. If the thread moved, post to the new one and record the new bucket/message ID in the
report so the next run inherits it.

## STEP 6.7 — TRACK UNANSWERED ASKS WITH A COUNTER (added 2026-07-24)

When a client or partner goes quiet, the failure mode is that an ask gets re-asked politely forever and
nobody notices it's been dead for a month. Maintain `report_dir`/ASK-LEDGER.md: one row per open ask with
owner, first-asked date, a **miss counter**, last status, and what it gates. Read it at STEP 0, rewrite it
at STEP 6, and append a one-line counter history entry per run (never rewrite history).

Classify each ask every run as ANSWERED / PARTIAL / SILENT — PARTIAL and SILENT both increment. Then apply
the ladder automatically, naming the rung in the report: **1–2 misses** restate in one line · **3 misses**
name it as overdue with the count visible plus a yes/no for Dennis offering to route around the blocked
person · **4 misses** top of the report, addressed to Dennis by name, recommend off-channel contact or
reassignment with a specific workaround · **5+ misses** declare the channel dead for that ask, stop
re-asking, state the assumption you're proceeding under, execute the workaround, log it.

Two fairness rules that keep the counts credible: never inflate a count, and when someone partially
delivers, say what they DID deliver in the same breath as the count. The counter is there to make drift
visible, not to build a case against anyone.

**Third rule, added 2026-08-01 — the "route around" rung has a hard exception: never route around your
contact into their own relationships.** The ladder's rungs 3–4 offer to bypass a blocked person. That is
correct when the blockage is organizational (a vendor, a shared inbox, an unstaffed queue) and wrong when
the blocked person's relationship IS the asset — a family member, their boss, their client, their
co-founder. Going directly to that person to save a week costs your contact standing on their own project,
permanently, in exchange for a scheduling win. It also reads as going over their head, because it is.
Where the ask can only be closed through your contact, the escalation path is: restate briefly → offer
concrete help that removes the work from them (draft it, run it, pre-fill it, do the pull yourself) →
ask the principal to reach them directly, off-channel. Then proceed on a stated assumption. Encode the
specific off-limits relationships in the calling task's parameters so the ladder cannot re-derive the
mistake next week — an agent that fires the same wrong rung every Friday is worse than one that never
escalates. (Learned when this file's own ladder told the family-law agent to book a meeting with the
implementer's father directly; Dennis countermanded it, the agent retracted it publicly in the client
thread the same night, and the guardrail is now in that task's parameters.)

## NON-NEGOTIABLES
- Metrics → Analysis → Action, in that order, every time. Analysis and Action are the value.
- Deliver every week, unprompted, and verify the post landed. A report nobody received didn't happen.
- Business outcomes beat vanity metrics. Every number cited has a verifiable source; estimated/missing data is labeled as such. Never fabricate.
- Posts read like Dennis wrote them — direct, confident, honest about what worked and what didn't.
- Self-improve: if you had to guess, the instruction was missing — note it for this file (see `recursive-self-improvement-qa`).

## See also
- `recursive-self-improvement-qa.md` (loop this run before moving on) · `boil-the-ocean.md` (operating principles)
- `dollar-a-day-strategist.md` — for ad-amplification reports (e.g. the NaiL dollar-a-day update), which are NOT MAA reports and should use that skill instead.

## Learned in the field

*Appended automatically by the self-improvement loop (Skill-Learnings/): dated lessons from real runs. Newest at the bottom.*

<!-- learning:2026-07-19-transcript-quote-verification -->
**July 19, 2026** (from: michaelkrigsman.com QA run (filed into the loop by skill-pack-propagation 2026-07-19))

Verify verbatim quotes at scale without blowing context: navigate Chrome to the source
transcript page, then match IN-PAGE via javascript_tool. Normalize both sides (lowercase,
curly to straight apostrophes, strip punctuation, collapse whitespace), test full-quote
containment, else slide an 8-word shingle window. Return one letter per quote (E = exact,
P = partial, M = missing). This verified 148 quotes across 16 client-rendered pages for
near-zero context cost. Partials are usually disfluency cleanups — pull plus/minus 300
characters around an anchor phrase to adjudicate before ever calling something a misquote.

<!-- learning:2026-07-20-ai-citations-on-lite -->
**July 20, 2026** (from: cxotalk-weekly-maa run)

Four lessons. (1) `site-explorer-ai-responses-count` WORKS on the Ahrefs Lite plan and returns
per-engine AI citation counts (select all 8 fields: chatgpt, copilot, gemini, google_ai_mode,
google_ai_overviews, google_ai_overviews_keywords, grok, perplexity) — a Brand-Radar-blocked run
can still report the AI-citation KPI as citation counts; label the method (it cannot see unlinked
mentions, share-of-voice, or verbatim answers). (2) Before declaring a metric blocked or
re-deriving it, check sibling scheduled tasks' outputs — the weekly GEO-Citation-Tracking digest
(emailed to Dennis, `GEO-Citation-Tracking/digests/`) already tracks per-engine citations for the
client roster; cross-reference it, don't duplicate the pulls. (3) When a traffic estimate jumps
implausibly, re-pull the PRIOR data date with today's exact config to rule out config drift, then
diff top-traffic keywords to find the driver — one run's "doubling" was a single novelty keyword,
correctly reported as noise, not growth. (4) An early trigger <7 days after the last report (but
not same-day) is a delta run: keep metrics brief and honest about the short window, spend the run
on relationship/context checks (threads move daily; rankings don't), and never send the client a
second report inside the window.

<!-- learning:2026-07-20-fleet-audit-server-side-proof-paths -->
**July 20, 2026** (from: Weekly fleet-hub-audit run — first run to populate money_hits (Ahrefs organic-keywords vs GCT money_queries, 12 confirmed sites, ~640 units) and to probe the Ahrefs GSC endpoints as a browser-free GSC path)

Two proof-collection upgrades for recurring audit runs. First, money_hits is cheap and worth running every time: one site-explorer-organic-keywords call per confirmed-GCT site (select keyword,best_position; where best_position lte 50; limit 100) costs ~50 units/site and turns "does this site rank for what its owner sells" into a number the impact score consumes (+5/hit, cap 15) — match money queries to ranking keywords by normalized substring in either direction, count each query once. Second, GSC does NOT have to be a browser step: the Ahrefs MCP exposes gsc-keywords/gsc-performance-history keyed by Ahrefs project_id, so any fleet domain added as a project in the Ahrefs workspace with GSC connected becomes pullable server-side at 4am with no Chrome leg. As of July 20, 2026 the workspace's 9 projects contain zero fleet personal-brand domains — adding the GSC-verified fleet domains (dennisyu.com, markosipila.com, piotrzawislak.com, trentonsandler.com, etc.) as Ahrefs projects is the unlock; until then missing GSC renders as "enrich" actions by design, not as an error. Learned July 20, 2026.

<!-- learning:2026-07-20-sandbox-mount-deadlock-host-fallback -->
**July 20, 2026** (from: Weekly fleet-hub-audit run — sandbox "Resource deadlock avoided" escalated from writes to READS (couldn't even cat _batch_audit.py), so the whole 24-chunk pipeline ran host-side via Desktop Commander instead)

The sandbox mount lock can escalate beyond single-file writes: a session can lose READ access to mounted project files ("Resource deadlock avoided" on cat/open), which silently no-ops any python script run from the sandbox against those files. When that happens, don't fight it file-by-file — move the WHOLE pipeline host-side (Desktop Commander start_process): macOS python3 runs stdlib-only audit scripts unmodified, and a strictly-sequential `for s in 0 8 … 88; do python3 chunk.py $s 8; done` loop in ONE host process preserves the WAF-safety of one-chunk-per-call while escaping the sandbox's 45s cap entirely. Three host-side gotchas learned the same run: (1) Desktop Commander MCP requests time out around 2 minutes no matter what timeout_ms you pass — never bake `sleep 150+` into a command; do instant file-size polls (`ls -la chunk_* | awk '$5>2'`) or long-poll a running process with read_process_output; (2) heredoc (`python3 - <<'EOF'`) commands are intermittently rejected with "Command not allowed" — keep fallbacks as `python3 -c` one-liners or run reads from the sandbox once the lock clears (it can clear for files the host process rewrites); (3) detached `( … ) &` subshells lose their output when the parent exits — don't use them for polling. Learned July 20, 2026.

<!-- learning:2026-07-20-ahrefs-free-dr-endpoint-auth-deadline -->
**July 20, 2026** (from: anthony-hilb-seo-tracker (weekly-brand-maa) — refiled from a stray root note by skill-pack-propagation on July 21, 2026)

⚠ **DATE CORRECTED 2026-07-27:** the live warning now reads **2026-08-10**, not 2026-08-01 — Ahrefs
pushed the cutoff back by 9 days. Verified on two `public-domain-rating-free` calls this run. Read the
warning text on every call rather than trusting this note; vendors move deprecation dates. Everything
below still applies, with August 10 as the operative date.

Ahrefs' free Domain Rating endpoint stops accepting unauthenticated calls on ~~August 1~~ **August 10**, 2026.
> **⚠ RESOLVED August 3, 2026 — read this first: use `site-explorer-domain-rating`, always.**
> Everything in this section down to "Rules for any skill that pulls Ahrefs Domain Rating" is
> the historical record of a deprecation that no longer needs tracking. Do not act on the dates.

The `public-domain-rating-free` MCP call still returns the normal DR value today but now
carries a deprecation warning: "Unauthenticated access to this endpoint will be removed on
2026-08-10. Requests will require a free API key." Every weekly/monthly tracker that pulls DR
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

<!-- learning:2026-07-24-basecamp-comment-extraction-and-readonly-fallback -->
**July 24, 2026** (from: family-law-leaderboard-weekly-checkin run)

Three Basecamp mechanics for any agent that reads or posts threads. (1) `get_page_text` on a
Basecamp message page returns ONLY the root post — the comments live in
`section.thread--comments article` nodes; extract them via in-page JS, and REDACT URLs/long
tokens before returning text (raw dumps trip the Chrome DLP block — observed on a thread
containing password-reset links; headers-first then per-comment bodies also keeps output under
the tool cap). (2) Basecamp service disruptions render a `system-degradations-banner` section
("database is in read-only mode… can't post new messages") — **but this banner goes stale and lies.**
Same day, hours later, the banner still claimed read-only while 37signals' status page read
"All Systems Operational" and the comment posted successfully on the first try. Corrected rule:
a degradation banner is a hint, never a verdict. Check the vendor status page, then ATTEMPT the
post; only a failed attempt justifies the Gmail-DRAFT fallback + UNPOSTED/ queue (STEP 6.6).
Deferring on the banner alone cost this project a week of client-visible silence.
(3) Threads get rotated: ops closes "Updates (Continuation-N)" with a pointer comment and opens
N+1 — before posting, confirm the ACTIVE thread (the closed one's last comment says "continue
here"), record the new bucket/message id in the report for the next run, and re-check the
"The client can see this" banner on the NEW thread; client-visibility does not carry over.

<!-- learning:2026-07-27-serp-depth-and-ledger-bootstrap -->
**July 27, 2026** (from: cxotalk-weekly-maa run)

Four lessons; the first nearly put a false alarm in front of a client.
(1) **DataForSEO `depth` alone does not go past page 1 — `max_crawl_pages` (default 1) does.**
A `depth: 30` pull returned 9 results with the client's entity home absent, which read as
"dropped off page one"; re-run with `max_crawl_pages: 4` it returned 21 results and **four**
of that domain's URLs (7, 9, 12, 14) — the opposite story. Any "did we lose a ranking?" check
must pass `max_crawl_pages` ≥ 3, and never report a disappearance from a single pull: two
datacenter pulls a minute apart genuinely disagreed on this keyword, and a logged-in browser
render is a third opinion, not a tiebreaker. At the page-1/page-2 boundary, report "contested
foothold" with both observations.
(2) **When a client reports a wrong fact about their brand, grep every owned surface for the
offending string AND the desired string before changing anything, then report the counts.**
Client complained he's labeled "journalist"; the site already said "Industry Analyst" and
"Journalist" occurred 0 times site-wide — the label was Google's own KP title. "It appears 0
times on your site, here's where it actually comes from" beat any edit, and the same pass
relocated a second standing request (remove a co-founder) from the website (already clean) to
Wikidata (untouched). Corollary: a `@graph` whose `Person` is a bare `@id` reference is a valid,
standard pattern — do NOT call it a bug; report that Google doesn't reliably dereference
cross-document `@id`s and recommend inlining `name`+`jobTitle`+`sameAs`.
(3) **Back-filling an ASK-LEDGER late: never retro-charge silence.** Start counting at the first
run that had the discipline available, not at the ask's original date, and collapse bunched runs
(this task fired 3× in 4 days) into one window — otherwise a client hits Rung 4 for going quiet
over a weekend. Done honestly, the finished ledger showed two of the three highest counts were
ours/ops', not the client's; an inflated ledger hides our own drift.
(4) The 2026-07-24 degradation-banner rule is now **confirmed twice** — banner shown, ignored,
post succeeded first try. Deferring on the banner alone should be treated as a bug, not caution.
And `public-domain-rating-free`'s deprecation warning moved from 2026-08-01 to **2026-08-10**:
read the warning string on each call rather than trusting a date transcribed into a skill file.

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

<!-- learning:2026-07-27-read-vendor-deprecation-warnings-live -->
**July 27, 2026** (from: cxotalk-weekly-maa run)

### A vendor date transcribed into an SOP silently rots — read the warning string on each call

`public-domain-rating-free`'s deprecation warning now reads **2026-08-10**, not the
2026-08-01 recorded in the July 20, 2026 learning. Ahrefs pushed it back 9 days.

**General rule: read the warning string on each call rather than trusting a date transcribed
into a skill file.** Vendors move deprecation dates in both directions, so a hard-coded date
in an SOP is wrong in a way nobody notices — it either panics a run early or lets it walk
off a cliff late. Where a date must be written down, write it as "as of <Month D, YYYY> the
API said X" so the staleness is visible on the page.

**Degradation-banner rule confirmed a second time.** Basecamp again rendered its "isn't
fully functional right now" banner during the run. Per the July 24, 2026 learning it was
treated as a hint, not a verdict — the post was attempted anyway and succeeded on the first
try, verified server-side by fresh navigation (comment count 24 → 25). Two-for-two. The
banner is stale often enough that deferring on it should be considered a bug, not caution.
Learned July 27, 2026.

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

<!-- learning:2026-07-27-flat-rankings-check-indexation-first -->
**July 27, 2026** (from: anthony-hilb-seo-tracker run — week 6 after publishing 16 guides)

### When a content tracker reads "flat" for weeks, check INDEXATION before you write "needs more time"

Five consecutive runs of this tracker reported the same three numbers (DR, 1 keyword, 7 visits)
and the same conclusion: *new content takes 4–12 weeks, nothing to do.* True as far as it went,
and completely blind. One index check this run found that **6 of the 16 published guides were
never indexed at all** — including three of the most commercial topics in the set. A page outside
the index has a ceiling of zero; no amount of waiting fixes it, and "flat rankings" and "not in
the index" are indistinguishable in an Ahrefs-only view because Ahrefs reports what *ranks*, not
what *exists in Google*.

**Rule: any tracker whose job is to measure whether published content is working must verify
indexation of the tracked URLs, not just rankings — every run, from the first run.** Ahrefs
organic-keywords answers "is it ranking"; only an index check answers "is it eligible to rank."

Two method notes, both learned the hard way in this run:

1. **The obvious `site:` classifier has a false-positive trap.** Testing `html.includes(slug)`
   marks everything INDEXED, because Google echoes your own query string back in the page.
   Classify strictly: NOT INDEXED only on `"did not match any documents"` + `About 0 results`;
   INDEXED only on a result count ≥ 1 **and** a real `https://domain/slug` link in the SERP HTML.
   Run it as sequential in-page `fetch` calls from a google.com tab with ~1s spacing — 16 URLs
   cost one tool call and no CAPTCHA.
2. **Rule out your own plumbing before blaming Google, and say which you ruled out.** Same run,
   four checks: all URLs HTTP 200, all present in the post sitemap, all internally linked from
   both the hub and the blog index, homepage Person schema intact. That turned the finding from
   "six pages are broken" into "six pages are fine and Google hasn't selected them" — a different
   diagnosis with a different fix. It also killed the internal-linking recommendation I was about
   to make, which would have been busywork against an already-satisfied condition.

Corollaries worth carrying to every tracker:

- **A tracker with no GSC property should say so as a finding, not a footnote.** Without Search
  Console we can see *that* a URL isn't indexed but not *why* (Discovered vs. Crawled – currently
  not indexed), and we're blind to impressions on long-tail queries below Ahrefs' volume floor.
  Getting the property verified is an ACTION with an owner, not an ops caveat.
- **`public-domain-rating-free` lags `site-explorer-domain-rating-history` by about a day.** Last
  week's snapshot logged DR 11; the history series shows that date was already 10. If a DR delta
  is the week's only movement, confirm it against the history endpoint before narrating it —
  and pull the history occasionally anyway, since it showed this site's DR lift landed July 6,
  three weeks *after* the publish date that four prior reports had credited it to.
- **Capture backlinks/refdomains from run one even in `tracker-lite`.** This tracker had five
  snapshots and no backlink series, so the first DR drop had no context to be interpreted against.
  One `site-explorer-backlinks-stats` call per run is cheap insurance against an unreadable metric.

Learned July 27, 2026.

<!-- learning:2026-07-31-blocked-is-a-claim-that-needs-evidence -->
**July 31, 2026** (from: trenton-sandler-weekly-maa run)

### "Blocked" is a claim that needs evidence — and a misdiagnosed blocker hides what the check would have caught

The July 19 run reported Google Search Console as unreachable, wrote "Dennis needs to
re-authenticate the Google account" into the ACTION list, and carried forward two-week-old
numbers rather than guess. That last part was right. The diagnosis was wrong.

There was no expired session. **Chrome's default Google profile was signed in as a
different account than the one that owns the property.** The default URL bounces to a
"Verify it's you" screen for an account that legitimately has no access — visually
identical to a genuine logout. Inserting one path segment (`/u/1/`, or `&authuser=1`)
returned the full 28-day report instantly, no prompt.

The cost wasn't the missed check. It was that the report GSC would have produced showed a
**21% click decline and the entity home falling to #4 for the client's own name** — a real,
escalating problem that stayed invisible for twelve days behind a wrong blocker.

**Rules:**

1. **Read the email address on the auth screen before concluding anything.** If it isn't
   the account that owns the property, the session is fine and the URL is wrong. Try
   `/u/1/` and `/u/2/`; confirm ownership under Settings → Users and permissions.
2. **Name what you tried when you report a gap.** "GSC unreachable" is not a finding;
   "GSC unreachable under authuser=0 (access@…) and authuser=1 (668sierra@)" is. A gap
   nobody can reproduce is a gap nobody can fix.
3. **Any blocker that survives two consecutive runs deserves a root-cause pass, not a
   third restatement.** Re-asking a human to fix something that isn't broken burns the
   ask and the goodwill, and per STEP 6.7 it inflates a ledger counter against them.

Same pass, same lesson, different surface: a standing note in this client's brief claimed
a schema fix "requires the Rank Math Schema Generator UI because the fields aren't
REST-exposed." Half true — the `rank_math_*` keys genuinely don't appear under
`wp/v2?_fields=meta` — and completely wrong as a conclusion, because the `rankmath/v1`
namespace is right there and authenticates with the app password. **A field not showing up
where you looked is not proof it can't be written.** That one sat open for two weeks.

<!-- learning:2026-07-31-elementor-cache-and-the-three-stat-stores -->
**July 31, 2026** (from: trenton-sandler-weekly-maa run)

### A 200 on the write is not evidence the change is live — and stats hide in more than one store

Two publishing lessons for any agent running `additive-auto` against a fleet WordPress site.

**1. Elementor's element cache will serve stale HTML after a successful write.** A
`POST /wp/v2/pages/<id>` to `meta._elementor_data` returned 200, and re-reading the meta
confirmed the new values persisted. The live page still showed the old numbers — **including
for authenticated requests**, which rules out an HTTP/CDN cache and means a cache-busting
query string shows you a false clean. The previous run had worked around this with a human
clicking "Clear Files & Data" in wp-admin. The actual fix needs no login:

```
DELETE /wp-json/elementor/v1/cache      (app-password Basic auth, full Chrome UA)
```

So the publish sequence is **write → DELETE cache → re-fetch anonymously → assert the NEW
string is present AND the OLD string is absent.** Both halves of that assertion matter; a
run that only checks for the new string can pass on a page that still shows both.

**2. When you find one stale statistic, sweep every page — the same numbers live in
different stores.** Fixing a stale follower count in a Rank Math meta description prompted a
site-wide check, which found *March-era* numbers still in the visible body copy: an About
page telling visitors "130,000+ followers / 53,800 subscribers" when the real figures were
145,000 and 57,200, and — worse — a **Sponsors page**, the one brands read before deciding
what to pay him, advertising an audience 15,000 smaller than it actually was.

Three different stores on one site, and prior runs had each fixed only the one they came
for:

| Store | Where it showed up |
|---|---|
| Elementor `_elementor_data` | `/media/` stat cards |
| Gutenberg `content` | `/about/`, `/sponsors/` body copy |
| Rank Math meta | homepage + `/about/` meta descriptions |

**Rule: a stat refresh is a site-wide sweep, not a page edit.** Grep every page for the OLD
values after every refresh and report the sweep result, not just the pages you touched.
And weight the commercial pages first — a stale number on a pricing or sponsors page isn't
a tidiness problem, it's the client negotiating against a figure that undersells them.

Corollary on honesty: leave a number alone when you can't source it. "250+ videos" stayed
because 252 was verified and 250+ is therefore true; bumping it to match a different page's
"276+" would have meant publishing a figure no source supported.

<!-- learning:2026-07-28-a-shipped-skill-must-not-carry-your-own-address -->
**July 28, 2026** (from: skill-pack-propagation daily run, July 28, 2026)

### A skill that ships must not carry your address, your staff, or your routing

`client-access-checklist` was mandated into every pack on July 27, 2026 and went live in all
seven public downloads. Written for internal use, it told the reader to add
`access@localservicespotlight.com` and `668sierra@gmail.com` as Full users on the **client's**
Search Console, and to route blocked work to a named staff member and an internal team alias.

`weekly-brand-maa` was worse in effect: it instructed the agent to "always send one combined
summary email to Dennis (668sierra@gmail.com)." Every workshop attendee who installed that pack
had an agent whose weekly job was to email *us* about *their* clients.

That is not only a privacy leak; it is a functional bug. An instruction that names a specific
person is correct in exactly one installation and wrong in every other one.

**Rules:**

1. **Before a skill is mandated into distributed packs, read it as a stranger who just
   downloaded it.** Every "we", "our account", named person and internal alias is a defect.
   Ask: *if a competitor installed this, what did I just hand them, and who would it email?*
2. **Addresses, owners and destinations are CONFIGURATION, not content.** Say "the owner
   address configured for this agent"; keep the actual values in the internal runbook and the
   credentials file — the two places that never ship.
3. **Grep the built artifact, not the source folder.** These files were fine in the folder they
   were written for; the defect only exists once the mandate copies them somewhere else. Add
   the sweep to the run: fetch each LIVE download and search it for your own addresses. That
   check takes seconds and is the only one that reflects what a stranger actually receives.
4. **Generalising a skill for distribution is part of mandating it, not a follow-up.** The
   mandate that copies a file into ten packs is the moment its audience changes.

Learned July 28, 2026.

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

<!-- learning:2026-08-03-classify-the-metric-dont-just-count-it -->
**August 3, 2026** (from: anthony-hilb-seo-tracker run, week 7 after publishing 16 guides)

### A tracker only sees what is on its checklist — so derive the checklist from the goal, not from the last run

Seven weekly runs of this tracker reported Domain Rating as the headline movement metric.
Four of them credited a DR lift (9 → 12 → 11 → 10) to the 16 guides published on June 14,
2026. This run classified the backlink profile for the first time and found that **385 of
the site's 398 live referring domains — 96% — are link-farm spam** (178 `.store`, 158
`.shop`), that the flood began in **mid-April, two months before the publish date those
reports credited**, and that **all 30 referring domains gained in the last week were spam
and zero were legitimate.** DR is a function of referring domains. The metric four reports
narrated as our content working was link farms.

The July 27, 2026 learning had already added `site-explorer-backlinks-stats` to this
tracker — so the run *counted* 371 referring domains and moved on. **Counting a metric is
not inspecting it.** One extra call with `history=live` and Ahrefs' own `is_spam` flag,
split into spam and not-spam, turned a number into the run's headline finding and retired
DR as a progress metric for the site.

The same blindness showed up twice more in the same run, which is what makes this a rule
rather than an anecdote:

- **The `/watch-and-learn/` hub had never been index-checked** in seven weeks — every run
  checked "the 16 guides" because that was the list it inherited. The hub is not indexed
  either.
- **The byline had never been checked at all.** All 16 guides on a *personal brand site*
  are published under a different person's name, with two conflicting `Article` schema
  nodes per page and an indexed `/author/<someone-else>/` archive. On a site whose entire
  purpose is establishing one person as the authority, authorship is arguably the primary
  metric, and it was on nobody's list.

**Rules:**

1. **Classify every metric you report, don't just size it.** For backlinks that means
   splitting the profile on the vendor's spam flag and reporting the ratio, from run one.
   A count with no composition can move for reasons that are the opposite of progress, and
   it will be narrated as progress because the number went up.
2. **When a metric's movement is about to be credited to our work, check whether anything
   else could have moved it** — and check the dates line up. The DR lift landed three weeks
   after the publish, in the middle of a spam flood. The timing alone should have stopped
   the claim.
3. **Rebuild the checklist from the goal each time, rather than inheriting last run's.**
   "Is the content working" is not "are these 16 URLs ranking" — it also covers the hub
   that links them, the byline that earns them E-E-A-T, and the profile that funds their
   crawl budget. An inherited list silently defines what the agent is able to notice.
4. **Retract, in writing, any prior conclusion the new evidence kills.** This run withdrew
   its own previous week's third action (a "distinctiveness pass" on six unindexed pages)
   after measuring that those pages average 2,058 words against 2,042 for the indexed ones
   — indistinguishable, so there was nothing to fix and the recommendation had been
   inference dressed as an action. A tracker that never contradicts itself is not being
   read carefully enough.

5. **A classification is a vendor's opinion — cross-check it against a second index before
   it drives an action.** This is the half that nearly shipped wrong. Having found "96%
   spam" in Ahrefs, the run was one step from recommending a 385-domain disavow. A
   two-minute check against DataForSEO returned **37 referring domains against Ahrefs' 398,
   and zero `.store`/`.shop` referrers against Ahrefs' 336** — and not from ignorance, since
   DataForSEO scores those same domains 45–68 for spam when queried directly. It simply
   doesn't record them linking to this site.

   The discipline that makes a cross-check useful is deciding, explicitly, **which
   conclusions survive it and which don't**, rather than letting the disagreement wash out
   everything at once:

   - *Survived:* retiring DR as the progress metric. Domain Rating is computed from Ahrefs'
     own index, so if Ahrefs sees 385 spam referring domains, Ahrefs' DR is driven by them
     no matter what another crawler sees. Airtight, and independent of the disagreement.
   - *Weakened:* the disavow. A network only one crawler can see is not obviously a network
     Google counts, and disavowing on one vendor's index is acting on the weaker half of
     the evidence.

   Generalise it: **when two sources disagree, don't average them and don't pick the one
   that makes the better story — partition your conclusions by which ones depend on the
   disputed data.** Some usually don't, and those are the ones you can still act on today.

Corollary on delivering the fix rather than the finding: the spam list was still enumerated
into a ready-to-upload `disavow.txt` (385 domains, with the 15 legitimate domains listed as
excluded-and-why), but **staged, not uploaded**, with the vendor disagreement written into
its own header so whoever opens it inherits the doubt along with the file. Build the
artifact so the decision costs five minutes; never make the decision on the client's behalf
from data that cannot answer it.

Learned August 3, 2026.

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

<!-- learning:2026-08-03-crawlability-must-be-tested-on-served-html -->
**August 3, 2026** (from: cxotalk-weekly-maa run)

### Never diagnose crawlability from rendered text — the client who corrected us was right for four weeks

For four consecutive reports, this engagement's #1 technical recommendation was: *"~40M words of
CXOTalk transcripts are client-rendered and invisible to the crawlers ChatGPT and Perplexity depend
on — server-render them."* It was the headline of the strategy, it was in every ANALYSIS section,
and it was **false**.

The client disputed it in writing on 7/28: *"I checked this carefully and I do not believe that
transcripts on cxotalk.com are hidden by JS."* Tested properly, he was right:

| Check | Result |
|---|---|
| Raw same-origin `fetch`, **no JS executed**, `/episode/{slug}` | HTTP 200, 660KB HTML, **59,761 chars** body text after stripping `<script>`, **97 speaker turns** |
| Same, `/episode/{slug}/transcript` | Identical — 59,761 chars, 97 turns |
| `robots.txt` | 916 bytes; only `Baiduspider` is `Disallow: /`. The file **explicitly names** "Googlebot, bingbot, Applebot, ClaudeBot, GPTBot, etc." as covered by the permissive `User-agent: *` group |

**The mechanism of the error.** Reading the *rendered* page returns **~349 words** from
`document.body.innerText`, because the transcript sits inside a collapsed/tabbed element.
`innerText` returns only **visible** text. The content was fully present in the served HTML the
entire time. A visible-text read was mistaken for a crawler's view, and nobody re-tested it for a
month because each week's report inherited the previous week's premise.

**Rules:**

1. **Test crawlability against the SERVED HTML, never the rendered view.** Same-origin
   `fetch(url)` → `DOMParser` → strip `script/style/noscript` → **`textContent`**. Never
   `innerText`, never `get_page_text`, never a screenshot. Those three answer "what can a human
   see," which is a different question and frequently the opposite answer.
2. **`innerText` vs `textContent` is the whole bug.** Collapsed accordions, inactive tabs,
   `height:0` containers and offscreen panels are invisible to `innerText` and perfectly visible
   to a crawler. Any conclusion of the form "the content isn't in the HTML" that was reached via
   `innerText` is unsupported.
3. **Check robots.txt in the same pass, and read it verbatim.** A JS thesis and a blocking thesis
   are two different claims; we asserted both and both were wrong. Quote the actual `User-agent`
   groups rather than characterising them.
4. **A recommendation that survives four reports without being re-tested is a belief, not a
   finding.** Standing recommendations need a re-verification cadence, because the cost of being
   wrong compounds: every week it went unchallenged, it displaced whatever the real fix was.
5. **When a client contradicts your technical claim, test their version first, not yours.** The
   instinct is to defend. The client here had checked something we hadn't, and one raw fetch
   settled it in under a minute. Being corrected and saying so plainly is cheaper than four more
   weeks of confident wrongness — and it upgraded the diagnosis (the citation gap is an
   authority/entity problem, not a plumbing one), which is a better answer than the one we lost.

**Same run, same family, caught before it shipped:** the week's first Ahrefs metrics pull passed
`country=us` where prior runs passed no country filter, returning 394 keywords vs 464 — a false
17% "collapse" that would have been the report's lead. Re-pulling the *prior week's date* under
*today's exact config* reproduced last week's numbers exactly, proving config drift rather than
decline. **Any alarming metric move must be re-pulled at the prior date under the current config
before it is narrated.** Two near-misses in one run, both of the same shape: *the measurement
apparatus changed, the world did not.*

Learned August 3, 2026.
