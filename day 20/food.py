from turtle import Turtle
import random
# now food class has all of the attributes of the Turtle class which now is the super class
class Food(Turtle):
    def __init__(self):
        # to get all of the attributes of super class
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)