# Pipeline Execution Artifact: Chapter 26 — The Cavern of the Ridge

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 26
title: "The Cavern of the Ridge"
word_count_target: 1500-2000
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Oakhaven Ridge, Upper Pine Defile, Mouth of the Beast Cavern
  atmosphere: Howling mountain wind, sharp scent of ozone and sulfur vents, pine needles frozen underfoot, ominous limestone darkness.
characters:
  - Chaitanya: Forward scout, analyzing biological scale and kinetic tracks.
  - Bennett: Heavy guard, assessing structural instability of the cavern entrance.
  - Tejaswini: Fire vanguard, holding a low-light torch, alert to heat signatures.
  - Anil: High vantage scout, tracking tree movements down the slope.
  - Lyra: Experienced guide, recognizing the anatomical signs of a Danava nesting site.
plot_beats:
  1: Ascending the dark Oakhaven Ridge under heavy overcast clouds.
  2: Discovering the mouth of the primary excavation cavern: wider than an iron rail coach, gouged from living basalt.
  3: Forensic inspection of the cavern lip: discarded chitin plates thick as iron breastplates, crushed boulders, caustic slime.
  4: Anil signals from the treetops: beast packs are already marshaling along the lower tree-line.
  5: The strategic deduction: The Danava intends to herd the townspeople into the narrow river bottlenecks.
  6: The decision: Race back to Langford to fortify the evacuation perimeter before the sun sets.
invariants:
  - Zero modernisms (no tea, no couches, birch torches, pine needles, flint strikers, rawhide straps).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Gauge the Danava’s physical mass, density, and acceleration limits from biological trace evidence.
    conflict: Time limit before the beast pack initiates the valley assault.
    somatic_tells: Kneeling in frozen mud, measuring chitin thickness with fingers, quiet unhurried respiration.
  Lyra:
    goal: Confirm the worst fears regarding frontier siege-beasts and plan a fighting withdrawal.
    conflict: Knowing the town militia stands zero chance against a Danava without military reinforcements.
    somatic_tells: Jaw clenched, arrow nocked, eyes wide and tracking darkness inside the cave.
  Bennett:
    goal: Prepare the squad for heavy impact defense.
    conflict: Realizing his ice palisades will struggle against a creature of this scale.
    somatic_tells: Testing spear point against a discarded chitin plate, grim nod.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 on the cold ridge, deepens to D3 during forensic analysis, widens to D4 strategic urgency."
  rhythm_profile: "Ominous, heavy atmospheric dread; visceral sensory evidence of titan-scale horror."
  sensory_palette:
    - Olfactory: Rotting pine mulch, sulfur fumes, caustic chitin secretions, cold ozone.
    - Tactile: Slippery shale, brittle frost needles, razor-sharp edge of monster carapace.
    - Auditory: Mountain gale howling through cave mouth, crack of snapping branches below.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_26_The_Cavern_of_the_Ridge.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 26,
  "characters": {
    "Unit_07": {
      "recon_complete": true,
      "threat_confirmed": "Tier-3 Danava active; horde mobilized for sunset descent."
    }
  },
  "world_state": {
    "location": "Oakhaven Ridge -> Langford Outskirts",
    "tactical_phase": "Transition to Full Defensive Siege"
  }
}
```
