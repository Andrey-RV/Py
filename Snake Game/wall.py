import turtle


class Wall():
    def __init__(self):
        self.walls = []
        self.create_walls()

    def create_walls(self):
        self.walls = [turtle.Turtle(shape="square") for x in range(120)]
        self.create_right_walls()
        self.create_left_walls()
        self.create_upper_walls()
        self.create_lower_walls()
        for wall in self.walls:
            wall.color("white")

    def create_right_walls(self):
        y_coord = -295
        for i in range(30):
            self.walls[i].goto(x=-295, y=y_coord)
            y_coord += 20
    
    def create_left_walls(self):
        y_coord = -295
        for i in range(30, 60):
            self.walls[i].goto(x=285, y=y_coord)
            y_coord += 20
    
    def create_upper_walls(self):
        x_coord = -295
        for i in range(90, 120):
            self.walls[i].goto(x=x_coord, y=295)
            x_coord += 20
    
    def create_lower_walls(self):
        x_coord = -295
        for i in range(60, 90):
            self.walls[i].goto(x=x_coord, y=-285)
            x_coord += 20
        
    def there_was_a_collision(self, snake):
        for wall in self.walls:
            if wall.distance(snake.segments[0].pos()) <= 15:
                return True
        return False 
