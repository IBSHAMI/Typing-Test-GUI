from tkinter import *


class TestPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.config(bg="#393e46")
        self.pack(side="left")
        smaller_label = Label(self, text="TYPING SPEED TEST", bg="#393e46", font=("Colfax", 11, "italic"),
                              fg="#EEEEEE")
        smaller_label.pack(fill="x", padx=120, pady=20)

        bigger_label = Label(self, text="TEST YOUR TYPING SKILLS", bg="#393e46", font=("Colfax", 30, "bold"),
                             fg="#EEEEEE")

        bigger_label.pack(fill="x", padx=120, pady=5)

        # ----------------Test Parameters Frame------------#
        test_params_frame = Frame(self, bg="#393e46")
        test_params_frame.pack(fill="x", pady=20)

        # Timer
        timer_text = Text(test_params_frame, width=15, height=3, highlightthickness=2.5,
                          highlightbackground="#00adb5")
        timer_text.grid(row=0, column=0, padx=100)

        # Words per min counter
        wpm_text = Text(test_params_frame, width=10, height=2)
        wpm_text.grid(row=0, column=1, padx=20)
        wpm_label = Label(test_params_frame, text="Words/min", bg="#393e46", font=("Colfax", 10, "bold"),
                          fg="#EEEEEE")
        wpm_label.grid(row=1, column=1, padx=5)

        # chars per min counter
        cpm_text = Text(test_params_frame, width=10, height=2)
        cpm_text.grid(row=0, column=2, padx=20)
        cpm_label = Label(test_params_frame, text="chars/min", bg="#393e46", font=("Colfax", 10, "bold"),
                          fg="#EEEEEE")
        cpm_label.grid(row=1, column=2, padx=5)

        # accuracy %
        accuracy_text = Text(test_params_frame, width=10, height=2)
        accuracy_text.grid(row=0, column=3, padx=20)
        accuracy_label = Label(test_params_frame, text="accuracy %", bg="#393e46", font=("Colfax", 10, "bold"),
                               fg="#EEEEEE")
        accuracy_label.grid(row=1, column=3, padx=5)

        # test words text bar
        text = Text(self, width=80, height=3, highlightthickness=2.8,
                    highlightbackground="#00adb5")
        text.insert("1.0", "HERE are there we need some thing here to assets us in this mesory what about me babe here come ")
        text.tag_add("second", "1.0", "end")
        text.tag_config("second", justify="center", font=("Colfax", 16, "bold"))
        text.config(state=DISABLED)
        text.pack()
        print(text.get("2.0", "end"))
