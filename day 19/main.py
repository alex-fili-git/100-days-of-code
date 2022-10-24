#listening to screen events; listening to what user does
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
start = -175
for color in colors:
    start += 50
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.pu()
    new_turtle.color(color)
    new_turtle.goto(x=-230,y=start)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()