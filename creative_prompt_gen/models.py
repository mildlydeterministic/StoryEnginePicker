"""
Defines the Prompt object and related enums or data structures.
"""

from enum import Enum
from typing import List, Optional

class PromptType(Enum):
    CHARACTER = "character"
    WORLD = "world"

class Prompt:
    """
    Represents a generated creative prompt.
    """
    def __init__(self, prompt_type: PromptType, cards: list):
        self.prompt_type = prompt_type
        self.cards = cards  # List of dicts: {deck, theme, card_number}

class CardDraw:
    """
    Represents a single card draw result.
    """
    def __init__(self, deck: str, theme: str, card_number: Optional[int]):
        self.deck = deck
        self.theme = theme
        self.card_number = card_number
