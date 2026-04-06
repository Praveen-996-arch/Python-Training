

from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

data = pd.read_csv(filepath_or_buffer = "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/data/french_words.csv")
list_of_words = pd.DataFrame.to_dict(data,orient='records')
random_word = {}
known_words = []
updated_list = []


#Generate a random french word
def generate_french_word():
    global random_word,flip_timer
    windows.after_cancel(flip_timer)
    random_word = rd.choice(list_of_words)
    print(random_word)
    canvas.itemconfig(canvas_image,image = flashcard_image)
    canvas.itemconfig(title_text ,text = "French",fill = "black")                              
    canvas.itemconfig(word_text ,text = random_word["French"],fill = "black")
    flip_timer=windows.after(3000,generate_english_word)
    
    
def generate_english_word():
    
    canvas.itemconfig(canvas_image,image = englishcard_image)
    canvas.itemconfig(title_text,fill = "white",text = "English")
    canvas.itemconfig(word_text,fill = "white",text = random_word["English"])

def updated_list():
    list_of_words.remove(random_word)
    pd.DataFrame(list_of_words).to_csv( "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/data/words_to_learn.csv", index = False)
    generate_french_word()
  

windows = Tk()
windows.title("Flash")
windows.config(padx = 50, pady = 50,bg = BACKGROUND_COLOR)
flip_timer = windows.after(3000,generate_english_word)

canvas = Canvas(width = 800, height = 526,bg = BACKGROUND_COLOR,highlightthickness=0)
flashcard_image = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/images/card_front.png")
englishcard_image = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/images/card_back.png")
canvas_image = canvas.create_image(400,263,image = flashcard_image)
title_text = canvas.create_text(400,150,text = "", font = (FONT_NAME, 40, "italic") )
word_text = canvas.create_text(400,263,text = "", font = (FONT_NAME, 60, "bold") )
canvas.grid(row = 0, column=0,columnspan=2)

#right button
button1 = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/images/right.png")
right_image = Button(image=button1,highlightthickness=0,command = updated_list)
right_image.grid(row=1, column = 1)

#wrong button

button2 = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/flasprojectstart/images/wrong.png")
wrong_image = Button(image=button2,highlightthickness=0,command = generate_french_word)
wrong_image.grid(row=1, column = 0)

generate_french_word()





windows.mainloop()

