# TODO: Make the turtle draw the hirst painting

import turtle as t
import colorgram as c
import random as r

tim = t.Turtle()
tim.speed("fastest")

total_colors = 10
colors = c.extract('image.jpeg', total_colors)

def draw_circle():
    color = r.choice(colorlist)
    tim.pendown()
    tim.dot(20, color)
    tim.penup()

# colorlist = []
# for color in colors:
#     colorlist.append(tuple(color.rgb))

colorlist = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52)]

size = 10

sqr_size = size * -22.5 

tim.teleport(sqr_size, sqr_size)

screen = t.Screen()
screen.colormode(255)



for _ in range(size):
    for _ in range(size):
        draw_circle()
        tim.forward(50)
    
    tim.teleport(sqr_size, tim.pos()[1] + 50)







screen.exitonclick()