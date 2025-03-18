from turtle import Screen

from Snake import *
from Food import *

import time
from random import randrange

WIDTH = 600
HEIGHT = 600

class GameManager:
	screen = Screen()
	snake = Snake()
	food = Food()



	def __init__(self):
		self.score = 0
		self.game_is_on = True

		self.__setup_screen()

	def __setup_screen(self):
		self.screen.setup(width=WIDTH, height=HEIGHT)
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
		self.__respawn_food()
		
		while self.game_is_on:
			self.screen.update()
			time.sleep(0.1) ## 100ms -> 10fps

			self.snake.move()
			self.borders_colision()
			self.__check_food()

			if self.snake.check_self_collision():
				self.__gameOver()

		self.screen.exitonclick()
	
	def __gameOver(self):
		self.game_is_on = False
		print("Game Over") ################ check

	def borders_colision(self):
		screen_width = self.screen.window_width()
		screen_height = self.screen.window_height()

		max_x = screen_width/2
		max_y = screen_height/2

		head = self.snake.head
		if head.xcor() >= max_x or head.ycor() >= max_y or head.xcor() <= max_x*-1 or head.ycor() <= max_y*-1:
			self.__gameOver()
			print(f"Borders Collision") ################ check

	def __respawn_food(self):
		screen_width = self.screen.window_width()
		screen_height = self.screen.window_height()

		max_x = int(screen_width/2)
		max_y = int(screen_height/2)

		new_x = randrange(max_x * -1 + 20, max_x - 20, 20)
		new_y = randrange(max_y * -1 + 20, max_y- 20, 20)

		new_pos = (new_x, new_y)

		self.food.spawn(new_pos)
	
	# Not Working Properly due to screen size problems

	def __check_food(self):
		food_pos = self.food.get_pos()
		head_pos = self.snake.head.pos()

		if food_pos == head_pos:
			self.score += 1

			print("Score: ", self.score) ################ check

			self.snake.eat()
			self.__respawn_food()