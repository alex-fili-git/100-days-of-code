import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", mode='r') as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No details for the website exists")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email/username: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="No details for the website exists")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_ = website_entry.get()
    password_ = password_entry.get()
    email = user_entry.get()
    new_data = {
        website_: {
            "email": email,
            "password": password_
        }
    }

    if len(password_) == 0 or len(website_) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open("data.json", mode='w') as f:
                json.dump(data, f, indent=4)
                # for txt files f.write(f"{website_} | {email} | {password_}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# logo
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:")
website.grid(column=0, row=1)
user = Label(text="Email/Username:")
user.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "alex@mail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)
add = Button(text="Add", command=save_password, width=36)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", command=search, width=13)
search.grid(column=2, row=1)



window.mainloop()