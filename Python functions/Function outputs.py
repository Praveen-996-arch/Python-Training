
f_name = input("Please enter your first name: ")
l_name = input("Please enter your last name: ")
def format_name(firstname, lastname):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs"
    firstname = firstname.title()
    lastname = lastname.title()
    return f"{firstname} {lastname}"

def full_name(firstname, lastname):
    full_name = f"{firstname} {lastname}"
    return full_name
    print("\n" + firstname + " " + lastname)

output=format_name(f_name,l_name)
print(output)
# output2 = full_name(output.range(0,5),output.range(7,10))
# print(output2)




