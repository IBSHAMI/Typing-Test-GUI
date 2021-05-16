from tkinter import *
from random import choices

# test varaibles
time = 60
wpm = 0
cpm = 0
accuracy = 0

with open("words.txt", "r") as words:
    # create a list 400 random words from our txt file
    test_words = choices(list(words), k=400)

    # strip \n from each words from our list except each word at index 9
    index_nostrip = 6
    final_word_list = []
    for i in range(len(test_words)):
        if i != index_nostrip:
            final_word_list.append(test_words[i].strip())
        elif i == index_nostrip:
            final_word_list.append(test_words[i])
            index_nostrip += 6

    # create the final string to be used in the test
    test_text = " ".join(final_word_list)


class TestPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.config(bg="#393e46")
        self.pack(side="left")
        self.create_page()

    def create_page(self):
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
        timer_text = Text(test_params_frame, width=15, height=2, highlightthickness=2.5,
                          highlightbackground="#00adb5")
        timer_text.insert("1.0", f"{time} s")
        timer_text.tag_add("timer_tag", "1.0", "end")
        timer_text.tag_config("timer_tag", justify="center", font=("Times New Roman", 20))
        timer_text.grid(row=0, column=0, padx=100)

        # Words per min counter
        wpm_text = Text(test_params_frame, width=10, height=2)
        wpm_text.insert("1.0", f"{wpm}")
        wpm_text.tag_add("wpm_tag", "1.0", "end")
        wpm_text.tag_config("wpm_tag", justify="center", font=("Times New Roman", 20))
        wpm_text.grid(row=0, column=1, padx=20)

        wpm_label = Label(test_params_frame, text="Words/min", bg="#393e46", font=("Colfax", 10, "bold"),
                          fg="#EEEEEE")
        wpm_label.grid(row=1, column=1, padx=5)

        # chars per min counter
        cpm_text = Text(test_params_frame, width=10, height=2)
        cpm_text.insert("1.0", f"{cpm}")
        cpm_text.tag_add("cpm_tag", "1.0", "end")
        cpm_text.tag_config("cpm_tag", justify="center", font=("Times New Roman", 20))
        cpm_text.grid(row=0, column=2, padx=20)

        cpm_label = Label(test_params_frame, text="chars/min", bg="#393e46", font=("Colfax", 10, "bold"),
                          fg="#EEEEEE")
        cpm_label.grid(row=1, column=2, padx=5)

        # accuracy %
        accuracy_text = Text(test_params_frame, width=10, height=2)
        accuracy_text.insert("1.0", f"{accuracy}")
        accuracy_text.tag_add("accuracy_tag", "1.0", "end")
        accuracy_text.tag_config("accuracy_tag", justify="center", font=("Times New Roman", 20))
        accuracy_text.grid(row=0, column=3, padx=20)

        accuracy_label = Label(test_params_frame, text="accuracy %", bg="#393e46", font=("Colfax", 10, "bold"),
                               fg="#EEEEEE")
        accuracy_label.grid(row=1, column=3, padx=5)

        # -------------------------test words text bar -----------------------------------#
        text = Text(self, width=80, height=6, highlightthickness=2.8,
                    highlightbackground="#00adb5")
        text.insert("1.0", test_text)
        text.tag_add("second", "1.0", "end")
        text.tag_config("second", justify="center", font=("Times New Roman", 20))
        text.config(state=DISABLED)
        text.pack()
        print(text.get("1.0", "end"))

        # --------------------------user Input entry  fame-------------------------#
        user_frame = Frame(self, bg="#393e46")
        user_frame.pack(fill="x", pady=10)

        # user entry widget
        entry = Entry(user_frame, width=40, font=("Times New Roman", 16), highlightthickness=2.8,
                      highlightbackground="#00adb5")
        entry.pack(side="left", padx=67)

        # button to retry
        retry_button = Button(self, bg="#00adb5", width=20, height=2, text="Try Again",
                              font=("Colfax", 10, "bold"))
        retry_button.pack(side="right")
