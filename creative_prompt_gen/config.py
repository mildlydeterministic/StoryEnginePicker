"""
Defines constants for deck structure, themes, and card counts.
"""

# Decks for each prompt type
CHARACTER_DECKS = ["Agent", "Engine", "Anchor", "Conflict", "Aspect"]
WORLD_DECKS = ["Region", "Landmark", "Namesake", "Origin", "Attribute", "Advent"]

# Available themes
THEMES = ["default", "fantasy", "horror", "sci-fi"]

# Card counts per deck per theme (placeholder values)
CARD_COUNTS = {
    "character": {deck: {theme: 0 for theme in THEMES} for deck in CHARACTER_DECKS},
    "world": {deck: {theme: 0 for theme in THEMES} for deck in WORLD_DECKS},
}
