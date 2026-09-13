# Contributing to AI Novel Writer

Thank you for your interest in contributing to **AI Novel Writer**! We welcome contributions that expand the 100-Author Graph Knowledgebase, refine craft technique definitions, improve the anti-slop linter, or enhance long-form fiction continuity.

---

## 🏛️ Ground Rules & Craft Standards

1. **Craft Above Automation**: We do NOT accept features that promote generic AI cliches, purple prose, or passive filter verbs (`he felt`, `she noticed`). All additions must elevate writing craft toward master literary benchmarks (Gardner psychic distance, somatic autonomic tells, Newtonian kinetics).
2. **Empirical Verification**: Every pull request must pass the test suite (`pytest`) with 100% success and zero syntax/lint errors.
3. **Privacy First**: Never commit private manuscripts, character dossiers with sensitive personal data, or API keys.

---

## 🛠️ Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/Jaswanth1902/AI_Novel_Engine.git
   cd AI_Novel_Engine
   ```

2. **Set up your environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   pip install pytest
   ```

3. **Run the test suite**:
   ```bash
   pytest
   ```

---

## 🖋️ Ways to Contribute

### 1. Expanding the Author Craft Knowledgebase
To propose a new master author or technique:
- Update `data/authors_100.json` with the author name, primary genres, signature techniques, reference works, and verified source repositories.
- Run `python novel_writer.py build-graph` to recompile the SQLite graph database (`state/author_knowledge_graph.sqlite`).
- Verify graph metrics via `python novel_writer.py graph-stats`.

### 2. Improving the Anti-Slop Linter
- Propose new regex detectors or somatic substitutions in `engine/linter.py`.
- Add corresponding unit tests in `tests/test_novel_engine.py`.

### 3. Enhancing the 5-Stage Pipeline
- Stage 1: `engine/director.py` (Scene contract generation & craft injection)
- Stage 2: `engine/actor.py` (Epistemic envelopes & knowledge asymmetry)
- Stage 3: `engine/stylist.py` (Psychic distance & prose calibration)
- Stage 4: `engine/core.py` (Prose drafting & kinetic rendering)
- Stage 5: `engine/gatekeeper.py` (Delta state JSON & continuity memory)

---

## 📜 Pull Request Process

1. Create a feature branch (`git checkout -b feature/craft-upgrade`).
2. Commit your changes with clear semantic messages (`feat: add Gene Wolfe craft techniques to graph`).
3. Ensure all tests pass (`pytest`).
4. Submit a Pull Request targeting `main`.

Thank you for helping us elevate the quality of open storytelling!
