# weight = float(input("Weight: "))
# height = float(input("Height: "))

# if height > 3:
#     raise ValueError("Human height cannot be more than 3 meters")

# bmi = weight / (height **2)
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    if index > len(fruits):
        raise IndexError("List index out of range of fruits")
    fruit = fruits[index]
    print(fruit + " pie")

make_pie(4)