from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO 0 : default setting
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Capstone Project")
screen.tracer(0)

# TODO 1:create a player
player = Player()

# TODO 1: move player by press "Up" key
screen.listen()
screen.onkey(key="Up", fun=player.go_up)

# TODO 2:generate car and move
car_manager = CarManager()

# TODO 5: show level on screen
scoreboard = Scoreboard()

is_game_on = True
# loop_times = 0
while is_game_on:
    time.sleep(0.1)
    screen.update()
    # loop_times += 1

   # TODO 2: move car
    car_manager.move_car()
    # NEW : this is my way to generate new car with separarte distance
    if car_manager.cars[-1].xcor() < 270:
        car_manager.generate_car()
    # new: another way to generate new car with separate distance
    # TODO : generate a new car only every 6th time in game loop
    # if loop_times == 6:
    #     loop_times = 0
    #     car_manager.generate_car()

    # TODO 4: detect collision between player and cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            is_game_on = False

    # TODO 5: detect when player cross successfully,
    #  player will back to start position and level game up
    # if player.ycor() > 280:
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()




screen.exitonclick()
