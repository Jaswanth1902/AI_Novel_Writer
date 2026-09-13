# Pipeline Execution Artifact: Chapter 27 — The Broken Bells of Langford

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 27
title: "The Broken Bells of Langford"
word_count_target: 1500-2000
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Langford Main Thoroughfare, Western Palisade Breach, Freight Station Sidings
  atmosphere: Smelling of sulfur smoke, burning pine tar, coal soot, cold rain, panicked crowds, and screeching corpse-beasts.
characters:
  - Chaitanya: Rear-guard point anchor, calculating choke-point throughput and kinetic vectors.
  - Bennett: Heavy defensive anchor, holding the ice palisade against the vanguard assault.
  - Tejaswini: Fire exterminator, maintaining a continuous thermal barrier across the avenue.
  - Anil: Rooftop skirmisher, directing traffic and neutralizing airborne leapers.
  - Lyra: Evacuation coordinator, loading civilians onto the military coal train.
plot_beats:
  1: Panic in Langford: bells tolling, frantic crowds surging toward the rail siding.
  2: The western palisade collapses under the initial charge of the Rakshasa and Vetala vanguard.
  3: Bennett erects the central ice-gravel bulwark to funnel the horde into the warehouse corridor.
  4: Anil provides rooftop suppression with downdrafts and sulfur darts.
  5: Tejaswini incinerates the vanguard with a sustained thermal sweep.
  6: Sudden seismic silence: the ground shakes as the Danava steps onto the main road.
invariants:
  - Zero modernisms (no tea, no couches, coal-fired locomotive, torchlight, pine barricades).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Channel civilian evacuation safely to the train and position Unit 07 for the primary siege-beast impact.
    conflict: Conserving energy for the Danava while holding the line against overwhelming minor beast numbers.
    somatic_tells: Breathing slow and deep, hands empty, eyes tracking the structural integrity of the street walls.
  Bennett:
    goal: Prevent the vanguard from flanking the fleeing townspeople.
    conflict: Sustaining massive ice structures in muddy, non-subzero conditions.
    somatic_tells: Teeth bared, forearms trembling from cold conduit strain, boots sunk deep in mud.
  Tejaswini:
    goal: Exterminate the necrotic vanguard with zero civilian collateral damage.
    conflict: Extreme core heat expenditure.
    somatic_tells: Hair escaping pins, sweat steaming from collar, eyes blazing with amber intensity.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 amidst chaotic civilian flight, narrows to D2 visceral combat action, broadens to D4 dread at the final tremor."
  rhythm_profile: "Percussive, rapid military pacing; stark auditory contrasts between civilian terror and disciplined defense."
  sensory_palette:
    - Olfactory: Coal smoke, burning pitch, charred hair, sulfur bile, ozone.
    - Tactile: Slippery mud, scorching heat of flame-sheets, biting chill of ice ramparts.
    - Auditory: Clanging bronze bell, shriek of dying Rakshasas, thunderous rhythmic footsteps.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_27_The_Broken_Bells_of_Langford.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 27,
  "characters": {
    "Unit_07": {
      "rear_guard_held": true,
      "civilian_status": "Evacuation train 90% loaded"
    }
  },
  "world_state": {
    "town_status": "Western wall destroyed; Langford burning.",
    "boss_arrival": "Tier-3 Danava engaged on the main avenue."
  }
}
```
