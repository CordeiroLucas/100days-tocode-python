from turtle import Turtle

MAX_Y = 230
MAX_X = 350

class Paddle(Turtle):
	def __init__(self, isPlayer = False):
		super().__init__("square")
		self.turtlesize(4,0.75)
		self.penup()
		self.color("white") 
		self.isPlayer = isPlayer
		
		if self.isPlayer:
			self.goto(-MAX_X, 0)
		else: self.goto(MAX_X,0)

	def up(self):
		if self.ycor() < MAX_Y:
			self.goto(self.xcor(), self.ycor() + 20)
	
	def down(self):
		if self.ycor() > -MAX_Y:
			self.goto(self.xcor(), self.ycor() - 20)
	
