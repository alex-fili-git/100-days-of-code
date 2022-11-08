# GUI with TKinter
Create a pop-up for running the program such that it is easy to interpret.
mainloop has always to be at the bottom to keep window running.
With tkinter you first have to create a variable and then specify how it will be displayed.


# function arguments
Default arguments and *Args and **Kwargs this comes down to advanced arguments.
Keyword arguments can be called in any order (def my_function(a,b,c) -> my_function(a=1,c=2,b=3))
Arguments with default values preset the values of a,b,c such that you don't have to alter them.
Now def my_function(a=1,c=2,b=3) -> my_function() (no inputs needed, but can create custom values by altering 1 value)

## *args
Functions that can take any number of arguments. The asteriks is the important part. Arguments are in the form of tuple.
def add(*args):
    for n in args:
        do something with all n arguments

## **kwargs
Creates a dictionary.