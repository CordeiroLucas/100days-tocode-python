from turtle import Screen

from Snake import *
from Food import *
from ScoreBoard import *

from time import sleep
from random import randrange

WIDTH = 600
HEIGHT = 600
UPDATE_SPEED = 0.12 ## in seconds | 150ms

class GameManager:
	screen = Screen()
	snake = Snake()
	food = Food()
	scoreBoard = ScoreBoard()

	def __init__(self):
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

		self.scoreBoard.high_score = self.get_highscore()
		
		while self.game_is_on:
			self.scoreBoard.update_scoreboard()

			sleep(UPDATE_SPEED)

			self.snake.move()
			self.__borders_colision()
			self.__check_food_collision()

			if self.snake.check_self_collision():
				self.__gameOver()
			self.screen.update()
	
	def __gameOver(self):
		self.game_is_on = False
		print("Game Over")
		self.scoreBoard.game_over()
		

	def reset_game(self):
		self.snake.reset_snake()
		self.scoreBoard.reset_scoreboard()
		self.food.reset_food()

		self.save_highscore(self.scoreBoard.high_score)

		self.__respawn_food()

		self.game_is_on = True
		self.run()

	def __borders_colision(self):
		screen_width = self.screen.window_width()
		screen_height = self.screen.window_height()

		max_x = screen_width/2
		max_y = screen_height/2

		head = self.snake.head
		if head.xcor() >= max_x or head.ycor() >= max_y or head.xcor() <= max_x*-1 or head.ycor() <= max_y*-1:
			self.__gameOver()

	def __respawn_food(self):
		screen_width = self.screen.window_width()
		screen_height = self.screen.window_height()

		max_x = int(screen_width/2)
		max_y = int(screen_height/2)

		new_x = randrange(max_x * -1 + 20, max_x - 20, 20)
		new_y = randrange(max_y * -1 + 20, max_y - 20, 20)

		new_pos = (new_x, new_y)

		self.food.spawn(new_pos)
	
	# Not Working Properly due to screen size problems

	def __check_food_collision(self):
		food_pos = self.food.get_pos()
		head_pos = self.snake.head.pos()

		dis_x = food_pos[0] - head_pos[0]
		dis_y = food_pos[1] - head_pos[1]

		## Distance measured by pythagorean theorem
		if (dis_x ** 2 + dis_y ** 2) ** 0.5 < 15: 
			self.scoreBoard.increase_score()
			self.snake.eat()
			self.__respawn_food()

	def save_highscore(self, score):
		with open("highscores.txt", "w") as f:
			f.write(str(score))
		
	def get_highscore(self):
		with open("highscores.txt", "r") as f:
			return int(f.read())