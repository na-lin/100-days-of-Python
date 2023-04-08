from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.show_level()

    def show_level(self):
        self.goto(-200, 240)
        self.write(arg=f"Level:{self.level + 1} ", move=True, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=True, align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.show_level()
