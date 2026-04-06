with open("/Users/manasapola/PycharmProjects/Basicsofpython/Mail_merge/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    letter_contents = letter_contents.replace("Angela", "Manasa")

# Strip() method is used to remove any extra spaces or newline characters from the names read from the file. This ensures that when we replace the placeholder in the letter with the name, it doesn't include any unwanted whitespace or newline characters that could affect the formatting of the final letter.
with open("/Users/manasapola/PycharmProjects/Basicsofpython/Mail_merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  
    for name in names:
        name = name.strip("\n")
        new_letter = letter_contents.replace("[name]", name)
        with open(f"/Users/manasapola/PycharmProjects/Basicsofpython/Mail_merge/Output/ReadytoSend/letter_for_{name}.docx", mode = 'w') as new_letter_file:
            new_letter_file.write(new_letter)