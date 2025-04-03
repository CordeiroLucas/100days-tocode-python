from gameObject import GameObject
from random import choice, randrange

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car(GameObject):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(1, 2)
        self.color(choice(COLORS))
        self.right(180)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

class CarManager:
    cars = []
    car_speed = STARTING_MOVE_DISTANCE
    def __init__(self):
        pass

    def spawn(self):
        car = Car()
        car.goto(280, randrange(-240, 240, 40))
        car.move()
        self.cars.append(car)

    def spawnManager(self):
        self.spawn_limit = 16

        if len(self.cars) <= self.spawn_limit:
            self.spawn()
    
    def moveCars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() <= -240:
                car.goto(280, randrange(-240, 240, 40))    
    
    def increment_speed(self):
        self.car_speed += MOVE_INCREMENT
