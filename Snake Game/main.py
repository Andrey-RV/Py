from snake import Snake
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

my_snake = Snake()

screen.listen()
screen.onkey(my_snake.move_up, "Up")
screen.onkey(my_snake.move_down, "Down")
screen.onkey(my_snake.move_left, "Left")
screen.onkey(my_snake.move_right, "Right")

while True:
    my_snake.move_forward()