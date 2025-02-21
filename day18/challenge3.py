## TODO: Make the turtle draw a dashed line

from turtle import Turtle, Screen
from random import random

timmy_turtle = Turtle()

def draw_shape(num_sides):
	angle = 360/num_sides
	for _ in range(num_sides):
		timmy_turtle.forward(100)
		timmy_turtle.right(angle)


num_shapes = 5
num_sides = 4

for _ in range(num_shapes):
	draw_shape(num_sides)
	timmy_turtle.color(random(), random(), random())
	num_sides+=1	

	
screen = Screen()
screen.exitonclick()