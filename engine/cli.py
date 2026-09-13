"""
AI Novel Engine - Command Line Interface
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine
"""

import argparse
import sys
import os
import glob
import re
import json
from engine.core import NovelEngine
from engine.linter import NovelLinter
from engine.attribute_extractor import AttributeExtractor
from engine.graph_knowledge import GraphKnowledgebase
from engine.character_dossier import CharacterDossier, CharacterDossierManager
from engine.critic import PlotCritic


def cmd_audit(args):
    target = args.target or "output"
    linter = NovelLinter(em_dash_threshold=args.threshold)

    files = []
    if os.path.isdir(target):
        for root, _, fs in os.walk(target):
            for f in sorted(fs):
                if f.endswith(".md") and "Pipeline_Execution" not in f:
                    files.append(os.path.join(root, f))
    else:
        files.append(target)

    all_passed = True
    total_words = 0
    total_dashes = 0
    total_violations = 0

    print(f"\n========================================================")
    print(f"  AI Novel Engine Audit: {len(files)} Chapter Files")
    print(f"========================================================\n")

    for p in files:
        res = linter.lint_file(p)
        total_words += res["words"]
        total_dashes += res["dashes"]
        total_violations += res["violation_count"]

        status = "PASSED" if res["passed"] else "FAILED"
        if not res["passed"]:
            all_passed = False

        density_str = f"{res['dash_density']:.1f} w/d" if res["dashes"] > 0 else "0 dashes"
        print(f"[{status}] {res['file']} | {res['words']} words | {res['dashes']} dashes ({density_str})")
        for v in res["violations"]:
            print(f"    - {v}")
        if not res["dash_compliant"]:
            print(f"    - Em-dash density ({res['dash_density']:.1f}) exceeds {linter.em_dash_threshold} ceiling!")

    print("\n--------------------------------------------------------")
    print(f"TOTAL WORDS: {total_words}")
    density = (total_words / total_dashes) if total_dashes > 0 else float("inf")
    print(f"TOTAL DASHES: {total_dashes} (Density: {density:.1f} words/dash)")
    print(f"TOTAL VIOLATIONS: {total_violations}")
    print(f"GATE STATUS: {'PASSED (SHIP)' if all_passed else 'FAILED'}")
    print("========================================================\n")

    sys.exit(0 if all_passed else 1)


def cmd_compile(args):
    output_dir = args.dir or "output"
    out_file = args.out or os.path.join(output_dir, "Complete_Manuscript.md")

    files = sorted(glob.glob(os.path.join(output_dir, "Chapter_*.md")))
    clean_chapters = [f for f in files if "Pipeline_Execution" not in f]

    print(f"Compiling {len(clean_chapters)} chapters into {out_file}...")

    compiled = []
    compiled.append("# The Mysteries of Life\n")
    compiled.append("### By Jaswanth Reddy\n")
    compiled.append("*A 5-Stage AI Novel Engine Master Edition*\n\n---\n\n")

    total_words = 0
    for idx, chap_path in enumerate(clean_chapters, 1):
        content = open(chap_path, encoding="utf-8").read().strip()
        words = len(content.split())
        total_words += words
        compiled.append(content)
        compiled.append("\n\n---\n\n")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("".join(compiled))

    print(f"Successfully compiled {len(clean_chapters)} chapters ({total_words} words) into {out_file}.")


def cmd_stats(args):
    output_dir = args.dir or "output"
    files = sorted(glob.glob(os.path.join(output_dir, "Chapter_*.md")))
    clean_chapters = [f for f in files if "Pipeline_Execution" not in f]
    pipeline_files = [f for f in files if "Pipeline_Execution" in f]

    total_words = 0
    chapter_stats = []

    for f in clean_chapters:
        text = open(f, encoding="utf-8").read()
        w = len(text.split())
        total_words += w
        m = re.search(r"Chapter_(\d+)", f)
        num = int(m.group(1)) if m else 0
        chapter_stats.append((num, os.path.basename(f), w))

    print(f"\n========================================================")
    print(f"  AI Novel Engine: Manuscript Statistics")
    print(f"========================================================")
    print(f"Clean Chapters: {len(clean_chapters)}")
    print(f"Pipeline Execution Logs: {len(pipeline_files)}")
    print(f"Total Word Count: {total_words:,} words")
    print(f"Average Chapter Length: {total_words // len(clean_chapters) if clean_chapters else 0} words")
    print("--------------------------------------------------------")
    for num, name, w in chapter_stats:
        print(f"  Ch {num:02d}: {name[:45]:<45} | {w:>5} words")
    print("========================================================\n")


