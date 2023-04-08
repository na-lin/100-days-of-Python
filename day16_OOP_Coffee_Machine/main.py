from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

# TODO: how to install a file include class and import it to create a object from the class
# NEW: use lowercase same as py file name to object is ok
# coffee_maker = CoffeeMaker() , instead of object_make_coffee = CoffeeMaker()
# menu = Menu() instead of object_menu = Menu()
# money_machine = MoneyMachine() instead of object_money
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    # TODO: ask use to order
    # order_string = "What would you like? " + '(' + object_menu.get_items() + "): "
    # choice = input(order_string).lower()
    # NEW : input also can use f-string as a prompt
    option = menu.get_items()
    choice = input(f"What would you like? ({option}):")

    # TODO: Turn off when prompt "off"
    if choice == "off":
        is_on = False

    # TODO: Print report  : coffeeMaker.report + MoneyMachine.report
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        # if drink is not exist, print hint for not available
        # if drink is exist ,return a MenuItem object, coffee_name = MenuItem()
        drink = menu.find_drink(choice)
        if drink is not None:
            # TODO: check resources sufficient : CoffeeMaker.is_resource_sufficient
            # argument = MenuItem , return True or False
            is_sufficient = coffee_maker.is_resource_sufficient(drink)
            # NEW: combine is_sufficient and is_payment_enough is one if statement
            if is_sufficient:
                # TODO: process coin : MoneyMachine.make_payment
                # argument = MenuItem.cose , return True or False
                # cost = drink.cost
                is_payment_enough = money_machine.make_payment(drink.cost)
                if is_payment_enough:
                    # TODO: make coffee : CoffeeMaker.make_coffee
                    coffee_maker.make_coffee(drink)
