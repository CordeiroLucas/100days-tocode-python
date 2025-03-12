class Snake:
    def __init__(self):
        self.speed:float = 1
        self.lenght:int = 1
        self.isAlive:bool = True

    def changeSpeed(self, speed):
        self.speed = speed

    def eat(self):
        self.lenght+=1

class GameManager:
    def __init__(self):
        self.foodNumber = 1
        self.score = 0
        self.gameOver = False



    snake = Snake()
    