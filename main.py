from turtle import *
from paddle import Paddle
from ball import Ball
import time
from bricks import BrickManager
from hud import ScoreBoard, Level, Lives, GameStatus, HighScore

screen = Screen()
screen.screensize(800, 600) # only affects the area that turtle can roam
screen.setup(800, 600) # affects actual screen dimensions
screen.bgcolor('blue')
screen.tracer(0)
paddle = Paddle((0, -280))
score_board = ScoreBoard()
level = Level()
lives = Lives()
state = GameStatus()
high_score = HighScore()

screen.listen()
screen.onkeypress(paddle.move_left, key='Left')
screen.onkeypress(paddle.move_right, key='Right')
game_on = True
ball = Ball()
bricks = BrickManager()
bricks.create_bottom_row()
bricks.create_middle_row()
bricks.create_top_row()


def next_level():
    bricks.create_bottom_row()
    bricks.create_middle_row()
    bricks.create_top_row()
    ball.move_speed *= .9


while game_on:
    time.sleep(ball.move_speed*.5)
    screen.update()
    ball.move()

    # detect wall bounce
    if ball.xcor() > 375 or ball.xcor() < -380:
        ball.bounce()

    # detect paddle hit or ceiling
    if (ball.ycor() < -260 and ball.distance(paddle) < 100) or ball.ycor() > 280:
        ball.hit()

    # detect brick hit
    # bottom row (each row has different point values
    for brick in bricks.bottom_row:
        if ball.distance(brick) <= 25:
            ball.hit()
            print(f'Struck brick at index {bricks.bottom_row.index(brick)}')
            bricks.bottom_row.remove(brick)
            brick.goto(1000, 0)
            score_board.update_score(1)

    for brick in bricks.middle_row:
        if ball.distance(brick) <= 25:
            ball.hit()
            print(f'Struck brick at index {bricks.middle_row.index(brick)}')
            bricks.middle_row.remove(brick)
            brick.goto(1000, 0)
            score_board.update_score(3)

    for brick in bricks.top_row:
        if ball.distance(brick) <= 25:
            ball.hit()
            print(f'Struck brick at index {bricks.top_row.index(brick)}')
            bricks.top_row.remove(brick)
            brick.goto(1000, 0)
            score_board.update_score(5)

    # detect miss
    if ball.ycor() < -270:
        ball.ball_reset()
        lives.update_lives()

    # detect level complete
    if len(bricks.bottom_row) == 0 and len(bricks.middle_row) == 0 and len(bricks.top_row) == 0:
        print('You beat this level')
        level.update_level()
        next_level()

    # detect game over
    if lives.lives == 0:
        state.game_over()
        game_on = False

    # detect new high score
    if score_board.score > high_score.high_score:
        new_high = score_board.score
        high_score.update_high(str(new_high))

screen.exitonclick()

