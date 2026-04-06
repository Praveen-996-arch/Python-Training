import random

random_integer = random.randint(1, 10)
print(random_integer)

if random_integer > 2:
    print("Heads")
else:
    print("Tails")

random_number_o_to_1 = random.random()
print(random_number_o_to_1)

if random_number_o_to_1 < 1:
    print("Heads")
else:
    print("Tails")

random_float_number1 = random.uniform(1,3)
print(random_float_number1)

if random_float_number1 < 3:
    print("Heads")
else:
    print("Tails")