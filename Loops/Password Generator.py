import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")
nr_letters= int(input("Enter number of letters: "))

nr_symbols = int(input("Enter number of symbols: "))
nr_numbers = int(input("Enter number of numbers: "))
initial_password = nr_letters + nr_symbols + nr_numbers
length=int(input("Enter length of password: "))
if initial_password <= length:
    print(f"length of the password is {length}")
    password = []
    final_password=""
    for i in range(0,nr_letters):
        password += random.choice(letters)
    for j in range(0,nr_symbols):
        password += random.choice(symbols)
    for k in range(0,nr_numbers):
        password += random.choice(numbers)

    print(password)
    print(final_password.join(password))
    (random.shuffle(password))
    print(final_password.join(password))

else:
    print("Length doesnt match with the individual count entered")



