"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Defines the CardSource interface for card data providers and shared card logic.
"""

from abc import ABC, abstractmethod
from typing import List
from ..models import CardData

class CardSource(ABC):
    """
    Abstract base class for card data sources.
    """
    @abstractmethod
    def draw_card(self, prompt_type: str, deck: str, themes: List[str]) -> CardData:
        """
        Draws a single card from the given deck using available themes.
        """
        pass

    @abstractmethod
    def get_card_count(self, prompt_type: str, deck: str, theme: str) -> int:
        """
        Returns the number of cards available for a given deck and theme.
        """
        pass

def normalize_deck_name(deck_input: str, prompt_type: str) -> str:
    """
    Normalize and validate a user-supplied deck name (case/plural-insensitive).
    Returns the canonical deck name if valid, else raises ValueError.
    """
    from ..config import CHARACTER_DECKS, WORLD_DECKS
    
    # Select deck list based on prompt type
    if prompt_type == "character":
        valid_decks = CHARACTER_DECKS
    elif prompt_type == "world":
        valid_decks = WORLD_DECKS
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
    
    normalized = deck_input.strip().lower()
    # Try to match ignoring case and plural 's'
    for deck in valid_decks:
        lower = deck.lower()
        if normalized == lower or normalized == lower + 's' or normalized.rstrip('s') == lower:
            return lower
    raise ValueError(f"Invalid deck name '{deck_input}' for prompt type '{prompt_type}'")


def get_card_count(prompt_type: str, deck: str, theme: str) -> int:
    """
    Wrapper to retrieve validated card counts from StaticCardSource.
    Returns 0 if not found.
    """
    from .static import StaticCardSource
    try:
        source = StaticCardSource()
        return source.get_card_count(prompt_type, deck, theme)
    except Exception:
        return 0
