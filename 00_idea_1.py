from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Temperature converter")

# first label test
temp_label = Label(root, text="temperature converter", bg="blue")
temp_label.grid(row=0, column=0, padx=3, pady=3)

# frame 1
frame1 = ttk.Frame(root)
frame1.grid(row=1, column=0, padx=2, pady=3)
help_button = ttk.Button(frame1, text="Help")


root.mainloop()