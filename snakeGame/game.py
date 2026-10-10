"""Coordinate the screen, game objects, input, and game loop."""

import time
from turtle import Screen

from .foodModel import foodModel
from .scoreBoard import scoreBoard
from .snakeModel import snakeModel


screenSize = 600
screenBackground = "black"
screenTitle = "My Snake Game"
frameDelay = 0.1
foodCollisionDistance = 10
wallXLimit = 280
wallYTop = 270
wallYBottom = -280
wallXLeft = -280


class game:
    """Own the lifecycle and orchestration of one game session."""

    def __init__(self) -> None:
        self.screen = self.createScreen()
        self.snake = snakeModel()
        self.food = foodModel()
        self.scoreBoard = scoreBoard()
        self.configureControls()

    @staticmethod
    def createScreen() -> Screen:
        screen = Screen()
        screen.setup(screenSize, screenSize)
        screen.bgcolor(screenBackground)
        screen.title(screenTitle)
        screen.tracer(0)
        return screen

    def configureControls(self) -> None:
        self.screen.listen()
        self.screen.onkey(self.snake.up, "w")
        self.screen.onkey(self.snake.down, "s")
        self.screen.onkey(self.snake.left, "a")
        self.screen.onkey(self.snake.right, "d")

    def run(self) -> None:
        """Run frames until the user closes the screen."""
        while True:
            self.runFrame()
        # Kept for compatibility with the original turtle window lifecycle.
        self.screen.exitonclick()

    def runFrame(self) -> None:
        self.screen.update()
        time.sleep(frameDelay)
        self.snake.move()

        if self.snake.head.distance(self.food) < foodCollisionDistance:
            self.food.refresh()
            self.scoreBoard.update()
            self.snake.extend()

        if self.hitWall() or self.hitSelf():
            self.scoreBoard.reset()
            self.snake.reset()

    def hitWall(self) -> bool:
        head = self.snake.head
        return (
            head.xcor() > wallXLimit
            or head.xcor() < wallXLeft
            or head.ycor() > wallYTop
            or head.ycor() < wallYBottom
        )

    def hitSelf(self) -> bool:
        return any(
            self.snake.head.distance(segment) < foodCollisionDistance
            for segment in self.snake.segments[1:]
        )
