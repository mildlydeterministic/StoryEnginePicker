"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Implements a static card source and defines CARD_COUNTS for use in prompt generation.
"""

import random
from .. import config
from .base import CardSource, normalize_deck_name
from ..models import CardData
from typing import List

# Card counts per deck per theme
CARD_COUNTS = {
    "world": {
        "region": { "default": 32, "fantasy": 8, "horror": 8, "sci-fi": 0, },
        "landmark": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "namesake": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "origin": { "default": 32, "fantasy": 8, "horror": 8, "sci-fi": 0, },
        "attribute": { "default": 48, "fantasy": 12, "horror": 12, "sci-fi": 0, },
        "advent": { "default": 32, "fantasy": 8, "horror": 8, "sci-fi": 0, },
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
        """
        Return the number of cards for a given deck and theme from CARD_COUNTS.
        """
        try:
            return CARD_COUNTS[prompt_type][normalize_deck_name(deck, prompt_type)][theme.lower()]
        except KeyError:
            return 0

    def draw_card(self, prompt_type: str, deck: str, themes: List[str]) -> CardData:
        """
        Randomly select a theme (weighted by card count) and draw a card number within that theme's range.
        Returns a CardData object. If no cards are available, returns CardData with missing=True.
        """
        deck = normalize_deck_name(deck, prompt_type)
        #update themes to lowercase for consistency
        themes = [theme.lower() for theme in themes if theme.lower() in CARD_COUNTS[prompt_type][deck]]
        pool = []
        for theme in config.THEMES:
            if theme in themes:
                count = CARD_COUNTS[prompt_type][deck][theme]
                if count > 0:
                    pool.append((theme, count))

        if not pool:
            return CardData(deck=deck, theme="", card_text=None, missing=True)

        total = sum(count for _, count in pool)
        choice_point = random.randint(1, total)

        for theme, count in pool:
            if choice_point <= count:
                return CardData(deck=deck, theme=theme, card_text=str(choice_point))
            choice_point -= count

        raise RuntimeError("Unreachable state in draw_card — theme selection failed.")
