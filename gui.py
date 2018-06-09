from tkinter import *
import registrationFunctions as rF

def show_entry_fields():
   print("Name: %s\nUID: %s" % (e1.get(), e2.get()))

def createVoter():
    response = rF.createVoter(e1.get(),e2.get())

master = Tk()
Label(master, text="Name").grid(row=0)
Label(master, text="UID").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Submit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
