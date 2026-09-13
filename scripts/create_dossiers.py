"""
AI Novel Engine - Seed Character Dossiers
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from engine.character_dossier import CharacterDossier, CharacterDossierManager

def main():
    manager = CharacterDossierManager()

    # 1. Jaswanth (Protagonist)
    jaswanth = CharacterDossier(
        name="Jaswanth",
        role="Protagonist",
        photo_path="assets/characters/jaswanth_protagonist.jpg",
        visual_description={
            "age": "19",
            "height": "180 cm (5 ft 11 in)",
            "build": "Lean, corded martial frame",
            "hair": "Short, tousled dark hair",
            "eyes": "Sharp amber-hazel, vigilant",
            "complexion": "Warm olive-bronze with minor sparring nicks",
            "attire": "High-collared charcoal wool and linen tunic with rawhide lacing"
        },
        signature_item="Cold-forged iron band around right wrist",
        somatic_tells=[
            "Fingers twitch toward the wrist band when assessing structural loads",
            "Breathing settles into a four-beat pulse during physical tension",
            "Jaw sets without raising the chin"
        ],
        epistemic_secrets=[
            "Aware that the second comet surge unlocked a subterranean grammar beneath Iron Peak",
            "Concealing the micro-fracture along his right forearm meridian from Proctors Rao and Meera"
        ],
        image_prompt="Cinematic portrait of a 19-year-old South Asian male fantasy protagonist named Jaswanth, lean athletic build, sharp focused gaze, short dark hair, wearing a charcoal wool and linen martial tunic with a high collar, cold forged iron band on right wrist, atmospheric lighting with soft mist and subtle embers, digital painting concept art."
    )
    p1 = manager.save_dossier(jaswanth)
    print(f"Created dossier: {p1}")

    # 2. Bennett (Ice Vanguard / Noble Ally)
    bennett = CharacterDossier(
        name="Bennett",
        role="Ally / Noble Foil",
        photo_path=None,
        visual_description={
            "age": "20",
            "height": "185 cm (6 ft 1 in)",
            "build": "Broad-shouldered, aristocratic military posture",
            "hair": "Ash-blond, combed back with clean precision",
            "eyes": "Pale slate-blue, measured and calculating",
            "complexion": "Fair, weathered by northern mountain wind",
            "attire": "Deep sea-blue tunic over padded linen, bone-handled silver carving knife at belt"
        },
        signature_item="Bone-handled silver carving knife",
        somatic_tells=[
            "Rolls a bone token between knuckles while deliberating tactical options",
            "Left shoulder drops slightly when entering an ice-anchor stance",
            "Speaks in clipped, low-register aristocratic cadences"
        ],
        epistemic_secrets=[
            "Knows that House Bennett's northern estates are defaulting on iron taxes to the capital",
            "Harbors deep guilt over the fallen squad members at Langford basin"
        ],
        image_prompt="Cinematic portrait of a 20-year-old noble northern warrior named Bennett, broad shoulders, ash-blond hair neatly combed back, pale slate-blue eyes, wearing a deep sea-blue tailored martial coat with silver embroidery, holding a bone-handled knife, mountain fortress background, concept art digital painting."
    )
    p2 = manager.save_dossier(bennett)
    print(f"Created dossier: {p2}")

    # 3. Tejaswini (Thermal Discipline Master)
    tejaswini = CharacterDossier(
        name="Tejaswini",
        role="Tactical Specialist / Prodigy",
        photo_path=None,
        visual_description={
            "age": "19",
            "height": "170 cm (5 ft 7 in)",
            "build": "Wiry, hyper-flexible, coiled kinetic balance",
            "hair": "Dark hair bound tightly in twin braids with copper needles",
            "eyes": "Deep obsidian, observant and unrelenting",
            "complexion": "Warm dusk, soot-dusted along the collarbone",
            "attire": "Reinforced leather cuirass over ochre raw silk with thermal venting seams"
        },
        signature_item="Three etched copper resonance needles pinned in hair",
        somatic_tells=[
            "Checks hair needles with thumb and forefinger before any confrontation",
            "Rhythmic exhale releasing thermal vapor from the nose",
            "Shifts weight from heel to ball of foot continuously"
        ],
        epistemic_secrets=[
            "Has decoded the heat-venting flaw in the Danava armor plates",
            "Withholding the full extent of her family's debt to the Grand Master"
        ],
        image_prompt="Cinematic portrait of a 19-year-old South Asian female martial prodigy named Tejaswini, dark hair in twin braids pinned with copper needles, intense obsidian eyes, reinforced ochre and leather armor with bronze accents, subtle heat haze around hands, atmospheric lighting, high-detail concept art."
    )
    p3 = manager.save_dossier(tejaswini)
    print(f"Created dossier: {p3}")

if __name__ == "__main__":
    main()
