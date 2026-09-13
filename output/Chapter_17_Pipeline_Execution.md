# Pipeline Execution Artifact: Chapter 17 — The Four Vanguard

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 17
title: "The Four Vanguard"
word_count_target: 1800-2400
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Candidate Barracks Quarter, Armory Porch, Western Carriage Gate, Quarters Common Room
  atmosphere: Clear late-autumn chill, smell of harness oil, sharp sound of whetstones on iron, wood smoke curling from perimeter braziers.
characters:
  - Chaitanya: Calm, observant, anchoring the squad through steady presence.
  - Bennett: Practical, disciplined northern ice specialist, focused on equipment integrity and survival protocols.
  - Anil: High-energy, agile scout, masking underlying anxiety with light banter.
  - Tejaswini: Noble, burdened by House Varma's lineage expectations, leaving on temporary leave before deployment.
plot_beats:
  1: Four days of rigorous routine: dawn runs, stone weights, weapon maintenance, tactical terrain maps.
  2: Armory porch banter: Anil complains of dried mutton rations while Bennett methodically oils iron spearheads.
  3: Tejaswini's temporary departure: carriage arrival at the western gate, filial obligations to House Varma, a quiet, charged farewell with Chaitanya.
  4: Bennett returns from the Registry with the red-wax dispatch: official formation of Vanguard Unit 7.
  5: Inspection of combat kit: tallowed boots, dried pemmican, signal whistles, sulfur flares.
  6: Anticipation of the weekend's first field trial; the calm before the storm.
invariants:
  - Strict absence of modern items (no tea, no couches, pine benches, tallow lamps, leather pouches).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Maintain operational balance, observe squad cohesion, and prepare for unknown field threats.
    conflict: Internalizing the forbidden mechanics while maintaining the facade of a disciplined wind cadet.
    somatic_tells: Relaxed shoulders, hands steadily binding leather wraps around boot ankles, steady respiration.
  Bennett:
    goal: Ensure zero equipment failure and confirm the legal standing of their unit.
    conflict: Pragmatic caution vs. the lethal realities of the frontier redoubts.
    somatic_tells: Calloused thumbs checking blade edges, deliberate slow speech, smell of lard and lamp oil on his knuckles.
  Anil:
    goal: Prove his agility and shake off the nervous dread of monster encounters.
    conflict: Eagerness to fight vs. instinctual fear of corpse-beasts.
    somatic_tells: Bouncing on the balls of his feet, twirling an iron dart between nimble fingers, nervous grin.
  Tejaswini:
    goal: Satisfy patriarchal clan duties without revealing her pact with Chaitanya.
    conflict: Family pressure to accept a safe capital commission vs. her sworn oath to stand at Chaitanya's side.
    somatic_tells: Rigid posture, fingers tightening around the gold-embroidered family signet, dark eyes holding Chaitanya's before stepping into the carriage.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "D2 during physical training and equipment prep; D3 during interpersonal dialogue; D4 briefly during the parting at the carriage."
  rhythm_profile: "Steady, rhythmic pacing capturing military domesticity, punctuated by tactile gear sounds and crisp dialogue."
  sensory_palette:
    - Olfactory: Neatsfoot oil, cold iron, horse sweat, boiled barley, dried clover.
    - Tactile: Abrasive whetstone slate, cold brass buckles, rough sheepskin linings.
    - Auditory: Rasp of file against spear-edge, clop of iron-shod hooves on gravel, crackle of cedar logs in the yard brazier.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_17_The_Four_Vanguard.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 17,
  "characters": {
    "Chaitanya": {
      "role": "Informal tactical core of Unit 7",
      "focus": "Refining pressure manipulation during private rest hours"
    },
    "Tejaswini": {
      "status": "On 36-hour filial leave to House Varma estate",
      "allegiance": "Firmly pledged to the squad over clan safety"
    },
    "Bennett": {
      "official_designation": "Squad Leader / Heavy Anchor of Unit 7"
    },
    "Anil": {
      "role": "Scout / Skirmisher"
    }
  },
  "world_state": {
    "unit_status": "Officially chartered Vanguard Strike Unit 7",
    "timeline": "Four days post-awakening; field trial scheduled for weekend"
  }
}
```
