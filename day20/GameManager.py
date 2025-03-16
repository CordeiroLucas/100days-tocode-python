from Snake import *
from Food import *
from turtle import Screen
import time

class GameManager:
	def __init__(self):
		self.score = 0
		self.game_is_on = True

		self.screen = Screen()		
		self.snake = Snake()
		self.food = Food()

		self.__setup_screen()

	def __setup_screen(self):
		self.screen.setup(width=600, height=600)
		self.screen.bgcolor("black")
		self.screen.title("My Snake Game")
		self.screen.tracer(0)

		self.__snake_controls()

	def __snake_controls(self):
		self.screen.listen()
		self.screen.onkeypress(self.snake.up, "Up")
		self.screen.onkeypress(self.snake.down, "Down")
		self.screen.onkeypress(self.snake.left, "Left")
		self.screen.onkeypress(self.snake.right, "Right")


	def run(self):
		while self.game_is_on:
			
			self.screen.update()
			time.sleep(0.1) ## 100ms -> 10fps

			self.snake.move()

			self.checkAlive()

		self.screen.exitonclick()
	
	def __gameOver(self):
		self.game_is_on = False

	def checkAlive(self):
		screen_width = self.screen.window_width()
		screen_height = self.screen.window_height()
		head = self.snake.head

		max_x = screen_width/2
		max_y = screen_height/2

		if head.xcor() > max_x or head.ycor() > max_y or head.xcor() < max_x*-1 or head.ycor() < max_y*-1:
			self.__gameOver()
		
			

			
		