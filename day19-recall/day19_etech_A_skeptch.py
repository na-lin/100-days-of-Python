import turtle
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# timmy.speed("fastest")
# for side_line in range(3, 11):
#     for _ in range(side_line):
#         timmy.forward(100)
#         timmy.right(int(360/side_line))


# import random
#
# direction = [0, 90, 180, 270]
# turtle.colormode(255)
# timmy.pensize(10)
# timmy.hideturtle()
# timmy.speed("fastest")
# while 20:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_rgb = (r, g, b)
#     timmy.color(color_rgb)
#
#     timmy.setheading(random.choice(direction))
#     timmy.forward(20)
#     timmy.color()

# import random
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r,g,b)
#     return color
#
# gap = 5
# radius = 100
# turtle.colormode(255)
# timmy.speed("fastest")
#
# for _ in range(int(360 / gap)):
#     timmy.color(random_color())
#     timmy.circle(radius)
#     current_heading = timmy.heading()
#     timmy.setheading(current_heading + gap)

screen.listen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def turn_right():
    timmy.setheading(timmy.heading() - 10)


def turn_left():
    timmy.setheading(timmy.heading() + 10)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

# user_bet = screen.textinput(title="Make a bet",prompt="Whick color will win?:")


screen.exitonclick()
