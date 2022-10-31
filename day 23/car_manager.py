from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self, level):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.pu()
        self.goto(x=300, y=random.randint(-230, 230))
        self.level = level

    def move_car(self):
        self.backward(self.level)



class CarManager:
    def __init__(self):
        self.cars = []
        self.level = STARTING_MOVE_DISTANCE

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -300:
                car.move_car()
            else:
                car.reset()
                car.hideturtle()
                self.cars.remove(car)

    def new_car(self):
        if random.randint(0, 5) == 1:
            new_car = Car(self.level)
            self.cars.append(new_car)

    def level_up(self):
        self.level += MOVE_INCREMENT
        for car in self.cars:
            car.level += MOVE_INCREMENT
