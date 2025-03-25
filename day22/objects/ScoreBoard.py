from turtle import Turtle

FONT = ("Sans", 32, "normal")

class ScoreBoard(Turtle):
	score_p0:int = 0
	score_p1:int = 0
	def __init__(self):
		super().__init__()
		self.screen.tracer(0)
		self.hideturtle()
		self.penup()
		self.color("white")
		self.score = 0
		self.goto(0,240)

	def display(self):
		self.clear()
		self.write(f"{self.score_p0} - {self.score_p1}",align="center", font=FONT)

	def point(self, player):
		match (player):
			case 0:
				self.score_p0 += 1
			case 1:
				self.score_p1 += 1