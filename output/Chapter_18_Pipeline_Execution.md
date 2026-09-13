# Pipeline Execution Artifact: Chapter 18 — The Shadow of the Bestiary

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 18
title: "The Shadow of the Bestiary"
word_count_target: 1800-2400
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Sunken Amphitheater (Ordnance Hall), Lower Quarry Proving Grounds
  atmosphere: Chalk dust, smell of old paper and bitter tea-substitutes (roasted chicory/millet), shifting to raw cold stone, sulfur, and static electricity in the quarry pit.
characters:
  - Chaitanya: Analytical, memorizing biological weak points and calculating spatial vectors.
  - Master Gopinath: One-armed veteran instructor, cynical, scarred from the Breach wars.
  - Tejaswini: Returned from House Varma, fully armed and armored, focused and lethal.
  - Bennett & Anil: Squad cohesion, grim focus mixed with tense tactical banter.
  - Proctor Rao: Mountainous earth-master in jointed basalt armor.
  - Proctor Meera: Lightning specialist, twitching with high-voltage electrostatic tension.
plot_beats:
  1: The Bestiary lecture in the amphitheater: Gopinath detailing Tier 1 (Rakshasa), Tier 2 (Vetala/Pishacha corpse-types), Tier 3 (Danavas), and Tier 4 (Asuras).
  2: Somatic realities of monster anatomy: marrow toxins, chitin density, sound-mimicry of the Vetala.
  3: Tejaswini’s return; unblemished armor, quiet arrival, wordless solidarity with Chaitanya.
  4: Sudden alarm bells: redirection to the Lower Quarry proving grounds for the live-trial evaluation.
  5: The arena environment: limestone scree, quarried monoliths, howling wind.
  6: Confrontation with Proctor Rao and Proctor Meera; the challenge laid down with live steel.
invariants:
  - Strict absence of modernisms (no couches, no tea, chalk boards, parchment scrolls, oil lanterns).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Absorb anatomical data to anticipate kinetic weaknesses; prepare to shield squad during unexpected ambush.
    conflict: Balancing disciplined concealment with the lethal necessity of surviving veteran proctors.
    somatic_tells: Eyes tracking the tension in Meera's copper batons, fingers testing the balance of his boot-knife, quiet diaphragmatic breaths.
  Master Gopinath:
    goal: Drill survival paranoia into green cadets before they are slaughtered on the frontier.
    conflict: Contempt for academy theory vs. urgency to keep these youths alive.
    somatic_tells: Scraping iron hook against wooden lectern, coughing up slate grit, rasping voice.
  Proctor Rao:
    goal: Break the arrogance of the candidate vanguard and test their physical threshold under crushing mass.
    conflict: Duty to evaluate vs. natural brutality of a seasoned earth soldier.
    somatic_tells: Shifting stone greaves, grinding molars, heavy rhythmic breathing.
  Proctor Meera:
    goal: Punish hesitation and test reaction speed with blinding velocity.
    conflict: Relentless military perfectionism.
    somatic_tells: Sparks snapping from fingertips, twitching eyelids, restless shifting weight.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 in the academic amphitheater, moves to D3 as the lore tightens, opens to D2-D4 in the quarry arena."
  rhythm_profile: "Authoritative, clinical taxonomy during the lecture; heavy, foreboding acoustic weight in the quarry."
  sensory_palette:
    - Olfactory: Dry chalk, roasted barley, sour slate dust, sharp ozone, cold grease.
    - Tactile: Chipped limestone benches, vibration of ground tremors, prickly hair standing on arms from static charge.
    - Auditory: Hook tapping on slate, hollow blast of warning horns, metallic hum of copper batons.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_18_The_Shadow_of_the_Bestiary.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 18,
  "characters": {
    "Chaitanya": {
      "knowledge": "Mastered the anatomical vulnerabilities of Tiers 1-4 monsters.",
      "combat_stance": "Prepared for unscripted engagement against Proctor Meera and Rao."
    },
    "Tejaswini": {
      "status": "Rejoined Unit 07 with ancestral cavalry sabre and flame focus."
    },
    "Unit_07": {
      "formation": "Deployed in the Lower Quarry for graded live-steel trial."
    }
  },
  "world_state": {
    "location": "Lower Quarry Proving Grounds",
    "threat_level": "Immediate: Two veteran Imperial Proctors engaging with lethal intent."
  }
}
```
