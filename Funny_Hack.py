import random
from tkinter import *
from random import randint
import time
import threading

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

def placewindows():
    while True:
        win = Toplevel(root)
        win.geometry("300x60+" + str(randint(0, root.winfo_screenmmwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
        win.overrideredirect(1)
        Label(win, text="You Got Hacked", fg="red").place(relx=.38, rely=.3)
        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(.05)

threading.Thread(target=placewindows).start()

root.mainloop()
