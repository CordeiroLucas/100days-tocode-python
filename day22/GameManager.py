from objects.Ball import *
from objects.Paddle import *
from objects.ScoreBoard import *
from turtle import Turtle, Screen

class GameManager:
	screen = Screen()
	ball = Ball()
	l_paddle = Paddle((-350, 0))
	r_paddle = Paddle((350, 0))
	ScoreBoard = ScoreBoard()

	screen.listen()
	screen.onkeypress(l_paddle.up, "w")
	screen.onkeypress(l_paddle.down, "s")

	screen.onkeypress(r_paddle.up, "Up")
	screen.onkeypress(r_paddle.down, "Down")

	def __init__(self):
		self.screen.bgcolor("black")
		self.screen.title("Pong Game")
		self.screen.setup(800, 600)
		self.screen.exitonclick()
		self.game_is_on = True
	
	def run(self):
		while(self.game_is_on):
			self.screen.update()