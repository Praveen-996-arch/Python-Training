from tkinter import *

window = Tk()
window.title("Hello World")
window.minsize(width=400, height=300)

def say_hello():
    print("Hello!")

button = Button(text = 'Click Me',width = 10, bg = 'blue', fg = 'black',command = say_hello)
button.config(text = 'Print')
button.pack()



window.mainloop()