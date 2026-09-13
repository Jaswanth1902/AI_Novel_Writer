# Pipeline Execution Artifact: Chapter 33 — Motion and Intent

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 33
title: "Motion and Intent"
word_count_target: 1200-1600
pov: Tejaswini (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Academy Training Grounds, Sand Rings, Third Quarry Ring, Inner Infirmary
  atmosphere: Smelling of scorched sand, ozone, crushed limestone, freezing vapor, sweat, pine needles, and quiet determination.
characters:
  - Tejaswini: Burning with protective fury, pushing her fire output to sustainable thresholds.
  - Bennett: Grounded, practicing deep subterranean ice anchoring despite broken ribs.
  - Anil: Aerial skirmisher, drilling high-velocity directional snaps.
  - Chaitanya: Motionless in the infirmary, internal meridians slowly knitting under primordial resonance.
plot_beats:
  1: The Academy shifts into full war-footing; training fields filled with relentless elemental drilling.
  2: Bennett practices deep foundation ice-anchoring to counter heavy siege impacts.
  3: Anil trains against practice ballista bolts, mastering rapid aerial deceleration.
  4: Tejaswini in the Third Quarry: refining heat-curtain efficiency to avoid core exhaustion.
  5: The collective realization that they must be strong enough to stand beside Chaitanya when he wakes.
  6: Tejaswini’s evening return to the infirmary; holding Chaitanya's hand as the third day of training ends.
invariants:
  - Zero modernisms (no tea, no couches, sand rings, oak targets, tallow lamps, cold basins).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Tejaswini:
    goal: Expand her thermal endurance to ensure she never runs dry during Chaitanya’s defense.
    conflict: Physical fatigue vs. burning determination.
    somatic_tells: Blistered palms callousing over, sweat stinging eyes, breathing locked to three-beat rhythm.
  Bennett:
    goal: Master deep foundation rooting to absorb kinetic shock without breaking ribs.
    conflict: Working through sharp bone pain.
    somatic_tells: Kneeling in sand, hands buried six inches in grit, grimacing as stone shifts.
  Anil:
    goal: Become untouchable in mid-air.
    conflict: Fear of being crushed again fueling hyper-vigilance.
    somatic_tells: Rapid footwork, agile twists, gasping breaths between arrow volleys.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 wide kinetic training panoramic, narrows to D2 individual discipline, finishes at D3 intimate devotion in the infirmary."
  rhythm_profile: "Percussive martial rhythm, sweat and physical exertion, transitioning into quiet nocturnal stillness."
  sensory_palette:
    - Olfactory: Scorched sand, hot sulfur oil, pine smoke, cold river mud, camphor.
    - Tactile: Abrasive red sand, blistering heat on knuckles, cold linen sheets.
    - Auditory: Roar of flame jets, thud of practice ballista bolts into timber, quiet rhythmic breathing.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_33_Motion_and_Intent.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 33,
  "characters": {
    "Unit_07": {
      "training_progress": "Subterranean anchoring (Bennett), Aerial evasion (Anil), Thermal efficiency (Tejaswini)",
      "chaitanya_recovery": "Meridians stabilizing; external breathing regular"
    }
  },
  "world_state": {
    "academy_atmosphere": "Total mobilization for the Vanguard Tournament"
  }
}
```
