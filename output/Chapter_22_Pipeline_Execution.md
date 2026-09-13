# Pipeline Execution Artifact: Chapter 22 — The Iron Rails to Langford

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 22
title: "The Iron Rails to Langford"
word_count_target: 1500-2000
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Rail Coach interior, mountain defiles, Langford Freight Platform, Muddy Thoroughfare
  atmosphere: Rattle of iron trucks, acrid coal soot, grey mountain drizzle, smell of wet shale, stagnant canal water, and nervous town militia.
characters:
  - Chaitanya: Observant, reading the geography and the psychological state of the frontier town.
  - Bennett: Direct, formal squad commander maintaining military protocol.
  - Tejaswini: Stoic noble warrior, familiar with the historical lore of the southern valley.
  - Anil: Restless, agile scout chafing at the enclosed train coach.
  - Lyra: Frontier scout operative, cynical, razor-tongued, deeply experienced with beast habits.
plot_beats:
  1: The transit through the Oakhaven mountain cut; tactile sensations of the steam train.
  2: Tejaswini and Chaitanya discuss the strategic isolation of Langford.
  3: Arrival at Langford station; the sullen, fearful atmosphere of the local miners and militia.
  4: Encounter with Lyra under the dripping timber canopy of the freight shed.
  5: Lyra's sharp, contemptuous triage of the candidate squad; Bennett's stoic response.
  6: Trek through the muddy streets of Langford toward the municipal requisition depot.
invariants:
  - Zero modernisms (no tea, no couches, coal-fired locomotive, oilcloth coats, muddy planks).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Gauge Lyra's competence and study the physical terrain of Langford for defensive chokepoints.
    conflict: Navigating Lyra's immediate disdain without displaying unearned arrogance.
    somatic_tells: Stable footing despite train car swaying, relaxed hands resting on pack straps, sharp peripheral gaze.
  Lyra:
    goal: Assess whether these green academy arrivals will be an asset or a lethal liability in the field.
    conflict: Bitterness over being saddled with 'pampered academy prodigies' vs. desperate need for reinforcements.
    somatic_tells: Chewing dried clover stem, cold grey eyes dissecting their gear, hand resting naturally on knife hilt.
  Bennett:
    goal: Assert Unit 07's operational standing and maintain chain of command.
    conflict: Resentment of Lyra's disrespect vs. military professionalism.
    somatic_tells: Chest squared, deep gravelly voice, jaw set tight against insult.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 inside the moving coach, deepens to D3 during dialogue, narrows to D2 upon setting foot in Langford's mud."
  rhythm_profile: "Locomotive kinetic rhythm shifting into cold, sullen frontier realism."
  sensory_palette:
    - Olfactory: Coal smoke, wet timber, damp horse manure, rotting pine needles, river fog.
    - Tactile: Slippery mud under iron-shod boots, cold drizzle on earlobes, oily canvas.
    - Auditory: Squeal of iron brake shoes, rhythmic drip of water from eaves, hollow rattle of crossbow bolts in wood quivers.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_22_The_Iron_Rails_to_Langford.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 22,
  "characters": {
    "Unit_07": {
      "location": "Langford",
      "status": "Arrived on site; under operational briefing with Operative Lyra."
    },
    "Lyra": {
      "role": "Frontier Reconnaissance Liaison",
      "disposition": "Skeptical, demanding, combat-hardened."
    }
  },
  "world_state": {
    "town_condition": "Langford under quiet panic; miners refusing night shifts; militia on edge."
  }
}
```
