from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        if coffee_machine.is_resource_sufficient(menu.find_drink(choice)) and money_machine.make_payment(menu.find_drink(choice).cost):
            coffee_machine.make_coffee(menu.find_drink(choice))