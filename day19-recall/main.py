from turtle import Turtle, Screen
from day20_snake_game import SnakeGame
import time
from day21_food import Food
from day21_scoreboard import ScoreBoard
# TODO: default setting
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.title("Snake Game")
screen.tracer(0)

# TODO: create snake
snake = SnakeGame()
food = Food()
score_board = ScoreBoard()

is_game_on = True
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Left', fun=snake.left)
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.random_food()
        snake.extend_segment()
        score_board.increase_score()
    if snake.head.xcor() > 230 or snake.head.xcor() < -230 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        is_game_on = False
        score_board.game_end()

    for snake_segment in snake.segments[1:]:
        if snake.head.distance(snake_segment) < 15:
            is_game_on = False
            score_board.game_end()

screen.exitonclick()
