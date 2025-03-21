from turtle import Turtle



class Paddle(Turtle):
	def __init__(self, isPlayer = False):
		super().__init__("square")
		self.turtlesize(4,0.75)
		self.penup()
		self.color("white") 
		self.isPlayer = isPlayer
		if self.isPlayer:
			self.goto(-350, 0)
		else: self.goto(350,0)

	def up(self):
		if self.ycor() < 230:
			self.goto(self.xcor(), self.ycor() + 20)
	
	def down(self):
		if self.ycor() > -230:
			self.goto(self.xcor(), self.ycor() - 20)
		