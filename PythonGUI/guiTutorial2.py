#!/usr/bin/python
from Tkinter import *

class App(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        frame = Frame()
        frame.pack()

        self.instruction = Label(frame, text="Password:")
        self.instruction.pack()

        self.button = Button(frame, text="Enter", command=self.reveal)
        self.button.pack()


    def reveal(self):
        # Do something.
        pass


root = Tk()
root.title("Password")
root.geometry("350x250")
App(root)
root.mainloop()
