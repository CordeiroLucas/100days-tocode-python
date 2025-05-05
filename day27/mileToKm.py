from tkinter import *


# Button
def milesToKm():
    print("Clicked")
    int(label_answer.get()) * 1.609
    label_answer.config(text=f"{int(int(label_answer.get()) * 1.609)}")

window = Tk()
window.title("Miles Converter")
window.config(padx=20, pady=20)

# Label
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("Arial", 12, "bold"))
label_miles.grid(column=2, row=0)

label_text = Label(text="is equal to", font=("Arial", 12, "bold"))
label_text.grid(column=0, row=2)

label_answer = Label(text="0", font=("Arial", 12, "bold"))
label_answer.grid(column=1, row=2)

label_km = Label(text="Km", font=("Arial", 12, "bold"))
label_km.grid(column=2, row=2)

button_calc = Button(text="Calculate", command=milesToKm)
button_calc.grid(column=1, row=3)

window.mainloop()
