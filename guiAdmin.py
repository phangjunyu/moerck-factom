from tkinter import *
import registrationFunctions as rF

def show_entry_fields():
    print("creating stuff")

master = Tk()
master.configure(background='grey')
button_frame = tk.Frame(root)

frame = Frame(master, width = 300,height = 250)

Button(master, text='Create new Polling Station', command=show_entry_fields).grid(row=0, column=1, sticky=W, pady=4)

mainloop( )
