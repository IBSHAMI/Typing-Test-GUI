from tkinter import *
from test_page import TestPage
from results_page import ResultsPage
import time

test_is_on = None
# start_timer = False
test_start_time = None
timer = 60
entry_button_state = True
button_color_on = "#393e46"
button_color_off = "#eeeeee"
button1_isClicked = True
button2_isClicked = False


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#222831")
        self.wm_geometry("800x500")
        self.container_buttons = Frame(self, bg="#00adb5")
        self.container_buttons.pack(side="top", fill="x", expand=False)
        self.container_pages = Frame(self, bg="#393e46")
        self.container_pages.pack(side="bottom", fill="both", expand=True)

        self.results_page = ResultsPage(self.container_pages)
        self.results_page.place(in_=self.container_pages, x=0, y=0, relwidth=1, relheight=1)
        self.test_page = TestPage(self.container_pages)
        self.test_page.place(in_=self.container_pages, x=0, y=0, relwidth=1, relheight=1)

        self.button_test_page = Button(self.container_buttons, bg=button_color_on, width=20, height=2, text="Test Page",
                                       font=("Colfax", 8, "bold"), command=button1_click)
        self.button_test_page.pack(side="left")

        self.button_results_page = Button(self.container_buttons, bg=button_color_off, width=20, height=2,
                                          text="Past results Page", font=("Colfax", 8, "bold"), command=button2_click)
        self.button_results_page.pack(side="left")


def button1_click():
    global button1_isClicked, button2_isClicked
    main.test_page.lift()
    main.button_test_page.config(bg=button_color_on)
    main.button_results_page.config(bg=button_color_off)
    button1_isClicked = True
    button2_isClicked = False


def button2_click():
    global button1_isClicked, button2_isClicked
    try:
        main.results_page.results_summary_label.destroy()
    except AttributeError:
        pass
    main.results_page.read_results_data()
    main.results_page.lift()
    main.button_test_page.config(bg=button_color_off)
    main.button_results_page.config(bg=button_color_on)
    button1_isClicked = False
    button2_isClicked = True


def check(event):
    global test_start_time, test_is_on, timer, entry_button_state, button1_isClicked
    if main.test_page.check_user_input() and button1_isClicked:
        main.test_page.retry_button.config(state=DISABLED)
        if not test_is_on:
            test_start_time = time.time()
        test_is_on = True
        main.test_page.test_running()
        test_time = 5
        timer = test_time
        while timer > 0:
            timer = test_time - (time.time() - test_start_time)
            main.test_page.time = round(timer)
            main.test_page.test_running()
            main.update()
        if test_is_on:
            main.test_page.save_test_result()
        main.test_page.retry_button.config(state=NORMAL)
        test_is_on = False
        main.test_page.try_again_button_clicked = False
        main.test_page.entry.config(state=DISABLED)
        main.test_page.timer.delete("1.0", END)
        main.test_page.timer.insert("1.0", f"TimeOver")
        main.test_page.timer.tag_add("timer_tag", "1.0", "end")
        main.test_page.timer.tag_config("timer_tag", justify="center", font=("Times New Roman", 20))
        main.test_page.timer.configure(state=DISABLED)
        entry_button_state = False


if __name__ == "__main__":
    main = MainWindow()
    main.bind("<KeyPress>", check)
    main.mainloop()
