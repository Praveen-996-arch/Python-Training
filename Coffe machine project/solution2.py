import main

# TODO: 1. Prompt the user by asking "What would you like

def resources_limit():
    if main.resources["water"] >= main.MENU[user_prompt]["ingredients"]["water"]:
        if main.resources["coffee"] >= main.MENU[user_prompt]["ingredients"]["coffee"]:
            if user_prompt != "espresso":
                if main.resources["milk"] >= main.MENU[user_prompt]["ingredients"]["milk"]:
                    process_coins()
                else:
                    print("Sorry there is not enough milk")
                    return True
            else:
                process_coins()
        else:
            print("Sorry there is not enough coffee")
    else:
        print("Sorry there is not enough water")
        return True
def process_coins():

            print(f"You have selected {user_prompt}. Please pay {main.MENU[user_prompt]["cost"]}")
            print("Please insert coins.")
            quarters = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickles = int(input("How many nickles?:"))
            pennies = int(input("How many pennies?:"))
            total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            print(f"total amount paid = {round(total_amount,2)}")
            transaction_successful(total_amount)

def transaction_successful(total_amount):
        if main.MENU[user_prompt]["cost"] == total_amount:
            print(f"Please enjoy your {user_prompt}")
            check_resources(milk_limit, coffee_limit, water_limit,total_amount)
        elif main.MENU[user_prompt]["cost"] > total_amount:
            print("Sorry there is not enough money. Money refunded")
            return True
        elif main.MENU[user_prompt]["cost"] < total_amount:
            exchange = total_amount - main.MENU[user_prompt]["cost"]
            if main.resources["money"] >= exchange:
                print(f"Please take the remaining {round(exchange,2)}")
            else:
                print("Sorry there is not enough change to return. Please enter the right amount or visit again")
                return True
            print(f"Please enjoy your {user_prompt}")
            check_resources(milk_limit, coffee_limit, water_limit,total_amount)
            return True


def check_resources(milk_limit, coffee_limit, water_limit,total_amount):
    main.resources["water"] = main.resources["water"] - water_limit
    main.resources["coffee"] = main.resources["coffee"] - coffee_limit
    if user_prompt != "espresso":
        main.resources["milk"] = main.resources["milk"] - milk_limit
    main.resources["money"] += total_amount
    # print(main.resources)


user_prompt = "report"

while user_prompt != "off":

    user_prompt=input("What would you like?(espresso/latte/cappuccino)")
    if user_prompt == "off":
        print("Machine is turning off")
        break
    elif user_prompt == "report":
        print(main.resources)
    elif user_prompt == "espresso" or user_prompt == "latte" or user_prompt == "cappuccino":
        coffee_limit = main.MENU[user_prompt]["ingredients"]["coffee"]
        water_limit = main.MENU[user_prompt]["ingredients"]["water"]
        if user_prompt != "espresso":
                milk_limit = main.MENU[user_prompt]["ingredients"]["milk"]
        else:
            milk_limit = 0
        resources_limit()
    print("\n"*20)


