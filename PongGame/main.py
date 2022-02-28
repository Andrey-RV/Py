from turtle import Screen
from board import Board
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))
ball = Ball()
board = Board()

screen.tracer(1)
screen.update()
screen.listen()
screen.onkeypress(paddle_1.go_up, "Up")
screen.onkeypress(paddle_1.go_down, "Down")
screen.onkeypress(paddle_2.go_up, "w")
screen.onkeypress(paddle_2.go_down, "s")

while True:
    ball.move()
    if ball.has_reached_a_wall():
        ball.bounce_y()
    if ball.has_made_contact_with_a_paddler(paddle_1, paddle_2):
        ball.bounce_x()
    if ball.went_out_of_bounds() == "right":
        screen.tracer(0)
        board.increase_left_player_score()
        ball.reset_position()
    elif ball.went_out_of_bounds() == "left":
        board.increase_right_player_score()
        ball.reset_position()

screen.exitonclick()