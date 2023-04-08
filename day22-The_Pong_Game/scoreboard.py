from turtle import Turtle

LEFT_SCORE_POSITION = (-100, 220)
RIGHT_SCORE_POSITION = (100, 220)
ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()

        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(LEFT_SCORE_POSITION)
        self.write(arg=self.l_score, move=True, align=ALIGNMENT, font=FONT)
        self.goto(RIGHT_SCORE_POSITION)
        self.write(arg=self.r_score, move=True, align=ALIGNMENT, font=FONT)

    def l_increase(self):
        self.l_score += 1
        self.write_score()

    def r_increase(self):
        self.r_score += 1
        self.write_score()
