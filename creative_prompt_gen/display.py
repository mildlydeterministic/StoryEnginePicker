"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Handles ASCII rendering of card and prompt output for the CLI.
"""

from .models import Prompt

def render_prompt(prompt: Prompt):
    """Render a full prompt as ASCII card boxes."""
    # TODO: Implement ASCII rendering of prompt
    pass

def render_card(deck_name, theme, card_number):
    """Render a single card as an ASCII box."""
    # TODO: Implement ASCII rendering of a single card
    pass
