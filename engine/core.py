"""
AI Novel Engine - Core Orchestrator
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Coordinates the 5-stage pipeline with Graph-Powered Craft Injection:
1. Director (Scene Contract + Master Author Craft Injection)
2. Actor (Epistemic Envelopes)
3. Stylist (Craft Calibration & Gardner Continuum)
4. Renderer (Prose Output)
5. Gatekeeper (State Delta & Linting)
"""

import os
from typing import Dict, Any, List, Optional
from engine.director import Director
from engine.actor import ActorEnvelopeManager
from engine.stylist import Stylist
from engine.gatekeeper import Gatekeeper
from engine.memory import StoryMemory
from engine.linter import NovelLinter
from engine.attribute_extractor import AttributeExtractor, ExtractedAttributes
from engine.graph_knowledge import GraphKnowledgebase


class NovelEngine:
    def __init__(self, workspace_root: Optional[str] = None):
        self.workspace_root = workspace_root or os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.memory = StoryMemory(os.path.join(self.workspace_root, "state", "story_state.sqlite"))
        self.director = Director()
        self.actor = ActorEnvelopeManager()
        self.stylist = Stylist()
        self.gatekeeper = Gatekeeper(self.memory)
        self.linter = NovelLinter()
        self.extractor = AttributeExtractor()
        self.graph = GraphKnowledgebase(os.path.join(self.workspace_root, "state", "author_knowledge_graph.sqlite"))

    def match_craft(self, text: str, top_k: int = 3, overrides: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Extracts attributes and generates craft injection from 100 authors graph."""
        attrs: ExtractedAttributes = self.extractor.extract(text, user_overrides=overrides)
        return self.graph.generate_craft_injection(attrs, top_k=top_k)

    def plan_scene_from_notes(
        self,
        chapter: int,
        title: str,
        notes: str,
        pov: str = "Jaswanth",
        top_k: int = 3
    ) -> Dict[str, Any]:
        """Plans a Stage 1 Scene Contract directly from raw notes using graph matching."""
        return self.director.compile_from_user_notes(
            chapter=chapter,
            title=title,
            user_notes=notes,
            pov=pov,
            top_k_authors=top_k,
        )

    def audit_chapter(self, filepath: str) -> Dict[str, Any]:
        return self.linter.lint_file(filepath)

    def audit_all_chapters(self, output_dir: Optional[str] = None) -> Dict[str, Any]:
        target_dir = output_dir or os.path.join(self.workspace_root, "output")
        results = []
        all_passed = True
        total_words = 0

        for root, _, files in os.walk(target_dir):
            for file in sorted(files):
                if file.endswith(".md") and "Pipeline_Execution" not in file:
                    p = os.path.join(root, file)
                    res = self.linter.lint_file(p)
                    total_words += res["words"]
                    if not res["passed"]:
                        all_passed = False
                    results.append(res)

        return {
            "all_passed": all_passed,
            "chapter_count": len(results),
            "total_words": total_words,
            "results": results,
        }
