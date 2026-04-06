from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

website_value =0
email_value =0
pwd_value =0
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]


    random.shuffle(password_list)

    #converting list to string using join() method

    password = "".join(password_list)

    pwd_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_value = website.get()
    email_value = email.get()
    pwd_value = pwd_entry.get()
    new_data = {
        website_value:
        {
            "Email" : email_value,
            "Password": pwd_value
        }
    }

    if len(website_value) == 0:
        messagebox.showwarning(title = "Warning", message = f"Please fill in all the mandatory fields. Website is missing")
    elif len(email_value) == 0:
        messagebox.showwarning(title = "Warning", message = f"Please fill in all the mandatory fields. Email is missing")
    elif len(pwd_value) == 0:
        messagebox.showwarning(title = "Warning", message = f"Please fill in all the mandatory fields. Password is missing")
    else:
        is_ok = messagebox.askokcancel(title=  website_value,message = f"These are the details entered: \n Email: {email_value}\n Password: {pwd_value}.\n Do you wish to continue?")
        if is_ok:
            try:
                with open("/Users/manasapola/PycharmProjects/Basicsofpython/password manager/password-manager-start/data.json", mode = 'r') as data_file:
                    data = json.load(data_file)        
                   
            except FileNotFoundError:
                with open("/Users/manasapola/PycharmProjects/Basicsofpython/password manager/password-manager-start/data.json", mode = 'w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("/Users/manasapola/PycharmProjects/Basicsofpython/password manager/password-manager-start/data.json", mode = 'w') as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website.delete(0,'end')
                pwd_entry.delete(0,'end')
    
def find_password():
    website_value = website.get().lower()
    email_value = email.get()
    pwd_value = pwd_entry.get()
    try:
        with open("/Users/manasapola/PycharmProjects/Basicsofpython/password manager/password-manager-start/data.json", mode = 'r') as data_file:
            data = json.load(data_file) 
    except FileNotFoundError:
        messagebox.showinfo(title = "Information", message = " No Data File Found")
    else:

        if website_value in data:
            messagebox.showinfo(title = "Information", message = f"Email: {data[website_value]["Email"]}\nPassword: {data[website_value]["Password"]}")
            pwd_entry.insert(0,data[website_value]["Password"])
        else:
            messagebox.showerror(title= "Error Message", message="Data Not Found")

        
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30 )


canvas = Canvas(height=200, width = 200)
logo = PhotoImage(file ="/Users/manasapola/PycharmProjects/Basicsofpython/password manager/password-manager-start/logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(row = 0, column = 1)

#website label
web_label = Label(text = "Website:")
web_label.grid(row = 1, column = 0)
#website entry

website = Entry(width=20)
website.focus()
website.grid(row = 1, column = 1)

#email label
email_label = Label(text = "Email/Username:")
email_label.grid(row = 2, column = 0)

#email entry
email = Entry(width=35)
email.insert(0,"manasa@email.com")
email.grid(row = 2, column = 1, columnspan = 2)

#Password label

pwd_label = Label(text = "Password:")
pwd_label.grid(row = 3, column = 0)

#Password entry
pwd_entry = Entry(width = 21)
pwd_entry.grid(row = 3, column = 1)

#Generate password button

pwd_button = Button(text = "Generate Password", width = 14, command = generate_password)
pwd_button.grid(row = 3, column = 2)

#Search button

search = Button(text = "Search", width = 14, command=find_password)
search.grid(row=1, column = 2)

#Add button
add_button = Button(text = "Add", width = 36,command = save_password)
add_button.grid(row = 4, column = 1, columnspan = 2)



window.mainloop()