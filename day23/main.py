import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
carManager = CarManager()

screen.listen()
screen.onkeypress(player.go_forward, "Up")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_down, "Down")

game_is_on = True
frame = 0

while game_is_on:
    frame+=1
    screen.update()
    score.display()

    if (frame == 6):
        carManager.spawnManager()
        frame = 0
    
    carManager.moveCars()

    if player.check_finish():
        score.next_level()
        carManager.increment_speed()
        
    if player.collision(carManager):
        game_is_on = False
        score.game_over()
        print("Collision")
    
    time.sleep(0.1)

screen.exitonclick()