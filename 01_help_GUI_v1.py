from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Help Page")

# help frame 1
style = ttk.Style()
style.configure('Frame1.TFrame', background="orange")
help_frame1 = ttk.Frame(root, style="Frame1.TFrame", width=20, height=20)
help_frame1.grid(row=0, column=0, padx=2, pady=3)
# help information
help_info_frame = ttk.Frame(root, style="Frame1.TFrame", width=20, height=20)
help_info_frame.grid(row=1, column=0, padx=5, pady=5)
# Help info label
help_text = ttk.Label(help_info_frame, text="Type in the numeric value you want to convert in either"
                                            "the Celsius or "
                                            "Fahrenheit search bar")
help_text.grid(row=1, column=0, padx=15, pady=15, sticky="NSEW")
# button

root.mainloop()
