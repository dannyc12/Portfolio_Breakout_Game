from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-150, 250)
        self.score = 0
        self.update_score(0)

    def update_score(self, points):
        self.clear()
        self.score += points
        self.write(f'Score: {self.score}', align='left', font=FONT)


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(50, 250)
        self.level = 1
        self.show_level()

    def show_level(self):
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f'Level: {self.level}', align='left', font=FONT)


class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-350, -250)
        self.lives = 3
        self.show_lives()

    def show_lives(self):
        self.write(f'Lives: {self.lives}', align='left', font=FONT)

    def update_lives(self):
        self.clear()
        self.lives -= 1
        self.write(f'Lives: {self.lives}', align='left', font=FONT)


class GameStatus(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-80, 0)

    def game_over(self):
        self.write('Game Over', align='left', font=FONT)


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(75, -250)
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.show_high()

    def show_high(self):
        self.write(f'High Score: {self.high_score}', align='left', font=FONT)

    def update_high(self, score):
        with open('data.txt', 'w') as data:
            data.write(score)



