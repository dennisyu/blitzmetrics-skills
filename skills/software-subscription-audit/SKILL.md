---
name: software-subscription-audit
description: The Software Subscription Audit — a quarterly (scheduled) money-finding agent. It inventories every software subscription you pay for, flags downgrades/duplicates/zombies with evidence, and hands you a savings list with exact next clicks. Found ~$5,000/year in the founder's own stack the first time it ran.
---

# Software Subscription Audit

*Born 19 Jul 2026: one founder reviewed her own stack with Claude after an unrelated hosting call and found ~$4,000/year of savings the same day (~$5,000 once support tickets cleared) — a project-management plan downgrade, an unused AI-voice tier, a cancelled tool nobody used, an idle multisite. Then she scheduled it quarterly. This skill is that exact workflow, packaged.*

**Use this when** money leaks quietly: subscriptions renew, seats sit empty, two tools do one job, and nobody is paid to notice. Run it quarterly — scheduled, not remembered.

## Hard rules
- **Evidence, not vibes.** Every recommendation cites what you actually pay (from invoices/statements you provide or screens you share) and what the vendor's CURRENT public pricing page says — fetched and verified live, with the URL.
- **Never cancel, downgrade, or email a vendor yourself.** You produce the decision list; the human clicks. Support-ticket drafts are staged as drafts.
- **No plan-shaming.** If a tool earns its keep, say so — a "keep" with reasons is as valuable as a "cut."

## Inputs
- Your subscription list — any of: a folder of invoices/receipts, a bank/card statement export (CSV), or just "here's what I think we pay for." The agent reconciles all three when given more than one (the statement always wins).
- Team size / seats actually used per tool (ask if unknown).
- Your links file (so recommendations respect tools that power live funnels — never suggest cutting the thing your opt-in page runs on).

## Steps
1. **Inventory.** Build the master table: tool · plan · seats · billing cycle · price paid · renewal date · owner · what it's for. Flag unknowns to ask about in one batch.
2. **Verify current pricing.** Fetch each vendor's live pricing page. Note where a cheaper tier now covers your real usage — plans change under you; the biggest single find in the origin run was exactly this (a Starter tier that now covered everything, ~$3,000/yr saved).
3. **Classify each line:**
   - **Zombie** — paid but unused ≥60 days → cancel candidate.
   - **Overplanned** — usage fits a lower tier or fewer seats → downgrade candidate.
   - **Duplicate** — two tools, one job → consolidate candidate.
   - **Hostage** — annual renewal approaching → calendar the decision BEFORE it auto-renews.
   - **Keep** — earning its seat; say why in one line.
4. **The savings list.** Sorted by $/year recovered, each with: the exact next click (settings URL or support-ticket draft), any risk ("downgrade loses X — confirm you don't use it"), and effort (2-min click vs support ticket).
5. **Stage the tickets.** For changes needing vendor support, write the ticket/email text as a DRAFT.
6. **Report + schedule.** One page: total found now, total pending tickets, renewal calendar for the next quarter. Then make sure the QUARTERLY schedule exists: *"Create a scheduled task: first Monday of the quarter, run my software-subscription-audit and leave the report in my Outputs folder."* That single sentence is the difference between finding money once and never leaking again.

## Output
`Outputs/subscription-audit/<date>/`: `inventory.md` (master table) · `savings-list.md` (ranked, with next clicks) · `tickets/` (draft support requests) · `report.md` (one page). Log line appended to `Outputs/subscription-audit/log.md`.

## Definition of done
- Every subscription classified with evidence; every recommendation has a live-verified pricing citation and an exact next click.
- Zero actions taken on your accounts — you hold the scissors.
- The quarterly schedule exists (or you said no on purpose).

## Notes
- This is a scheduled agent by design: it exists BECAUSE it's scheduled. Quarterly beats "when I get around to it" by roughly $5,000/year, per the origin run.
- For agencies: run it FOR a client before a strategy engagement — walking in with found savings buys a lot of trust, and a quarterly "stack audit" is the easiest productized service to explain (statement in, savings list out).
- Money recovered here funds your $1/day amplification for a long time.

## Pairs with
→ sales-every-day (fund the winners) → dollar-a-day-strategist → measurement-analytics (one watches what comes in, this watches what quietly goes out) → recursive-self-improvement-qa

---
*Built by Dennis Yu (BlitzMetrics / Local Service Spotlight), from a real 19 Jul 2026 audit. The agent finds the money; you keep the judgment.*
