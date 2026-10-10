"""Snake model and movement controls."""

from turtle import Turtle

moveDistance = 20
upDirection = 90
downDirection = 270
leftDirection = 180
rightDirection = 0

class snakeModel:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for segmentIndex in range(3):
            self.addSegment(segmentIndex)

    def addSegment(self, segmentIndex):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(-moveDistance * segmentIndex, 0)
        self.segments.append(newSegment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]

    def extend(self):
        self.addSegment(3)
        self.segments[-1].color("black")

    def move(self):
        self.segments[-1].color("white")
        for segmentIndex in range(len(self.segments) - 1, 0, -1):
            newX = self.segments[segmentIndex - 1].xcor()
            newY = self.segments[segmentIndex - 1].ycor()
            self.segments[segmentIndex].goto(newX, newY)
        self.head.forward(moveDistance)

    def right(self):
        if self.head.heading() != leftDirection:
            self.head.setheading(rightDirection)

    def up(self):
        if self.head.heading() != downDirection:
            self.head.setheading(upDirection)

    def left(self):
        if self.head.heading() != rightDirection:
            self.head.setheading(leftDirection)

    def down(self):
        if self.head.heading() != upDirection:
            self.head.setheading(downDirection)
