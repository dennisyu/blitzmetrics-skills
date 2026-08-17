---
name: personal-brand-people-directory
description: Use when building /people/{slug}/ honor cards on a personal brand WordPress site from photos, honor posts, DealCon, or a who's-who inventory. Live first on low-traffic sites. No query-string URLs. Publish as the person.
---

# Personal brand people directory

**Use this when** a personal-brand WordPress site needs a public `/people/` directory of the humans the owner builds with — honor cards at `/people/{slug}/`, not a second blog and not a CRM.

Canonical public writeup: https://dennisyu.com/how-we-build-people-pages/

Agents that run this are shared as **Local Service Spotlight**. The BlitzMetrics site stays up; the operating name for shared agents is Local Service Spotlight.

Companion rule: prefer the site owner's person user as WordPress author. If only `admin` exists, publish as admin and flag a byline fix. Do not create users unless asked.

## What you are building

1. One hub page at `/people/` (do not create a second hub if one exists).
2. One child page per person at `/people/{slug}/`.
3. Pretty permalinks only. No `?p=`, `?page_id=`, `?utm_`, `?fbclid`, or other URL variables on the page URL or in any href.
4. Short honor cards the owner can narrate later. Do not invent a company or title.

Working example: https://dennisyu.com/people/ (100+ children). First portable copy: https://dennisyu.com/derek/people/ — move that tree onto the person's own domain when the entity home is ready. Do not publish this method onto moneyberg.com or derekmoneyberg.com until Dennis says yes.

## When to publish live

Low-traffic personal brand sites: publish the card live first. The owner gives feedback on the live page.

Do not publish to a client's production domain (funnels, paid traffic, reputation-sensitive) without an explicit yes. Build on a working-example path the owner already controls, then migrate.

## Auth and author

- REST only if wp-admin HTML is blocked.
- Application password on the agent computer. Never print it.
- Set `author` to the site owner's person user. If only `admin` exists, publish as admin and flag a byline fix.

## Hub

If `/people/` already exists, use it. New cards are children of that page.

Hub copy is a directory, not a second about page. Every hub link to `/people/{slug}/` must resolve. If the hub names someone and the child 404s, create the child.

## Card template

Match https://dennisyu.com/people/zach-peyton/ and https://dennisyu.com/people/jack-wendt/:

- Back link to `/people/`
- Role line in italics (one line)
- Optional photo if you have a real image of the owner with that person
- `h2` name
- 1–2 short factual paragraphs
- Optional "Find them online" list — verified URLs only, no query strings
- Link any existing entity home or article on the same site
- Closing line: this page honors the people the owner builds with
- JSON-LD `ProfilePage` about a `Person`
- `status=publish`, `comment_status=closed`, parent = hub id
- If no photo: "Photo gallery coming — [owner] will narrate."

If a slug already exists under the hub, UPDATE it. Do not create a duplicate.

Do not fill ACF person fields with lorem or theme placeholders.

## How to pick the next people

Work the inventory in this order. Skip anyone who already has `/people/{slug}/`.

1. Named photo folders (Google Drive / Google Photos people albums), highest count first.
2. Honor posts and "Life Lessons" articles that name a person.
3. People who already have an entity home or DealCon audit on the site but no directory card — add a short card that points at the existing home.
4. Hub links that 404.
5. A who's-who inventory the owner already published (podcast guest list, speaking list, client list). Verify each name from that source. Do not invent.

Company folders are not people. Empty photo folders stay skipped.

If the name is not unique in the owner's world, publish a minimal stub: name, "one of the people [owner] has photographed and works with," gallery coming. Do not invent a company.

## Photos

A photo of the owner *with* the person is the honor proof. A stock headshot of the person alone is not that.

If Drive/MCP downloads truncate, publish the card without the image and keep going. Do not block the directory on photos.

Never put query strings on media or outbound URLs.

## URL variables

After each batch, scan hub + children:

- No `?` in permalinks
- No `?` in content hrefs (except a real YouTube `watch?v=` you chose not to link — prefer not to link those)
- No `{{url}}`, `%post_url%`, `{url}`, or leftover tokens

Strip query strings. If the link is only useful because of the query, drop the link.

## Receipt

Write a short report: ids, slugs, live URLs, photo yes/no, identity notes, any stub, any hub 404 you fixed.

## Do not

- Do not create a second `/people/` hub
- Do not clone repositories
- Do not print credentials
- Do not publish unsourced titles
- Do not put this method on a production client domain without a yes
- Do not treat a working example on the owner's site as the client's live site
- Do not report this skill as Installed, Enabled, Tested, Scheduled, or Observed without a receipt

## Definitive article & pairings

- Reference: https://dennisyu.com/how-we-build-people-pages/
- Pairs with: business-website-agent → **personal-brand-people-directory** → evidence-verification

After adding this file, run `python3 scripts/sync_shared_rules.py` so house-rule blocks are stamped in. Do not hand-edit generated shared-rule blocks.
