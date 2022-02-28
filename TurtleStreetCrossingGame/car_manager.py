from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    speed_increment = 0
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.goto(x=320 , y=random.randint(-250, 250))
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE + self.speed_increment)

    @classmethod
    def increase_speed(cls):
        cls.speed_increment += MOVE_INCREMENT