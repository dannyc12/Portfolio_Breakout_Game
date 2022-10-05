from turtle import Turtle


class BrickManager:

    def __init__(self):
        self.bottom_row = []
        self.middle_row = []
        self.top_row = []
        self.bottom = 100
        self.middle = 150
        self.top = 200

    def create_bottom_row(self):
        for i in range(11):
            brick = Turtle('square')
            brick.color('yellow')
            brick.penup()
            brick.shapesize(1, 3.1)
            brick.setposition(-355 + i*70, self.bottom)
            self.bottom_row.append(brick)

    def create_middle_row(self):
        for i in range(11):
            brick = Turtle('square')
            brick.color('green')
            brick.penup()
            brick.shapesize(1, 3.1)
            brick.setposition(-355 + i*70, self.middle)
            self.middle_row.append(brick)

    def create_top_row(self):
        for i in range(11):
            brick = Turtle('square')
            brick.color('red')
            brick.penup()
            brick.shapesize(1, 3.1)
            brick.setposition(-355 + i*70, self.top)
            self.top_row.append(brick)



