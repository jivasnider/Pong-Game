from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
screen.onkeypress(fun=r_paddle.up, key="8")
screen.onkeypress(fun=r_paddle.down, key="2")

ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if r_paddle.distance(ball) < 54 and ball.xcor() > 320 or ball.distance(l_paddle) < 54 and ball.xcor() < -320:
        ball.paddle_bounce()
    if ball.xcor() > 365:
        ball.reset_position()
        scoreboard.l_score_counter()
    if ball.xcor() < -365:
        ball.reset_position()
        scoreboard.r_score_counter()
    if scoreboard.l_score > 9:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("LEFT HAS WON", align="center", font=("Courier", 50, "normal"))
    if scoreboard.r_score > 9:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("RIGHT HAS WON", align="center", font=("Courier", 50, "normal"))

screen.exitonclick()
