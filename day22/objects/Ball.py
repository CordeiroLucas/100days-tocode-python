from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.shapesize(0.7, 0.7)
        self.penup()
        self.color("white")