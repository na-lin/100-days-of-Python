from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
import random

START_POSITION = [(350, 0), (-350, 0)]
# TODO 1:set up the Main screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO 2 : create and move a paddle
paddle_right = Paddle(START_POSITION[0])
paddle_left = Paddle(START_POSITION[1])

# TODO 3:create a ball and make it move
ball = Ball()

# TODO 7 : track score
score = ScoreBoard()

# TODO 2: move a paddle
screen.listen()
# paddle left
screen.onkey(key="Up", fun=paddle_right.go_up)
screen.onkey(key="Down", fun=paddle_right.go_down)

# Paddle right
screen.onkey(key="w", fun=paddle_left.go_up)
screen.onkey(key="s", fun=paddle_left.go_down)


def update():
    screen.update()


screen.onkey(key="f", fun=update)
is_game_on = True

# is_at_edge = 1
screen.update()
while is_game_on:
    # TODO : change each time to controll ball speed
    # time.sleep(ball.move_speed)
    time.sleep(0.1)

    screen.update()
    # TODO: convert between move and rebound
    # TODO 4: detect the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    ball.move()

    # TODO 5 : decect collision with paddle
    if ball.xcor() == 330 and ball.distance(paddle_right) < 60 or ball.xcor() == 330 and ball.distance(paddle_left) < 60:
        ball.bounce_paddel()

    # TODO 6 : dectect when paddle misses boall
    # if ball.xcor() > 350 and ball.distance(paddle_right)> 50:
    # restart create ball
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_increase()

    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_increase()

screen.exitonclick()
