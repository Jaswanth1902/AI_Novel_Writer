"""
AI Novel Engine - Stage 1: The Director (Scene Contract Compiler)
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Transforms raw story intent, chapter outlines, or rough scene fragments into 
deterministic YAML Scene Contracts with:
- Fabula extraction (who is in the room, where, what physical action occurs)
- Ticking clock & stakes
- Dramatic turning point (crisis / dilemma / reversal)
- Hard sensory palette (olfactory, tactile, acoustic)
- Explicit negative constraints
"""

import yaml
from typing import Dict, List, Any, Optional


class Director:
    def __init__(self, default_pov: str = "Third-Person Limited"):
        self.default_pov = default_pov

    def create_scene_contract(
        self,
        chapter: int,
        title: str,
        pov: str,
        setting_primary: str,
        atmosphere: str,
        characters: List[Dict[str, str]],
        plot_beats: List[str],
        sensory_palette: Dict[str, List[str]],
        turning_point: str,
        ticking_clock: str,
        word_target: str = "1200-1800",
        banned_terms: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Compiles a validated Stage 1 YAML Scene Contract."""

        contract = {
            "chapter": chapter,
            "title": title,
            "word_count_target": word_target,
            "pov": pov,
            "setting": {
                "primary": setting_primary,
                "atmosphere": atmosphere,
            },
            "characters": characters,
            "dramatic_engine": {
                "ticking_clock": ticking_clock,
                "turning_point": turning_point,
            },
            "plot_beats": {i + 1: beat for i, beat in enumerate(plot_beats)},
            "sensory_palette": sensory_palette,
            "invariants": {
                "zero_filter_verbs": True,
                "em_dash_ceiling": "<= 1 per 800 words (target: 0-1 per chapter)",
                "banned_crutches": ["scriptorium", "portico", "visage", "countenance", "ebon"],
                "custom_banned": banned_terms or [],
            },
        }
        return contract

    def export_contract_yaml(self, contract: Dict[str, Any]) -> str:
        return yaml.dump(contract, sort_keys=False, default_flow_style=False)
