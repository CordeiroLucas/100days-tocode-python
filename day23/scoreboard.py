from gameObject import GameObject

FONT = ("Courier", 24, "normal")


class Scoreboard(GameObject):
    level:int
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level {self.level}", font=FONT)
    
    def next_level(self):
        self.level += 1
    
    def display(self):
        self.clear()
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", font=FONT, align="center")
