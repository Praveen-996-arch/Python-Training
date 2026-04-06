
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    checkmark.config(text = "")
    timer_label.config(text = "Timer", fg = GREEN)
    reps = 0
   
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = 1 * 60
    short_break_sec = 1* 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
   
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        countdown(work_sec)
        timer_label.config(text = "Work", fg = GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        if reps == 2:
            checkmark.config(text = "✔")
        elif reps == 4:
            checkmark.config(text = "✔✔")
        elif reps == 6:
            checkmark.config(text = "✔✔✔")
        countdown(short_break_sec)
        timer_label.config(text = "Short Break", fg = PINK)
    elif reps == 8:
        countdown(long_break_sec)
        timer_label.config(text = "Long Break", fg = RED)
       

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:  
        timer = window.after(1000,countdown, count -1)
    else:
        start_timer()
        


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
window.config(padx = 100, pady = 50,bg= YELLOW)


#Label
timer_label = Label(text = "Timer",font=(FONT_NAME, 40,"normal"),bg= YELLOW,fg = GREEN) 

timer_label.grid(row = 0, column = 1)

#canvas

canvas = Canvas(width = 200, height = 230,bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "/Users/manasapola/PycharmProjects/Basicsofpython/pomodoro/tomato.png")
canvas.create_image(100,112, image= tomato_img )
timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME, 32,"bold"),fill = 'white')

canvas.grid(row = 1, column = 1)


#checkmark
checkmark = Label( fg = GREEN , bg = YELLOW)
checkmark.grid(row=3,column = 1 )


# button
start_button = Button(text = "Start", highlightbackground = YELLOW,command = start_timer)
start_button.grid(row = 2, column =0)

reset_button = Button(text = 'Reset', highlightbackground= YELLOW, command = reset_timer)
reset_button.grid(row = 2, column = 2)





window.mainloop()
