from objects.Ball import *
from objects.Paddle import *
from objects.ScoreBoard import *
from turtle import Screen
import time

class GameManager:
	screen = Screen()
	ball = Ball()
	l_paddle = Paddle((-350, 0))
	r_paddle = Paddle((350, 0))
	# ScoreBoard = ScoreBoard()

	screen.listen()
	screen.onkeypress(l_paddle.up, "w")
	screen.onkeypress(l_paddle.down, "s")
	
	screen.onkeypress(r_paddle.up, "Up")
	screen.onkeypress(r_paddle.down, "Down")

	def __init__(self):
		self.screen.tracer(0)
		self.screen.bgcolor("black")
		self.screen.title("Pong Game")
		self.screen.setup(800, 600)
		self.game_is_on = True
	
	def run(self):
		while(self.game_is_on):
			self.ball.move()
			self.screen.update()
			time.sleep(0.05)
		self.screen.exitonclick()