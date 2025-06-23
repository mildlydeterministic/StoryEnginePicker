# 📐 Low-Level Design — Creative Prompt Generator

## ✳️ Core Data Model

### `CardData`

```python
from dataclasses import dataclass

@dataclass
class CardData:
    deck: str
    theme: str
    card_text: str | None = None
    card_location: str | None = None
    missing: bool = False
```

- Unified format for card data throughout the app.
- `card_text` used for display (e.g., ASCII).
- `card_location` reserved for graphical or file-based cards.
- `missing=True` indicates no card was available for the deck.

---

## 🔌 `cards/base.py` — Shared Logic and CardSource Interface

### Responsibilities

- Defines the abstract `CardSource` interface.
- Provides helper functions for deck name normalization and theme selection parsing.
- Offers a single point of truth for validating input against supported prompt types, decks, and themes.

### Public API

```python
class CardSource(ABC):
    @abstractmethod
    def draw_card(prompt_type: str, deck: str, themes: list[str]) -> CardData:
        '''Draws a single card from the given deck using available themes.'''

    @abstractmethod
    def get_card_count(prompt_type: str, deck: str, theme: str) -> int:
        '''Returns the number of cards available for a given deck and theme.'''
```

```python
def normalize_deck_name(deck_input: str, prompt_type: str) -> str:
    '''Normalize and validate a user-supplied deck name (case/plural-insensitive).'''

def parse_theme_selection(user_input: str) -> list[str]:
    '''Convert a comma-separated numeral input into a list of valid themes.'''

def get_card_count(prompt_type: str, deck: str, theme: str) -> int:
    '''Wrapper to retrieve validated card counts from config.'''
```

---

## 📁 `cards/static.py` — StaticCardSource Implementation

### Responsibilities

- Implements `CardSource` using hardcoded values in `CARD_COUNTS`.
- Performs weighted random selection from valid themes.

### Public API

```python
class StaticCardSource(CardSource):
    def draw_card(...) -> CardData:
        '''Implements weighted random draw from in-memory theme counts.'''

    def get_card_count(...) -> int:
        '''Returns the static card count from CARD_COUNTS config.'''
```

---

## 🧠 `generator.py` — Prompt Logic

### Responsibilities

- Generates full prompts and individual card draws.
- Encapsulates logic for card selection, redraws, and deck ordering.

### Public API

```python
def generate_full_prompt(source: CardSource, prompt_type: str, themes: list[str]) -> list[CardData]:
    '''Draws a complete set of cards, one from each deck for the given prompt type.'''

def generate_single_card(source: CardSource, prompt_type: str, deck: str, themes: list[str]) -> CardData:
    '''Draws a single card from a specific deck using selected themes.'''

def redraw_cards(source: CardSource, prompt_type: str, themes: list[str], existing_cards: list[CardData], redraw_decks: list[str]) -> list[CardData]:
    '''Redraws only the cards in the decks listed while preserving the others.'''
```

---

## 🖼 `display_ascii.py` — Text Renderer

### Responsibilities

- Converts lists of `CardData` into human-readable ASCII prompt rows.
- Handles missing cards cleanly.

### Public API

```python
def render_prompt(prompt_type: str, cards: list[CardData]) -> None:
    '''Displays an entire prompt in ASCII format, deck-by-deck.'''
```

### Internal Helpers

```python
def format_card_box(card: CardData) -> list[str]:
    '''Formats a single card into a boxed ASCII representation.'''

def format_missing_box(deck: str) -> list[str]:
    '''Generates a placeholder box for a missing card.'''

def combine_horizontal(boxes: list[list[str]]) -> str:
    '''Combines multiple ASCII card boxes into a single printable row.'''
```

---

## 🧰 `cli.py` — CLI Interaction

### Responsibilities

- Presents menus and gathers user input via `input()`
- Validates input against config rules
- Dispatches control to the generator and display layers

### Public API

```python
def prompt_type_selection() -> str:
    '''Prompt the user to choose between Character and World prompt types.'''

def theme_selection() -> list[str]:
    '''Prompt the user to select one or more themes via numbered menu.'''

def deck_selection(prompt_type: str) -> str:
    '''Prompt the user to choose a valid deck based on prompt type.'''

def redraw_selection(available_decks: list[str]) -> list[str]:
    '''Prompt the user for which cards to redraw in a generated prompt.'''
```

---

## 🚀 `main.py` — Entry Point

### Responsibilities

- Manages the full application lifecycle
- Connects CLI inputs to card source and rendering

### Public API

```python
def main() -> None:
    '''Starts and maintains the main CLI loop for user interaction.'''
```

---

## 🔁 Extensibility Summary

| Component     | Replaceable | Notes |
|---------------|-------------|-------|
| Card Source   | ✅           | Add DB, API, or file-backed cards |
| Display       | ✅           | Swap CLI for rich UI or GUI |
| Generator     | 🔒 Stable    | Doesn’t change per UI or source |
| Input Handler | ✅           | CLI can be replaced with TUI or web |