import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#print(Rock)
RPS= [ Rock, paper, scissors]
#print(RPS[1])
#print(RPS)
#print(random.choice(RPS))
#print(RPS[random_index])
#user_input
user_input=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
print(user_input)
user_input = int(user_input)
if user_input >=0 and user_input <=2:
  print(RPS[user_input])
#compute_input
random_index = random.randint(0 ,2)
print("computer chose:")
print(random_index)
computer_input = print(RPS[random_index])
# #print(computer_input)
if user_input == 0 and random_index == 2:
    print("You win!")
elif user_input == 2 and random_index ==1:
    print("You win!")
elif user_input == 1 and random_index == 0:
    print("You win!")
elif user_input == random_index:
    print("Match is draw")
elif user_input != 0 or user_input != 1 or user_input != 2:
    print("Please enter a valid number")
else:
    print("You lose!")

