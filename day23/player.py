from gameObject import GameObject
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.shape("turtle")
        pass

    def check_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            self.reset_pos()
            return True
        else: return False

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def go_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def go_down(self):
        self.left(180)
        self.go_forward()
        self.right(180)
    
    def go_left(self):
        self.left(90)
        self.go_forward()
        self.right(90)
    
    def go_right(self):
        self.right(90)
        self.go_forward()
        self.left(90)

    def collision(self, carManager:CarManager):
        for car in carManager.cars:
            if self.distance(car) < 20:
                return True
        return False