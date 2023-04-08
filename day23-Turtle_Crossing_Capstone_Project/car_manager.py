from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WEST = 180


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle(shape="square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(WEST)
        # TODO :leve safe zone
        random_y = random.randint(-250, 250)
        new_car.goto(x=300, y=random_y)

        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            # car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * level)
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT