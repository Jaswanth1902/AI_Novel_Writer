"""
AI Novel Engine - Stage 3 & 4: The Stylist (Prose & Craft Calibration)
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Synthesizes master directives:
- John Gardner's Psychic Distance continuum (D1-D5)
- Brandon Sanderson's 3 Laws of Magic & Narrative Triangle
- Stephen King's visceral telepathy and adverb eradication
- Ursula K. Le Guin's acoustic sentence music
- Cormac McCarthy's elemental monosyllabic weight
- Live Graph Injected Master Techniques from 100 Authors
"""

from typing import Dict, List, Any, Optional


class Stylist:
    def __init__(self):
        pass

    def build_stylist_config(
        self,
        distance_profile: str,
        rhythm_profile: str,
        sensory_priorities: List[str],
        vibe: str = "grimdark_visceral",
        em_dash_budget: int = 1,
        craft_injection: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        base_directives = [
            "Stephen King Invariant: Zero filter verbs (no 'he felt', 'she noticed', 'he wondered').",
            "Brandon Sanderson Second Law: Limitations and physical costs must dictate supernatural exertion.",
            "Cormac McCarthy Invariant: Ground character consciousness in external interaction with terrain.",
            "Ursula K. Le Guin Invariant: Vary sentence cadence to match the character's respiratory rhythm.",
            "Jaswanth Invariant: Zero faux-archaic crutches ('scriptorium', 'portico', 'visage', 'countenance').",
            "Newtonian Dynamics: Preserve momentum, friction, inertia, torque, and dielectric paths in combat.",
            "Epistemic Asymmetry: Zero telepathic mind-reading; dialogue must carry subtext and friction.",
        ]

        injected_techniques = []
        reference_authors = []
        reference_works = []

        if craft_injection:
            injected_techniques = craft_injection.get("signature_techniques", []) or craft_injection.get("curated_craft_techniques", [])
            reference_authors = craft_injection.get("reference_authors", []) or craft_injection.get("top_reference_authors", [])
            reference_works = craft_injection.get("reference_works", []) or craft_injection.get("matched_works", [])

        # Combine base laws with matched master author directives
        active_directives = base_directives + injected_techniques

        return {
            "gardner_distance": distance_profile,
            "rhythm_profile": rhythm_profile,
            "sensory_priorities": sensory_priorities,
            "vibe_calibration": vibe,
            "em_dash_budget": em_dash_budget,
            "reference_authors": reference_authors,
            "reference_works": reference_works,
            "master_directives": active_directives,
        }
