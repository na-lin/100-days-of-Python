from turtle import Turtle, Screen
import random

class RacingTurtlrGame:

    def __init__(self):
        screen = Screen()
        screen.setup(width=500,height=400)
        self.bet = screen.textinput(title="Make a bet",prompt="What color will win?")
        self.turtles = []
        self.create_turtle()

    def create_turtle(self):
        color_set = ["red","orange","yellow","green","blue","purple"]
        for turtle in range(6):
            new_turtle = Turtle(shape="turtle")
            new_turtle.color(color_set[turtle])
            new_turtle.penup()
            new_turtle.goto(x= - 230,y= -100 + 30*turtle)
            self.turtles.append(new_turtle)

    def race(self):

        for turtle in self.turtles:

            random_forward = random.randint(0, 10)
            turtle.forward(random_forward)

            x_position = turtle.xcor()
            if x_position > 230:
                winner = turtle.color()
                if winner[0] == self.bet:
                    print(f"You won, the winner was {winner[0]}")
                    return "end"
                else:
                    print(f"You lose, the winner was {winner[0]}")
                    return "end"
