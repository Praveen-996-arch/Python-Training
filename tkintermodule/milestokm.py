from tkinter import *

window = Tk()
window.minsize(height = 200, width = 350)
window.title("Mile to Km Converter")

#entry

def button_clicked():
    mile_value = float(input.get())
    print(mile_value)
    km_value =  mile_value * 1.609
    my_label3.config(text = km_value)

input = Entry(width = 5)
input.grid(row = 1, column = 2)


#label
#Miles
my_label = Label(text = "Miles")
my_label.grid(row = 1, column = 3)

#is_equal_to
my_label2 = Label(text = "is equal to")
my_label2.grid(row = 2, column = 1)
#km value
my_label3 = Label(text = "0")
my_label3.grid(row = 2, column = 2)
#Km
my_label4 = Label(text = "Km")
my_label4.grid(row = 2, column = 3)

#calculate Button

calculate = Button(text="Calculate", command = button_clicked)
calculate.grid(row = 3, column = 2)




window.mainloop()

