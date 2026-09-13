# Pipeline Execution Artifact: Chapter 21 — The Despatch of Vyadha Block

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 21
title: "The Despatch of Vyadha Block"
word_count_target: 1500-2000
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Vyadha Block Administrative Outpost, Western Transit Yards
  atmosphere: Raw dawn fog, smell of damp pine timber, wet iron, sulfur smoke from locomotive boilers, crisp cold mountain air.
characters:
  - Chaitanya: Calm, observant, testing the balance of his field pack and inspecting iron transit tokens.
  - Bennett: Disciplined squad leader, presenting the black-wax cylinder to the duty officer.
  - Tejaswini: Stoic, clad in heavy travel woolens over armor, alert to the movement of frontier veterans.
  - Anil: Shivering in the morning chill, eager to move.
  - Warrant Officer Kaelan: Weary, scarred frontier clerk, pragmatic, unimpressed by academy ranks.
plot_beats:
  1: Unit 07 arrives at the Vyadha Block headquarters at the fourth bell of dawn.
  2: Confrontation with Warrant Officer Kaelan; breaking the pitch seal of Proctor Rao's dispatch.
  3: Official orders revealed: deployment to Langford, a frontier mining and timber hub sixty miles south.
  4: Rumors of the southern sector: irregular tremors, missing frontier patrols, corpse-packs probing perimeter palisades.
  5: Requisitioning field rations, iron train tokens, and heavy grease-tallowed oilcloths.
  6: Marching to the military rail platform as the steam locomotive fires its firebox.
invariants:
  - Zero modernisms (no tea, no couches, coal-fired steam locomotive, pine benches, earthenware cups).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Assess the logistical realities of the frontier command and verify transit routes.
    conflict: Maintaining absolute operational discipline while preparing for genuine live combat against Breach horrors.
    somatic_tells: Breath steady in white plumes, shoulders loose beneath sixty pounds of iron and canvas, eyes tracking sentry rotations.
  Warrant Officer Kaelan:
    goal: Process fresh meat for the border without wasting time on academy ceremony.
    conflict: Duty to follow proctor orders vs. cynicism toward green candidates.
    somatic_tells: Staining index finger with black ink, squinting through tobacco smoke, hacking morning cough.
  Bennett:
    goal: Establish formal military legitimacy for Unit 07.
    conflict: Burden of leadership weighing on his posture.
    somatic_tells: Standing at rigid attention, square chin lifted, grip firm on the cylinder.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "D2 throughout the administrative and logistical handover, opening to D3 as the squad enters the rail yards."
  rhythm_profile: "Military procedural pacing; short, precise observations; tactile weight of iron, canvas, and coal smoke."
  sensory_palette:
    - Olfactory: Damp oak, coal dust, wet wool, stale pipe tobacco, hot boiler oil.
    - Tactile: Cold iron transit tokens, abrasive hemp pack straps, gravel grinding under boots.
    - Auditory: Rhythmic hiss of boiler steam, clack of wooden abacus, scrape of steel pen nib.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_21_The_Despatch_of_Vyadha_Block.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 21,
  "characters": {
    "Unit_07": {
      "status": "Mobilized for Langford Frontier Station",
      "equipment": "Winter field kit, live iron munitions, travel transit tokens"
    }
  },
  "world_state": {
    "destination": "Langford (Southern Mining Valley)",
    "transit_mode": "Military Coal-Steam Transport",
    "threat_intel": "Unconfirmed beast incursions along the Fourth Trench"
  }
}
```
