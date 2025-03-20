from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, isPlayer = False):
        super().__init__("square")
        self.penup()
        self.color("white") 
        self.isPlayer = isPlayer