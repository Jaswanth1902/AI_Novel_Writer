# Pipeline Execution Artifact: Chapter 23 — War-Room in the Mist

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 23
title: "War-Room in the Mist"
word_count_target: 1500-2000
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Langford Municipal Storehouse, Trestle Planning Room
  atmosphere: Smelling of damp grain, sheep tallow, wet slate, bitter barley broth, outside river mist pressing against barred windows.
characters:
  - Chaitanya: Analytical point guard, studying terrain topology and hydrological gradients.
  - Lyra: Tactical briefing lead, blunt, battle-hardened frontier scout.
  - Bennett: Squad commander, recording defensive variables and logistics.
  - Tejaswini: Fire specialist, assessing combustion zones and civilian containment lines.
  - Anil: Mobile scout, assessing vantage points and vertical retreat paths.
plot_beats:
  1: Establishment of the forward operations post in the stone storehouse.
  2: Meal of boiled grain mash and salt fish; physical decompression from the train ride.
  3: Lyra unrolls the charcoal terrain map of Langford; details the three anomaly clusters.
  4: The tactical reality of the Breach: corpse-packs as vanguard harbingers of a Danava siege-beast.
  5: Division of squad roles and tactical responsibilities.
  6: Target selection: immediate departure for the Old Water Mill on the northern perimeter.
invariants:
  - Zero modernisms (no tea, no couches, charcoal maps, tallow dips, wooden bowls).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Identify the underlying pattern linking the three anomaly sites.
    conflict: Concealing his non-traditional aerodynamic sensory detection from Lyra while providing accurate assessments.
    somatic_tells: Tracing map elevation lines with blunt index finger, steady breathing, eyes evaluating timber roof supports.
  Lyra:
    goal: Drill survival discipline into the squad and establish absolute operational control.
    conflict: Grudging recognition of the squad's competence vs. ingrained cynicism.
    somatic_tells: Tapping iron bodkin point on map, leaning over the table, hoarse whisper.
  Tejaswini:
    goal: Demonstrate noble military capability and prepare fire assets for immediate deployment.
    conflict: Suppressing aristocratic friction with Lyra.
    somatic_tells: Straight posture, checking sabre scabbard lock, steady amber warmth radiating from palms.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 inside the cold storehouse, focuses to D3 during map briefing, expands to D4 tactical foresight."
  rhythm_profile: "Deliberate, strategic, clinical; tension building through environmental details and beast ecology."
  sensory_palette:
    - Olfactory: Damp grain dust, sheep tallow, boiled barley, cold river mud, grease.
    - Tactile: Rough splintered oak, damp sheepskin, cold iron dagger point.
    - Auditory: Rain beating on roof slate, guttering tallow flame, rasp of charcoal on sheepskin vellum.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_23_War-Room_in_the_Mist.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 23,
  "characters": {
    "Unit_07": {
      "briefing_complete": true,
      "current_objective": "Reconnaissance at the Old Water Mill"
    },
    "Lyra": {
      "alliance_status": "Cautious operational partnership with Unit 07"
    }
  },
  "world_state": {
    "threat_assessment": "Coordinated corpse-type vanguard active in Langford; possible Tier 3 Danava backing."
  }
}
```
