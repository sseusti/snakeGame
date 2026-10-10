"""Application entry point for the Snake game."""

from snakeGame.game import game


def main() -> None:
    """Create the game and start its event loop."""
    game().run()


if __name__ == "__main__":
    main()