def cmd_build_graph(args):
    graph = GraphKnowledgebase(auto_build=False)
    json_path = args.json or os.path.join(os.path.dirname(__file__), "..", "data", "authors_100.json")
    print(f"Building Graph Knowledgebase from {json_path}...")
    res = graph.build_graph_from_json(json_path)
    print(f"Success! Graph constructed: {res['nodes']} nodes, {res['edges']} edges.")


def cmd_graph_stats(args):
    graph = GraphKnowledgebase()
    stats = graph.get_graph_stats()

    print(f"\n========================================================")
    print(f"  AI Novel Engine: Graph Knowledgebase Statistics")
    print(f"========================================================")
    print(f"Total Graph Nodes: {stats['total_nodes']}")
    print(f"Total Graph Edges: {stats['total_edges']}")
    print("--------------------------------------------------------")
    print("Nodes Distribution:")
    for node_type, count in sorted(stats["nodes_by_type"].items()):
        print(f"  - {node_type:<18}: {count:>4}")
    print("--------------------------------------------------------")
    print("Edges Distribution:")
    for rel, count in sorted(stats["edges_by_relation"].items()):
        print(f"  - {rel:<18}: {count:>4}")
    print("========================================================\n")


def cmd_match(args):
    text = args.text
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    if not text:
        print("Error: Provide --text or --file to match.")
        sys.exit(1)

    extractor = AttributeExtractor()
    graph = GraphKnowledgebase()

    overrides = {}
    if args.genre:
        overrides["genre"] = args.genre
    if args.era:
        overrides["era"] = args.era

    attrs = extractor.extract(text, user_overrides=overrides)
    bundle = graph.generate_craft_injection(attrs, top_k=args.top)

    print(f"\n========================================================")
    print(f"  Narrative Attribute Extraction & Graph Match")
    print(f"========================================================")
    print(f"Primary Genre : {attrs.primary_genre}")
    print(f"Secondary     : {', '.join(attrs.secondary_genres) if attrs.secondary_genres else 'None'}")
    print(f"Vibes         : {', '.join(attrs.vibes)}")
    print(f"Tech Era      : {attrs.tech_era}")
    print(f"Magic System  : {attrs.magic_hardness}")
    print(f"Pacing        : {attrs.pacing}")
    print(f"Confidence    : {attrs.confidence:.2f}")
    print("--------------------------------------------------------")
    print(f"Top {len(bundle['top_reference_authors'])} Reference Authors Matched:")
    for author in bundle["raw_matches"]:
        print(f"  * {author['name']} (Score: {author['score']})")
        print(f"    Reasons: {', '.join(author['match_reasons'])}")
        print(f"    Works  : {', '.join(author['reference_works'][:2])}")
    print("--------------------------------------------------------")
    print("Curated Craft Directives Injected:")
    for tech in bundle["curated_craft_techniques"]:
        print(f"  - {tech}")
    print("--------------------------------------------------------")
    print("Source Repositories to Pull Works/Style:")
    for repo in bundle["source_repositories"]:
        print(f"  [Link] {repo}")
    print("========================================================\n")


def cmd_plan(args):
    engine = NovelEngine()
    text = args.notes
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    if not text:
        print("Error: Provide --notes or --file for scene planning.")
        sys.exit(1)

    contract = engine.plan_scene_from_notes(
        chapter=args.chapter,
        title=args.title,
        notes=text,
        pov=args.pov,
        top_k=args.top,
    )

    yaml_str = engine.director.export_contract_yaml(contract)
    print(f"\n# Compiled Stage 1 Scene Contract with Graph Craft Injection:\n")
    print(yaml_str)


def cmd_critique(args):
    engine = NovelEngine()
    text = args.notes
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read()

    if not text:
        print("Error: Provide --notes or --file to critique.")
        sys.exit(1)

    overrides = {}
    if args.genre:
        overrides["genre"] = args.genre
    if args.era:
        overrides["era"] = args.era

    # Load characters if requested
    chars = []
    if args.characters:
        names = [n.strip() for n in args.characters.split(",")]
        for n in names:
            c = engine.character_manager.load_dossier(n)
            if c:
                chars.append(c)
    elif not args.no_characters:
        chars = engine.character_manager.list_dossiers()

    # Optional custom photo passed via CLI
    if args.photo and chars:
        chars[0].photo_path = args.photo

    report_md = engine.critic.generate_markdown_critique(
        plot_text=text,
        characters=chars,
        overrides=overrides,
    )

    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report_md)
        print(f"\nSuccessfully generated plot critique and character sheet at {args.out} ({len(report_md)} characters).")
    else:
        # Safe printing for various terminal encodings
        if hasattr(sys.stdout, "reconfigure"):
            try:
                sys.stdout.reconfigure(encoding="utf-8")
            except Exception:
                pass
        print(report_md)


