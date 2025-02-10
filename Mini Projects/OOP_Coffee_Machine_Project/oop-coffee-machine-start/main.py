from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)

#constructing objects!
demora_money_machine = MoneyMachine()
demora_coffee_maker = CoffeeMaker()
demora_menu = Menu()

#check for machine and case foe while loop
is_machine_on = True

#while loop for machine!
while is_machine_on:
    order = input("Welcome to Demora's Cafe! What would you like to Order? Select between 'Espresso', 'Latte' or 'Cappuccino': ").lower()
    if order == "report": #secret button to check items and cash by admin
        demora_money_machine.report()
        demora_coffee_maker.report()
    elif order == "off": #secret button to close by admin
        is_machine_on = False
        break
    else:
        drink = demora_menu.find_drink(order)
        if drink:
            if demora_coffee_maker.is_resource_sufficient(drink):
                if demora_money_machine.make_payment(drink.cost):
                    demora_coffee_maker.make_coffee(drink)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
            else:
                print("Sorry, there aren't enough resources to make this drink.")
        else:
            print("Sorry, that drink is not on the menu.")
