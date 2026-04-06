import menu

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Created a object for the classes in the above package
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
coffee_menu = Menu()

def order_a_drink(user_prompt):
# user_prompt = "report"
    while user_prompt != "off":
        user_prompt=input("What would you like?(espresso/latte/cappuccino)").lower()
        if user_prompt == "off":
            print("Machine is turning off")
            break
        elif user_prompt == "report":
            report = coffeeMaker.report()
            moneyMachine.report()
        elif user_prompt in coffee_menu.get_items():
            find_a_drink = coffee_menu.find_drink(user_prompt)
            is_resource_sufficient = coffeeMaker.is_resource_sufficient(find_a_drink)
            if is_resource_sufficient:
                print(f"Price of {user_prompt} is {find_a_drink.cost}")
                payment= moneyMachine.make_payment(cost=find_a_drink.cost)
            #Checking if the payment made is less than the drink cost
                if payment:
                    coffeeMaker.make_coffee(find_a_drink)
                    coffeeMaker.report()
                    moneyMachine.report()

order_a_drink("on")
print("testing")






