from library import *
from turtle import Turtle, Screen
from random import randint, choice

#testing

screen = Screen()
width = 500
height = 400
screen.setup(width, height)

tim = Turtle()
tim.speed(1)
tim.pensize(15)

while(True):
    tim.forward(20)
    tim.left(choice([90, -90]))

food = Turtle()
food.fillcolor("black")

food.teleport(randint(1, width), randint(1, height))

food.begin_fill()
food.circle(5)
food.end_fill()

screen.exitonclick()