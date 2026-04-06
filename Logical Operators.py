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
    elif age >= 18 and age <45:
        bill=12
        print("Please pay 15$")
    elif age >=45 and age <= 55:
        bill=0
        print("Payment is not needed")
    else:
        bill = 12
        print("Adult tickets are 12$")

    if input("Do you want photos") == 'Yes':
        print(f"Total bill is {bill + 3} $")
    else:
        print("Thankyou")
else:
    print("You cannot ride rollercoaster")