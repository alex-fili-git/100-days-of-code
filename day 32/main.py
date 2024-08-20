##################### Extra Hard Starting Project ######################
import smtplib
from random import choice
import datetime as dt
import pandas as pd

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birthdays = pd.read_csv("birthdays.csv", header=0)
for index, person in birthdays.iterrows():
    if person.month == dt.datetime.now().month and person.day == dt.datetime.now().day:
        letter = choice(letters)
        with open(f"letter_templates/{letter}") as file:
            email = file.read()
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user="asm.notifier@gmail.com", password="qypnyz-curcu9-xeDdom")
            connection.sendmail(from_addr="asm.notifier@gmail.com", to_addrs="emailsenderday32@yahoo.com",
                                msg=f"Subject:Happy Birthday\n\n{email.replace('[NAME]', person.nameperson)}")




