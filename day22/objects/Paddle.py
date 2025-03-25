from turtle import Turtle

MAX_Y = 230
MAX_X = 350

class Paddle(Turtle):
	def __init__(self, position):
		super().__init__("square")
		self.screen.tracer(0)
		self.turtlesize(5,1)
		self.penup()
		self.color("white") 
		self.goto((position))

	def up(self):
		if self.ycor() < MAX_Y - 20:
			self.goto(self.xcor(), self.ycor() + 20)
	
	def down(self):
		if self.ycor() > -MAX_Y + 20:
			self.goto(self.xcor(), self.ycor() - 20)