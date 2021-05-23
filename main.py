from tkinter import *
from test_page import TestPage
from results_page import ResultsPage
import time

# ------------- Test and screen elements variables ---------- #
test_is_on = None  # check if test is running
test_start_time = None  # record test initial time
timer = None  # test total allowed seconds
button_color_on = "#393e46"
button_color_off = "#eeeeee"
# The app contains 2 pages (test page and past results page)
# You can navigate between the pages through pages buttons in top
# At first the test page will be shown so button 1 is on
button1_isClicked = True
button2_isClicked = False
# Value that will hold the main app
# set to None at beginning to not raise an error
main = None
try_again_allowed = True  # During test user not allowed to hit try again this var for button status


# ------------------- Main App class ---------------------#
# Contains 2 Frames
# Buttons frame to hold pages buttons for navigation
# pages frame to contain both (test and result page)
class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bg="#222831")
        self.wm_geometry("800x500")
        self.container_buttons = Frame(self, bg="#00adb5")
        self.container_buttons.pack(side="top", fill="x", expand=False)
        self.container_pages = Frame(self, bg="#393e46")
        self.container_pages.pack(side="bottom", fill="both", expand=True)

        # Place is used because I needed to place both pages exactly in top of each other
        # by specifying there exact pixel locations on the container_pages frame
        self.results_page = ResultsPage(self.container_pages)
        self.results_page.place(in_=self.container_pages, x=0, y=0, relwidth=1, relheight=1)
        self.test_page = TestPage(self.container_pages)
        self.test_page.place(in_=self.container_pages, x=0, y=0, relwidth=1, relheight=1)

        # buttons placed in the buttons frame
        self.button_test_page = Button(self.container_buttons, bg=button_color_on, width=20, height=2, text="Test Page",
                                       font=("Colfax", 8, "bold"), command=button1_click)
        self.button_test_page.pack(side="left")

        self.button_results_page = Button(self.container_buttons, bg=button_color_off, width=20, height=2,
                                          text="Past results Page", font=("Colfax", 8, "bold"), command=button2_click)
        self.button_results_page.pack(side="left")


# ---------------------------------------------------------------------------------------------------------------------#

# Both functions will be used to navigate between the pages when any of the buttons is pressed
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


# --------------------------------------------------------------------------------------------------------------------#

# function to implement the test and count for timer
def check(event):
    global test_start_time, test_is_on, timer, button1_isClicked
    # check if the test page is on and if the user gives an input to the entry widget
    if main.test_page.check_user_input() and button1_isClicked:
        # if user give input to entry widget we start the test
        # we unbind any event listener to avoid any disturbance during the test
        main.unbind("<KeyPress>")
        # disable try again button
        if main.test_page.entry.get() != "":
            main.test_page.retry_button.config(state=DISABLED)
        # record the time of the test starting
        if not test_is_on:
            test_start_time = time.time()
        test_is_on = True
        # initialize the test page test running function
        main.test_page.test_running()
        test_time = main.test_page.test_time
        timer = test_time
        while timer > 0:
            timer = test_time - (time.time() - test_start_time)
            main.test_page.time = round(timer)
            main.test_page.test_running()
            main.update()
        # make sure the test results is only recorded one time
        if test_is_on and main.test_page.test_time != 0:
            main.test_page.save_test_result()
        main.test_page.test_time = 0

        # allow user to press try again button after test is over
        main.test_page.retry_button.config(state=NORMAL)
        test_is_on = False
        main.test_page.try_again_button_check = False
        main.test_page.entry.config(state=DISABLED)
        main.test_page.timer.delete("1.0", END)
        main.test_page.timer.insert("1.0", f"TimeOver")
        main.test_page.timer.tag_add("timer_tag", "1.0", "end")
        main.test_page.timer.tag_config("timer_tag", justify="center", font=("Times New Roman", 20))
        main.test_page.timer.configure(state=DISABLED)
        main.bind("<KeyPress>", check)


if __name__ == "__main__":
    main = MainWindow()
    # bind the main app window to any keypress event
    main.bind("<KeyPress>", check)
    main.mainloop()
