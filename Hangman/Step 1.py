import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
#chosen_word = list(chosen_word)
#length_of_chosen_word = len(chosen_word)
#print(length_of_chosen_word)

# for i in range(length_of_chosen_word):
#     guess = input("Guess a letter:\n")
#     guess = guess.lower()
#     print(guess)
#     if guess in chosen_word:
#         print("Right")
#     else:
#         print("Wrong")
#
# print("You have entered the enough letters. Please try again")

guess = input("Guess a letter:\n")
guess = guess.lower()
i=0
# for i in range(length_of_chosen_word):
#     if guess == chosen_word[i]:
#         print("Right")
#     else:
#         print("Wrong")
#     i += 1

## without converting string to list

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

