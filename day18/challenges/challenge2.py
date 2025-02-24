## TODO: Make the turtle draw a square

from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.color("red")

timmy_turtle.speed(5)

number = 4
angle = 90

for n in range(number):
    timmy_turtle.color("red")

    timmy_turtle.forward(100)
    timmy_turtle.right(angle)

screen = Screen()
screen.exitonclick()