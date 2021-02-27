from tkinter import *


def cal_bmi():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi = round(weight / height ** 2, 2)
    bmi_results.config(text=f"your BMI is {bmi}")


window = Tk()
window.title("BMI Calculator")

height_label = Label(text="Height in cm")
height_label.grid(column=0, row=0)

height_entry = Entry(width=10)
height_entry.grid(column=1, row=0)

weight_label = Label(text="Weight in g")
weight_label.grid(column=0, row=1)

weight_entry = Entry(width=10)
weight_entry.grid(column=1, row=1)

bmi_results = Label(text="0")
bmi_results.grid(column=0, row=3)

cal_btn = Button(text="Calculate", command=cal_bmi)
cal_btn.grid(column=1, row=2)




window.mainloop()