def cmd_character_card(args):
    manager = CharacterDossierManager()
    dossier = CharacterDossier(
        name=args.name,
        role=args.role or "Protagonist",
        photo_path=args.photo,
        signature_item=args.item or "Cold forged iron band",
        visual_description={"summary": args.desc} if args.desc else {},
        somatic_tells=[t.strip() for t in args.tells.split(";")] if args.tells else [],
    )

    if args.save:
        p = manager.save_dossier(dossier)
        print(f"Saved character dossier for {args.name} to {p}")

    print("\n" + dossier.render_markdown_card())


def main():
    parser = argparse.ArgumentParser(description="AI Novel Engine CLI - Developed for Jaswanth1902")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # audit
    audit_parser = subparsers.add_parser("audit", help="Run automated anti-slop linter on manuscript")
    audit_parser.add_argument("--target", default="output", help="Directory or file to audit")
    audit_parser.add_argument("--threshold", type=int, default=800, help="Em-dash density ceiling (words/dash)")
    audit_parser.set_defaults(func=cmd_audit)

    # compile
    compile_parser = subparsers.add_parser("compile", help="Compile chapters into complete manuscript")
    compile_parser.add_argument("--dir", default="output", help="Directory containing chapters")
    compile_parser.add_argument("--out", default=None, help="Output manuscript filepath")
    compile_parser.set_defaults(func=cmd_compile)

    # stats
    stats_parser = subparsers.add_parser("stats", help="Print manuscript metrics and word count breakdown")
    stats_parser.add_argument("--dir", default="output", help="Output directory")
    stats_parser.set_defaults(func=cmd_stats)

    # build-graph
    bg_parser = subparsers.add_parser("build-graph", help="Rebuild SQLite knowledge graph from 100 authors JSON")
    bg_parser.add_argument("--json", default=None, help="Path to authors JSON")
    bg_parser.set_defaults(func=cmd_build_graph)

    # graph-stats
    gs_parser = subparsers.add_parser("graph-stats", help="Print knowledge graph metrics and distribution")
    gs_parser.set_defaults(func=cmd_graph_stats)

    # match
    match_parser = subparsers.add_parser("match", help="Match user narrative brief against 100 authors graph")
    match_parser.add_argument("--text", default=None, help="Raw user story pitch / scene brief")
    match_parser.add_argument("--file", default=None, help="Path to text/markdown notes file")
    match_parser.add_argument("--genre", default=None, help="Explicit genre override")
    match_parser.add_argument("--era", default=None, help="Explicit era override")
    match_parser.add_argument("--top", type=int, default=3, help="Number of matching authors to retrieve")
    match_parser.set_defaults(func=cmd_match)

    # plan
    plan_parser = subparsers.add_parser("plan", help="Compile a Stage 1 Scene Contract with graph craft injection")
    plan_parser.add_argument("--chapter", type=int, default=37, help="Chapter number")
    plan_parser.add_argument("--title", default="The Silent Convergence", help="Chapter title")
    plan_parser.add_argument("--notes", default=None, help="Raw notes or synopsis")
    plan_parser.add_argument("--file", default=None, help="Path to notes file")
    plan_parser.add_argument("--pov", default="Jaswanth", help="POV character name")
    plan_parser.add_argument("--top", type=int, default=3, help="Top authors to inject")
    plan_parser.set_defaults(func=cmd_plan)

    # critique
    critique_parser = subparsers.add_parser("critique", help="Generate plot diagnostic, craft upgrades, and character visual sheet")
    critique_parser.add_argument("--notes", default=None, help="Raw plot outline or scene notes")
    critique_parser.add_argument("--file", default=None, help="Path to notes file")
    critique_parser.add_argument("--out", default=None, help="Output markdown report path")
    critique_parser.add_argument("--characters", default=None, help="Comma-separated character names to attach")
    critique_parser.add_argument("--no-characters", action="store_true", help="Do not attach character dossiers")
    critique_parser.add_argument("--photo", default=None, help="Optional photo path for primary character")
    critique_parser.add_argument("--genre", default=None, help="Explicit genre override")
    critique_parser.add_argument("--era", default=None, help="Explicit era override")
    critique_parser.set_defaults(func=cmd_critique)

    # character-card
    char_parser = subparsers.add_parser("character-card", help="Create and render a character visual card with optional photo")
    char_parser.add_argument("--name", required=True, help="Character name")
    char_parser.add_argument("--role", default="Protagonist", help="Archetype or role")
    char_parser.add_argument("--photo", default=None, help="Local image path or URL")
    char_parser.add_argument("--item", default=None, help="Signature anchor item")
    char_parser.add_argument("--desc", default=None, help="Visual physical description")
    char_parser.add_argument("--tells", default=None, help="Semicolon-separated somatic tells")
    char_parser.add_argument("--save", action="store_true", help="Save into assets/characters/")
    char_parser.set_defaults(func=cmd_character_card)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
