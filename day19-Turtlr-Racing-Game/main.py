from turtle import Turtle, Screen
import random

is_on_race = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
color = ["red", "orange", "yellow", "green", "blue", "purple"]

# use y_position instead of :racer.goto(x= -230, y=(-100 + gap * turtle_index)) , easy to change if we want
# gap = 30
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []  # racer_turtle -- all_turtle
# name:  use turtle_index istead of turtle
# name: racer -- new_turtle
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


# TODO:Teacher solution: once a turtle run over the end, other turtle wil stop running
if user_bet:
    is_on_race = True
while is_on_race:
    for turtle_racer in all_turtle:
        if turtle_racer.xcor() > 230:
            is_on_race = False
            # winner_color += color[all_turtle.index(turtle_racer)]
            winner_color = turtle_racer.fillcolor()
            if user_bet == winner_color:
                print(f"You won.The winner is {winner_color}")
            else:
                print(f"You lose.The winner is {winner_color}")

        turtle_racer.forward(random.randint(0, 10))
screen.exitonclick()


# TODO: My solution: once a turtle run over the end, other turtle wil stop running
#
# def race_turtle(is_on):
#     while is_on:
#         for turtle_racer in all_turtle:
#             if turtle_racer.xcor() >= 230:
#                 is_on = False
#                 # winner_color += color[all_turtle.index(turtle_racer)]
#                 winner_color = turtle_racer.fillcolor()
#                 return winner_color
#             turtle_racer.forward(random.randint(0, 10))
#
#
# if user_bet:
#     is_on_race = True
# game_result = race_turtle(is_on_race)
# if user_bet == game_result:
#     print(f"You won. The winner is {game_result}")
# else:
#     print(f"You lose. The winner is {game_result}")
# screen.exitonclick()
