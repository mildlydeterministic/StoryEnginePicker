"""
Entrypoint script for launching the creative prompt generator CLI.
"""

from .cli import main_menu

def main():
    """Run the CLI application."""
    main_menu()

if __name__ == "__main__":
    main()
