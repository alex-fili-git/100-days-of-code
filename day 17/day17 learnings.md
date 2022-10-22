# Creating Classes
A class is a blueprint for creating an object.
To set up class: define with 'class'. To leave a class empty use 'pass'.
PascalCase : naming such that all have first letter cap, used for classes.
camelCase
snake_case : used for everything else

Constructor is a part of the blueprint that helps to specify object. Also known as 
initializing. to do this:

class: Car:
    def __init__(self):
    #initialise attributes
you can add parameters to your classes
class Car:
    def __init__(self, seats):
        self.seats = seats
now you define an object by Car(5)
but by defining that parameters should be included in call function. It must be parsed.

Add methods:
class Car:
    def enter_race_mode(self):
        self.seats = 2
Now with 'mycar.enter_race_mode()' seats are changed to 2

With the keyword 'self' in a function, the function knows to alter the value of object self
