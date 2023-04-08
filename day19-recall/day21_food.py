from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("yellow")
        self.penup()
        self.random_food()

    def random_food(self):
        x_position = random.randint(-220, 220)
        y_position = random.randint(-220, 220)
        self.goto(x=x_position, y=y_position)