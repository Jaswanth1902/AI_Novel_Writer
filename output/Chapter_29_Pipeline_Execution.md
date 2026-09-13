# Pipeline Execution Artifact: Chapter 29 — The Pyres of Morning

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 29
title: "The Pyres of Morning"
word_count_target: 1500-2000
pov: Tejaswini (Third-Person Limited, Gardner Distance D2-D4, shifting from Chaitanya due to coma)
setting:
  primary: Langford Main Street Ruins, Storehouse Field Hospital, Station Platform
  atmosphere: Cold grey morning mist, smell of burning beast pyres, charred fat, bitter vinegar bandages, damp flour, and soot.
characters:
  - Tejaswini: Exhausted, fiercely protective, maintaining Chaitanya's core temperature with controlled thermal transfer.
  - Chaitanya: Comatose, severe physical and internal meridian trauma.
  - Bennett: Bandaged, fractured ribs, stoic northern discipline.
  - Anil: Battered, limping, assisting with field stretcher logistics.
  - Lyra: Battle-scarred scout liaison, delivering the official frontier casualty and victory dispatch.
plot_beats:
  1: Morning breaks over the smoking ruins of Langford; pyres of dead beasts burning in the streets.
  2: Confirmation of mission success: five hundred civilians saved, horde scattered into the southern wastes.
  3: Field treatment inside the storehouse: Bennett’s broken ribs bound; Anil reporting status.
  4: Tejaswini’s vigil at Chaitanya’s side; using micro-thermal conduction through her palms to sustain his failing pulse.
  5: Lyra arrives with the official Vanguard dispatch, acknowledging their impossible victory.
  6: Loading Chaitanya onto the evacuation carriage for the rail journey back to the Academy.
invariants:
  - Zero modernisms (no tea, no couches, vinegar bandages, pine stretchers, iron stove, steam train).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Tejaswini:
    goal: Keep Chaitanya alive at all costs and prevent anyone from discovering the unnatural nature of his injuries.
    conflict: Overwhelming emotional panic vs. rigorous noble composure.
    somatic_tells: Hands glowing with steady low-grade heat, dry cracked lips, refusal to sit or take water, unyielding stare.
  Bennett:
    goal: Maintain command structure and ensure the safe extraction of his squad.
    conflict: Agonizing physical pain from broken ribs.
    somatic_tells: Shallow guarded breaths, grimace when shifting weight on pine crutch, gravelly voice.
  Lyra:
    goal: Formalize the military record and pay homage to candidates who fought like legends.
    conflict: Awe of Chaitanya’s lethal capability vs. military protocol.
    somatic_tells: Bowing head slightly, voice stripped of cynicism, holding out the stamped vellum dispatch.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 in the smoking morning ruins, narrows to D3 intimate somatic tension around Chaitanya’s pallet, widens to D4 historical gravity."
  rhythm_profile: "Solemn, measured, elegiac; tactile textures of post-battle fatigue and medical recovery."
  sensory_palette:
    - Olfactory: Burning beast tallow, vinegar, damp flour paste, blood, cold pine smoke.
    - Tactile: Cold limp hand clutched in warm fingers, rough canvas stretcher, biting frost in the air.
    - Auditory: Crackle of distant pyres, wheeze of strained lungs, slow rhythmic thrum of locomotive idle.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_29_The_Pyres_of_Morning.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 29,
  "characters": {
    "Chaitanya": {
      "vital_status": "Comatose, stabilized by Tejaswini's thermal conduction",
      "injuries": "Fractured left clavicle, 3 broken ribs, severe meridian exhaustion"
    },
    "Unit_07": {
      "status": "Victorious, heavily wounded, mobilized for return transit"
    }
  },
  "world_state": {
    "langford": "Secured; beast incursion repelled; town under salvage operations"
  }
}
```
