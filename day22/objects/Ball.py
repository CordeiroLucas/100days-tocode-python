from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.screen.tracer(0)
        self.penup()
        self.color("white")
        self.right(-45)
    
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)