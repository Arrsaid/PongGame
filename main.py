from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
t = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "z")
screen.onkey(l_paddle.go_down, "s")

r_board = Scoreboard((80, 220))
l_board = Scoreboard((-80, 220))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 360:
        ball.reset()
        l_board.increase_score()

    if ball.xcor() < -360:
        ball.reset()
        r_board.increase_score()

screen.exitonclick()
