import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = []
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
loop_number = 0
while game_is_on:
    if loop_number%6 == 0:
        cars.append(CarManager())
    for car in cars:
        car.move()
    if turtle.hit_a_car(cars):
        scoreboard.game_over()
        game_is_on = False
    if turtle.won():
        CarManager.increase_speed()
        scoreboard.next_level()
    loop_number += 1
    time.sleep(0.1)
    screen.update()

screen.exitonclick()