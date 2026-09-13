"""
AI Novel Engine - Story State & Epistemic Memory Engine
Author: Jaswanth1902
Repository: Jaswanth1902/AI_Novel_Engine

Local-first SQLite WAL memory engine tracking:
- Chronological timeline events
- Character locations, health, and status
- Epistemic knowledge state (who knows what, sworn oaths)
- Inventory and physical artifacts
"""

import sqlite3
import os
import json
from typing import Dict, List, Any, Optional

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "..", "state", "story_state.sqlite")


class StoryMemory:
    def __init__(self, db_path: str = DEFAULT_DB_PATH):
        self.db_path = os.path.abspath(db_path)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.execute("PRAGMA foreign_keys=ON;")
        return conn

    def _init_db(self):
        with self._get_connection() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS timeline (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    chapter INTEGER NOT NULL,
                    timestamp_desc TEXT NOT NULL,
                    event_summary TEXT NOT NULL,
                    location TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS characters (
                    name TEXT PRIMARY KEY,
                    archetype TEXT NOT NULL,
                    status TEXT NOT NULL,
                    location TEXT NOT NULL,
                    physical_condition TEXT NOT NULL,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );

                CREATE TABLE IF NOT EXISTS knowledge_asymmetry (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    character_name TEXT NOT NULL,
                    fact TEXT NOT NULL,
                    chapter_learned INTEGER NOT NULL,
                    is_secret BOOLEAN DEFAULT 0,
                    FOREIGN KEY (character_name) REFERENCES characters(name)
                );

                CREATE TABLE IF NOT EXISTS artifacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    holder TEXT NOT NULL,
                    description TEXT NOT NULL,
                    state TEXT NOT NULL
                );
            """)

    def record_event(self, chapter: int, timestamp_desc: str, event_summary: str, location: str):
        with self._get_connection() as conn:
            conn.execute(
                "INSERT INTO timeline (chapter, timestamp_desc, event_summary, location) VALUES (?, ?, ?, ?)",
                (chapter, timestamp_desc, event_summary, location),
            )

    def update_character(self, name: str, archetype: str, status: str, location: str, physical_condition: str):
        with self._get_connection() as conn:
            conn.execute(
                """
                INSERT INTO characters (name, archetype, status, location, physical_condition)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    status=excluded.status,
                    location=excluded.location,
                    physical_condition=excluded.physical_condition,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (name, archetype, status, location, physical_condition),
            )

    def record_knowledge(self, character_name: str, fact: str, chapter_learned: int, is_secret: bool = False):
        with self._get_connection() as conn:
            conn.execute(
                "INSERT INTO knowledge_asymmetry (character_name, fact, chapter_learned, is_secret) VALUES (?, ?, ?, ?)",
                (character_name, fact, chapter_learned, 1 if is_secret else 0),
            )

    def get_character_knowledge(self, character_name: str) -> List[Dict[str, Any]]:
        with self._get_connection() as conn:
            cur = conn.execute(
                "SELECT fact, chapter_learned, is_secret FROM knowledge_asymmetry WHERE character_name = ?",
                (character_name,),
            )
            return [dict(row) for row in cur.fetchall()]

    def get_world_summary(self) -> Dict[str, Any]:
        with self._get_connection() as conn:
            chars = conn.execute("SELECT * FROM characters").fetchall()
            events = conn.execute("SELECT * FROM timeline ORDER BY chapter DESC LIMIT 10").fetchall()
            return {
                "characters": [dict(c) for c in chars],
                "recent_timeline": [dict(e) for e in events],
            }
