from turtle import Screen
from wall import Wall
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

wall = Wall()
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.move_up, "Up")
screen.onkey(my_snake.move_down, "Down")
screen.onkey(my_snake.move_left, "Left")
screen.onkey(my_snake.move_right, "Right")

while True:
    my_snake.move_forward()
    if food.the_food_was_eaten(by_whom=my_snake):
        scoreboard.increase_score()
    if wall.there_was_a_collision(my_snake):
        break