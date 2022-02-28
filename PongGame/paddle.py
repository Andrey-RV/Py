import turtle

class Paddle(turtle.Turtle):
    def __init__(self, position):
        """Take a tuple containing the coordinates of the paddle"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)
