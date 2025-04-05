from turtle import Turtle
from time import sleep

FONT = ("Arial", 14, "bold")
ALIGNMENT = "center"

class ScoreBoard(Turtle):
    """Class to manage the score board of the game"""
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.goto(0, 270)
        
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
        self.screen.update()
        sleep(1)