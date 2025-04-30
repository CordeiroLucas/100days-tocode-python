import tkinter
from tkinter import Button

# Button
def button_clicked():
    print("Clicked")
    my_label.config(text=entry.get())


window = tkinter.Tk()
window.title("Mile Converter")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "I am a label"
my_label.config(text="Config")

entry = tkinter.Entry(width=10)
entry.pack()

button = Button(text="click me", command=button_clicked)
button.pack()

window.mainloop()
