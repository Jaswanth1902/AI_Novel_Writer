"""
AI Novel Engine - Graph Knowledgebase
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

SQLite-backed graph knowledgebase linking:
- Authors (100 master authors across all genres)
- Reference Works (novels, sagas, collections)
- Genres & Subgenres
- Aesthetic Vibes & Tone profiles
- Technological Eras & Historical settings
- Signature Craft Techniques
- Source Repositories & Archives

Enables deterministic graph traversal to match user narrative briefs with
canonical reference books and inject master author techniques into prose drafting.
"""

import os
import json
import sqlite3
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from engine.attribute_extractor import ExtractedAttributes

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "author_knowledge_graph.sqlite")
DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "authors_100.json")


class GraphKnowledgebase:
    """Graph database and craft recommendation engine for novel writing."""

    def __init__(self, db_path: Optional[str] = None, auto_build: bool = True):
        self.db_path = db_path or DEFAULT_DB_PATH
        os.makedirs(os.path.dirname(os.path.abspath(self.db_path)), exist_ok=True)
        self._init_schema()
        if auto_build and self.get_node_count() == 0:
            self.build_graph_from_json(DEFAULT_DATA_PATH)

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA synchronous=NORMAL;")
        return conn

    def _init_schema(self):
        with self._get_conn() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS nodes (
                    id TEXT PRIMARY KEY,
                    type TEXT NOT NULL,
                    name TEXT NOT NULL,
                    metadata TEXT
                );

                CREATE TABLE IF NOT EXISTS edges (
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    relation TEXT NOT NULL,
                    weight REAL DEFAULT 1.0,
                    PRIMARY KEY (source_id, target_id, relation),
                    FOREIGN KEY (source_id) REFERENCES nodes(id) ON DELETE CASCADE,
                    FOREIGN KEY (target_id) REFERENCES nodes(id) ON DELETE CASCADE
                );

                CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(type);
                CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_id);
                CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_id);
                CREATE INDEX IF NOT EXISTS idx_edges_relation ON edges(relation);
            """)

    def get_node_count(self) -> int:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM nodes")
            return cur.fetchone()[0]

    def build_graph_from_json(self, json_path: str) -> Dict[str, int]:
        """Ingests the 100 authors master database and constructs the knowledge graph."""
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Authors JSON database not found at {json_path}")

        with open(json_path, "r", encoding="utf-8") as f:
            authors_data = json.load(f)

        nodes_inserted = 0
        edges_inserted = 0

        with self._get_conn() as conn:
            cur = conn.cursor()
            # Clear existing data for clean idempotent rebuild
            cur.execute("DELETE FROM edges;")
            cur.execute("DELETE FROM nodes;")

            for author in authors_data:
                author_id = f"author:{author['id']}"
                author_name = author["name"]
                author_meta = json.dumps({
                    "magic_hardness": author.get("magic_hardness", "none_mundane"),
                    "source_repositories": author.get("source_repositories", []),
                }, ensure_ascii=False)

                # 1. Author Node
                cur.execute(
                    "INSERT OR REPLACE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                    (author_id, "author", author_name, author_meta)
                )
                nodes_inserted += 1

                # 2. Key Works
                for work in author.get("key_works", []):
                    work_id = f"work:{author['id']}:{work.lower().replace(' ', '_').replace(':', '')}"
                    cur.execute(
                        "INSERT OR IGNORE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                        (work_id, "work", work, json.dumps({"author": author_name}))
                    )
                    nodes_inserted += 1

                    # Edge: Author WROTE Work
                    cur.execute(
                        "INSERT OR IGNORE INTO edges (source_id, target_id, relation, weight) VALUES (?, ?, ?, ?)",
                        (author_id, work_id, "WROTE", 1.0)
                    )
                    edges_inserted += 1

                # 3. Genres
                for genre in author.get("genres", []):
                    genre_slug = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")
                    genre_id = f"genre:{genre_slug}"
                    cur.execute(
                        "INSERT OR IGNORE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                        (genre_id, "genre", genre, "{}")
                    )
                    nodes_inserted += 1

                    # Edge: Author EXCELS_IN Genre
                    cur.execute(
                        "INSERT OR IGNORE INTO edges (source_id, target_id, relation, weight) VALUES (?, ?, ?, ?)",
                        (author_id, genre_id, "EXCELS_IN", 1.0)
                    )
                    edges_inserted += 1

                # 4. Vibes
                for vibe in author.get("vibes", []):
                    vibe_slug = vibe.lower().replace(" ", "_").replace("-", "_")
                    vibe_id = f"vibe:{vibe_slug}"
                    cur.execute(
                        "INSERT OR IGNORE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                        (vibe_id, "vibe", vibe, "{}")
                    )
                    nodes_inserted += 1

                    # Edge: Author EVOKES_VIBE Vibe
                    cur.execute(
                        "INSERT OR IGNORE INTO edges (source_id, target_id, relation, weight) VALUES (?, ?, ?, ?)",
                        (author_id, vibe_id, "EVOKES_VIBE", 1.0)
                    )
                    edges_inserted += 1

                # 5. Tech Eras
                for era in author.get("tech_eras", []):
                    era_slug = era.lower().replace(" ", "_").replace("-", "_")
                    era_id = f"era:{era_slug}"
                    cur.execute(
                        "INSERT OR IGNORE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                        (era_id, "tech_era", era, "{}")
                    )
                    nodes_inserted += 1

                    # Edge: Author OPERATES_IN TechEra
                    cur.execute(
                        "INSERT OR IGNORE INTO edges (source_id, target_id, relation, weight) VALUES (?, ?, ?, ?)",
                        (author_id, era_id, "OPERATES_IN", 1.0)
                    )
                    edges_inserted += 1

                # 6. Signature Craft Techniques
                for idx, tech in enumerate(author.get("signature_techniques", [])):
                    tech_id = f"technique:{author['id']}:{idx+1}"
                    cur.execute(
                        "INSERT OR IGNORE INTO nodes (id, type, name, metadata) VALUES (?, ?, ?, ?)",
                        (tech_id, "craft_technique", tech, json.dumps({"author": author_name}))
                    )
                    nodes_inserted += 1

                    # Edge: Author MASTERS Technique
                    cur.execute(
                        "INSERT OR IGNORE INTO edges (source_id, target_id, relation, weight) VALUES (?, ?, ?, ?)",
                        (author_id, tech_id, "MASTERS", 1.0)
                    )
                    edges_inserted += 1

            conn.commit()

        return {"nodes": self.get_node_count(), "edges": self.get_edge_count()}

    def get_edge_count(self) -> int:
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM edges")
            return cur.fetchone()[0]

    def get_graph_stats(self) -> Dict[str, Any]:
        """Returns comprehensive graph metrics and distribution."""
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT type, COUNT(*) FROM nodes GROUP BY type")
            node_dist = dict(cur.fetchall())

            cur.execute("SELECT relation, COUNT(*) FROM edges GROUP BY relation")
            edge_dist = dict(cur.fetchall())

            cur.execute("SELECT COUNT(DISTINCT source_id) + COUNT(DISTINCT target_id) FROM edges")
            connected_elements = cur.fetchone()[0]

        return {
            "total_nodes": sum(node_dist.values()),
            "total_edges": sum(edge_dist.values()),
            "nodes_by_type": node_dist,
            "edges_by_relation": edge_dist,
            "connected_elements": connected_elements,
        }

    def match_authors(self, attributes: ExtractedAttributes, top_k: int = 3) -> List[Dict[str, Any]]:
        """Traverses the graph to score and rank authors against extracted attributes."""
        with self._get_conn() as conn:
            cur = conn.cursor()

            cur.execute("SELECT id, name, metadata FROM nodes WHERE type = 'author'")
            authors = cur.fetchall()

            scored_authors = []

            for author_id, author_name, metadata_str in authors:
                meta = json.loads(metadata_str or "{}")
                score = 0.0
                match_reasons = []

                # Fetch connected genres
                cur.execute("""
                    SELECT n.name FROM nodes n
                    JOIN edges e ON e.target_id = n.id
                    WHERE e.source_id = ? AND e.relation = 'EXCELS_IN'
                """, (author_id,))
                author_genres = [r[0].lower() for r in cur.fetchall()]

                # Fetch connected vibes
                cur.execute("""
                    SELECT n.name FROM nodes n
                    JOIN edges e ON e.target_id = n.id
                    WHERE e.source_id = ? AND e.relation = 'EVOKES_VIBE'
                """, (author_id,))
                author_vibes = [r[0].lower() for r in cur.fetchall()]

                # Fetch connected eras
                cur.execute("""
                    SELECT n.name FROM nodes n
                    JOIN edges e ON e.target_id = n.id
                    WHERE e.source_id = ? AND e.relation = 'OPERATES_IN'
                """, (author_id,))
                author_eras = [r[0].lower() for r in cur.fetchall()]

                # 1. Match Primary Genre (Weight: 12.0 for exact/stem match, 6.0 for word match)
                pri_genre_clean = attributes.primary_genre.lower()
                pri_words = set(pri_genre_clean.split())
                for ag in author_genres:
                    if ag == pri_genre_clean or pri_genre_clean in ag or ag in pri_genre_clean:
                        score += 12.0
                        match_reasons.append(f"Primary genre: {ag}")
                        break
                    elif any(w in ag for w in pri_words if len(w) > 3):
                        score += 6.0
                        match_reasons.append(f"Genre overlap: {ag}")
                        break

                # 2. Match Secondary Genres (Weight: 4.0)
                for sec in attributes.secondary_genres:
                    sec_clean = sec.lower()
                    sec_words = set(sec_clean.split())
                    for ag in author_genres:
                        if sec_clean in ag or ag in sec_clean or any(w in ag for w in sec_words if len(w) > 3):
                            score += 4.0
                            match_reasons.append(f"Secondary genre: {ag}")
                            break

                # 3. Match Vibes (Weight: 3.0)
                for v in attributes.vibes:
                    v_clean = v.lower()
                    v_parts = [p for p in v_clean.split("_") if len(p) > 3]
                    for av in author_vibes:
                        if v_clean in av or av in v_clean or any(part in av for part in v_parts):
                            score += 3.0
                            match_reasons.append(f"Vibe: {av}")
                            break

                # 4. Match Era (Weight: 2.0)
                era_clean = attributes.tech_era.lower()
                era_parts = [p for p in era_clean.split("_") if len(p) > 3]
                for ae in author_eras:
                    if era_clean in ae or ae in era_clean or any(part in ae for part in era_parts):
                        score += 2.0
                        match_reasons.append(f"Era: {ae}")
                        break

                # 5. Magic Hardness Alignment (Weight: 3.0 exact, 1.5 category)
                author_magic = meta.get("magic_hardness", "none_mundane")
                if author_magic == attributes.magic_hardness:
                    score += 3.0
                    match_reasons.append(f"Magic law: {author_magic}")
                elif any(term in author_magic and term in attributes.magic_hardness for term in ["progression", "hard", "soft", "none"]):
                    score += 1.5
                    match_reasons.append(f"Magic compatibility: {author_magic}")

                if score > 0:
                    # Retrieve Works
                    cur.execute("""
                        SELECT n.name FROM nodes n
                        JOIN edges e ON e.target_id = n.id
                        WHERE e.source_id = ? AND e.relation = 'WROTE'
                    """, (author_id,))
                    works = [r[0] for r in cur.fetchall()]

                    # Retrieve Craft Techniques
                    cur.execute("""
                        SELECT n.name FROM nodes n
                        JOIN edges e ON e.target_id = n.id
                        WHERE e.source_id = ? AND e.relation = 'MASTERS'
                    """, (author_id,))
                    techniques = [r[0] for r in cur.fetchall()]

                    scored_authors.append({
                        "id": author_id.replace("author:", ""),
                        "name": author_name,
                        "score": round(score, 2),
                        "match_reasons": match_reasons[:4],
                        "magic_hardness": author_magic,
                        "reference_works": works,
                        "signature_techniques": techniques,
                        "source_repositories": meta.get("source_repositories", []),
                    })

            scored_authors.sort(key=lambda x: x["score"], reverse=True)
            return scored_authors[:top_k]

    def generate_craft_injection(
        self,
        attributes: ExtractedAttributes,
        top_k: int = 3
    ) -> Dict[str, Any]:
        """Produces a ready-to-inject bundle of master author craft directives and reference works."""
        matches = self.match_authors(attributes, top_k=top_k)

        reference_authors = [m["name"] for m in matches]
        all_reference_works = []
        curated_techniques = []
        source_repos = []

        for m in matches:
            all_reference_works.extend(m["reference_works"][:2])
            for t in m["signature_techniques"][:2]:
                curated_techniques.append(f"[{m['name']}] {t}")
            source_repos.extend(m["source_repositories"][:2])

        return {
            "query_attributes": attributes.to_dict(),
            "top_reference_authors": reference_authors,
            "matched_works": list(dict.fromkeys(all_reference_works)),
            "curated_craft_techniques": curated_techniques,
            "source_repositories": list(dict.fromkeys(source_repos)),
            "pacing_recommendation": attributes.pacing,
            "sensory_palette": attributes.sensory_palette,
            "raw_matches": matches,
        }
