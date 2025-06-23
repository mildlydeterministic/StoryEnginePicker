# Creative Prompt Generator — Requirements Specification

## 1. **Project Overview**

This is a **Python-based creative writing prompt generator** that builds prompts from custom card decks grouped by prompt type and theme. It will initially operate through a **basic command-line interface** using `input()` and ASCII-style output. Later enhancements may include UI elements and structured card data pulled from files or external storage.

---

## 2. **Core Concepts**

### 2.1 Prompt Types

There are two types of prompts:

- `character`
- `world`

### 2.2 Decks

Each prompt type has its own fixed set of decks:

- **Character decks** (drawn in this order):\
  `Agent`, `Engine`, `Anchor`, `Conflict`, `Aspect`

- **World decks** (drawn in this order):\
  `Region`, `Landmark`, `Namesake`, `Origin`, `Attribute`, `Advent`

### 2.3 Themes

Cards are categorized by theme. The valid themes are:

- `default`
- `fantasy`
- `horror`
- `sci-fi`

Each card:

- Belongs to **exactly one** theme
- Is represented by an integer for now (e.g., `1` to `N`)
- Is stored as a count (per deck, per theme) in `CARD_COUNTS`

---

## 3. **Functional Requirements**

### 3.1 Full Prompt Generation

- The user selects:
  - A prompt type (`character` or `world`)
  - One or more themes (e.g., `fantasy`, `sci-fi`)
- For each deck in the selected prompt type (in order):
  - Combine all available cards from the selected themes
  - Select a **theme** weighted by its card count
  - Randomly draw a card **within that theme's range**
  - Track the **theme that the selected card came from**
  - If the deck has no available cards across selected themes, mark it as `[Missing]`

### 3.2 Single Card Draw

- The user explicitly provides:
  - Prompt type
  - Deck name (must belong to the selected prompt type)
  - One or more themes
- A single card is drawn from the selected deck using theme-weighted random selection
- The output shows:
  - Deck name
  - Theme the selected card came from
  - Card number (within that theme)
- If no cards are available, output `[Missing]`

### 3.3 Redraw Cards

- After a full prompt has been generated:
  - The user may choose to redraw one or more cards from the same prompt
  - Only the selected decks are re-rolled
  - The updated prompt is re-rendered

---

## 4. **Interface Requirements**

### 4.1 Main CLI Flow

At startup, the program displays:

```
Welcome to the Creative Prompt Generator!

What would you like to do?
1. Generate a new full prompt
2. Draw a single card from a specific deck
3. Exit
>
```

If the user selects **1. Generate a full prompt**:

#### Step 1: Prompt Type Selection

```
Choose a prompt type:
1. Character
2. World
>
```

#### Step 2: Theme Selection

```
Select theme(s) to draw from:
1. default
2. fantasy
3. horror
4. sci-fi

Enter comma-separated numbers (e.g., "1,2") or press Enter for default only:
>
```

#### Step 3: Generate and Display Prompt

- The full prompt is printed as a **horizontal row** of ASCII card boxes
- Each box shows:
  - Deck name
  - Theme of selected card
  - Card number or `[Missing]` if unavailable

If the user selects **2. Draw a single card**:

#### Step 1: Prompt Type Selection

(Same as above)

#### Step 2: Deck Selection

```
Available decks for 'Character':
- Agent
- Engine
- Anchor
- Conflict
- Aspect

Enter deck name:
>
```

#### Step 3: Theme Selection

(Same as full prompt)

#### Step 4: Draw and Display Card

- Show deck name, theme, and card number
- Or `[Missing]` if no cards are available

---

### 4.2 After Full Prompt Output

```
What would you like to do next?
1. Redraw one or more cards
2. Generate a new full prompt
3. Draw a single card from a specific deck
4. Exit
>
```

If the user chooses **1. Redraw**:

```
Enter comma-separated deck names to redraw (e.g., "Agent,Conflict") or press Enter to cancel:
>
```

Redraw those decks using the same themes as before and re-render the full prompt.

---

## 5. **Non-Functional Requirements**

- Python 3.10+
- Uses only the standard library
- `CARD_COUNTS` is defined in `config.py` with 0s as placeholders
- Code is modular and extensible
- All input is via `input()`, all output is text-based

---

## 6. **Extensibility Goals**

Planned future enhancements:

- Load card content (text, images) from file
- Replace numbers with meaningful card data
- Add web or rich terminal UI (e.g., `prompt_toolkit`, `textual`)
- Support saving generated prompts
- Introduce user-defined decks/themes via config files

---

## 7. **Example Output (Full Prompt)**

```
Prompt Type: Character
Themes: fantasy, horror

+------------------+  +------------------+  +------------------+
| Deck: Agent      |  | Deck: Engine     |  | Deck: Conflict   |
| Theme: horror    |  | Theme: fantasy   |  | Theme: fantasy   |
| Card: #3         |  | Card: #1         |  | Card: #7         |
+------------------+  +------------------+  +------------------+
```

