"""
Implements a static card source using CARD_COUNTS from config.
"""

from .. import config
from .base import CardSource

class StaticCardSource(CardSource):
    """
    Card source that uses static CARD_COUNTS from config.
    """
    def get_card_count(self, prompt_type: str, deck: str, theme: str) -> int:
        # TODO: Return card count from config.CARD_COUNTS
        pass

    def draw_card(self, prompt_type: str, deck: str, theme: str) -> int:
        # TODO: Randomly select a card number within the available range
        pass
