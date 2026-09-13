# Pipeline Execution Artifact: Chapter 15 — A Secret from the World

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 15
title: "A Secret from the World"
word_count_target: 1800-2400
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Sub-Archive Ascent, Main Scriptoria Hall, Courtyard at Dawn, Mess Hall (Barracks Trestles)
  atmosphere: Pre-dawn chill, smell of damp granite and tallow smoke, cold river mist clinging to limestone flags, harsh warmth of steaming barley mash.
characters:
  - Chaitanya: Calm, carrying the physical weight of forbidden knowledge, steady pulse, sharp tactile focus.
  - Old Nikos: Night archivist, suspicious, bleary-eyed, smelling of bitter chicory and dry ink.
  - Anil: Half-asleep roommate, snoring on pallet, oblivious.
  - Tejaswini: Alert, guarded, burning with unspoken tension, fiercely loyal beneath her noble composure.
plot_beats:
  1: Chaitanya emerges from the sub-archive stone shaft, resealing the subterranean flagstone with silent breath control.
  2: Confrontation in the upper Great Archive with Old Nikos; Chaitanya deflects scrutiny with architectural pretexts.
  3: Return to the barracks before dawn horn; ritual cold-water wash, resetting physical composure.
  4: Breakfast mess hall; rough pine benches, salt fish, steamed grain broth. The crowded room contrasts with intimate silence.
  5: The whispered question: "Can you keep a secret from the entire world for me?" Tejaswini's visceral autonomic reaction and unwavering affirmation.
  6: Rendezvous set for the secluded Fourth Practice Yard at the western bluffs.
invariants:
  - Zero modernisms (no tea, no couches, whale oil/tallow, stoneware bowls).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Reseal the forbidden archive entrance, evade Nikos's gaze, and secure Tejaswini's absolute confidence without exposing his breakthrough to the academy wardens.
    conflict: The weight of breaking the Imperial Fourfold Order creates lethal stakes; one slip of tongue means execution by the Inscription Tribunal.
    somatic_tells: Steady respiration, slow pulse, muscles taut from cold granite contact, eyes alert to ambient air pressure changes.
  Old Nikos:
    goal: Catch late-night rule-breakers or protect archive relics from careless adepts.
    conflict: Drowsiness vs. institutional paranoia.
    somatic_tells: Yellowed thumbnail picking at candle wax, rasping throat, rheumy eyes squinting through brass-rimmed spectacles.
  Tejaswini:
    goal: Understand Chaitanya's sudden withdrawal and read the true intention behind his guarded eyes.
    conflict: Deep aristocratic discipline clashing with intense, personal devotion to him.
    somatic_tells: Knuckles pale around a stoneware bowl, flame-aura micro-flares beneath skin, shallow rapid breath, jaw locked tight.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 (cold masonry ascent), deepens to D4 (internal friction of forbidden grammar), pulls to D3 during dialogue in mess hall."
  rhythm_profile: "Short, sharp sensory cadences during evasion; measured, quiet tension during the breakfast dialogue."
  sensory_palette:
    - Olfactory: Damp cellar mold, stale tallow, charred grain porridge, cold morning river mist.
    - Tactile: Abrasive limestone grit, icy well water against bare collarbones, rough splinters of pine trestles.
    - Auditory: Rasp of iron hinges, distant cadence of morning reveille horns, clatter of pewter spoons.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_15_A_Secret_from_the_World.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 15,
  "characters": {
    "Chaitanya": {
      "mental_state": "Resolute, carrying dangerous knowledge of constraint collapse.",
      "pact_formed": true,
      "confidante": "Tejaswini"
    },
    "Tejaswini": {
      "emotional_state": "Heightened apprehension, fierce loyalty solidified.",
      "commitment": "Agreed to meet at the Fourth Practice Yard."
    },
    "Old Nikos": {
      "suspicion_level": "Mildly deflected, but watchful."
    }
  },
  "world_state": {
    "time": "Dawn of the 5th day post-awakening",
    "location": "Academy Barracks & Mess Hall",
    "approaching_event": "Private duel at the Fourth Practice Yard"
  }
}
```
