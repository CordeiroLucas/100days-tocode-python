## TODO: Make the turtle draw a dashed line

from turtle import Turtle, Screen

timmy_turtle = Turtle()

section = 15


for _ in range(section):
    timmy_turtle.pendown()
    timmy_turtle.forward(10)
    timmy_turtle.penup()
    timmy_turtle.forward(10)

screen = Screen()
screen.exitonclick()