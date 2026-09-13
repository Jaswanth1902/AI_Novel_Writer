"""
AI Novel Engine - Automated Quality Linter
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Enforces:
- 0 Filter Verbs
- 0 Banned AI Cliches
- 0 Banned Faux-Archaic Crutches (scriptorium, portico, visage, countenance, ebon, eldritch)
- 0 Technological Anachronisms (configurable per era: Stone, Medieval, ATLA-Industrial, Victorian, Sci-Fi)
- Strict Em-dash density (>= 800 words per dash)
"""

import os
import re
import sys
import yaml
from typing import Dict, List, Tuple, Any, Optional

BANNED_AI_CLICHES = [
    "testament to",
    "tapestry of",
    "delve",
    "delved",
    "beacon of",
    "symphony of",
    "shivers down",
    "shiver down",
    "cacophony",
    "labyrinthine",
    "a dance of",
    "intertwined",
    "resonated with",
    "palpable tension",
    "a grim reminder",
    "steely resolve",
    "unspoken understanding",
    "silent sentinel",
    "whispers of",
    "little did he know",
    "little did she know",
]

BANNED_FAUX_ARCHAIC_CRUTCHES = [
    "scriptorium",
    "portico",
    "visage",
    "countenance",
    "ebon",
    "eldritch",
]

DEFAULT_ANACHRONISMS = [
    "couch",
    "couches",
    "sofa",
    "sofas",
    "tea",
    "teacup",
    "teapot",
    "coffee",
    "zipper",
    "cigarette",
]

FILTER_VERB_PATTERNS = [
    r"\b(he|she|they|i|we)\s+felt\b",
    r"\b(he|she|they|i|we)\s+noticed\b",
    r"\b(he|she|they|i|we)\s+wondered\b",
    r"\b(he|she|they|i|we)\s+realized\b",
    r"\b(he|she|they|i|we)\s+decided\b",
    r"\b(he|she|they|i|we)\s+heard\s+that\b",
    r"\b(he|she|they|i|we)\s+saw\s+that\b",
    r"\b(jaswanth|chaitanya|bennett|anirudh)\s+(felt|noticed|wondered|realized)\b",
    r"\bfelt\s+like\b",
    r"\bnoticed\s+that\b",
    r"\bseemed\s+to\s+be\b",
]


class LintViolation:
    def __init__(self, line_num: int, category: str, pattern: str, snippet: str):
        self.line_num = line_num
        self.category = category
        self.pattern = pattern
        self.snippet = snippet.strip()

    def __str__(self) -> str:
        return f"Line {self.line_num} [{self.category}]: Found '{self.pattern}' -> \"{self.snippet}\""


class NovelLinter:
    def __init__(self, em_dash_threshold: int = 800, era: str = "industrial_atla"):
        self.em_dash_threshold = em_dash_threshold
        self.era = era
        self.era_anachronisms = self._load_era_anachronisms(era)

    def _load_era_anachronisms(self, era: str) -> List[str]:
        cfg_path = os.path.join(os.path.dirname(__file__), "..", "config", "genre_matrix.yaml")
        if os.path.exists(cfg_path):
            with open(cfg_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                return data.get("technological_eras", {}).get(era, {}).get("forbidden", DEFAULT_ANACHRONISMS)
        return DEFAULT_ANACHRONISMS

    def lint_text(self, text: str) -> Dict[str, Any]:
        lines = text.splitlines()
        words = len(text.split())
        dashes = len(re.findall(r"—|--", text))
        violations: List[LintViolation] = []

        for idx, line in enumerate(lines, 1):
            # Check filter verbs
            for pattern in FILTER_VERB_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    m = re.search(pattern, line, re.IGNORECASE)
                    violations.append(LintViolation(idx, "FILTER_VERB", m.group(0), line))

            # Check banned AI cliches
            for phrase in BANNED_AI_CLICHES:
                if re.search(r"\b" + re.escape(phrase) + r"\b", line, re.IGNORECASE):
                    violations.append(LintViolation(idx, "BANNED_AI_CLICHE", phrase, line))

            # Check banned faux-archaic crutches
            for word in BANNED_FAUX_ARCHAIC_CRUTCHES:
                if re.search(r"\b" + re.escape(word) + r"\b", line, re.IGNORECASE):
                    violations.append(LintViolation(idx, "BANNED_CRUTCH", word, line))

            # Check anachronisms
            for item in self.era_anachronisms:
                if re.search(r"\b" + re.escape(item) + r"\b", line, re.IGNORECASE):
                    violations.append(LintViolation(idx, f"ANACHRONISM_{self.era.upper()}", item, line))

        dash_density = (words / dashes) if dashes > 0 else float("inf")
        dash_compliant = dash_density >= self.em_dash_threshold

        passed = (len(violations) == 0) and dash_compliant

        return {
            "passed": passed,
            "words": words,
            "dashes": dashes,
            "dash_density": dash_density,
            "dash_compliant": dash_compliant,
            "violations": violations,
            "violation_count": len(violations),
        }

    def lint_file(self, filepath: str) -> Dict[str, Any]:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        results = self.lint_text(text)
        results["file"] = os.path.basename(filepath)
        results["filepath"] = filepath
        return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m engine.linter <path_to_markdown_or_dir> [--era <era>]")
        sys.exit(1)

    target = sys.argv[1]
    era = "industrial_atla"
    if "--era" in sys.argv:
        idx = sys.argv.index("--era")
        if idx + 1 < len(sys.argv):
            era = sys.argv[idx + 1]

    linter = NovelLinter(era=era)

    files_to_check = []
    if os.path.isdir(target):
        for root, _, files in os.walk(target):
            for file in sorted(files):
                if file.endswith(".md") and "Pipeline_Execution" not in file:
                    files_to_check.append(os.path.join(root, file))
    else:
        files_to_check.append(target)

    all_passed = True
    total_words = 0
    total_dashes = 0
    total_violations = 0

    print(f"\n========================================================")
    print(f"  AI Novel Engine Quality Gate: Auditing {len(files_to_check)} Files [Era: {era}]")
    print(f"========================================================\n")

    for fpath in files_to_check:
        res = linter.lint_file(fpath)
        total_words += res["words"]
        total_dashes += res["dashes"]
        total_violations += res["violation_count"]

        status = "PASSED" if res["passed"] else "FAILED"
        if not res["passed"]:
            all_passed = False

        density_str = f"{res['dash_density']:.1f} w/d" if res["dashes"] > 0 else "0 dashes"
        print(f"[{status}] {res['file']} | Words: {res['words']} | Dashes: {res['dashes']} ({density_str})")

        if res["violations"]:
            for v in res["violations"]:
                print(f"    - {v}")
        if not res["dash_compliant"]:
            print(f"    - Em-dash density ({res['dash_density']:.1f}) exceeds threshold ({linter.em_dash_threshold} w/d)!")

    print("\n--------------------------------------------------------")
    print(f"TOTAL WORDS: {total_words}")
    density_overall = (total_words / total_dashes) if total_dashes > 0 else float("inf")
    print(f"TOTAL DASHES: {total_dashes} (Density: {density_overall:.1f} words/dash)")
    print(f"TOTAL VIOLATIONS: {total_violations}")
    print(f"OVERALL QUALITY GATE: {'PASSED (SHIP)' if all_passed else 'FAILED'}")
    print("========================================================\n")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
