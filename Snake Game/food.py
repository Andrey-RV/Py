from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(x=random.randint(-280, 280), y=random.randint(-270, 270))
    
    def the_food_was_eaten(self, by_whom):
        """Return True if the food object distance from the snake is less than 15 and places it in a new random position."""
        if self.distance(by_whom.segments[0].pos()) < 15:
            self.goto(x=random.randint(-280, 280), y=random.randint(-270, 270))
            return True
        return False