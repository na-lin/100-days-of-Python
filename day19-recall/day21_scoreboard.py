from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
TITLE_POSITION = (-10,220)
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        self.goto(TITLE_POSITION)
        self.write(arg=f"Score = {self.score}",move=True,align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_end(self):
        self.home()
        self.write(arg="GAME END ",move=True,align=ALIGNMENT,font=FONT)

