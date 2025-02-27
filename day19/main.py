from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_fowards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def turn_left():
    tim.left(90)

def turn_right():
    tim.right(90)

screen.listen()
screen.onkey(key="w", fun=move_fowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.exitonclick() 