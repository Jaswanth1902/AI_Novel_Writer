"""
AI Novel Engine - Attribute Extractor
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Analyzes user-submitted story notes, outlines, scene briefs, or pitch documents,
and extracts multi-dimensional parameters for narrative calibration:
- Primary & secondary genres
- Emotional vibes & aesthetic tones
- Technological era & setting constraints
- Magic hardness & supernatural laws
- Narrative pacing & cadence
- Conflict dynamics & dramatic engine
- Recommended sensory palette
"""

import re
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional, Set


@dataclass
class ExtractedAttributes:
    primary_genre: str
    secondary_genres: List[str] = field(default_factory=list)
    vibes: List[str] = field(default_factory=list)
    tech_era: str = "medieval"
    magic_hardness: str = "none_mundane"
    pacing: str = "balanced"
    conflict_type: str = "attritional_survival"
    pov_recommendation: str = "deep_third_limited"
    sensory_palette: List[str] = field(default_factory=list)
    detected_keywords: List[str] = field(default_factory=list)
    confidence: float = 0.0

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def summary(self) -> str:
        sec = ", ".join(self.secondary_genres) if self.secondary_genres else "None"
        vibes_str = ", ".join(self.vibes) if self.vibes else "neutral"
        sensory_str = ", ".join(self.sensory_palette[:5])
        return (
            f"Genre: {self.primary_genre} (Secondary: {sec})\n"
            f"Vibes: {vibes_str}\n"
            f"Era: {self.tech_era} | Magic: {self.magic_hardness}\n"
            f"Pacing: {self.pacing} | Conflict: {self.conflict_type}\n"
            f"Sensory Palette: {sensory_str}\n"
            f"Confidence: {self.confidence:.2f}"
        )


