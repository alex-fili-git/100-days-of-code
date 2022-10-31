import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


carmanager = CarManager()
scoreboard = Scoreboard()
player = Player()
screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # manage the cars on screen
    carmanager.new_car()
    carmanager.move_cars()
    # detect collision
    for car in carmanager.cars:
        if player.distance(car) < 25 and abs(player.ycor() - car.ycor()) < 23:
            game_is_on = False
            scoreboard.game_over()
    # level up
    if player.ycor() > 280:
        scoreboard.level_up()
        carmanager.level_up()
        player.level_up()


screen.exitonclick()