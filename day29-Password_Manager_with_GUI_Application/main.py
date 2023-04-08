from tkinter import *
from tkinter import messagebox
import pyperclip
from password_generator import password_generator
from save_information import check_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = password_generator()
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # TODO : get value from entry
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    # TODO: check validation when some field not be entry
    if website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any filed empty!")

    else:
        check_password(website, email, password)
        # TODO : clear all field after add button is be pressed
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# TODO 1: set windows setting
window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

# TODO 2 :  set canvas image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# TODO 3 : add label, entry and button to finish UI
# TODO 3.1 : Label
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:  ", bg="white")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

# TODO 3.2 : Entry
website_entry = Entry(width=46)
website_entry.focus()
website_entry.config(relief="solid")
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

email_username_entry = Entry(width=46)
email_username_entry.insert(0, "test@gmail.com")
email_username_entry.config(relief="solid")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = Entry(width=26)
password_entry.config(relief="solid")
password_entry.grid(column=1, row=3, sticky="w")

# TODO 3.3 : Button
generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", width=46, bg="white", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="w")

window.mainloop()
