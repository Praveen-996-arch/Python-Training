programming_dictionary = {
    "Bug": "A bug is a mistake or error in a program",
    "Function": "A function is a block of reusable code that performs a specific task",
    "c": "d", }

#print(programming_dictionary[])

programming_dictionary["Loop"] = True
#Redefining the existing key value
programming_dictionary["Loop"] = "A loop is used to repeat a block of code multiple times."
print(programming_dictionary)

for key in programming_dictionary:
    print(f"{key[0]} : {programming_dictionary[key]}")
    # print(programming_dictionary[key])

# when user want to empty dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# empty_dictionary = {}
#
# print(empty_dictionary)