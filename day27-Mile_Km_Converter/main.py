from tkinter import *

# TODO 1: windows default
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=50)
window.config(padx=50, pady=20)

# TODO 2: Entry
mile = Entry(width=10)
mile.grid(row=0, column=1)

# TODO 3: Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=10, pady=10)

mile_label = Label(text="Miles")
mile_label.grid(row=0, column=2)
mile_label.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

convert_mile = Label(text="0")
convert_mile.grid(row=1, column=1)
convert_mile.config(padx=10, pady=10)


# TODO 4 : button
def convert():
    input_mile = float(mile.get())
    km = round(input_mile * 1.609344,2)
    convert_mile.config(text=f"{km}")


button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
