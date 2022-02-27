import turtle
import time


class Snake:
    CUSTOM_DISTANCE = 20
    def __init__(self):
        self.segments = []
        self.snake_setup()

    def snake_setup(self):
        """Build a "snake" with 3 white squares next to each other."""
        self.segments = [turtle.Turtle(shape="square") for x in range(3)]
        self.segments[0].goto(x=20, y=0)
        self.segments[2].goto(x=-20, y=0)
        for segment in self.segments:
            segment.color("white")
            segment.penup()
        turtle.update()

    def move_forward(self):
        """Moves the first segment forward by a custom distance and sets every next segments's coordinates to the previous segment coordinates."""
        for i in range(len(self.segments)-1, 0, -1):
            coordinates = self.segments[i-1].pos()
            self.segments[i].goto(x=coordinates[0], y=coordinates[1])
        self.segments[0].forward(Snake.CUSTOM_DISTANCE)
        time.sleep(0.1)
        turtle.update()

    def move_up(self):
        """Turn the first segment by 90 degrees"""
        self.segments[0].setheading(90)
    
    def move_down(self):
        """Turn the first segment by 270 degrees"""
        self.segments[0].setheading(270)
    
    def move_right(self):
        """Turn the first segment by 0 degrees"""
        self.segments[0].setheading(0)

    def move_left(self):
        """Turn the first segment by 180 degrees"""
        self.segments[0].setheading(180)