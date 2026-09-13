"""
Unit & Integration Tests for AI Novel Engine v2.0
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine
"""

import pytest
import os
import json
from engine.linter import NovelLinter
from engine.attribute_extractor import AttributeExtractor, ExtractedAttributes
from engine.graph_knowledge import GraphKnowledgebase
from engine.director import Director
from engine.stylist import Stylist
from engine.core import NovelEngine


def test_author_database_integrity():
    json_path = os.path.join(os.path.dirname(__file__), "..", "data", "authors_100.json")
    assert os.path.exists(json_path), "authors_100.json must exist"

    with open(json_path, "r", encoding="utf-8") as f:
        authors = json.load(f)

    assert len(authors) == 100, f"Expected 100 authors, got {len(authors)}"

    ids = set()
    for a in authors:
        assert "id" in a and a["id"], "Author must have id"
        assert "name" in a and a["name"], "Author must have name"
        assert "genres" in a and len(a["genres"]) > 0, f"Author {a['name']} missing genres"
        assert "vibes" in a and len(a["vibes"]) > 0, f"Author {a['name']} missing vibes"
        assert "signature_techniques" in a and len(a["signature_techniques"]) >= 3, f"Author {a['name']} requires signature techniques"
        assert "key_works" in a and len(a["key_works"]) >= 2, f"Author {a['name']} requires key works"
        assert "source_repositories" in a and len(a["source_repositories"]) >= 1, f"Author {a['name']} requires source repos"
        assert a["id"] not in ids, f"Duplicate author id: {a['id']}"
        ids.add(a["id"])


def test_graph_knowledgebase():
    graph = GraphKnowledgebase()
    stats = graph.get_graph_stats()

    assert stats["total_nodes"] >= 1000, f"Expected >= 1000 nodes, got {stats['total_nodes']}"
    assert stats["nodes_by_type"]["author"] == 100
    assert stats["nodes_by_type"]["craft_technique"] >= 300
    assert stats["total_edges"] >= 1200


def test_attribute_extractor():
    extractor = AttributeExtractor()

    # Test Progression Fantasy
    p_text = "He circulated celestial qi through damaged meridians to reach the fifth core realm."
    p_attrs = extractor.extract(p_text)
    assert p_attrs.primary_genre == "Progression Fantasy"
    assert p_attrs.magic_hardness == "progression_meridian"

    # Test Cyberpunk
    c_text = "The netrunner slammed into cyberware ice as megacorp neon reflected off wet asphalt."
    c_attrs = extractor.extract(c_text)
    assert c_attrs.primary_genre == "Cyberpunk"
    assert c_attrs.tech_era == "near_future"

    # Test Hard Sci-Fi
    s_text = "The orbital shuttle fired its reaction thrusters to cancel delta-v before vacuum decompression."
    s_attrs = extractor.extract(s_text)
    assert s_attrs.primary_genre == "Hard Sci-Fi"
    assert s_attrs.tech_era == "far_future"


def test_graph_matching_and_craft_injection():
    extractor = AttributeExtractor()
    graph = GraphKnowledgebase()

    text = "A gritty mercenary with a scarred hand defending an iron gate in freezing mud."
    attrs = extractor.extract(text)
    injection = graph.generate_craft_injection(attrs, top_k=3)

    assert len(injection["top_reference_authors"]) >= 1
    assert len(injection["matched_works"]) >= 1
    assert len(injection["curated_craft_techniques"]) >= 1
    assert len(injection["source_repositories"]) >= 1


def test_linter_invariants():
    linter = NovelLinter()

    # Negative test: filter verb
    res1 = linter.lint_text("Jaswanth felt the cold iron bite into his palm.")
    assert not res1["passed"]
    assert any("filter_verb" in str(v).lower() for v in res1["violations"])

    # Negative test: banned crutch (scriptorium)
    res2 = linter.lint_text("He walked into the dark scriptorium to study the texts.")
    assert not res2["passed"]
    assert any("scriptorium" in str(v).lower() for v in res2["violations"])

    # Negative test: banned crutch (portico)
    res3 = linter.lint_text("Rain dripped from the stone portico.")
    assert not res3["passed"]
    assert any("portico" in str(v).lower() for v in res3["violations"])

    # Positive clean prose test
    res4 = linter.lint_text("Cold iron bit into the palm. Rain pounded the stone threshold. A hammer struck the anvil three times.")
    assert res4["passed"]
    assert res4["violation_count"] == 0


def test_director_scene_contract():
    director = Director()
    contract = director.compile_from_user_notes(
        chapter=37,
        title="The Glass Lattice",
        user_notes="Jaswanth discovers that the obsidian core of the tower is leaking dielectric current into the subterranean aquifers.",
        pov="Jaswanth"
    )

    assert contract["chapter"] == 37
    assert contract["title"] == "The Glass Lattice"
    assert "craft_injection" in contract
    assert len(contract["craft_injection"]["reference_authors"]) > 0
    assert len(contract["craft_injection"]["signature_techniques"]) > 0


def test_character_dossier():
    from engine.character_dossier import CharacterDossier, CharacterDossierManager
    manager = CharacterDossierManager()
    dossiers = manager.list_dossiers()
    assert len(dossiers) >= 1, "Expected at least one character dossier"
    jaswanth = manager.load_dossier("Jaswanth")
    assert jaswanth is not None
    assert jaswanth.name == "Jaswanth"
    assert jaswanth.photo_path is not None
    md = jaswanth.render_markdown_card()
    assert "Character Dossier: Jaswanth" in md
    assert "Cold-forged iron band" in md


def test_plot_critic():
    from engine.critic import PlotCritic
    from engine.character_dossier import CharacterDossierManager
    critic = PlotCritic()
    manager = CharacterDossierManager()
    chars = manager.list_dossiers()

    sample_plot = "Unit 07 races against dawn to seal the thermal vents before the turbine hall explodes."
    eval_res = critic.evaluate_plot(sample_plot, characters=chars)

    assert "scorecard" in eval_res
    assert eval_res["scorecard"]["overall_score"] > 0
    assert len(eval_res["master_authors_matched"]) > 0
    assert len(eval_res["structural_upgrades"]) > 0

    report = critic.generate_markdown_critique(sample_plot, characters=chars)
    assert "# 📝 Plot Diagnostic" in report
    assert "Anti-Plagiarism" in report

