from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.x_move = 5
        self.y_move = 5
        self.penup()
        self.move_speed = .02

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def ball_reset(self):
        self.goto(0, 0)

    def bounce(self):
        # change x direction when ball strikes wall
        self.x_move *= -1

    def hit(self):
        # change y direction when ball strikes paddle or brick
        self.y_move *= -1
        self.move_speed *= .95
