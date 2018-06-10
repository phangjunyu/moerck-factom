import tkinter as tk
import pb
import glossary

def show_entry_fields():
   print("Name: %s\nUID: %s" % (e1.get(), e2.get()))

def guiCreateVoter():
    voterRegistered = pb.register_vote(e1.get(),e2.get())

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       p2 = args[1]

       label2 = tk.Label(self, text="Name")
       label3 = tk.Label(self, text="UID")
       e1 = tk.Entry(self)
       e2 = tk.Entry(self)
       label2.pack(side="left", fill="x", expand=True)
       e1.pack(side="left", fill="x", expand=True)
       label3.pack(side="left", fill="x", expand=True)
       e2.pack(side="left", fill="x", expand=True)


       b = tk.Button(self, text='Submit', command=p2.lift)
       b.pack(side="left",fill="x", expand=True)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       p3 = args[1]
       def myfn(p3):
           print("hello")
           p3.lift()
       checkCmd = tk.IntVar()
       checkCmd2 = tk.IntVar()
       checkBox1 = tk.Checkbutton(self, variable=checkCmd, onvalue=1, offvalue=0, text="Command  Prompt").pack()
       checkBox2 = tk.Checkbutton(self, variable=checkCmd2, onvalue=1, offvalue=0, text="Command  Prompt").pack()
       buttonCmd = tk.Button(self, text="Run Checked Items", command=lambda: myfn(p3)).pack()
       b = tk.Button(self, text='Submit', command=p3.lift)
       b.pack(side="left",fill="x", expand=True)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="You Have Successfully Submitted your Vote!")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p3 = Page3(self)
        p2 = Page2(self,p3)
        p1 = Page1(self,p2)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)


        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)


        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
