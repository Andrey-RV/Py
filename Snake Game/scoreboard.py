from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.color("white")
        self.score = 0
        self.write(arg=f"Score : {self.score}", align="center", font=('Arial', 15,'normal'))
    
    def increase_score(self, alignment="center", font_choice=('Arial', 15,'normal')):
        """Clear the previous text from the screen, increases the score by one and prints the new score.\n\n
        If no argument is provided, by default, the text alignment is set to center and the front to Arial, 15, normal"""
        self.score += 1
        self.clear()
        self.write(arg=f"Score : {self.score}", align=alignment, font=font_choice)
