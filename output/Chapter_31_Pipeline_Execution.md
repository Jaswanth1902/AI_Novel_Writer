# Pipeline Execution Artifact: Chapter 31 — The Morning of Unspoken Questions

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 31
title: "The Morning of Unspoken Questions"
word_count_target: 1200-1600
pov: Bennett (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Candidate Quarters, Inner Infirmary Corridor, Quadrangle
  atmosphere: Cold morning fog, smell of pine ash, wet stone, bitter herbal tinctures, heavy respectful silence from passing cadets.
characters:
  - Bennett: Wounded squad leader, coping with broken ribs and the weight of command.
  - Anil: Subdued, checking his leather wraps, observing the changed mood of the academy.
  - Tejaswini: Exhausted, standing guard at Chaitanya’s infirmary door.
  - Chaitanya: Comatose in the inner sanctuary, pulse stabilizing.
plot_beats:
  1: Dawn in the shared quarters; waking to the quiet ache of healing bones and unspoken memories.
  2: Bennett and Anil prepare for the day without their usual banter; the shared weight of survival.
  3: Walking through the central quadrangle; junior cadets stopping in their tracks to stare in hushed reverence.
  4: Visiting the inner infirmary; two Veteran Guards in fluted iron armor guarding the portal.
  5: Tejaswini refuses to leave the bedside; the cold room smelling of dried yarrow and mountain moss.
  6: The unspoken question: what will happen to the Academy when Chaitanya opens his eyes?
invariants:
  - Zero modernisms (no tea, no couches, pine pallets, herbal poultices, iron sconces).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Bennett:
    goal: Maintain squad routine and protect Chaitanya's perimeter while managing physical pain.
    conflict: Internal guilt over having his ice wall smashed vs. pride in their collective survival.
    somatic_tells: Right hand unconsciously pressing his bound ribs, jaw tight, footsteps heavy and slow.
  Tejaswini:
    goal: Guard Chaitanya's recovery and prevent intrusive preceptors from examining his core.
    conflict: Extreme sleep deprivation threatening her noble composure.
    somatic_tells: Hollowed cheekbones, fingers lightly resting on the scabbard of her sabre, dark vigilant eyes.
  Anil:
    goal: Prove that he can be dependable in the aftermath.
    conflict: Lingering phantom terror of the Danava’s backhand.
    somatic_tells: Limping slightly on his left leg, shoulders squared, quiet tone.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 physical stiffness in the barracks, moves to D3 psychological weight of command, settles at D2 quiet intimacy in the infirmary."
  rhythm_profile: "Slow, measured, introspective; tactile focus on physical soreness, bandages, and morning silence."
  sensory_palette:
    - Olfactory: Pine needle floor wax, vinegar liniment, boiled barley, dried yarrow.
    - Tactile: Tight linen binding around ribs, cold bronze door latches, rough woolen blankets.
    - Auditory: Muffled footsteps on damp flagstones, crackle of cold tallow wicks, steady deep breathing.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_31_The_Morning_of_Unspoken_Questions.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 31,
  "characters": {
    "Chaitanya": {
      "status": "Comatose, stable, breathing deepening"
    },
    "Unit_07": {
      "cohesion": "Tied by shared trauma and secret blood-pact",
      "academy_standing": "Treated as living legends by cadet body"
    }
  },
  "world_state": {
    "location": "Tattva Academy Infirmary & Quarters",
    "phase": "Post-battle decompression"
  }
}
```
