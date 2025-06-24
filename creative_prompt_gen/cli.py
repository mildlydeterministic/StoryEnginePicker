"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Handles the command-line interface input loop and menu navigation for the creative prompt generator.
"""

from typing import List
from . import generator, display, config
from .cards.static import StaticCardSource
from .cards.base import normalize_deck_name
import sys

def parse_theme_selection(user_input: str) -> List[str]:
    """
    Convert a comma-separated numeral input into a list of valid themes.
    """
    if not user_input.strip():
        return config.THEMES[:]
    indices = [i.strip() for i in user_input.split(",") if i.strip().isdigit()]
    return [config.THEMES[int(i)-1] for i in indices if 0 < int(i) <= len(config.THEMES)]

def prompt_type_selection() -> str:
    print("Choose a prompt type:")
    for i, t in enumerate(["Character", "World"], 1):
        print(f"{i}. {t}")
    while True:
        choice = input("> ").strip()
        if choice == "1":
            return "character"
        elif choice == "2":
            return "world"
        print("Invalid selection. Please enter 1 or 2.")

def theme_selection() -> List[str]:
    print("Select theme(s) to draw from:")
    for i, t in enumerate(config.THEMES, 1):
        print(f"{i}. {t}")
    user_input = input('Enter comma-separated numbers (e.g., "1,2") or press Enter for default only:\n> ')
    return parse_theme_selection(user_input)

def deck_selection(prompt_type: str) -> str:
    decks = config.CHARACTER_DECKS if prompt_type == "character" else config.WORLD_DECKS
    print(f"Available decks for '{prompt_type.capitalize()}':")
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")
    while True:
        user_input = input("Enter deck number:\n> ").strip()
        if user_input.isdigit():
            idx = int(user_input)
            if 1 <= idx <= len(decks):
                return decks[idx-1]
        print(f"Invalid selection. Please enter a number between 1 and {len(decks)}.")

def redraw_selection(available_decks: list[str]) -> list[str]:
    print("Enter comma-separated card positions to redraw (e.g., '1,3') or press Enter to cancel:")
    print("Card positions:")
    for i, deck in enumerate(available_decks, 1):
        print(f"  {i}. {deck}")
    user_input = input("> ").strip()
    if not user_input:
        return []
    indices = [i.strip() for i in user_input.split(",") if i.strip().isdigit()]
    selected = []
    for idx in indices:
        pos = int(idx)
        if 1 <= pos <= len(available_decks):
            selected.append(available_decks[pos-1])
    return selected

def main_menu():
    source = StaticCardSource()
    last_prompt = None
    last_prompt_type = None
    last_themes = None
    def full_prompt_flow():
        nonlocal last_prompt, last_prompt_type, last_themes
        prompt_type = prompt_type_selection()
        themes = theme_selection()
        cards = generator.generate_full_prompt(source, prompt_type, themes)
        display.render_prompt(prompt_type, cards)
        last_prompt = cards
        last_prompt_type = prompt_type
        last_themes = themes
        # Redraw menu
        while True:
            print("\nWhat would you like to do next?")
            print("1. Redraw one or more cards")
            print("2. Generate a new full prompt")
            print("3. Draw a single card from a specific deck")
            print("4. Exit")
            sub_choice = input("> ").strip()
            if sub_choice == "1":
                decks = [c.deck for c in cards]
                to_redraw = redraw_selection(decks)
                if to_redraw:
                    cards = generator.redraw_cards(source, prompt_type, themes, cards, to_redraw)
                    display.render_prompt(prompt_type, cards)
                    last_prompt = cards
                else:
                    print("No decks selected for redraw.")
            elif sub_choice == "2":
                # Immediately start a new full prompt
                return full_prompt_flow()
            elif sub_choice == "3":
                single_card_flow(source)
            elif sub_choice == "4":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid selection.")
    while True:
        print("\nWelcome to the Creative Prompt Generator!\n")
        print("What would you like to do?")
        print("1. Generate a new full prompt")
        print("2. Draw a single card from a specific deck")
        print("3. Exit")
        choice = input("> ").strip()
        if choice == "1":
            full_prompt_flow()
        elif choice == "2":
            single_card_flow(source)
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid selection.")

def single_card_flow(source):
    prompt_type = prompt_type_selection()
    deck = deck_selection(prompt_type)
    themes = theme_selection()
    card = generator.generate_single_card(source, prompt_type, deck, themes)
    display.render_prompt(prompt_type, [card])
