from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("50_states.csv")

screen = Screen()

turtle = Turtle()
turtle.penup()
turtle.hideturtle()

index_found = data.loc[data.state == "Texas"].index[0] # Search By State Name and Return its Index
state_coord = (float(data.x[index_found]), float(data.y[index_found]))

print(data.state[index_found])
print(data.x[index_found])
print(data.y[index_found])

turtle.goto(state_coord)
turtle.write(data.state[index_found])

screen.bgpic("blank_states_img.gif")

screen.exitonclick()