class AttributeExtractor:
    """Deterministic, rule-grounded narrative attribute extractor."""

    GENRE_CLUSTERS: Dict[str, Dict[str, Any]] = {
        "Progression Fantasy": {
            "keywords": [
                "cultivation", "meridian", "qi", "core", "breakthrough", "dantian", "tribulation",
                "sect", "levels", "stats", "rank", "realm", "ascending", "essence", "elixir",
                "training", "tier", "advancement", "stage", "spirit stone", "martial path"
            ],
            "default_era": "medieval",
            "default_magic": "progression_meridian",
            "default_pacing": "escalating",
            "default_vibes": ["escalating_velocity", "unyielding_will", "tactile_combat"],
            "conflict": "will_vs_cosmic_constraints",
            "sensory": ["ozone", "hot iron", "bone marrow chill", "ground stone", "sulfur"]
        },
        "Grimdark": {
            "keywords": [
                "mud", "gallows", "trench", "infection", "amputation", "cynical", "mercenary",
                "brutal", "bastard", "torture", "treachery", "grimy", "gangrene", "blood",
                "siege", "slaughter", "unforgiving", "corpse", "rot", "iron", "despair"
            ],
            "default_era": "late_medieval",
            "default_magic": "hard_brutal",
            "default_pacing": "kinetic_staccato",
            "default_vibes": ["grimdark_visceral", "bleak_cynicism", "attritional_grit"],
            "conflict": "attritional_survival",
            "sensory": ["cold grease", "vinegar bandages", "wet wool", "sour wine", "shattered bone"]
        },
        "Epic Fantasy": {
            "keywords": [
                "kingdom", "throne", "dynasty", "ancient evil", "prophecy", "high king",
                "citadel", "dragon", "oath", "sword", "archmage", "realm", "warrior",
                "chivalry", "emperor", "sorcery", "banner", "cavalry", "crown"
            ],
            "default_era": "medieval",
            "default_magic": "hard_sandersonian",
            "default_pacing": "unhurried_epic",
            "default_vibes": ["monumental_awe", "mythic_majesty", "architectural_scale"],
            "conflict": "sociopolitical_destiny",
            "sensory": ["cold iron", "tallow", "crushed pine", "stone dust", "leather"]
        },
        "Hard Sci-Fi": {
            "keywords": [
                "orbital", "vacuum", "relativistic", "delta-v", "radiation", "propulsion",
                "light-year", "telemetry", "spectrometry", "fusion reactor", "gravity well",
                "physics", "entropy", "astrophysics", "payload", "cryogenic", "sensor array"
            ],
            "default_era": "far_future",
            "default_magic": "none_mundane",
            "default_pacing": "analytical",
            "default_vibes": ["cerebral_analytical", "pure_physics", "ontological_wonder"],
            "conflict": "intellect_vs_thermodynamics",
            "sensory": ["recycled air", "cryo-frost", "hydraulic fluid", "ozone", "metallic tang"]
        },
        "Cyberpunk": {
            "keywords": [
                "neon", "cyberware", "megacorp", "neural", "deck", "netrunner", "synthetic",
                "chrome", "implant", "subdermal", "interface", "hacker", "black market",
                "biotech", "sprawl", "wetware", "aug", "terminal", "algorithm"
            ],
            "default_era": "near_future",
            "default_magic": "none_mundane",
            "default_pacing": "syncopated_furious",
            "default_vibes": ["kinetic_momentum", "neon_noir", "existential_rebellion"],
            "conflict": "individual_vs_megacorp",
            "sensory": ["rain on asphalt", "scorched silicon", "ozone", "chemical vapor", "cheap stimulants"]
        },
        "Cosmic Horror": {
            "keywords": [
                "non-euclidean", "abyss", "tentacle", "madness", "void", "insanity", "forbidden",
                "tome", "eldritch", "stars", "cyclopean", "sanity", "monolith", "alien god",
                "nameless", "decay", "grotesque", "whispers", "chasm"
            ],
            "default_era": "early_20th_century",
            "default_magic": "cosmic_irrational",
            "default_pacing": "creeping_claustrophobic",
            "default_vibes": ["claustrophobic_dread", "existential_nihilism", "uncanny_cold"],
            "conflict": "human_fragility_vs_incomprehensible",
            "sensory": ["damp cellar", "brine", "rotting kelp", "copper", "stale incense"]
        },
        "Mystery / Noir": {
            "keywords": [
                "detective", "alibi", "suspect", "fingerprint", "corpse", "crime scene",
                "revolver", "informant", "interrogation", "motive", "blackmail", "corrupt",
                "shadows", "raincoat", "autopsy", "witness", "clue", "case"
            ],
            "default_era": "mid_20th_century",
            "default_magic": "none_mundane",
            "default_pacing": "methodical_tension",
            "default_vibes": ["methodical_tension", "hardboiled_cynicism", "nocturnal_paranoia"],
            "conflict": "truth_vs_deception",
            "sensory": ["stale tobacco", "wet pavement", "cold coffee", "damp trench coat", "whiskey"]
        },
        "LitRPG": {
            "keywords": [
                "quest", "dungeon", "inventory", "experience points", "skill tree", "hud",
                "boss room", "loot", "status sheet", "buff", "debuff", "health bar",
                "party member", "system prompt", "mana pool", "cooldown"
            ],
            "default_era": "modern_into_game",
            "default_magic": "system_apocalypse",
            "default_pacing": "kinetic_escalating",
            "default_vibes": ["kinetic_absurdity", "system_optimization", "indomitable_defiance"],
            "conflict": "survivor_vs_rigged_system",
            "sensory": ["blue holographic glare", "singed hair", "healing potion copper", "cracked concrete"]
        },
        "Historical Fiction": {
            "keywords": [
                "regiment", "musket", "carriage", "parliament", "treaty", "vessel", "frigate",
                "squadron", "nobility", "peasant", "monarch", "colonel", "admiral", "bayonet",
                "broadside", "campaign", "ballroom", "rebellion"
            ],
            "default_era": "victorian_gaslamp",
            "default_magic": "none_mundane",
            "default_pacing": "measured_tapestry",
            "default_vibes": ["historic_elegance", "military_precision", "lyrical_melancholy"],
            "conflict": "duty_vs_conscience",
            "sensory": ["black powder smoke", "salted beef", "pitch pine", "wool broadcloth", "damp rigging"]
        },
        "Literary Realism": {
            "keywords": [
                "memory", "regret", "marriage", "silence", "father", "daughter", "estrangement",
                "interiority", "suburban", "clock", "grief", "conversation", "solitude",
                "longing", "unspoken", "habit", "mundane", "aging"
            ],
            "default_era": "modern",
            "default_magic": "none_mundane",
            "default_pacing": "deliberate_reflective",
            "default_vibes": ["luminous_interiority", "quiet_desperation", "domestic_realism"],
            "conflict": "self_vs_unlived_life",
            "sensory": ["dust in sunlight", "drying paint", "lukewarm tap water", "creaking floorboards"]
        }
    }

    ERA_PATTERNS: Dict[str, List[str]] = {
        "stone_age": ["flint", "mammoth", "hide", "sinew", "tallow", "fire pit", "caves"],
        "bronze_age": ["bronze", "chariot", "papyrus", "clay tablet", "spear", "pharaoh"],
        "classical_antiquity": ["legion", "gladius", "toga", "senate", "colosseum", "amphora", "centurion"],
        "medieval": ["chainmail", "bastion", "longsword", "moat", "parchment", "candle wax", "feudal", "keep"],
        "late_medieval": ["plate armor", "crossbow", "siege tower", "gallows", "guild", "quill"],
        "renaissance": ["rapier", "galleon", "printing press", "astrolabe", "oil canvas", "florence"],
        "flintlock_era": ["musket", "flintlock", "black powder", "frigate", "broadside", "tricorn"],
        "industrial_atla": ["coal locomotive", "steam boiler", "iron rails", "smokestack", "airship", "cable car"],
        "victorian_gaslamp": ["gas lamp", "cobblestone", "hansom cab", "pocket watch", "top hat", "fog"],
        "early_20th_century": ["trench", "gramophone", "telegraph", "artillery", "mustard gas", "typewriter"],
        "mid_20th_century": ["revolver", "rotary phone", "neon sign", "radar", "propeller plane", "radio"],
        "modern": ["smartphone", "laptop", "subway", "freeway", "internet", "cctv", "dna"],
        "near_future": ["drone", "neural interface", "cyberware", "ar glasses", "synthetic meat", "megatower"],
        "far_future": ["antimatter", "dyson sphere", "warp", "generation ship", "cryo-pod", "quantum computer"]
    }

    VIBE_KEYWORDS: Dict[str, List[str]] = {
        "grimdark_visceral": ["bleak", "visceral", "gritty", "unforgiving", "cynical", "bloody", "morally grey"],
        "kinetic_momentum": ["fast-paced", "relentless", "furious", "action-packed", "high-octane", "adrenaline"],
        "cerebral_analytical": ["thoughtful", "scientific", "rigorous", "philosophical", "intellectual", "deconstructive"],
        "haunting_melancholy": ["sad", "tragic", "wistful", "melancholy", "grief", "ruins", "decay", "lonely"],
        "monumental_awe": ["vast", "epic", "cosmic", "grand", "mythic", "wonder", "ancient", "monumental"],
        "claustrophobic_dread": ["paranoia", "suffocating", "trapped", "suspense", "dread", "creeping", "eerie"],
        "subversive_wit": ["ironic", "satirical", "dry humor", "dark comedy", "witty", "irreverent"],
        "luminous_interiority": ["introspective", "poetic", "impressionistic", "stream of consciousness", "subtle"]
    }

    def __init__(self):
        pass

    def extract(self, text: str, user_overrides: Optional[Dict[str, Any]] = None) -> ExtractedAttributes:
        """Extracts structured narrative parameters from freeform text and applies overrides."""
        cleaned = text.lower()
        words = set(re.findall(r"\b[a-zA-Z\-]{3,}\b", cleaned))

        # 1. Score Genres
        genre_scores: Dict[str, float] = {}
        for genre, data in self.GENRE_CLUSTERS.items():
            matches = [k for k in data["keywords"] if k.lower() in cleaned or any(kw in words for kw in k.lower().split())]
            score = len(matches)
            if score > 0:
                genre_scores[genre] = score

        if not genre_scores:
            primary_genre = "Epic Fantasy"
            secondary_genres = []
            confidence = 0.35
        else:
            sorted_genres = sorted(genre_scores.items(), key=lambda x: x[1], reverse=True)
            primary_genre = sorted_genres[0][0]
            secondary_genres = [g[0] for g in sorted_genres[1:4]]
            max_score = sorted_genres[0][1]
            confidence = min(0.95, 0.45 + (max_score * 0.08))

        cluster_info = self.GENRE_CLUSTERS.get(primary_genre, self.GENRE_CLUSTERS["Epic Fantasy"])

        # 2. Score Tech Eras
        era_scores: Dict[str, int] = {}
        for era, keywords in self.ERA_PATTERNS.items():
            matches = [k for k in keywords if k.lower() in cleaned or k.lower() in words]
            if matches:
                era_scores[era] = len(matches)

        if era_scores:
            tech_era = max(era_scores.items(), key=lambda x: x[1])[0]
        else:
            tech_era = cluster_info["default_era"]

        # 3. Score Vibes
        matched_vibes: List[str] = []
        for vibe, keywords in self.VIBE_KEYWORDS.items():
            if any(k in cleaned for k in keywords):
                matched_vibes.append(vibe)

        if not matched_vibes:
            matched_vibes = list(cluster_info.get("default_vibes", ["grimdark_visceral"]))

        # 4. Infer Magic Hardness
        magic_hardness = cluster_info.get("default_magic", "semi_hard")

        # 5. Build Attributes
        attrs = ExtractedAttributes(
            primary_genre=primary_genre,
            secondary_genres=secondary_genres,
            vibes=matched_vibes,
            tech_era=tech_era,
            magic_hardness=magic_hardness,
            pacing=cluster_info.get("default_pacing", "balanced"),
            conflict_type=cluster_info.get("conflict", "attritional_survival"),
            pov_recommendation="deep_third_limited",
            sensory_palette=cluster_info.get("sensory", ["cold iron", "stone dust", "pine smoke"]),
            detected_keywords=list(words.intersection({k for d in self.GENRE_CLUSTERS.values() for k in d["keywords"]}))[:12],
            confidence=confidence,
        )

        # 6. Apply User Overrides if provided
        if user_overrides:
            if "genre" in user_overrides and user_overrides["genre"]:
                attrs.primary_genre = user_overrides["genre"]
            if "era" in user_overrides and user_overrides["era"]:
                attrs.tech_era = user_overrides["era"]
            if "magic_hardness" in user_overrides and user_overrides["magic_hardness"]:
                attrs.magic_hardness = user_overrides["magic_hardness"]
            if "pacing" in user_overrides and user_overrides["pacing"]:
                attrs.pacing = user_overrides["pacing"]
            if "vibes" in user_overrides and user_overrides["vibes"]:
                if isinstance(user_overrides["vibes"], list):
                    attrs.vibes = user_overrides["vibes"]
                else:
                    attrs.vibes = [user_overrides["vibes"]]

        return attrs
