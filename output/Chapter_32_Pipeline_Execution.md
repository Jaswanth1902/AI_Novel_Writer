# Pipeline Execution Artifact: Chapter 32 — The Hall of Weight

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 32
title: "The Hall of Weight"
word_count_target: 1200-1600
pov: Bennett (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Academy Central Corridor, Western Artillery Bastion, Armory Repair Yard
  atmosphere: Smelling of graphite grease, cold stone, iron filings, sharp mountain wind whistling through embrasures, heavy military responsibility.
characters:
  - Bennett: Squad commander, grappling with the mortality of his subordinates and the burden of command.
  - Anil: Subdued scout, learning the quiet discipline of veteran soldiers.
  - Proctor Rao: Veteran earth-master, blunt, pragmatic, offering strategic protection through hard truths.
plot_beats:
  1: Walking the echoing stone corridor of the administrative block; the isolation of leadership.
  2: Summoned to the Western Artillery Bastion; the smells and sounds of siege weapon repair.
  3: Proctor Rao conducts a private, unvarnished debrief with Bennett and Anil.
  4: The grim frontier truth: the Langford Danava was an outrunner; the spring Breach thaw will be catastrophic.
  5: The political threat: Inscription Preceptors probing Unit 07's anomalies.
  6: The path forward: The Grand Selection Tournament announced. Winning is the only shield against the Tribunal.
invariants:
  - Zero modernisms (no tea, no couches, graphite grease, ballista carriages, iron braziers).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Bennett:
    goal: Secure the survival and operational autonomy of Unit 07.
    conflict: Physical vulnerability from broken ribs vs. need to project unyielding strength.
    somatic_tells: Tight grip on crutch, jaw clenching against chest pain, eyes locked with Rao's.
  Proctor Rao:
    goal: Prepare these boys for the political and martial storm heading toward them.
    conflict: Affection for these promising warriors vs. the brutal realities of imperial politics.
    somatic_tells: Wiping greasy hands on leather apron, spitting into sawdust box, voice deep as bedrock.
  Anil:
    goal: Understand the broader strategic landscape beyond his personal survival.
    conflict: Anxiety over the impending tournament.
    somatic_tells: Standing straight, arms at his sides, head tilted attentively.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D3 internal reflection in the corridor, deepens to D2 sensory industrial weight in the bastion, widens to D4 imperial geopolitics."
  rhythm_profile: "Somber, heavy, authoritative; cadence of iron and stone."
  sensory_palette:
    - Olfactory: Graphite lubricant, cold iron filings, stale tobacco, bitter river fog.
    - Tactile: Cold limestone walls, abrasive wooden crutch head, rough iron ballista gears.
    - Auditory: Ringing hammers on iron rivets, creak of heavy timber winches, wind through arrow slits.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_32_The_Hall_of_Weight.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 32,
  "characters": {
    "Bennett": {
      "command_resolve": "Steeled to lead Unit 07 into the Grand Tournament"
    },
    "Unit_07": {
      "strategic_directive": "Must win the Selection Tournament to secure immunity from Inscription scrutiny"
    }
  },
  "world_state": {
    "looming_event": "The Grand Vanguard Selection Tournament",
    "threat_intel": "Breach spring thaw will unleash massive Danava migrations"
  }
}
```
