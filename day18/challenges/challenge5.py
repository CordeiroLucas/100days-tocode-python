## TODO: Make the turtle draw a dashed line

from turtle import Turtle, Screen
from random import random

timmy_turtle = Turtle()
timmy_turtle.speed(0)


spacing = 10

def draw_spirograph(spacing):
	num_circles =  360 / spacing
	for _ in range(int(num_circles)):
		timmy_turtle.circle(150)
		timmy_turtle.color(random(), random(), random())
		timmy_turtle.setheading(timmy_turtle.heading()+spacing)

draw_spirograph(int(spacing))

screen = Screen()
screen.exitonclick()