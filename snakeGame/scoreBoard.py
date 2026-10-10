"""Score display and high-score persistence."""

from pathlib import Path
from turtle import Turtle

highScoreFile = Path(__file__).resolve().parent.parent / "highScore.txt"

class scoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with highScoreFile.open() as data:
            self.highScore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}  High score: {self.highScore}", False, "center", ("Courier", 22, "normal"))
        self.score += 1

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with highScoreFile.open("w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.update()

