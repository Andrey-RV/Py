import turtle
import random


def set_turtles_colors():
    """Set each turtle color to a random color from the rainbow colors"""
    for i in range(6):
        turtles[i].color(colors[i])


def move_turtles_to_the_initial_positions():
    """Move all turtles to the very left of the screen"""
    y_coord=-100
    for i in range(6):
        turtles[i].penup()
        turtles[i].goto(x=-230, y=y_coord)
        y_coord+=40


def is_there_a_winner():
    """Returns true if any of the turtles has already moved past y position y=220"""
    for i in range(6):
        turtles[i].forward(random.randint(0, 10))
        if turtles[i].pos()[0]>=220:
            if player_won(turtles[i]):
                print("You won the bet.")
            else:
                print("You lost the bet.")
            print(f"The {turtles[i].color()[0]} turtle is the winner.")
            return False
    return True


def player_won(turtle_winner):
    """Returns true if the turtle who has reached the final position was the player's choice"""
    if turtle_winner.color()[0] == player_bet:
        return True
    return False


screen = turtle.Screen()
screen.setup(width=500, height=400)
turtles = [turtle.Turtle(shape="turtle") for i in range(6)]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
player_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter one of the rainbow colors: ")

if player_bet:
    set_turtles_colors()
    move_turtles_to_the_initial_positions()
    is_race_on = True
else:
    is_race_on = False
    
while is_race_on:
    is_race_on = is_there_a_winner()
           
screen.exitonclick()