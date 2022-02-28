from turtle import Turtle
import time

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.walls = []
        self.create_walls()
        self.show_welcome_message()
        self.create_scoreboard()
    
    def create_walls(self):
        self.walls = [Turtle(shape="square") for x in range(4)]
        self.walls[0].goto(x=-300, y=0)
        self.walls[1].goto(x=290, y=0)
        self.walls[2].goto(x=0, y=300)
        self.walls[3].goto(x=0, y=-290)
        self.walls[0].turtlesize(stretch_wid=30, stretch_len=1)
        self.walls[1].turtlesize(stretch_wid=30, stretch_len=1)
        self.walls[2].turtlesize(stretch_wid=1, stretch_len=30)
        self.walls[3].turtlesize(stretch_wid=1, stretch_len=30)
        for wall in self.walls:
            wall.color("white")

    def show_welcome_message(self):
        self.hideturtle()
        self.home()
        self.color("white")
        self.write("Welcome to the snake game.\nYou objetive is to eat as much 'food' as possible.\nThe moment the snake touches itself or the walls the game is over.\nUse the arrow keys to move the snake around!.", align="center", font=("Courier", 10, "normal"))
        self.penup()
        time.sleep(5)
        self.clear()

    def create_scoreboard(self):
        self.goto(x=0, y=250)
        self.write(arg=f"Score : {self.score}", align="center", font=('Courier', 15,'normal'))

    def increase_score(self, alignment="center", font_choice=('Courier', 15,'normal')):
        """Clear the previous text from the screen, increases the score by one and prints the new score."""
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", align=alignment, font=font_choice)
    
