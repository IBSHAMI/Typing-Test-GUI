from tkinter import *


class TestPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.config(bg="#393e46")
        self.pack(side="left")
        smaller_label = Label(self, text="TYPING SPEED TEST", bg="#393e46", font=("Colfax", 11, "italic"),
                              fg="#EEEEEE")
        smaller_label.pack(side="top", fill="x", padx=120, pady=30)

        bigger_label = Label(self, text="TEST YOUR TYPING SKILLS", bg="#393e46", font=("Colfax", 30, "bold"),
                             fg="#EEEEEE")

        bigger_label.pack(side="top", fill="x", padx=120, pady=10)
