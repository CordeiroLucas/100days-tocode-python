from turtle import Turtle

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(0.5, 0.5)
		self.color("blue")
		self.hideturtle()
		self.speed("fastest")

	def spawn(self, pos):
		self.goto(pos)
		self.showturtle()

	def get_pos(self):
		return self.pos()