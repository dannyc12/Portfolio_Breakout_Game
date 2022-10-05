from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(1, 10)
        self.penup()
        self.goto(position)

    def move_right(self):
        if self.xcor() <= 300:
            self.setposition((self.xcor()+15), self.ycor())

    def move_left(self):
        if self.xcor() >= -300:
            self.setposition((self.xcor()-15), self.ycor())


