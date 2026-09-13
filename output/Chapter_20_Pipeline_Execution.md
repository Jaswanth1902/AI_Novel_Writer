# Pipeline Execution Artifact: Chapter 20 — The Call to Vyadha Block

---

## Stage 1: YAML Scene Contract

```yaml
chapter: 20
title: "The Call to Vyadha Block"
word_count_target: 1800-2400
pov: Chaitanya (Third-Person Limited, Gardner Distance D2-D4)
setting:
  primary: Lower Quarry Pit (scorched limestone, smoking slag), Proctors' Field Pavilion, South-facing Bluff
  atmosphere: Acrid smoke of extinguished flames, sharp ozone, cold dusk settling over the valley, shadows lengthening across the jagged mountain peaks.
characters:
  - Chaitanya: Calm, recovering physical energy, maintaining his cover under Meera's piercing scrutiny.
  - Tejaswini: Exhausted but victorious, proud, unyielding solidarity with the squad.
  - Bennett: Bruised, pragmatic, nursing a strained shoulder while checking his spearhead.
  - Anil: Sprawled on stone, bruised, boasting with weary relief.
  - Proctor Rao: Grudging respect, battlefield veteran giving brutal, honest tactical critique.
  - Proctor Meera: Suspicious, analytical lightning bender, probing Chaitanya's unorthodox defense.
plot_beats:
  1: The proctors yield: Rao's booming surrender and Meera's cold, measured sheath of her batons.
  2: The physical cost: the squad collapses onto the limestone; shared water skin; somatic recovery.
  3: The debrief: Rao’s tactical critique of their positioning and Bennett's ice anchorage.
  4: Meera corners Chaitanya: questions the physics of how he grounded her lightning without earth or water seals; Chaitanya deflects with ionization mechanics.
  5: The Black-Wax Dispatch: Rao presents the iron cylinder bearing the signet of Vyadha Block—the front-line fortress at the Breach.
  6: Departure orders: packing at dawn; Unit 07 stands as true soldiers, facing the dark frontier.
invariants:
  - Strict absence of modernisms (no tea, no couches, well-water from skin flasks, iron tallow lamps).
  - Zero filter verbs (no "he felt", "she noticed", "he wondered").
  - Em-dash ceiling: <= 2 across entire chapter.
```

---

## Stage 2: Actor Envelopes

```yaml
actors:
  Chaitanya:
    goal: Secure the passing evaluation, protect his heretical principles from Meera's sharp intuition, and prepare for the true crucible at the frontier.
    conflict: Surviving Meera's cross-examination without raising red flags to the Inscription Preceptors.
    somatic_tells: Deliberate, even swallowing of cold water, maintaining steady eye contact, hands resting quietly on knees.
  Tejaswini:
    goal: Validate the squad's standing and stand as an impenetrable wall between Chaitanya and inquisitive proctors.
    conflict: Physical fatigue from high-output fire deployment.
    somatic_tells: Soot on cheekbones, breathing through the nose to steady pulse, hand resting on sabre hilt.
  Proctor Rao:
    goal: Verify that these candidates can handle real death without breaking.
    conflict: Reluctant admiration vs. veteran cynicism.
    somatic_tells: Spitting red quarry dust, rubbing his fractured basalt armor with a chuckle, loud booming cadence.
  Proctor Meera:
    goal: Pierce the anomaly of Chaitanya’s defense and understand how a wind-user defeated lightning without conductive tools.
    conflict: Instinct that something is deeply irregular vs. lack of empirical proof.
    somatic_tells: Narrowed eyelids, fingers drumming on copper batons, head tilted like a hawk watching prey.
```

---

## Stage 3: Stylist Config

```yaml
stylist:
  distance_shift: "Begins at D2 in the smoking debris of the arena, moving to D3 during the tense debrief and Meera's interrogation, widening to D4 in the final vista toward the Breach."
  rhythm_profile: "Lyrical exhaustion giving way to militaristic, razor-sharp dialogue and solemn thematic weight."
  sensory_palette:
    - Olfactory: Scorched basalt, sweet metallic tang of molten copper, cold water from pigskin flask, pine smoke at twilight.
    - Tactile: Bruised muscles aching in the chill, rough limestone under palms, cold iron seal on parchment.
    - Auditory: Ringing bells fading into dusk wind, clatter of sheathed steel, gravel crunching under boots.
  em_dash_budget: 1
```

---

## Stage 4: Clean Prose Manuscript

*(See separate file: `Chapter_20_The_Call_to_Vyadha_Block.md`)*

---

## Stage 5: Delta State JSON

```json
{
  "chapter": 20,
  "characters": {
    "Chaitanya": {
      "reputation": "Recognized as tactical genius by veteran proctors; secretly monitored by Proctor Meera.",
      "readiness": "Mobilized for active frontier deployment."
    },
    "Unit_07": {
      "status": "Graduated to Active Vanguard Strike Unit.",
      "deployment_destination": "Vyadha Block (The Southern Breach Frontier)",
      "departure_time": "Dawn"
    }
  },
  "world_state": {
    "location": "Lower Quarry -> Academy Barracks",
    "arc_milestone": "Completion of Academy Phase; entrance into Frontier Warfare Arc (Chapters 21+)."
  }
}
```
