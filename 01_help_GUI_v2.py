from tkinter import *
from tkinter import ttk
import random


class Converter:
    def __init__(self, parent):
        # Formatting variables....
        background_colour = "yellow"

        # style configuration
        style = ttk.Style()
        style.configure('Frame1.TLabel', background=background_colour, foreground='black')

        # Converter Main Screen GUI.....
        self.converter_frame = ttk.Frame(style="Frame1.TLabel")
        self.converter_frame.grid()
        self.temp_converter_label = Label(self.converter_frame, text="Help", bg=background_colour)
        self.temp_converter_label.grid(row=0, column=0, padx=20, pady=20)
        # self.help_button.Button(root, text="Help button")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Help")
    something = Converter(root)
    root.mainloop()
