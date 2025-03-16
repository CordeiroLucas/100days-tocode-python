from turtle import Turtle, Screen
import time
from Snake import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
 
snake = Snake()

screen.listen()

## TODO: Make the snake controllable by arrow keys 

# screen.onkeypress(snake.up(), "Up")
# screen.onkeypress(snake.down(), "Down")
# screen.onkeypress(snake.left(), "Left")
# screen.onkeypress(snake.right(), "Right")

game_is_on = True
while game_is_on:

	
	screen.update()
	time.sleep(0.1) ## 100ms -> 10fps

	snake.move()
	

screen.exitonclick()