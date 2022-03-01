from turtle import Turtle
import time

class Board(Turtle):
    score = 0
    highest_score = 0

    def __init__(self):
        super().__init__()
        self.walls = []
        self.hideturtle()
        self.penup()
        self.create_walls()
        self.update_scoreboard()
    
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

    def update_scoreboard(self):
        self.clear()
        self.color("white")
        self.goto(x=-100, y=250)
        self.write(arg=f"Score : {self.score},", align="center", font=('Courier', 15,'normal'))
        self.goto(x=80, y=250)
        self.write(f"Highest Score : {Board.highest_score}", align="center", font=('Courier', 15,'normal'))
    
    def increase_score(self):
        """Clear the previous text from the screen, increases the score by one and prints the new score."""
        Board.score += 1
        self.update_scoreboard()

    @classmethod
    def update_highest_score(cls,):
        if cls.score > Board.highest_score:
            cls.highest_score = cls.score
        cls.score = 0

    
