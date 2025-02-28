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
	turtles.append(Turtle())

	turtles[n].color(colors[n])
	turtles[n].shape("turtle")
	turtles[n].penup()
	turtles[n].speed(speed)

	# print(f"{n} - ", turtles[n].color())

	y =  -(screen.window_height()/total) + n * screen.window_height()/total - 75

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