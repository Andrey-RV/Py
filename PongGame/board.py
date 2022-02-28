import turtle

class Board(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.draw_central_line()
        self.score_board_setup()

    def score_board_setup(self):
        turtle.tracer(0)
        self.goto(x=-45, y=220)
        self.write(arg=f"{self.left_player_score}", align="center", font=('Pong Score', 40,'normal'))
        self.goto(x=70, y=220)
        self.write(arg=f"{self.right_player_score}", align="center", font=('Pong Score', 40,'normal'))
        turtle.update()
        turtle.tracer(1)

    def draw_central_line(self):
        turtle.tracer(0)
        self.goto(x=0, y=-285)
        self.setheading(90)
        self.pendown()
        self.pensize(5)
        for _ in range(20):
            self.forward(15)
            self.penup()
            self.forward(20)
            self.pendown()
        self.penup()
        turtle.update()
        turtle.tracer(1)

    def increase_right_player_score(self):
        self.right_player_score += 1
        self.clear()
        self.score_board_setup()
        self.draw_central_line()
    
    def increase_left_player_score(self):
        self.left_player_score += 1
        self.clear()
        self.score_board_setup()
        self.draw_central_line()
    
