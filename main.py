from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from test_page import TestPage


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#222831")
        self.wm_geometry("800x500")
        container_buttons = Frame(self, bg="#00adb5")
        container_buttons.pack(side="top", fill="x", expand=False)
        container_pages = Frame(self, bg="#393e46")
        container_pages.pack(side="bottom", fill="both", expand=True)

        test_page = TestPage(self)
        test_page.place(in_=container_pages)
        button = Button(container_buttons, bg="#eeeeee", width=20, height=2,  text="Test Page",
                        font=("Colfax", 8, "bold"))
        button.pack(side="left")


if __name__ == "__main__":
    main = MainWindow()

    main.mainloop()
