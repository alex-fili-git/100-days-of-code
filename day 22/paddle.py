from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.pu()
        if side == "left":
            self.goto(x=-400, y=0)
        else:
            self.goto(x=400, y=0)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)