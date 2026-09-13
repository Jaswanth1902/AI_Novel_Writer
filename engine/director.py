"""
AI Novel Engine - Stage 1: The Director (Scene Contract Compiler)
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Transforms raw story intent, chapter outlines, or rough scene fragments into 
deterministic YAML Scene Contracts with:
- Multi-Genre & Vibe Calibration (Epic Fantasy, Grimdark, Sci-Fi, Cyberpunk, Progression)
- Technological Era Anachronism Enforcement
- Fabula extraction (who is in the room, where, what physical action occurs)
- Ticking clock & stakes
- Dramatic turning point (crisis / dilemma / reversal)
- Hard sensory palette (olfactory, tactile, acoustic)
- Explicit negative constraints (0 filter verbs, 0 crutches, 0 anachronisms)
"""

import os
import yaml
from typing import Dict, List, Any, Optional

CONFIG_DIR = os.path.join(os.path.dirname(__file__), "..", "config")


class Director:
    def __init__(self, default_genre: str = "progression_fantasy", default_era: str = "industrial_atla"):
        self.default_genre = default_genre
        self.default_era = default_era
        self.genre_matrix = self._load_genre_matrix()

    def _load_genre_matrix(self) -> Dict[str, Any]:
        path = os.path.join(CONFIG_DIR, "genre_matrix.yaml")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)
        return {}

    def create_scene_contract(
        self,
        chapter: int,
        title: str,
        pov: str,
        setting_primary: str,
        atmosphere: str,
        characters: List[Dict[str, str]],
        plot_beats: List[str],
        turning_point: str,
        ticking_clock: str,
        genre: Optional[str] = None,
        era: Optional[str] = None,
        custom_sensory: Optional[Dict[str, List[str]]] = None,
        word_target: str = "1200-1800",
        custom_banned: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Compiles a validated Stage 1 YAML Scene Contract based on Master Craft Directives."""
        active_genre = genre or self.default_genre
        active_era = era or self.default_era

        genre_cfg = self.genre_matrix.get("genres", {}).get(active_genre, {})
        era_cfg = self.genre_matrix.get("technological_eras", {}).get(active_era, {})

        sensory_palette = custom_sensory or {
            "primary": genre_cfg.get("sensory_palette", ["cold iron", "tallow", "shale"]),
            "environmental": ["cold mountain air", "damp stone", "river mist"],
        }

        contract = {
            "chapter": chapter,
            "title": title,
            "word_count_target": word_target,
            "classification": {
                "genre": active_genre,
                "technological_era": active_era,
                "pacing_cadence": genre_cfg.get("pacing", "kinetic_staccato"),
            },
            "pov": pov,
            "setting": {
                "primary": setting_primary,
                "atmosphere": atmosphere,
            },
            "characters": characters,
            "dramatic_engine": {
                "ticking_clock": ticking_clock,
                "turning_point": turning_point,
                "conflict_type": genre_cfg.get("conflict_type", "attritional_survival"),
            },
            "plot_beats": {i + 1: beat for i, beat in enumerate(plot_beats)},
            "sensory_palette": sensory_palette,
            "invariants": {
                "zero_filter_verbs": True,
                "em_dash_ceiling": "<= 1 per 800 words (target: 0-1 per chapter)",
                "banned_crutches": ["scriptorium", "portico", "visage", "countenance", "ebon", "eldritch"],
                "era_forbidden_terms": era_cfg.get("forbidden", []),
                "custom_banned": custom_banned or [],
            },
        }
        return contract

    def export_contract_yaml(self, contract: Dict[str, Any]) -> str:
        return yaml.dump(contract, sort_keys=False, default_flow_style=False)
