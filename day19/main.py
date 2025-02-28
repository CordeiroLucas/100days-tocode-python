from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "green", "blue", "yellow", "brown"]

speed = 5
total = 5
turtles:list[Turtle] = []
for n in range(total):
	new_turtle = Turtle()

	new_turtle.color(colors[n])
	new_turtle.shape("turtle")
	new_turtle.penup()
	new_turtle.speed(speed)
	turtles.append(new_turtle)

	# print(f"{n} - ", turtles[n].color())

	y =  -100 + n * 50

	turtles[n].goto(-230, y)

running = True
while running:
	selected:Turtle = choice(turtles)
	selected.forward(10)

	if selected.pos()[0] == 250:
		running = False
		break

# print(user_bet)
if selected.color()[0] == user_bet:
	print("Ganhou")
else:
	# print(selected.color()[0])
	print("Perdeu")

screen.exitonclick()