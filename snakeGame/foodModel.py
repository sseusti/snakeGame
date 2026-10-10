from turtle import Turtle
import random

class foodModel(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-13, 13)
        randomY = random.randint(-13, 13)
        self.goto(randomX * 20, randomY * 20)
