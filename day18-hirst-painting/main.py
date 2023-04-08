import extract_color
from turtle import Turtle, Screen
import turtle
# TODO: extract RGB store in triple and print a list contain triple include RGB
import random
# color_list = extract_color.extract_colors()
# color_list.remove((253, 251, 248))
# color_list.remove((254, 250, 252))
rgb_colors_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                   (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
                   (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
                   (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
                   (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231),
                   (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112), (16, 54, 243), (240, 16, 16)]

# TODO 2: 10*10 row , 20 size each dot, around 50 space
tim = Turtle()
# turtle.colormode(255)
# TODO: draw dot by turtle, size = 20
turtle.colormode(255)
tim.speed("fastest")
# TODO: put up pen
tim.penup()
tim.hideturtle()
# TODO: use turtle to create a 10*10 row
y_position = -(50*5)
# tim.goto(-200, 0)
for row in range(10):
    tim.goto(-200, y_position)
    for column in range(0, 10):
        tim.dot(20, random.choice(rgb_colors_list))
        tim.forward(50)
    y_position += 50

screen = Screen()
screen.exitonclick()

