from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# TODO: make a etch-A sketch app , W - F. S - B . A - counter- clockwise, D - clockwise, c- clear- back center

# event listener
# start listening

def move_forward():
    """"plus W key to go forward"""
    tim.forward(20)

def move_backward():
    """"plus S key to go backward"""
    tim.back(20)

def clear_drawing():
    """"plus C key to clear draw"""
    tim.reset()

    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()

def turn_left():
    """"plus A key to counter clockwise"""
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
    tim.left(10)

def turn_right():
    """"plus D key to  clockwise"""
    tim.right(5)
    # new_heading = tim.heading() - 10
    # tim.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()
