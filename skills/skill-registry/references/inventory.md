# Skill inventory — audited 6 August 2026

Snapshot of what is actually installed and activatable on Dennis's account, taken by
listing each registry directly rather than from memory or documentation.

---

## Registry 1 — Plugins (team-wide)

| Plugin | Skills | Commands | Status |
|---|---|---|---|
| `blitzadmin-wordpress` | wordpress-site-management | site-audit, publish-content, list-sites | Installed |
| `blitzmetrics-authority` | geo-visibility-audit, skill-registry | — | **This plugin — new** |

No BlitzMetrics marketplace exists yet. The only plugin catalog attached to the
account is Anthropic's `knowledge-work-plugins`. **Standing up a BlitzMetrics
marketplace is the single highest-leverage fix** — it turns plugin install from a
manual file hand-off into a subscribe-once channel for the whole team.

## Registry 2 — Account skills (Dennis only)

Custom, BlitzMetrics-built:

| Skill | Last updated |
|---|---|
| personal-brand-strategist | 3 Aug 2026 |
| positive-mentions-harvester | 3 Aug 2026 |
| fleet-uptime-monitor | 27 Jul 2026 |
| video-repurposing-agent | 27 Jul 2026 |
| video-editing-agent | 27 Jul 2026 |
| facebook-ad-agent | 22 Jul 2026 |

Anthropic-supplied, also enabled: morning, skill-creator, xlsx, pptx, pdf, docx.

**Gap:** the 28 July end-of-day report describes *22* packaged BlitzMetrics / LSS
skills. Six are installed here. The other sixteen are either only in the canonical
pack, only on a teammate's machine, or only in a document. Reconcile the list before
assuming any of them will run.

**Constraint:** these are per-person and cannot be installed by a session. Each teammate
must accept a delivered `.skill` file individually — which is exactly why anything
shared belongs in Registry 1 instead.

## Registry 3 — Cloud scheduled tasks

Recurring and enabled:

| Task | Cadence (UTC) |
|---|---|
| Weekly authority-citation sync — self-publishing, auth-probing | Mon 11:37 |
| Weekly SEO + security watch — dennisyu.com & blitzmetrics.com | Mon 11:01 |
| GitLab access — chase until site-builder token lands | Daily 14:00 |

Also present: one long-dated one-shot (Jan 2027 roofing review), several fired
`send_later` reminders, and `[RETIRED 7/28/26] Weekly Fleet Audit — replaced by local
scheduled-jobs-health-audit`.

**Note the retired one.** It documents that fleet auditing moved to a *local* job —
which a cloud-side audit cannot see. Do not conclude it stopped running.

**Opportunity:** the weekly authority-citation sync is the natural host for
`geo-visibility-audit`. It already runs Monday morning and already concerns citations.
Update its prompt rather than creating a competing job.

## Registry 4 — Local Cowork scheduled jobs (desktop)

Not enumerable from a cloud session — the scheduled-task listing explicitly excludes
desktop-stored jobs. Known to exist from the retirement note above and from the team's
reports: `scheduled-jobs-health-audit`, an Obsidian daily upkeep agent, and the Monday
skills-pack sync.

**Audit these from the desktop app.** A cloud-only inventory will always show this
registry as empty, which is a measurement artefact, not a finding.

## Registry 5 — Canonical pack + Monday sync

Per the 28 July report: 22 skills packaged with an install guide, and a weekly Monday
job that pulls the canonical pack, byte-diffs it against a stored baseline, and rebuilds
the skill plugin only when something changed.

**Unresolved:** the pack's canonical location was not identifiable from this session.
Google Drive holds a `Skill Files` folder with a single `SKILL.md`, and a
`Skills list 21.07.2026` sheet that belongs to a client's course inventory, not to this
pack. Confirm whether the source of truth is a repo, a Drive folder, or a teammate's
local directory — and write the answer here. **An unlocatable source of truth is the
biggest structural risk in this framework:** the sync job will keep rebuilding from it,
and nobody else can contribute to it.

---

## Open items

1. Locate and document the canonical pack's real location. Owner: whoever runs the Monday sync.
2. Reconcile 22 packaged vs 6 installed. Publish the delta.
3. Stand up a BlitzMetrics plugin marketplace so packs install by subscription.
4. Fold `geo-visibility-audit` into the Monday authority-citation sync prompt.
5. Audit the local desktop jobs from the desktop app and list them here.
6. Re-run this inventory monthly; record the diff, not just the totals.
