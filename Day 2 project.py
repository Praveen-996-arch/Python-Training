print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill?"))
tip=float(input("How much tip would you like to give?10,15,12:"))
no_of_people=float(input("How many people to split the bill?"))

bill = float((total_bill*(tip/100)+total_bill)/no_of_people)
total_bill=round(bill,2)

print(f"Each person should pay: {round(bill,3)}")
print(f"Each person should pay: {total_bill}")
