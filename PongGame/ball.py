import turtle

class Ball(turtle.Turtle):
    def __init__(self, speed=3):
        """You may enter the ball speed optional argument."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_moving_rate = speed
        self.y_moving_rate = speed

    def move(self):
        self.goto(x=self.xcor()+self.x_moving_rate, y=self.ycor()+self.y_moving_rate)
    
    def has_reached_a_wall(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            return True
        return False
    
    def went_out_of_bounds(self):
        if self.xcor() <=-380:
            return "left"
        elif self.xcor() >= 380:
            return "right"

    def reset_position(self):
        turtle.tracer(0)
        self.home()
        self.bounce_x()
        turtle.update()
        turtle.tracer(1)

    def has_made_contact_with_a_paddler(self, paddle_1, paddle_2):
        if (
                (self.distance(paddle_1) < 50 or self.distance(paddle_2) < 50)
                and (self.xcor() >= 330 or self.xcor() <= -330)
           ):
             return True
        return False

    def bounce_y(self):
        self.y_moving_rate *= -1

    def bounce_x(self):
        self.x_moving_rate *= -1
