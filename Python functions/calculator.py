def add(a, b):
    return  a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

Operations_list = {}
Operations_list["+"] = add
Operations_list["-"] = subtract
Operations_list["*"] = multiply
Operations_list["/"] = divide

def calculator():
    first_number = float(input("What's the first number?: "))
    first_number = round(first_number, 5)
    user_continue = 'y'
    while user_continue == 'y':
            # user_operation = input("*\n-\n*\n/\nPick an operation: ")
        for symbol in Operations_list:
                print(symbol)
        user_operation = input("Pick an operation:")
        second_number = float(input("What's the second number?: "))
        final_result = Operations_list[user_operation](first_number, second_number)
        print(f"{first_number} {user_operation} {second_number} = {round(final_result,4)}")
                # print(final_result)
        user_continue=input("Type 'y' if you want to continue with previous result. if not type 'no': ").lower()
        if user_continue == "y":
            first_number = round(final_result, 4)
        else:
            first_number = 0
            print("\n" * 20)
            calculator()

calculator()






