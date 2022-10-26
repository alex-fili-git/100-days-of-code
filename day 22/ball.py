import turtle
from turtle import Turtle
import random
SPEED = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed_x = SPEED
        self.move_speed_y = SPEED
        self.move_speed = 0.1
        self.shape("square")
        self.color("white")
        self.pu()
        turtle.tracer(False)
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + self.move_speed_x
        new_y = self.ycor() + self.move_speed_y
        self.goto(x=new_x, y=new_y)

    def bounce(self):
        self.move_speed_y *= -1

    def hit(self):
        self.move_speed_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.hit()