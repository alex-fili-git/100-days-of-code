# Class inheritance
# Copy behavior from a parent class
# class Fish:
#     def __init__(self):

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")
#to inherit a class add parentheses after name of class
# and provide class you want to inherit from
class Fish(Animal):
    def __init__(self):
        super().__init__() #to get hold of everything an Animal is and can do

    def breathe(self):
        super().breathe() #now we will do everything the super class can do
        #but we can add now
        print("Doing it underwater.")

nemo = Fish()
nemo.breathe()

# slicing lists, works also for tuple
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
# [num1:num2:stepsize]
piano_keys[2:5:2] # -> ["c", "e"]
piano_keys[::2] # -> every second item: ["a", "c", "e", "g"]
piano_keys[::-1] # -> reverses list
