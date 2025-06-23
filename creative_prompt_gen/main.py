"""
This module is part of the Creative Prompt Generator.
Refer to `spec.md`, `high-level-design.md`, and `low-level-design.md` in the docs folder 
under project root for full requirements and design details.

Entrypoint script for launching the creative prompt generator CLI.
"""

from .cli import main_menu

def main():
    """Run the CLI application."""
    main_menu()

if __name__ == "__main__":
    main()
