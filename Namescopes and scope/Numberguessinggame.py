import random
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")


def guess(computer_number, attempts):

    while attempts >= 1:
        guessed_number = input("Make a guess: ")
        if int(guessed_number) > computer_number:
            print("Too high")
        elif int(guessed_number) < computer_number:
            print("Too low")
        elif int(guessed_number) == computer_number:
            print(f"You got it.The answer was {guessed_number}")
            return True
        if attempts > 1:
            print("Guess again")
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
        else:
            print("You lose")
            return True

    return "You lose"

def set_difficulty(difficulty):
    random_number = random.randint(1, 100)
    if difficulty_level == "easy":
        print("You have 10 attempts to guess the number")
        guess(random_number, 10)
    elif difficulty_level == "hard":
        print("You have 5 attempts to guess the number")
        guess(random_number, 5)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
set_difficulty(difficulty_level)


