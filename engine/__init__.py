"""
AI Novel Engine Package
Author: Jaswanth1902
"""

from engine.core import NovelEngine
from engine.linter import NovelLinter
from engine.director import Director
from engine.actor import ActorEnvelopeManager
from engine.stylist import Stylist
from engine.gatekeeper import Gatekeeper
from engine.memory import StoryMemory

__version__ = "2.0.0"
__all__ = [
    "NovelEngine",
    "NovelLinter",
    "Director",
    "ActorEnvelopeManager",
    "Stylist",
    "Gatekeeper",
    "StoryMemory",
]
