from turtle import Turtle

MAX_Y = 280

class Ball(Turtle):
	speed = 10
	def __init__(self, shape = "circle"):
		super().__init__(shape)
		self.screen.tracer(0)
		self.penup()
		self.color("white")
		self.seth(135)
		print(self.heading())
	
	def run(self):
		self.__wall_bounce()
		self.__move()

	def __move(self):
		self.forward(self.speed)

	def __wall_bounce(self):
		if (self.ycor() >= MAX_Y or self.ycor() <= -MAX_Y):
			heading = self.heading()
			match (heading):
				case 315:
					heading += 90
				case 45:
					heading -= 90
				case 135:
					heading += 90
				case 225:
					heading -= 90
			self.seth(heading)

	def check_collision(self, paddle):
		if self.distance(paddle) < 40 and (paddle.xcor() >= 320 or paddle.xcor() < -320):
			self.seth(self.heading()+90)
		