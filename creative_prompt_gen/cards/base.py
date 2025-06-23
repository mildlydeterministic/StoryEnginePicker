"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Defines the CardSource interface for card data providers.
""" 

from abc import ABC, abstractmethod

class CardSource(ABC):
    """
    Abstract base class for card data sources.
    """
    @abstractmethod
    def get_card_count(self, prompt_type: str, deck: str, theme: str) -> int:
        """Return the number of cards for a given deck and theme."""
        pass

    @abstractmethod
    def draw_card(self, prompt_type: str, deck: str, theme: str) -> int:
        """Draw a card number from the specified deck and theme."""
        pass
