
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(f"chosen word is {chosen_word}")
lives = 0
placeholder = ""
hyphen = '_'
incorrect_guess = ""
for letter in range(len(chosen_word)):
    placeholder = placeholder + hyphen
print(placeholder)

while lives < 6 and placeholder != chosen_word:
    a=-1
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        if guess not in placeholder:
            for i in chosen_word:
                a=a+1
                if i == guess:
                    placeholder = placeholder[:a] + guess + placeholder[a+1:]
                i += i
            print(placeholder)
            print(hangman_art.hangman_stages[lives])
        else:
            print(f"You have already guessed the {guess}")
    else:
        if guess not in incorrect_guess:
            lives +=1
            print(f"'{guess}' is not in the chosen word. You lose a life!")
            print(hangman_art.hangman_stages[lives])
            print(f"{6-lives} more lives left")
            incorrect_guess += guess
            if lives == 6:
                print(f"It was {chosen_word}. You Lose!")
        else:
            print(f"You have already guessed the word {guess} and it is incorrect. Please guess another alphabet")
    if placeholder == chosen_word:
        print("Congratulations! You guessed the word!")


