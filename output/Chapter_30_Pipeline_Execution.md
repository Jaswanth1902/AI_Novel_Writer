# Pipeline Execution Artifact: Chapter 30 — The Silent Carriage

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 30
title: "The Silent Carriage"
word_count_target: 1500-2000
pov: Tejaswini (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Military Rail Coach Interior, Oakhaven Mountain Cuts, Academy Central Platform
  atmosphere: Rhythmic sway of iron wheels, cold mountain air, coal smoke, scent of vinegar and dried blood, tense reverent silence.
characters:
  - Tejaswini: Guardian at Chaitanya's side, securing the blood-pact of secrecy among the squad.
  - Chaitanya: Comatose, breathing stabilized, receiving continuous thermal conduction.
  - Bennett: Wounded squad leader, binding the squad into an unbreakable brotherhood.
  - Anil: Sobered scout, confronting the lethal realities of the frontier.
  - Proctor Rao: Veteran observer, receiving the wounded unit with deep military respect.
plot_beats:
  1: The train journey north through the snowy defiles; the intimate, silent vigil inside the coach.
  2: Bennett and Anil reflect on the impossibility of what Chaitanya achieved against the Danava.
  3: Tejaswini seals the covenant of silence: warning that exposing Chaitanya's power means execution by the Inscription Tribunal.
  4: Bennett and Anil swear an iron blood-pact to guard Chaitanya's secret with their lives.
  5: Arrival at the Academy central platform; hundreds of stunned cadets and instructors watching.
  6: Proctor Rao receives the stretcher; orders the inner infirmary secured with live steel.
invariants:
  - Zero modernisms (no tea, no couches, coal-fired locomotive, vinegar dressings, pine litters).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Tejaswini:
    goal: Secure the survival of Chaitanya and lock the squad into an absolute conspiracy of silence.
    conflict: Physical and emotional exhaustion threatening her noble facade.
    somatic_tells: Fingers maintaining continuous thermal pulse, dark eyes unblinking, voice quiet as razor-steel.
  Bennett:
    goal: Reaffirm his oath as squad commander and acknowledge Chaitanya as the true core of Unit 07.
    conflict: Frustration at his own broken ribs vs. profound loyalty.
    somatic_tells: Wincing as train jolts, calloused thumb stroking the broken spear socket, deep steady voice.
  Anil:
    goal: Process the trauma of near-death and cement his loyalty to the squad.
    conflict: Shedding his former frivolous attitude.
    somatic_tells: Head bowed, dart twirling stopped, solemn nodding.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 close interior carriage, deepens to D3 psychological brotherhood, opens to D2 public spectacle on the platform."
  rhythm_profile: "Hypnotic, rhythmic cadence mimicking the locomotive; transition from private sacred trauma to public military reverence."
  sensory_palette:
    - Olfactory: Bituminous coal soot, vinegar liniment, cold snow, damp wool, blood.
    - Tactile: Constant vibration of iron floorboards, rough blankets, cold wind on cheeks.
    - Auditory: Click-clack of rail joints, slow measured breath, silence of a crowd.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_30_The_Silent_Carriage.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 30,
  "characters": {
    "Unit_07": {
      "reputation": "Legendary: First candidate unit to fell a Tier-3 Danava",
      "conspiracy_sealed": "Blood-pact sworn: Bennett, Tejaswini, and Anil bound to protect Chaitanya's secret",
      "chaitanya_location": "Inner Infirmary, Tattva Academy"
    }
  },
  "world_state": {
    "arc_milestone": "Conclusion of Langford Expedition Arc (Chapters 21-30).",
    "approaching_arc": "The Recovery & Academy Selection Tournament (Chapters 31-40)."
  }
}
```
