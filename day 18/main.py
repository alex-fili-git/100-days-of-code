# import colorgram
# colors = colorgram.extract("hirst_painting.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
color_list = [(242, 230, 68), (184, 18, 42), (253, 235, 240), (219, 238, 244), (188, 72, 35), (16, 139, 83), (113, 180, 207), (191, 179, 21), (23, 121, 168), (24, 38, 74), (219, 60, 97), (241, 232, 2), (212, 161, 92), (75, 174, 96), (180, 44, 62), (37, 45, 112), (15, 165, 212), (220, 130, 157), (216, 71, 51), (125, 184, 123), (6, 59, 38), (166, 27, 24), (9, 94, 54), (238, 157, 178), (147, 208, 221), (5, 85, 111), (160, 212, 182), (237, 170, 163)]

brush = Turtle()
brush.pu()
turtle.colormode((255))
brush.speed("fastest")
brush.hideturtle()

def draw_hirst(width, height):
    for h in range(int(-height/2), int(height/2)):
        brush.goto(int(-width/2)*50, h*50)
        for w in range(width):
            brush.dot(20, random.choice(color_list))
            brush.forward(50)

draw_hirst(10, 10)

screen = Screen()
screen.exitonclick()