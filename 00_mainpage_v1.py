from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Temperature converter")
root.configure(background='yellow')

# frame 1
style = ttk.Style()
style.configure('Frame1.TFrame', background="yellow")
frame1 = ttk.Frame(root, style="Frame1.TFrame", width=20, height=20)
frame1.grid(row=0, column=0, padx=2, pady=3)
# first label test
temp_label = Label(frame1, text="Temperature Converter", justify="center", bg="yellow", font=("Arial", "16", "bold"))
temp_label.grid(row=0, column=0, columnspan=3, rowspan=4, padx=15, pady=15, sticky="NSEW")

# button
help_button = ttk.Button(frame1, text="Help")
help_button.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()

