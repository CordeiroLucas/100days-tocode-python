from GameManager import *
 
gameManager = GameManager()

while True:
    gameManager.run()
    gameManager.reset_game()

gameManager.screen.exitonclick()
############################################################