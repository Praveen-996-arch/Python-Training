import random
word_list = ["aardvark", "baboon", "camel", "elephant"]
chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
hyphen = '_'
for letter in range(len(chosen_word)):
    placeholder = placeholder + hyphen

print(placeholder)

while(placeholder != chosen_word):
    a=-1
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for i in chosen_word:
            a=a+1
            if i == guess:
                placeholder = placeholder[:a] + guess + placeholder[a+1:]
            i += i
        print(placeholder)
    count = chosen_word.count(guess)
    print(f"number of {guess} in {chosen_word} are {count}")
print("Congratulations! You guessed the word!")

