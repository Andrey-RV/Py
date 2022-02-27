import turtle


class Wall():
    def __init__(self):
        self.walls = []
        self.create_walls()

    def create_walls(self):
        self.walls = [turtle.Turtle(shape="square") for x in range(4)]
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
