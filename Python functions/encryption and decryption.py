
import ceaser_logo
print(ceaser_logo.logo)
print(ceaser_logo.logo2)
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def caesar(original_text, shift_amount,direction):
    cipher_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for letter1 in original_text.upper():
        if letter1 in alphabets:
            index_of_letter1 = alphabets.index(letter1)
            shifted_position = index_of_letter1 + shift_amount
            shifted_position %= len(alphabets)
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter1
    if direction == 'encode':
        print(f"Here's the encoded result: {cipher_text.lower()}")
    elif direction == 'decode':
        print(f"Here's the decoded result: {cipher_text.lower()}")

def variables():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("Please enter a text: \n")
    shiftcount = int(input("Please enter the amount to be shifted: \n"))
    caesar(original_text=text,shift_amount=shiftcount,direction=direction)

def main(response):
    while response == 'yes':
        variables()
        response = input("Type 'yes' if you want to go again.Otherwise, type 'no'\n")

main("yes")






