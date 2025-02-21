from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("red")

timmy_turtle.speed(40)

number = 424
for n in range(number):
    if n%2==0:
        timmy_turtle.color("green")
    else:
        timmy_turtle.color("red")

    timmy_turtle.forward(400)
    timmy_turtle.left(179)



screen = Screen()
screen.exitonclick()