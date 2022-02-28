from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=250)
        self.show_level()

    def show_level(self):
        self.write(f"Level: {self.level}", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.show_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
