## TODO: Make the turtle walk in random directions

from turtle import Turtle, Screen
from random import random, choice

directions = [0, 90, 180, 270]

timmy_turtle = Turtle()
timmy_turtle.pensize(10)

def walk():
	timmy_turtle.color(random(), random(), random())
	timmy_turtle.setheading(choice(directions))
	timmy_turtle.forward(25)

steps = 500
speed = 0

timmy_turtle.speed(speed)

for _ in range(steps):
	walk()

screen = Screen()
screen.exitonclick()