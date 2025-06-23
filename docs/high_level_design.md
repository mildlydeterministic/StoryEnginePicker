# 🧰 Creative Prompt Generator — High-Level Design
This design provides high level guidance and detail for the requirements detailed in spec.md. Low level design for the modules and methods is present in low_level_design.md

## 📁 Project Structure

```
creative_prompt_gen/
├── cli.py                 # Input loop, menu flow
├── generator.py           # Core generation logic
├── config.py              # Deck and theme definitions
├── cards/
│   ├── __init__.py
│   ├── base.py            # CardSource interface
│   └── static.py          # StaticCardSource using CARD_COUNTS
├── display.py             # ASCII card renderer
├── models.py              # Prompt object and enums (if needed)
└── main.py                # Optional entrypoint for CLI
```

---

## 🔄 Prompt Generation

- Single function: `generate_prompt(prompt_type, themes, redraw_decks=None)`
- Returns a structured `prompt` object:

```python
{
  "type": "character",
  "themes": ["fantasy", "horror"],
  "cards": [
    {"deck": "Agent", "theme": "fantasy", "card": 2},
    {"deck": "Engine", "theme": "default", "card": 6},
    ...
  ]
}
```

- Card selection is:
  - Random
  - Weighted by number of cards per theme
  - Numbered relative to its own theme only

---

## 🔌 CardSource Abstraction

- `CardSource` interface defines:
  - `get_card_count(prompt_type, deck, theme)`
  - `draw_card(prompt_type, deck, themes) -> dict | None`
- `StaticCardSource` pulls from `CARD_COUNTS` and is hardcoded for now
- Future sources (YAML, JSON) can implement the same interface

---

## 🎨 Display

- ASCII-rendered card boxes per deck using `display.py`
- Horizontal row layout, one box per deck
- Each card includes:
  - Deck name
  - Theme drawn from
  - Card number or `[Missing]`
- Prompt type and selected themes are printed once above the row

---

## 🧑‍💻 CLI Flow

- Menu-based interaction using `input()`
- Theme selection via numbered menu (`THEMES = ["default", "fantasy", "horror", "sci-fi"]`)
- Prompt type and decks validated case-insensitively, with support for plural forms
- Redraw logic handled via `generate_prompt()` with `redraw_decks`

---

## ❌ Excluded for Now

- Seeded randomness
- File-based card definitions
- UI beyond CLI
- Prompt saving/loading
- Card text/image metadata

---

## ✅ Design Goals Achieved

| Goal                          | Met? |
|-------------------------------|------|
| Encapsulation for easy growth | ✅   |
| CLI usability and clarity     | ✅   |
| Clean, testable logic         | ✅   |
| Robust error handling         | ✅   |
| Prompt structure extensibility| ✅   |

