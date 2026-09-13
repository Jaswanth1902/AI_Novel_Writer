"""
AI Novel Engine - Plot Critic & Editorial Director
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Analyzes user-submitted plots, scene briefs, or manuscript outlines:
1. Conducts narrative diagnostic across 5 craft dimensions.
2. Synthesizes master author craft directives from the Graph Knowledgebase.
3. Formulates concrete, non-derivative plot elevation upgrades (Anti-Plagiarism Invariant).
4. Embeds character visual dossiers with optional photo portraits.
"""

import os
import re
from typing import Dict, List, Any, Optional
from engine.attribute_extractor import AttributeExtractor, ExtractedAttributes
from engine.graph_knowledge import GraphKnowledgebase
from engine.character_dossier import CharacterDossier


class PlotCritic:
    """Automated literary critic, structural diagnostic, and plot elevation engine."""

    def __init__(self):
        self.extractor = AttributeExtractor()
        self.graph = GraphKnowledgebase()

    def evaluate_plot(
        self,
        plot_text: str,
        characters: Optional[List[CharacterDossier]] = None,
        overrides: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Performs a comprehensive diagnostic and synthesizes structural upgrades."""
        attrs: ExtractedAttributes = self.extractor.extract(plot_text, user_overrides=overrides)
        injection = self.graph.generate_craft_injection(attrs, top_k=3)

        cleaned = plot_text.lower()

        # 1. Diagnostic Scoring (1-10)
        # Tension & Ticking Clock
        has_urgency = any(w in cleaned for w in ["before", "deadline", "dawn", "closing", "running out", "trap", "hunt", "countdown"])
        score_tension = 8.5 if has_urgency else 5.5

        # Epistemic Friction / Hidden Knowledge
        has_secrecy = any(w in cleaned for w in ["secret", "hide", "conceal", "lie", "unaware", "unknown", "suspect", "betray"])
        score_friction = 8.0 if has_secrecy else 5.0

        # Physical / Somatic Cost
        has_somatic = any(w in cleaned for w in ["blood", "wound", "exhaustion", "bone", "mud", "cold", "pain", "sweat", "burn"])
        score_somatic = 8.5 if has_somatic else 6.0

        # Dilemma & Irreversibility
        has_dilemma = any(w in cleaned for w in ["choose", "choice", "sacrifice", "cost", "risk", "decide", "lose", "either"])
        score_dilemma = 8.0 if has_dilemma else 5.5

        # Originality vs Trope Density
        has_cliche = any(w in cleaned for w in ["chosen one", "destiny", "save the world", "ancient prophecy", "ultimate power"])
        score_originality = 6.0 if has_cliche else 8.5

        overall_score = round((score_tension + score_friction + score_somatic + score_dilemma + score_originality) / 5.0, 1)

        # 2. Identify Weaknesses & Opportunities
        opportunities = []
        if score_tension < 7.0:
            opportunities.append("Ticking Clock Weakness: The scene lacks external time pressure. Introduce an environmental or antagonistic deadline.")
        if score_friction < 7.0:
            opportunities.append("Epistemic Transparency: Characters appear to share identical knowledge. Introduce an asymmetric secret or tactical misunderstanding.")
        if score_somatic < 7.0:
            opportunities.append("Insufficient Somatic Toll: The action risks reading like an abstract video game. Anchor the scene in visceral physical costs, muscle fatigue, or terrain friction.")
        if score_dilemma < 7.0:
            opportunities.append("Low-Stakes Turning Point: The climax appears to resolve via straightforward combat/success. Force an irreversible dilemma where any choice costs something dear.")

        # 3. Formulate Actionable Upgrades (Anti-Plagiarism Grounding)
        ref_authors = injection.get("top_reference_authors", [])
        techniques = injection.get("curated_craft_techniques", [])

        upgrades = [
            {
                "title": "Upgrade 1: The Irreversible Forked Dilemma (Sanderson & Martin)",
                "directive": "Do not let the protagonist solve the crisis cleanly. Introduce two competing moral imperatives (e.g. saving an ally vs securing the vital intelligence). Whichever path is chosen must leave permanent consequences.",
                "anti_plagiarism_note": "Borrow the structural paradigm of irrecoverable loss—do NOT copy the specific plot points or magic systems of A Song of Ice and Fire or Mistborn."
            },
            {
                "title": "Upgrade 2: Sensory Palette Deceleration (King & Le Guin)",
                "directive": f"Ground the crucial moment in 3 hyper-specific sensory anchors ({', '.join(attrs.sensory_palette[:3])}). Slow down the subjective narrative clock right before the turning point occurs.",
                "anti_plagiarism_note": "Borrow King's 'iceberg description' technique—projecting vivid physical detail without purple melodrama."
            },
            {
                "title": "Upgrade 3: Epistemic Asymmetry & Subtextual Dialogue (Hemingway & Hobb)",
                "directive": "Have the characters converse with dual agendas. Ensure neither character openly states their true terror. Dialogue must be a tactical spar over tea, weapons, or terrain while the real conflict hums beneath.",
                "anti_plagiarism_note": "Borrow the iceberg theory of dialogue where 90% of character motivation remains unsaid below the waterline."
            },
            {
                "title": "Upgrade 4: Newtonian & Thermodynamic Costs (Hard SF & Progression Invariants)",
                "directive": f"Every exertion in this {attrs.primary_genre} setting must expend measurable energy, strain physical biology, or attract collateral consequences from the environment.",
                "anti_plagiarism_note": "Borrow the Newtonian law of action and reaction—ensuring every punch, spell, or tactical maneuver produces equal structural recoil."
            }
        ]

        return {
            "plot_summary": plot_text[:250] + ("..." if len(plot_text) > 250 else ""),
            "extracted_attributes": attrs.to_dict(),
            "scorecard": {
                "overall_score": overall_score,
                "tension_urgency": score_tension,
                "epistemic_friction": score_friction,
                "somatic_grounding": score_somatic,
                "dilemma_stakes": score_dilemma,
                "originality": score_originality,
            },
            "critical_opportunities": opportunities,
            "master_authors_matched": ref_authors,
            "matched_techniques": techniques,
            "structural_upgrades": upgrades,
            "characters": [c.to_dict() for c in (characters or [])],
        }

    def generate_markdown_critique(
        self,
        plot_text: str,
        characters: Optional[List[CharacterDossier]] = None,
        overrides: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Renders an executive-grade Markdown Comments & Plot Critique Report."""
        eval_data = self.evaluate_plot(plot_text, characters=characters, overrides=overrides)
        scorecard = eval_data["scorecard"]
        attrs = eval_data["extracted_attributes"]

        lines = []
        lines.append("# 📝 Plot Diagnostic, Elevation Critique & Character Visual Sheet")
        lines.append("**AI Novel Engine v2.1 — Master Craft Advisory Panel**\n")
        lines.append("---\n")

        # 1. Executive Summary & Scorecard
        lines.append("## 1. 📊 Executive Plot Diagnostic & Scorecard\n")
        lines.append(f"> [!NOTE]\n> **Evaluated Concept**: *\"{eval_data['plot_summary']}\"*\n")
        lines.append(f"**Overall Narrative Health Score**: `{scorecard['overall_score']} / 10.0`\n")

        lines.append("| Narrative Dimension | Score | Status | Focus Area |")
        lines.append("| :--- | :---: | :---: | :--- |")
        lines.append(f"| **Tension & Ticking Clock** | `{scorecard['tension_urgency']}/10` | {'🟢 Optimal' if scorecard['tension_urgency'] >= 7.5 else '🟡 Needs Urgency'} | Physical/temporal deadlines |")
        lines.append(f"| **Epistemic Friction & Subtext** | `{scorecard['epistemic_friction']}/10` | {'🟢 Optimal' if scorecard['epistemic_friction'] >= 7.5 else '🟡 Needs Asymmetry'} | Concealed information & agendas |")
        lines.append(f"| **Somatic & Physical Grounding** | `{scorecard['somatic_grounding']}/10` | {'🟢 Optimal' if scorecard['somatic_grounding'] >= 7.5 else '🟡 Needs Weight'} | Biological cost & terrain resistance |")
        lines.append(f"| **Dilemma & Irreversibility** | `{scorecard['dilemma_stakes']}/10` | {'🟢 Optimal' if scorecard['dilemma_stakes'] >= 7.5 else '🟡 Needs Dilemma'} | Forked choices with permanent costs |")
        lines.append(f"| **Originality & Trope Subversion**| `{scorecard['originality']}/10` | {'🟢 Optimal' if scorecard['originality'] >= 7.5 else '🟡 High Trope Density'} | Avoidance of stock cliches |")
        lines.append("")

        # 2. Core Weaknesses / Opportunities
        if eval_data["critical_opportunities"]:
            lines.append("## 2. ⚠️ Critical Structural Blind Spots (Where the Plot Stalls)\n")
            for opp in eval_data["critical_opportunities"]:
                lines.append(f"> [!WARNING]\n> **{opp.split(':')[0]}**:{opp.split(':')[1]}\n")
            lines.append("")

        # 3. Master Authors Inspiration & Anti-Plagiarism Protocol
        lines.append("## 3. 📚 Matched Master Craft References & Anti-Plagiarism Invariant\n")
        lines.append(f"Based on your extracted parameters (**Genre**: `{attrs['primary_genre']}`, **Era**: `{attrs['tech_era']}`, **Vibes**: `{', '.join(attrs['vibes'])}`), the Graph Knowledgebase matched the following literary masters:\n")

        for author in eval_data["master_authors_matched"]:
            lines.append(f"- **{author}**")
        lines.append("")

        lines.append("> [!IMPORTANT]\n> ### 🛡️ The Anti-Plagiarism & Originality Guarantee\n"
                     "> The AI Novel Engine **strictly prohibits copying content, character names, proprietary lore, or specific scene beats** from reference authors. "
                     "Instead, we extract only **abstract craft mechanics** (sentence rhythms, epistemic information barriers, sensory palette deceleration, and cost structures) "
                     "and apply them exclusively to your unique setting and characters.\n")

        lines.append("### Master Techniques to Emulate (Structural Mechanics Only):")
        for tech in eval_data["matched_techniques"]:
            lines.append(f"- {tech}")
        lines.append("")

        # 4. How to Make the Plot 10x Better (Actionable Upgrades)
        lines.append("## 4. 🚀 Actionable Upgrades: How to Elevate This Plot\n")
        for upg in eval_data["structural_upgrades"]:
            lines.append(f"### {upg['title']}\n")
            lines.append(f"{upg['directive']}\n")
            lines.append(f"> [!TIP]\n> **Originality Guard**: {upg['anti_plagiarism_note']}\n")

        # 5. Character Visual Profiles & Photo Gallery
        lines.append("## 5. 👥 Character Visual Profiles & Photo Dossiers\n")
        if characters:
            for char in characters:
                lines.append(char.render_markdown_card())
                lines.append("---\n")
        else:
            lines.append("*No character dossiers were explicitly attached to this critique.*")
            lines.append("You can attach character cards with photos via:")
            lines.append("```bash")
            lines.append('python novel_engine.py critique --notes "..." --character-name "Jaswanth" --photo "assets/characters/jaswanth.png"')
            lines.append("```\n")

        # 6. Drafting Checklist
        lines.append("## 6. ✅ Next Steps: Pre-Drafting Delivery Gate Checklist\n")
        lines.append("- [ ] **Zero Filter Verbs**: Verify no instances of `felt`, `noticed`, `wondered`, `realized`.")
        lines.append("- [ ] **Em-Dash Ceiling**: Target $\\le 1$ dash for the entire chapter ($\\ge 800$ words/dash).")
        lines.append("- [ ] **Banned Crutches Removed**: Zero occurrences of `scriptorium`, `portico`, `visage`, `countenance`.")
        lines.append(f"- [ ] **Era Anachronism Check**: Ensure no out-of-era items violate the `{attrs['tech_era']}` matrix.")
        lines.append("- [ ] **Irreversible Turning Point**: Ensure the chapter ends on a physical state change that cannot be undone.\n")

        return "\n".join(lines)
