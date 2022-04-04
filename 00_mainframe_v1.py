from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Temperature converter")

# frame 1
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0, columnspan=5, rowspan=5, padx=2, pady=3)
# first label test
temp_label = Label(frame1, text="temperature converter", bg="blue")
temp_label.grid(row=0, column=0, columnspan=3, rowspan=3,)

# button
help_button = ttk.Button(frame1, text="Help")

root.mainloop()
