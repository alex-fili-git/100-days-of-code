# from turtle import Turtle, Screen
# #now we have an object called Timmy of class Turtle
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
# timmy.forward(100)
#
# #from timmy get its attribute
# my_screen = Screen()
# #continue running until click which exits
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)