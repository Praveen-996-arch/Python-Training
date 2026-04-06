print("Welcome to python pizza deliveries")
pizza_size=input("What size pizza do you want? S, M or L")
#pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
#extra_cheese = input("Do you want extra cheese? Y or N: ")
small_pizza_bill = 15
medium_pizza_bill = 20
large_pizza_bill = 25
P_small_pizza = 2
P_medium_pizza = 3
c_small_pizza = 1
if pizza_size == 'S':
    print(f"Total bill is {small_pizza_bill}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
    if pepperoni == 'Y':
        small_pizza_bill = small_pizza_bill + P_small_pizza
        print(f"Total bill is {small_pizza_bill}")
    else:
        print("No pepperoni needed")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        small_pizza_bill +=1
        print(f"Total bill is {small_pizza_bill}")
    else:
        print("No extra_cheese needed")
elif pizza_size == 'M':
    print(f"Total bill is {medium_pizza_bill}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
    if pepperoni == 'Y':
        medium_pizza_bill += 3
        print(f"Total bill is {medium_pizza_bill}")
    else:
        print("No pepperoni needed")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        medium_pizza_bill += 1
        print(f"Total bill is {medium_pizza_bill}")
    else:
        print("No extra_cheese needed")
elif pizza_size == 'L':
    print(f"Total bill is {large_pizza_bill}")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
    if pepperoni == 'Y':
        large_pizza_bill += 3
        print(f"Total bill is {large_pizza_bill}")
    else:
        print("No pepperoni needed")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        large_pizza_bill += 1
        print(f"Total bill is {large_pizza_bill}")
    else:
        print("No extra_cheese needed")
else:
    print("Total bill")
# if pepperoni == 'Y':
#         small_pizza_bill = small_pizza_bill+P_small_pizza
#         print(f"Total bill is {small_pizza_bill}")
#         medium_pizza_bill += 3
#         print(f"Total bill is {medium_pizza_bill}")
#         large_pizza_bill += 3
#         print(f"Total bill is {large_pizza_bill}")
# else:
#         print("No pepperoni needed")


    # if extra_cheese == 'Y':
    #         total_bill = (small_pizza_bill + P_small_pizza + c_small_pizza)
    #     print(f"total bill is {total_bill}")
    #
    # elif pizza_size == 'M':
    #     if pepperoni == 'N':
    #         if extra_cheese == 'Y':
    #             total_bill = (medium_pizza_bill + P_medium_pizza + c_small_pizza)
