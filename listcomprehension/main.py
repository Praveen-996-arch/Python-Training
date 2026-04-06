# numbers = [ 1 ,2 , 3, 5]
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Manasa"
# new_name = [letter for letter in name]
# print(new_name)

# range_list = [n+2 for n in range(1,5)]
# print(range_list)

names = ["Manu", "Praveen", "Isha"]
new_names = [name.upper() for name in names if len(name)==4]
print(new_names)