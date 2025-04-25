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

states_guessed = []
missing_states = []

game_is_on = True
while game_is_on:
	guess = screen.textinput(f"{current_score}/50 | Guess the US States", "Type a State")
	
	all_states = data.state.to_list()
	

	if guess in all_states:
		index_found = data.loc[data.state == guess].index[0] # Search By State Name and Return its Index

		state_coord = (float(data.x[index_found]), float(data.y[index_found]))

		turtle.goto(state_coord)
		turtle.write(data.state[index_found])

		current_score+=1
		states_guessed.append(data.state[index_found])
		print(data.state[index_found])
		continue

	if guess.lower() == "exit":
		print("Saindo do Programa")
		break

	if guess not in all_states:
		print("Errouu")
		game_is_on = False
		break

###################

print(states_guessed)

missing_states = [state for state in all_states if state not in states_guessed]

new_data = pd.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

print(missing_states)

screen.exitonclick()