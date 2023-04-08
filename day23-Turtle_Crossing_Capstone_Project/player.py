from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

NORTH = 90


class Player(Turtle):
    # TODO 1: create turtle
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(NORTH)
        # self.goto(STARTING_POSITION)
        self.go_to_start()

    # TODO 2 : move turtle up
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # TODO 3 : reset turtle position in staring_position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
