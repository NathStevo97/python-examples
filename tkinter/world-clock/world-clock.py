from datetime import datetime  # convert time data obtained
import pytz  # collect data from various timeszones
from tkinter import *  # used to create GUI
import time  # use the clock function continuously

root = Tk()
root.geometry("550x100")  # set GUI window size


def times():
    home = pytz.timezone("Europe/London")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M")
    ukClock.config(text=current_time)
    ukName.config(text="London")
    ukClock.after(1000, times)

    home = pytz.timezone("Europe/Sofia")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M")
    bulgClock.config(text=current_time)
    bulgName.config(text="Bulgaria")
    bulgClock.after(1000, times)

    home = pytz.timezone("Asia/Colombo")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M")
    slClock.config(text=current_time)
    slName.config(text="Sri Lanka")
    slClock.after(3000, times)


ukName = Label(root, font=("times", 20, "bold"))  # define country name label
ukName.place(x=15, y=5)
ukClock = Label(root, font=("times", 25, "bold"))  # define country clock label
ukClock.place(x=20, y=40)
ukNota = Label(
    root, text="Hours:    Minutes:", font=("times", 10, "bold")
)  # define clock time notation label
ukNota.place(x=10, y=80)

bulgName = Label(root, font=("times", 20, "bold"))
bulgName.place(x=210, y=5)
bulgClock = Label(root, font=("times", 25, "bold"))
bulgClock.place(x=220, y=40)
bulgNota = Label(root, text="Hours:    Minutes:", font=("times", 10, "bold"))
bulgNota.place(x=210, y=80)

slName = Label(root, font=("times", 20, "bold"))
slName.place(x=400, y=5)
slClock = Label(root, font=("times", 25, "bold"))
slClock.place(x=420, y=40)
slNota = Label(root, text="Hours:    Minutes:", font=("times", 10, "bold"))
slNota.place(x=410, y=80)

times()

root.mainloop()

"""
for tz in pytz.all_timezones:
    print(tz)
"""
