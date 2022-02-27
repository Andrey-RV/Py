from turtle import Screen
from wall import Wall
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    while True:
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.tracer(0)
        screen.bgcolor("black")
        screen.title("Snake Game")

        wall = Wall()
        my_snake = Snake()
        food = Food()
        scoreboard = Scoreboard()

        game_is_on=True
        screen.listen()
        screen.onkey(my_snake.move_up, "Up")
        screen.onkey(my_snake.move_down, "Down")
        screen.onkey(my_snake.move_left, "Left")
        screen.onkey(my_snake.move_right, "Right")

        while game_is_on:
            my_snake.move_forward()
            if food.the_food_was_eaten(by_whom=my_snake):
                scoreboard.increase_score()
            if my_snake.collided_with_the_wall():
                choice = screen.textinput("YOU LOSE!", f"Your score was {scoreboard.score}.\nDo you want to play again? Enter 'yes' or 'no': ")
                if choice == "yes":
                    screen.clear()
                    break
                else:
                    return None


main()
