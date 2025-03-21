from objects.Ball import *
from objects.Paddle import *
from objects.ScoreBoard import *
from turtle import Turtle, Screen

class GameManager:
	screen = Screen()
	ball = Ball()
	player = Paddle(True)
	enemy = Paddle()
	ScoreBoard = ScoreBoard()

	screen.listen()
	screen.onkeypress(player.up, "Up")
	screen.onkeypress(player.down, "Down")

	def __init__(self):
		self.screen.bgcolor("black")
		self.screen.title("Pong Game")
		self.screen.setup(800, 600)
		self.screen.exitonclick()
	
	def run(self):
		print(self.player.isPlayer)
		print(self.enemy.isPlayer)
	
		pass