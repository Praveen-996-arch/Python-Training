# print("Welcome to the rollercoaster!")
# height= int(input("What is your height?"))
# #if else condition
# if height >= 40:
#     print("You can ride the rollercoaster")
# else:
#     print("You cant ride the rollercoaster")

# Comparison operators = <,>,<=,>=,==,!=,%

# user_input=int(input("Please enter a number:"))
# if user_input%2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

#Nested if/else
# print("Welcome to the rollercoaster!")
# height= int(input("What is your height?"))
# age=int(input("Please enter your age"))
# if height >= 40:
#     if age <= 12:
#         print("You can ride the rollercoaster")
#     else:
#         print("You cannot ride the rollercoaster")
# else:
#     print("You cant ride the rollercoaster")

#if/elif/else

# print("Welcome to the rollercoaster!")
# height= int(input("What is your height?"))
# age=int(input("Please enter your age"))
# if height >=120:
#     if age <12:
#         print("Please pay 5$")
#     elif age >=12 and age <=18:
#         print("Please pay 10$")
#     else:
#         print("Please pay 15$")
# else:
#     print("You cannot ride rollercoaster")

# Multiple if
print("Welcome to the rollercoaster!")
height= int(input("What is your height?"))
age=int(input("Please enter your age"))
if height >=120:
    if age <12:
        bill=5
        print("Please pay 5$")
    elif age >=12 and age <=18:
        bill=7
        print("Please pay 10$")
    else:
        bill=12
        print("Please pay 15$")
    if input("Do you want photos") == 'Yes':
        print(f"Total bill is {bill+3} $")
    else:
        print("Thankyou")
else:
    print("You cannot ride rollercoaster")

