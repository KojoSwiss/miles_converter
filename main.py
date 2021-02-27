from tkinter import *


def miles_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilo_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculate = Button(text="Calculate", command=miles_km)
calculate.grid(column=1, row=2)

window.mainloop()
