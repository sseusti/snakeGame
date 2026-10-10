# Snake the Game

A small Snake game built with Python's standard-library `turtle` module. The project is also a hands-on example of object-oriented programming: the game, snake, food, and scoreboard each have a separate class and responsibility.

## Requirements

- Python 3
- A graphical desktop environment supported by `turtle` (Tkinter)

The game uses only Python's standard library, so no third-party packages need to be installed. The included `requirements.txt` documents this; it intentionally contains no package entries.

## Run

From the project directory, run:

```bash
python main.py
```

If you use a virtual environment, you can install the declared dependencies with `pip install -r requirements.txt`. This is currently a no-op because there are no external dependencies.

Use **W**, **A**, **S**, and **D** to move the snake. Close the game window to exit.

## Project structure

```text
.
├── main.py                 # Application entry point
├── highScore.txt           # Persisted high score
└── snakeGame/
    ├── __init__.py
    ├── game.py              # Screen setup, input, and game loop
    ├── snakeModel.py        # Snake segments, movement, and direction
    ├── foodModel.py         # Food turtle and random placement
    └── scoreBoard.py        # Score display and high-score persistence
```

## How it works

The project uses `turtle.Screen` as the game window and `turtle.Turtle` objects as its visual elements. The screen's automatic drawing is paused with `tracer(0)`; each game frame updates the screen explicitly, which keeps the animation synchronized with the game loop.

The classes build on `Turtle` where an object is itself drawn on the screen:

- `foodModel` inherits from `Turtle` and configures its shape, color, size, and position. Its `refresh()` method chooses a new grid position.
- `scoreBoard` inherits from `Turtle` and uses turtle drawing methods to display the score. It reads and writes the high score in `highScore.txt`.
- `snakeModel` manages a collection of `Turtle` segments. It creates, moves, extends, and resets the snake, and changes the head's direction in response to key presses.
- `game` composes these objects with a `Screen`. It configures the window and controls, advances frames, and checks collisions.

This separation keeps screen and game coordination in `game`, while each game object owns its own state and turtle-specific behavior. `main.py` is a small entry point that creates the game and starts it.
