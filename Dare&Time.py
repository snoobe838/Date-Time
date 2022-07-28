from tkinter import*
from tkinter.ttk import*

from time import strftime
from datetime import datetime


note = Tk()
note.geometry("500x200")
note.title("Date&Time")
note.configure(background ="black")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

def date():
    string = strftime("%b %d, %Y")
    label.config(text=string)
    label.after(1000,date)
    

label = Label(note, font=("DS-Digital",80),background ="black", foreground ="forestgreen")
label.pack(anchor = 'center')
date()

label = Label(note, font=("DS-Digital",50),background ="black", foreground ="forestgreen")
label.pack(anchor = 's')
time()


mainloop()
