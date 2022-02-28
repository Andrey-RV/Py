import turtle

class Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.score_board_setup()

    def score_board_setup(self):
        turtle.tracer(0)
        self.goto(x=-80, y=200)
        self.write(arg=f"{self.left_player_score}", align="center", font=('Courier', 70,'normal'))
        self.goto(x=80, y=200)
        self.write(arg=f"{self.right_player_score}", align="center", font=('Courier', 70,'normal'))
        turtle.update()
        turtle.tracer(1)

    def increase_right_player_score(self):
        self.right_player_score += 1
        self.clear()
        self.score_board_setup()
    
    def increase_left_player_score(self):
        self.left_player_score += 1
        self.clear()
        self.score_board_setup()
    
