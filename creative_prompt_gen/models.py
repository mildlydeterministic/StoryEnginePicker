"""
Defines the Prompt object, CardData, and related enums or data structures.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class CardData:
    """
    Unified format for card data throughout the app.
    """
    deck: str
    theme: str
    card_text: Optional[str] = None
    card_location: Optional[str] = None
    missing: bool = False

# ...existing or future model code (Prompt, enums, etc.)...
