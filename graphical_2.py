from tkinter import *

root = Tk()
username = StringVar()
password = StringVar()

username.set("Admin")
password.set("ADMIN")

global saved_username
global saved_password
saved_username = "Admin"
saved_password = "ADMIN"

def login(event):
    global username_save
    username_save = username.get()
    password_save = password.get()
    if username_save.lower() == saved_username.lower():
        if password_save == saved_password:
            forget_login()

        else:
            print("Wrong username or password")
    else:
        print("Wrong username or password")
def forget_login():
    label_username.grid_forget()
    label_password.grid_forget()
    entry_username.grid_forget()
    entry_password.grid_forget()
    button_login.grid_forget()
    setup()

def setup():
    Frame_test_delete_me = Frame(root, width=200, height=400)
    Frame_test_delete_me.grid()
    label_loggedin = Label(root, text="You logged in as " + username_save)
    label_loggedin.grid(row=0)
label_username = Label(root, text="Username")
label_password = Label(root, text="Password")
entry_username = Entry(root, textvariable=username)
entry_password = Entry(root, textvariable=password)

button_login = Button(root, text="LOGIN")
button_login.bind("<Button-1>", login)


button_login.grid(row=3, columnspan=3)
label_username.grid(row=0, column=0, sticky=E)
label_password.grid(row=1, column=0, sticky=E)

entry_username.grid(row=0, column=1)
entry_password.grid(row=1, column=1)

root.mainloop()