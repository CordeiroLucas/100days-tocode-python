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
	guess = screen.textinput(f"{current_score}/50 | Guess the US States", "Type a State")
	
	all_states = data.state.to_list()
	states_guessed = []

	if guess in all_states:
		index_found = data.loc[data.state == guess].index[0] # Search By State Name and Return its Index
		print(index_found)

		state_coord = (float(data.x[index_found]), float(data.y[index_found]))

		turtle.goto(state_coord)
		turtle.write(data.state[index_found])

		current_score+=1
		states_guessed.append(data.state[index_found])

	if guess.lower() == "exit":
		print("Saindo do Programa")

		missing_states = []
		for state in all_states:
			if state not in states_guessed:
				missing_states.append(state)
		break

	if guess not in all_states:
		print("Errouu")
		game_is_on = False

###################

print(missing_states)

screen.exitonclick()