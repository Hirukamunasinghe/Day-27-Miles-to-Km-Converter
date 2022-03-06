from tkinter import *

def miles_to_km_converter():
    miles = float(miles_input.get())
    km = round(miles*1.609, 2)
    kilometer_result.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilometers converter")
window.config(padx = 20, pady = 20)

#Miles input
miles_input = Entry()
miles_input.grid(column = 1, row = 0)

#Miles label
miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

#is_equal_to label
is_equal_to = Label(text = "is equal to")
is_equal_to.grid(column = 0, row = 1)

#Kilometer result
kilometer_result = Label(text = "0")
kilometer_result.grid(column = 1, row=1)

#Kilometer label
kilometer_label = Label(text = "Km")
kilometer_label.grid(column =2, row =1)

#Calculate button
calculate_button = Button(text = "Calculate", command =miles_to_km_converter )
calculate_button.grid(column =1, row=2)


window.mainloop()


