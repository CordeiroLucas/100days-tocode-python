from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write("Score: ", align="center", font=("Arial", 14, "bold"))
        self.color("white")
    
    def update(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=("Arial", 14, "bold"))