from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# TODO 0: default setting
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# TODO 1: create a snake body
snake = Snake()
food = Food()
score = ScoreBoard()

# TODO 3: control snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# TODO 2: move snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # TODO 4: detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        # TODO : extend snake itself
        snake.extend_segment()
        # TODO 5: track score
        score.increase_score()
    # TODO 6: detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        score.reset()
        # TODO: add snake segment


    # TODO 7 : detect collision with tail.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 20:
            snake.reset_snake()
            score.reset()


screen.exitonclick()
