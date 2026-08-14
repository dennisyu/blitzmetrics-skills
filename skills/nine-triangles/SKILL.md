---
name: nine-triangles
description: Apply the versioned Nine Triangles operational reference and resolve conflicting or reconstructed triangle names. Use when someone asks for the Nine Triangles, ACC versus AEC, SBP versus ABP, MAA, GCT, DDD, CID, LDT, CCS, or MOF; when mapping a marketing or operations problem to the framework; or when auditing a copied course, article, prompt, or skill pack for framework drift.
---

# Nine Triangles

Use the versioned names in `references/canonical-framework.md`. Read that reference
whenever exact names, source authority, or historical aliases matter. Do not rebuild
the framework from search snippets or memory.

## Apply the framework

1. State the business problem and desired result in one sentence.
2. Select the one triangle that directly governs the next decision. Do not force all
   nine into every analysis.
3. Evaluate all three corners separately. Record evidence for each corner; do not
   let strength in one hide a missing second or third corner.
4. Identify the weakest corner and convert it into one owner, action, deadline, and
   success measure.
5. Use MAA on the next review: measure the result, analyze why it moved, then choose
   the next action.
6. Report the framework version and acceptance status exactly as recorded in the
   reference so copied packs can be reconciled later. Do not call a candidate
   reference canonical.

## Guardrails

- Treat legacy aliases as aliases, not extra triangles.
- Never call a vendor or WordPress plugin part of the Nine Triangles. Link Whisper,
  Yoast, HighLevel, DataForSEO, and similar tools are optional implementation choices.
- Do not recommend a tool merely because an old pack named it. Verify that it is
  required, currently supported, safe, and the simplest fit for the action.
- Do not redistribute paid course material. Provide the operational names and
  workflow here, then link to the authorized course or definitive article for the
  full curriculum.
- When two BlitzMetrics sources disagree, name the discrepancy and follow the
  authority order in the reference. Never silently choose the wording that makes a
  clean-looking answer.

## Output

Return:

- selected triangle and exact three corners;
- evidence and gap for each corner;
- weakest corner;
- one accountable next action with deadline and metric;
- framework version and any legacy alias encountered.

Pair with `measurement-analytics` for MAA data, `content-factory` for GCT and
funnel execution, and `skill-registry` when a copied pack needs reconciliation.

<!-- shared-rule:silent-media-playback:start -->
## Silent media playback

- Never let audio from browser, video, audio, presentation, or application testing play through the user's speakers unless the user explicitly asks to hear it.
- Before starting any media playback, mute the player and set its volume to zero. Keep it muted for the full test, including replays, reloads, new tabs, and alternate players.
- Apply this rule to the primary agent and every delegated agent. Include the mute requirement whenever work that may involve media playback is delegated.
- If the mute state cannot be controlled and verified before playback, do not start playback. Use metadata, captions, transcripts, frames, screenshots, network state, or player state instead.
- Only unmute when the user explicitly requests audible playback in the current task.
<!-- shared-rule:silent-media-playback:end -->
