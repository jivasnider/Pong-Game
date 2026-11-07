from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcord_start = 10
        self.ycord_start = 10
        self.move_speed = 0.04

    def move(self):
        x_cord = self.xcor() + self.xcord_start
        y_cord = self.ycor() + self.ycord_start
        self.goto(x_cord, y_cord)

    def bounce_wall(self):
        self.ycord_start *= -1

    def paddle_bounce(self):
        self.xcord_start *= -1
        self.move_speed *= 0.75

    def reset_position(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.move_speed = 0.1