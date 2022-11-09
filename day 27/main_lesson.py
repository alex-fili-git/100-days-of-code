from tkinter import *

window = Tk()
window.title("Top bar title")
# set the size to the minimum but client can sitll alter the size
window.minsize(width=500, height=300)

# label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# automatically center the variable on the screen with pack method
my_label.pack()
# you can change or update your input
my_label["text"] = "New"
my_label.config(text="New text")
# button
def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click here", command=button_clicked)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



window.mainloop()

# # function arguments
# # # positional arguments
# def add(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result
#
# # # unlimited arguments based on name: keyword arguments
# # # this gives a dictionary representing kwargs
# def calculate(n, **kwargs):
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     # or get values by
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#
# calculate(2, add=3, multiply=5)
#
# class Car:
#     #we can create a class with kwargs ourself, with the get method we don't get an error if name does not exist.
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
