import tkinter

window = tkinter.Tk()
window.title("Top bar title")
# set the size to the minimum but client can sitll alter the size
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
# automatically center the variable on the screen with pack method
my_label.pack(side="left")

window.mainloop()

# function arguments
# # positional arguments
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

# # unlimited arguments based on name: keyword arguments
# # this gives a dictionary representing kwargs
def calculate(n, **kwargs):
    for key,value in kwargs.items():
        print(key)
        print(value)
    # or get values by
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

class Car:
    #we can create a class with kwargs ourself, with the get method we don't get an error if name does not exist.
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
