try:
    year = int(input("Please enter a year: "))
except ValueError:
    print("Please enter a valid year")
    year = int(input("Please enter a year: "))


if year > 1989 and year < 1994:
    print("You are millenial")
else:
    if year > 1994:
        print("You are a Genz")