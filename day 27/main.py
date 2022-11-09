from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.insert(END, string=0)
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
output_label = Label(text=0)
output_label.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

def button_clicked():
    output_label.config(text=round(int(miles_input.get())*1.609344))


calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)


window.mainloop()