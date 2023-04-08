# ---------------------------- SAVE PASSWORD ------------------------------- #
# check whether same website and same email password already exist in file,
# is yes,delete old password inforation , if no, delete website and password entry information
#append   password information into data.txt if file don't exit or want to change old password into new one
#
from tkinter import messagebox
import os.path


# website,email,password

def save_information(website, email, password):
    # TODO: POP up a message box to let user double check their inputs
    is_ok = messagebox.askokcancel(title=f"{website}", message=f"There are the details entered:\nEmail:{email}"
                                                            f"\nPassword:{password}\nIs it ok to save")

    if is_ok:
        # TODO: write data into file, each data become a line in file and append to add data
        with open("data.txt", mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")


def check_password(website, email, password):

    if os.path.isfile("data.txt"):
        with open("data.txt") as file:
            data = file.readlines()
            entry_infor = f"{website} | {email}"
            for infor in data:
                if entry_infor in infor:
                    exist_password = infor.split(" | ")[2]
                    is_change = messagebox.askyesno(title="Caution",
                                                    message=f"This website password already exist."
                                                            f"\nOld Password is {exist_password}"
                                                            f"\nDo you want to use new password: {password} "
                                                            f"to replace old password: {exist_password}?")
                    if is_change:
                        # TODO: if want to change, delete old infor
                        with open("data.txt", mode="w") as file:
                            for line in data:
                                if entry_infor not in line:
                                    file.write(line)
                    else:
                        return

    save_information(website, email, password)


# for debug
# check_password("AA", "test@gmail.com", "NEW_PASS")
