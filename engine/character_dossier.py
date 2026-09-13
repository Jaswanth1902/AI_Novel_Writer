"""
AI Novel Engine - Character Visual Dossier & Photo System
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Manages character visual profiles, physical architecture, somatic tells,
and optional photo / portrait integration for scene visualization.
"""

import os
import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Any, Optional

DEFAULT_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "characters")


@dataclass
class CharacterDossier:
    name: str
    role: str = "Protagonist"
    photo_path: Optional[str] = None
    visual_description: Dict[str, str] = field(default_factory=dict)
    somatic_tells: List[str] = field(default_factory=list)
    signature_item: str = "Cold forged iron band"
    image_prompt: Optional[str] = None
    epistemic_secrets: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CharacterDossier":
        return cls(
            name=data.get("name", "Unknown"),
            role=data.get("role", "Protagonist"),
            photo_path=data.get("photo_path"),
            visual_description=data.get("visual_description", {}),
            somatic_tells=data.get("somatic_tells", []),
            signature_item=data.get("signature_item", "Cold forged iron band"),
            image_prompt=data.get("image_prompt"),
            epistemic_secrets=data.get("epistemic_secrets", []),
        )

    def render_markdown_card(self, relative_asset_root: str = "assets/characters") -> str:
        """Renders an executive GitHub-flavored Markdown card with optional photo."""
        lines = []
        lines.append(f"### 👤 Character Dossier: {self.name} *({self.role})*\n")

        # Photo rendering
        if self.photo_path:
            # Handle both local relative paths and URLs
            photo_display = self.photo_path
            lines.append(f'<div align="center">\n')
            lines.append(f'  <img src="{photo_display}" alt="{self.name}" width="280" style="border-radius: 8px; border: 1px solid #444; box-shadow: 0 4px 12px rgba(0,0,0,0.3); margin-bottom: 12px;" />\n')
            lines.append(f'  <br/><em>Figure: Visual portrait of {self.name}</em>\n')
            lines.append(f'</div>\n\n')

        # Visual Specs Table
        lines.append("| Visual Trait | Specification |")
        lines.append("| :--- | :--- |")
        lines.append(f"| **Role / Archetype** | {self.role} |")
        lines.append(f"| **Signature Anchor** | `{self.signature_item}` |")

        for trait, val in self.visual_description.items():
            trait_clean = trait.replace("_", " ").title()
            lines.append(f"| **{trait_clean}** | {val} |")

        lines.append("")

        # Somatic Tells
        if self.somatic_tells:
            lines.append("**Somatic Tells & Physical Micro-Gestures:**")
            for tell in self.somatic_tells:
                lines.append(f"- *{tell}*")
            lines.append("")

        # Epistemic Secrets
        if self.epistemic_secrets:
            lines.append("**Hidden Epistemic Envelopes (Secrets Withheld):**")
            for sec in self.epistemic_secrets:
                lines.append(f"- 🔒 {sec}")
            lines.append("")

        # AI Image Prompt
        if self.image_prompt:
            lines.append("<details>")
            lines.append(f"<summary>🖼️ <em>Click to reveal AI Portrait Generation Prompt</em></summary>\n")
            lines.append("```text")
            lines.append(self.image_prompt)
            lines.append("```")
            lines.append("</details>\n")

        return "\n".join(lines)


class CharacterDossierManager:
    """Manages character visual sheets, saving, loading, and directory galleries."""

    def __init__(self, storage_dir: Optional[str] = None):
        self.storage_dir = storage_dir or DEFAULT_ASSETS_DIR
        os.makedirs(self.storage_dir, exist_ok=True)

    def save_dossier(self, dossier: CharacterDossier) -> str:
        slug = dossier.name.lower().replace(" ", "_")
        filepath = os.path.join(self.storage_dir, f"{slug}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(dossier.to_dict(), f, indent=2, ensure_ascii=False)
        return filepath

    def load_dossier(self, name: str) -> Optional[CharacterDossier]:
        slug = name.lower().replace(" ", "_")
        filepath = os.path.join(self.storage_dir, f"{slug}.json")
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return CharacterDossier.from_dict(data)

    def list_dossiers(self) -> List[CharacterDossier]:
        dossiers = []
        for root, _, files in os.walk(self.storage_dir):
            for file in sorted(files):
                if file.endswith(".json"):
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            dossiers.append(CharacterDossier.from_dict(json.load(f)))
                    except Exception:
                        pass
        return dossiers
