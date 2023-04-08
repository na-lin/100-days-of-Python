import random
import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("arrow")
# tim.color("medium violet red")
# timmy_turtle.forward(100)
# timmy_turtle.right(90)

# TODO challenge 1: draw a square, 100 by 100
# for _ in range(0, 4):
#     tim.right(90)
#     tim.forward(100)

# TODO Challenge 2: draw a dashed line : 10 paces , 10 gap , 50 times

# tim.penup()
# tim.back(300)
# tim.pendown()
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# TODO: challenge 3: draw a triangle-3, square-4, pentagon-5, hexagon-6, heptagon-7, octagon-8, nonagon-9, decagon-10
# draw with random color
# size 100 in terms of each length
color_set = ["coral", "medium slate blue", "saddle brown", "gold", "red", "dark olive green", "black", "dark green",
             "dark turquoise", "pink"]

# angles = 3
# while angles <= 10:
#     color = random.choice(color_set)
#     tim.color(color)
#     for _ in range(angles):
#         tim.forward(100)
#         turn_angle = round(360 / angles)
#         tim.right(turn_angle)
#
#     angles += 1
# TODO: challenge 3: draw a triangle-3, square-4, pentagon-5, hexagon-6, heptagon-7, octagon-8, nonagon-9, decagon-10
color_set = ["coral", "medium slate blue", "saddle brown", "gold", "red", "dark olive green", "black", "dark green",
             "dark turquoise", "pink"]


# # NEW: use function to do repeat instructions , more readable
# def draw_shape(number_side):
#     angle = 360 / number_side
#     for _ in range(number_side):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     color = random.choice(color_set)
#     tim.color(color)
#     draw_shape(shape_side_n)

# TODO: challenge 4: draw a random walk, thickness, speed up turtle
# east, north, west, south
# direction = [0, 90, 180, 270]
#
#
# def random_walk(times):
#     tim.speed(10.0)
#     for _ in range(times):
#         tim.color(random.choice(color_set))
#         tim.pensize(8)
#         # tim.right(random.choice(direction))
#         tim.setheading(random.choice(direction))
#         tim.forward(20)
#
#
# tim.shape("circle")
# tim.shapesize(0.1, 0.1, 0.1)
#
# random_walk(100)

# TODO 5 : challege: change color
# teacher solution
# tap into actual model instead of actual object
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_turple = (r, g, b)
    return color_turple


direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.pencolor(random_color())
    tim.setheading(random.choice(direction))
    tim.forward(20)

# TODO 6 : make a spirograph , random color, documentation, radius = 100, change tilt
# tim.speed("fastest")
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color_turple = (r, g, b)
#     return color_turple
#
#
# def draw_spirograph(size_of_gap):
#     times = round(360 / size_of_gap)
#     for _ in range(times):
#         tim.pencolor(random_color())
#         tim.circle(100)
#         # tim.tiltangle(angle)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(5)

# angle = 5
# # if use range(2,361,5),each time angle will be different,not determined. so the graphic would not as a spirography
# # change range number into times , set angle determined
# for _ in range(int(360/angle)):
#     tim.pencolor(random_color())
#     tim.circle(100)
#     # tim.tiltangle(angle) this don't change direction
#     # left and setheading are both ok, but setheading is more readable
#     tim.left(angle)
#     # tim.setheading(tim.heading() + angle)

screem = Screen()
screem.exitonclick()
