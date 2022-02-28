import turtle
import time


class Snake:
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

    def move_forward(self, distance=20):
        """Move the snake by a certain distance. If no argument is given, the default value is 20."""
        for i in range(len(self.segments)-1, 0, -1):
            coordinates = self.segments[i-1].pos()
            self.segments[i].goto(x=coordinates[0], y=coordinates[1])
        self.segments[0].forward(distance)
        time.sleep(0.1)
        turtle.update()

    def move_up(self):
        """Set the snake heading to 90 degrees"""
        self.segments[0].setheading(90)
    
    def move_down(self):
        """Set the snake heading to 270 degrees"""
        self.segments[0].setheading(270)
    
    def move_right(self):
        """Set the snake heading to 0 degrees"""
        self.segments[0].setheading(0)

    def move_left(self):
        """Set the snake heading to 180 degrees"""
        self.segments[0].setheading(180)

    def increase_size(self):
        self.segments.append(turtle.Turtle(shape="square"))
        self.segments[-1].color("white")
        self.segments[-1].penup()
    turtle.update()
    
    def collided_with_the_wall(self):
        if (
            self.segments[0].xcor()>280 or self.segments[0].ycor()>280 or
            self.segments[0].xcor()<-270 or self.segments[0].ycor()<-270
           ):
             return True
        return False
    
    def collided_with_itself(self):
        for segment in self.segments[1:]:
            if self.segments[0].pos() == segment.pos():
                return True
        return False