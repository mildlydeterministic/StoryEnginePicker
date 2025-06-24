"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high_level_design.md`, and `low_level_design.md` in the docs folder 
under project root for full requirements and design details.

Implements prompt generation logic, including full prompt, single card draw, and redraws.
"""

from .cards.base import CardSource
from .models import CardData
from typing import List
from . import config

def generate_full_prompt(source: CardSource, prompt_type: str, themes: List[str]) -> List[CardData]:
    """
    Draws a complete set of cards, one from each deck for the given prompt type.
    """
    if prompt_type == "character":
        deck_list = config.CHARACTER_DECKS
    elif prompt_type == "world":
        deck_list = config.WORLD_DECKS
    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
    return [generate_single_card(source, prompt_type, deck, themes) for deck in deck_list]

def generate_single_card(source: CardSource, prompt_type: str, deck: str, themes: List[str]) -> CardData:
    """
    Draws a single card from a specific deck using selected themes.
    """
    return source.draw_card(prompt_type, deck, themes)

def redraw_cards(source: CardSource, prompt_type: str, themes: List[str], existing_cards: List[CardData], redraw_decks: List[str]) -> List[CardData]:
    """
    Redraws only the cards in the decks listed while preserving the others.
    """
    result = []

    for card in existing_cards:
        if card.deck in redraw_decks:
            result.append(generate_single_card(source, prompt_type, card.deck, themes))
        else:
            result.append(card)
    return result
