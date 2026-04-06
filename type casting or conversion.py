#Type casting or conversion : Converting one data type to another data type
# Converts strings to int value
print(int("123")+int("456"))
#Converts strings to float and int value
print(float("34.67")+ int("123"))

print(bool("2"))

name_of_user=input("Enter your name")
length_of_name=len(name_of_user)
#String cannot be concatenated with int, hence the int is converted to string
print("Number of letters in your name: " + str((length_of_name)))
