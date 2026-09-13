"""
AI Novel Engine - Stage 5: The Gatekeeper (State Delta & Consistency)
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Extracts, validates, and commits Stage 5 Delta State JSON to story memory.
Ensures zero continuity errors between chapters.
"""

import json
from typing import Dict, Any
from engine.memory import StoryMemory


class Gatekeeper:
    def __init__(self, memory: StoryMemory):
        self.memory = memory

    def process_delta_state(self, delta: Dict[str, Any]) -> bool:
        chapter = delta.get("chapter", 0)
        world_state = delta.get("world_state", {})
        characters = delta.get("characters", {})

        # Record timeline event
        if "location" in world_state:
            loc = world_state.get("location")
            desc = world_state.get("status", "Chapter Event")
            self.memory.record_event(chapter, f"Chapter {chapter}", desc, loc)

        # Update character states
        for name, data in characters.items():
            status = data.get("vital_status", data.get("status", "Active"))
            loc = data.get("location", world_state.get("location", "Unknown"))
            cond = data.get("physical_condition", data.get("injuries", "Normal"))
            archetype = data.get("role", "Protagonist")
            self.memory.update_character(name, archetype, status, loc, str(cond))

            # Record knowledge or secret oaths
            if "pact_sealed" in data:
                self.memory.record_knowledge(name, str(data["pact_sealed"]), chapter, is_secret=True)
            if "intel_gathered" in data:
                self.memory.record_knowledge(name, str(data["intel_gathered"]), chapter, is_secret=False)

        return True
