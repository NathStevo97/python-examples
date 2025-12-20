# importing tkinter
# tkinter is the standard Python interface fir GUI development
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# import strftime function - gets system time
from time import strftime
from datetime import datetime, timedelta

# create the tkinter window
root = tk.Tk()
root.title("Clock")


# Display time on the label
def time(region):
    if region == "uk":
        hour_diff = 0
        min_diff = 0
    elif region == "bulgaria":
        hour_diff = 2
        min_diff = 0
    elif region == "sriLanka":
        hour_diff = 5
        min_diff = 30
    string = datetime.now() + timedelta(hours=hour_diff, minutes=min_diff)
    string = string.strftime("%H:%M:%S")
    print(string)
    # lbl.config(text = string)
    # lbl.after(1000, time(region))


# lbl = tk.Label(root, font = ('calibri', 40, 'bold'), background = 'purple', foreground = 'white')

# Place clock at the centre of the tkinter window
# lbl.pack(side=tk.BOTTOM)

time("uk")
time("bulgaria")
time("sriLanka")

# tk.mainloop()


"""
from tkinter import *

root = Tk()
root.geometry('250x150')

button1 = Button(text="button1")
button1.pack(side = BOTTOM, pady=6)

button2 = Button(text="button2")
button2.pack(side = BOTTOM, pady=3)

root.mainloop()
"""
