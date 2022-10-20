#create code for a coffeemachine
import resource


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def is_sufficient(choice):
    """Returns if there is enough resources in the machine."""
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if choice != "espresso" and MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True

def change(q, d, n, p, cost):
    """Returns change if enough money was inserted, else False."""
    paid = q*0.25+d*0.1+0.05*n+0.01*p
    if paid > cost:
        global money 
        money += round(paid - cost, 2)
        return round(paid - cost, 2)
    print("Sorry that's not enough money. Money refunded.")
    return False

def update_resources(choice):
    """Update amount of resources after a drink is made."""
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    resources["water"] -= MENU[choice]["ingredients"]["water"]

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

is_on = True
while is_on:
    order = input(" What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        report()
    else:
        if is_sufficient(order):
            price = MENU[order]["cost"]
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            if change(quarters, dimes, nickles, pennies, price):
                update_resources(order)
                print(f'Here is ${"{:.2f}".format(change(quarters, dimes, nickles, pennies, price))} in change.\n Here is your {order}. Enjoy!')
