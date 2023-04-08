from turtle import Turtle, Screen
PADDLE_WIDTH = 5
PADDLE_HEIGHT = 1
MOVE_PIXELS = 20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.speed("fastest")
        self.position = position

        # TODO: create a paddle
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + MOVE_PIXELS
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_PIXELS
        self.goto(self.xcor(), new_y)
