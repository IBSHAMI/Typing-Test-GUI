from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from test_page import TestPage
import time

test_is_on = False
# start_timer = False
test_start_time = None
timer = 60


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#222831")
        self.wm_geometry("800x500")
        container_buttons = Frame(self, bg="#00adb5")
        container_buttons.pack(side="top", fill="x", expand=False)
        container_pages = Frame(self, bg="#393e46")
        container_pages.pack(side="bottom", fill="both", expand=True)

        self.test_page = TestPage(self)
        self.test_page.place(in_=container_pages)
        button = Button(container_buttons, bg="#eeeeee", width=20, height=2, text="Test Page",
                        font=("Colfax", 8, "bold"))
        button.pack(side="left")


def check(event):
    global test_start_time, test_is_on, timer
    if main.test_page.check_user_input():
        if not test_is_on:
            test_start_time = time.time()
        test_is_on = True
        main.test_page.test_running()
    while timer > 0:
        timer = 60 - (time.time() - test_start_time)
        main.test_page.time = round(timer)
        main.test_page.test_running()
        main.update()
    test_is_on = False


if __name__ == "__main__":
    main = MainWindow()
    main.bind("<KeyPress>", check)
    main.mainloop()
