# Pipeline Execution Artifact: Chapter 35 — The Stirring in the Quiet

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 35
title: "The Stirring in the Quiet"
word_count_target: 1200-1600
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Inner Infirmary Sanctuary, Dormitory Corridors, Unit 07 Quarters
  atmosphere: Cool moonlight, quiet corridors, warm glow of the iron stove, smell of wood smoke, bone broth, and unspoken relief.
characters:
  - Chaitanya: Fully restored, possessing deeper meridian equilibrium, calm and commanding.
  - Tejaswini: Radiant relief, fierce emotional connection, steadfast partner.
  - Bennett: Stunned squad leader, immense professional and personal gratitude.
  - Anil: Overjoyed scout, enthusiastic, energized by their leader's return.
plot_beats:
  1: Chaitanya speaks to Tejaswini in the moonlight; the intimate reality of their shared survival.
  2: Somatic inventory: testing joint mobility and verifying the internal integration of the primordial grammar.
  3: Quiet walk through the midnight corridors back to the candidate barracks.
  4: The unexpected entrance: Anil and Bennett stunned as Chaitanya steps through the door unassisted.
  5: Shared reunion by the iron stove: warm broth, camaraderie, and laughter in the dark.
  6: Bennett introduces the tournament directive; Chaitanya accepts the challenge of the Grand Arena.
invariants:
  - Zero modernisms (no tea, no couches, iron stove, bone broth, pine benches, tallow lamps).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Reassure his squad, assess their tactical readiness, and ground his newly integrated meridian balance.
    conflict: None; absolute clarity of purpose.
    somatic_tells: Fluid unhurried movements, steady warm respiration, gentle touch on Tejaswini's temple.
  Tejaswini:
    goal: Ensure Chaitanya does not overexert his newly knitted frame while allowing herself to breathe again.
    conflict: Maintaining military composure vs. overwhelming tenderness.
    somatic_tells: Damp eyes blinking fast, lips trembling into a smile, walking shoulder-to-shoulder with him.
  Bennett & Anil:
    goal: Welcome their comrade back from the brink of death.
    conflict: Speechless awe giving way to boisterous relief.
    somatic_tells: Bennett's broad hand clasping Chaitanya's uninjured shoulder; Anil scrambling to ladle broth.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D3 intimate moonlight dialogue, widens to D2 sensory physical movement through corridors, settles at D2 warm domestic camaraderie."
  rhythm_profile: "Lyrical quiet opening into rhythmic, joyous dialogue and crisp military focus."
  sensory_palette:
    - Olfactory: Camphor, moonlight mist, hot beef broth, dry oak smoke, clean wool.
    - Tactile: Warm ceramic bowl in cold palms, firm grip of an iron-hard hand clasp, cold flagstones under boots.
    - Auditory: Quiet whisper in the dark, sudden scrape of a chair, laughter stifled against dorm walls.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_35_The_Stirring_in_the_Quiet.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 35,
  "characters": {
    "Chaitanya": {
      "status": "Fully conscious, mobile, integrated primordial meridian lattice",
      "location": "Unit 07 Dormitory Quarters"
    },
    "Unit_07": {
      "morale": "Peak; unified in preparation for the Grand Tournament"
    }
  },
  "world_state": {
    "squad_state": "Complete four-man vanguard reconstituted"
  }
}
```
