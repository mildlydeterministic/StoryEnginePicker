"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high_level_design.md`, and `low_level_design.md` in the docs folder 
under project root for full requirements and design details.

Responsible for rendering prompts and cards as ASCII art for the CLI.
"""

from .models import CardData
from typing import List

BOX_WIDTH = 20

def render_prompt(prompt_type: str, cards: List[CardData]) -> None:
    """
    Displays an entire prompt in ASCII format, deck-by-deck, using card data.
    Each card is rendered as a box, and all boxes are combined into a single row for display.
    Handles missing cards by rendering a placeholder box.
    """
    boxes = []
    for card in cards:
        if getattr(card, "missing", False):
            boxes.append(format_missing_box(card.deck))
        else:
            boxes.append(format_card_box(card))
    print(combine_horizontal(boxes))

def format_card_box(card: CardData) -> List[str]:
    """
    Formats a single card into a boxed ASCII representation.
    Returns a list of strings, each representing a row of the card's ASCII art box.
    """
    top = "+" + "-" * (BOX_WIDTH - 2) + "+"
    deck_line = f"| Deck: {card.deck:<12}"[:BOX_WIDTH-1] + "|"
    theme_line = f"| Theme: {card.theme:<11}"[:BOX_WIDTH-1] + "|"
    card_line = f"| Card: {card.card_text or '[Missing]':<11}"[:BOX_WIDTH-1] + "|"
    bottom = top
    # Pad with spaces if needed
    box = [top, deck_line, theme_line, card_line, bottom]
    return box

def format_missing_box(deck: str) -> List[str]:
    """
    Generates a placeholder box for a missing card.
    Returns a list of strings, each representing a row of the missing card's ASCII art box.
    """
    top = "+" + "-" * (BOX_WIDTH - 2) + "+"
    deck_line = f"| Deck: {deck:<12}"[:BOX_WIDTH-1] + "|"
    theme_line = f"| Theme: {'':<11}"[:BOX_WIDTH-1] + "|"
    card_line = f"| Card: [Missing] "[:BOX_WIDTH-1] + "|"
    bottom = top
    box = [top, deck_line, theme_line, card_line, bottom]
    return box

def combine_horizontal(boxes: List[List[str]]) -> str:
    """
    Combines multiple ASCII card boxes (each as a list of strings) into a single printable row.
    Returns a single string suitable for printing, with boxes side by side.
    """
    if not boxes:
        return ""
    # Each box is a list of strings (rows). Zip to combine rows horizontally.
    combined_rows = ["  ".join(parts) for parts in zip(*boxes)]
    return "\n".join(combined_rows)

