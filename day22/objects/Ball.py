from turtle import Turtle

MAX_Y = 280

class Ball(Turtle):
	speed = 10
	def __init__(self, shape = "circle"):
		super().__init__(shape)
		self.screen.tracer(0)
		self.penup()
		self.color("white")
		self.seth(45)
		print(self.heading())
	
	def move(self):
		self.__wall_bounce()
		self.forward(self.speed)

	def __wall_bounce(self):
		if (self.ycor() >= MAX_Y or self.ycor() <= -MAX_Y):
			match (self.heading()):
				case 315:
					self.seth(45)
				case 45:
					self.seth(315)
				case 135:
					self.seth(225)
				case 225:
					self.seth(135)