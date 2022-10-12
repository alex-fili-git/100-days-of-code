print("Welcome to the tip calculator.")
total_cost = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
no_people = input("How many people to split the bill? ")
pay_per_person = round(float(total_cost) * (1+int(tip)/100) / int(no_people), 2)
print(f'Each person should pay : ${"{:.2f}".format(pay_per_person)}')