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
from engine.core import NovelEngine
from engine.linter import NovelLinter


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

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
