import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(width=500, height=300)
window.config(padx=20, pady = 20)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="Another Text")
my_label.grid(row = 0, column=0)

#Buttons


button = tkinter.Button(text="Click Me", command = button_clicked)
button2 = tkinter.Button(text = "Second button", comman = button_clicked)
# button.pack()
button.grid(row=1,column=1)
button2.grid(row =0, column = 2)

#Entry


input = tkinter.Entry(width=10)#get the text from the entry widget and set it to the label
# input.pack()
input.grid(row=2,column=3)

#text
text = tkinter.Text(height = 5, width = 30)
#Puts cursor in textbox.

text.insert(tkinter.END,chars ="Enter a text of 2000 characters")
# text.pack()
# text.place(x=100,y=200)
# text.grid(column=0,row=3)

print(text.get("1.0",tkinter.END))

#spinbox

def spinbox_used():
    print(spinbox.get())
    
spinbox = tkinter.Spinbox(from_= 0,to=10,width=10, command=spinbox_used)
# spinbox.pack(side= 'left')


#checkbutton
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Option1",variable = checked_state)
checked_state.get()
print(checked_state.get())
# checkbutton.pack()

#Radiobutton
checked_state1 = tkinter.IntVar()

radiobutton = tkinter.Radiobutton(text = "Radio1",value =1,variable = checked_state1)
radiobutton2 = tkinter.Radiobutton(text = "Radio2",value =2,variable = checked_state1)
print(checked_state1.get())
# radiobutton.pack()
# radiobutton2.pack()

#Listbox

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height = 4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()






window.mainloop()