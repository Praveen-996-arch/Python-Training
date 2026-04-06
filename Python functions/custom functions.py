# def greet():
#     print("Hello World")
#     print("How r you")
#
#
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")
#
# greet_with_name(123)

# def greet_with(name, location):
#     print(f"Hello {name}!.\nHow it is like in {location}?")
#
# greet_with("Jack", "Florida") #default way of calling parameters

#Keyword Arguments - To make sure that correct argument is assigned to correct parameter

def greet_with(name, location):
    print(f"Hello {name}!.\nHow it is like in {location}?")

greet_with(name = "Jack", location = "Florida")
greet_with(location = "Alabama", name = "David")

