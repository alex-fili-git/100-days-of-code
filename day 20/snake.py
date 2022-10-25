from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.pu()
            new_square.goto(x=i * -20, y=0)
            self.snake.append(new_square)

    def extend(self):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.pu()
        new_square.goto(self.snake[-1].position())
        self.snake.append(new_square)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            self.snake[segment].goto(self.snake[segment - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
