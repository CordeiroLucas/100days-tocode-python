from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.title("U S States Game")

turtle = Turtle()
turtle.penup()
turtle.hideturtle()


#################
total_states = data.count().state
current_score = 0
game_is_on = True
while game_is_on:
	guess = screen.textinput("Guess the US States", "Type a State")

	print(guess)

	index_found = data.loc[data.state == guess] # Search By State Name and Return its Index

	
	if not index_found.empty:
		index_found = index_found.index[0]
		print(index_found)

		state_coord = (float(data.x[index_found]), float(data.y[index_found]))

		print("Infos: ")
		print(data.state[index_found])
		print(data.x[index_found])
		print(data.y[index_found])

		turtle.goto(state_coord)
		turtle.write(data.state[index_found])
		current_score+=1
	else:
		print("Errouu")
		game_is_on = False
	print(f"{current_score}/{total_states}")

###################

screen.exitonclick()