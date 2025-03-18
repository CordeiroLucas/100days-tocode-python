from turtle import Turtle

class Food:
	def __init__(self):
		self.food = Turtle("circle")
		self.food.penup()
		self.food.shapesize(0.5, 0.5)
		self.food.color("blue")
		self.food.hideturtle()

	def spawn(self, pos):
		self.food.goto(pos)
		self.food.showturtle()

	def get_pos(self):
		return self.food.pos()