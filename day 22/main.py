import turtle
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
import time
from ball import Ball


def draw_middle_line():
    middle_line = Turtle("square")
    middle_line.hideturtle()
    middle_line.color("white")
    middle_line.pensize(5)
    middle_line.pu()
    middle_line.goto(x=0, y=280)
    middle_line.setheading(270)
    middle_line.pd()
    for i in range(-280, 280, 20):
        middle_line.forward(10)
        middle_line.pu()
        middle_line.forward(10)
        middle_line.pd()


screen = Screen()
screen.setup(width=900,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
draw_middle_line()


scoreboard = Scoreboard()
player1 = Paddle(side="left")
player2 = Paddle(side="right")
ball = Ball()

screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # detect score
    if ball.xcor() > 450:
        scoreboard.update(2)
        ball.reset_position()
    elif ball.xcor() < -450:
        scoreboard.update(1)
        ball.reset_position()

    # detect collision with paddle
    if -410 < ball.xcor() < -380 and ball.distance(player1) < 50 or 410 > ball.xcor() > 380 and ball.distance(player2) < 50:
        ball.hit()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()



screen.exitonclick()
