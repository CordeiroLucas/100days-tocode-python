## TODO: Make the turtle draw a dashed line

from turtle import Turtle, Screen
from random import random

timmy_turtle = Turtle()

def draw_shape(num_sides):
	angle = 360/num_sides
	for _ in range(num_sides):
		timmy_turtle.forward(100)
		timmy_turtle.right(angle)



for shape_side_n in range(3,11):
	draw_shape(shape_side_n)
	timmy_turtle.color(random(), random(), random())

	
screen = Screen()
screen.exitonclick()