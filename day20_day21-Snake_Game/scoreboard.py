from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        #TODO: read high score from data.txt file
        with open("data.txt") as data:
            self.high_score =int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-10, y=270)
        self.write(arg=f'Score: {self.score} High Score:{self.high_score} ', move=True, align=ALIGNMENT, font=FONT)


    # def game_over(self):
    #     self.home()
    #     self.write(arg=f'GAME OVER', move=True, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score

        #TODO:save high score into file
        with open("data.txt",mode='w') as data:
            data.write(str(self.high_score))

        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()



