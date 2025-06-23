"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Implements a static card source and defines CARD_COUNTS for use in prompt generation.
"""

from .. import config
from .base import CardSource

# Card counts per deck per theme
CARD_COUNTS = {
    "world": {
        "region": { "default": 32, "fantasy": 8, "horror": 8, "sci-fi": 0, },
        "landmark": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "namesake": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "origin": { "default": 32, "fantasy": 8, "horror": 8, "sci-fi": 0, },
        "attribute": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "advent": { "default": 30, "fantasy": 8, "horror": 8, "sci-fi": 0, },
    },
    "character": {
        "agent": { "default": 36, "fantasy": 12, "horror": 12, "sci-fi": 12, },
        "engine": { "default": 36, "fantasy": 12, "horror": 12, "sci-fi": 12, },
        "anchor": { "default": 36, "fantasy": 12, "horror": 12, "sci-fi": 12, },
        "conflict": { "default": 36, "fantasy": 12, "horror": 12, "sci-fi": 12, },
        "aspect": { "default": 36, "fantasy": 12, "horror": 12, "sci-fi": 12, },
    },
}

class StaticCardSource(CardSource):
    """
    Card source that uses static CARD_COUNTS.
    """
    def get_card_count(self, prompt_type: str, deck: str, theme: str) -> int:
        # TODO: Return card count from CARD_COUNTS
        pass

    def draw_card(self, prompt_type: str, deck: str, theme: str) -> int:
        # TODO: Randomly select a card number within the available range
        pass
