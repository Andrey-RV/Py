from turtle import Screen, write
from snake import Snake
from food import Food
from board import Board


def main():
    while True:
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.tracer(0)
        screen.bgcolor("black")
        screen.title("Snake Game")

        board = Board()
        my_snake = Snake()
        food = Food()
        
        screen.listen()
        screen.onkey(my_snake.move_up, "Up")
        screen.onkey(my_snake.move_down, "Down")
        screen.onkey(my_snake.move_left, "Left")
        screen.onkey(my_snake.move_right, "Right")

        while True:
            my_snake.move_forward()
            if food.the_food_was_eaten(by_whom=my_snake):
                board.increase_score()
                my_snake.increase_size()
            if my_snake.collided_with_the_wall() or my_snake.collided_with_itself():
                choice = screen.textinput("YOU LOSE!", f"Your final score is {board.score}.\nDo you want to play again? Enter 'yes' or 'no': ")
                if choice == "yes":
                    screen.clear()
                    board.update_highest_score()
                    break
                else:
                    return None


main()