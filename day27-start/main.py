from tkinter import *

def button_click():
    my_label["text"] = "Button Got Clicked"

window = Tk()
window.title("my first GUI program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="My label")
# my_label["text"] = "New Label"
# my_label.config(text="Second Label")
my_label.grid(row=0,column=0)

# button
# make button actually work like turtle event listener , use command when button detect a command
button_1 = Button(text="Button 1", command=button_click)
button_2 = Button(text="Button 2")
button_1.grid(row=1,column=1)
button_2.grid(row=0,column=2)

# Entry
def show_input():
    my_label["text"] = my_input.get()
    print(my_input.get())
    # print(text)
    # print(type(text.get()))
    print(text.get())


text = IntVar()
my_input = Entry(width=10,textvariable=text)
button_1.configure(text="Click Me", command=show_input)
my_input.grid(row=2,column=3)


window.mainloop()
