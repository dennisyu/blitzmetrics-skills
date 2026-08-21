---
{
  "title": "Capture what you learn as a standard, in the same session",
  "severity": "error",
  "captured": "2026-08-16",
  "captured_from": "Dennis Yu, Cowork session, 2026-08-16: 'our goal is recursive self-improvement ... as I learn stuff, it propagates out for everyone else to be able to benefit from it ... that way, we don't keep losing things that I tell you are important to put into our centralized knowledge.' Written after tracing why a rule published on 2026-05-17 was still being broken by agents on 2026-08-15. Extended in Codex, 2026-08-20, after comparing 291 private agent notes with 127 applied learning notes and finding no automatic link between the two systems.",
  "applies_to": ["agent-behaviour"]
}
---

## Capture what you learn as a standard, in the same session

- **A rule that lives only in an article, a chat message, a call recording, or your
  context window is a rule the next agent will break.** That is not a prediction. The
  black-button rule was published, illustrated, and given an enforcement plugin on
  17 May 2026, and on 15 August 2026 an agent holding the entire skill pack in context
  shipped a black button. The rule was never in `standards/`, so it never reached the
  skills, so it was not there to be read.
- When anyone — the client, the account owner, an audit, or your own failure — states a
  rule that should hold next time, **your job is not to remember it. Capture it before the
  session ends.** A direct instruction can become a proposed `standards/<slug>.md` with
  provenance. A causal claim such as “this tactic improves sales” also needs the outcome
  receipt required by `report-business-impact-not-volume`; otherwise it is a hypothesis,
  not canon.
- Scaffold it in one command, which forces every field including where the rule came
  from:

  ```bash
  python3 scripts/new_standard.py "no autoplay with sound" \
    --from "Dennis Yu, Cowork session, 2026-08-16" --applies-to published-html
  ```

- Then write the rule, run `python3 scripts/sync_shared_rules.py`, and open the pull
  request. The sync copies the candidate into `AGENTS.md` and every distributed
  `SKILL.md`. That proves source parity only. It reaches a person after merge and
  surface-specific sync; it becomes working capability only after a fresh-session
  activation receipt. Never call source consistency “propagated everywhere.”
- **Every substantive run record needs a learning disposition:** `proposed`, `applied`,
  `rejected`, or `none` with a reason. Link the affected skill/standard and source/resulting
  commit. If the record contains a reusable lesson but no disposition, the loop is open.
- Keep private facts, credentials, client URLs, and raw revenue receipts in the private run
  record. Publish the sanitized, reusable rule and enough non-sensitive evidence for another
  agent to evaluate it. “Build in public” does not mean leak client data.
- **Give the rule a machine check whenever one is honest.** A `checks` block in the
  header compiles straight into the live fleet sweep, so a violation on a published page
  is caught by a schedule instead of by a person noticing. Every check must carry
  passing and failing examples — a pattern that matches nothing reports a clean site
  forever, which is worse than no check at all.
- **Where a machine check would be dishonest, say so and leave `checks` out.** Judgement
  rules are still rules; they are enforced by being read pre-flight, and pretending a
  regex covers them hides the fact that nothing does.
- **Provenance is required, not decoration.** `captured_from` is how the team sees which
  channels leak. If dozens of recorded calls have produced no standards, those calls are
  not being captured, and that is visible at a glance instead of being a suspicion.
- **When a new rule contradicts an existing one, resolve it in the file and say so
  out loud.** Two standards that disagree are worse than one that is wrong, because
  every agent that reads both will pick whichever it happened to see last. Write the
  reconciliation into the newer rule and flag it to the account owner for confirmation.
- A harvester may draft the branch and pull request; it must not silently merge a learning
  into canonical instructions. Independent QA, repository checks, and an attributable
  canary keep one persuasive but wrong run from teaching the entire fleet.
- The order is Checklist → Content → Software. Write the checkable rule first, publish
  the article that teaches it second, and let the sweep be generated from the rule
  rather than hand-written beside it. Writing the article first is how rules get lost:
  the article is the artifact everyone can see, so it feels finished, and the
  enforceable form never gets written.
