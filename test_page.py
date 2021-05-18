from tkinter import *
from random import choices
import datetime


# test variables
time = 60
wpm = 0
cpm = 0
accuracy = 0


def create_text():
    with open("words.txt", "r") as words:
        # create a list 400 random words from our txt file
        test_words = choices(list(words), k=600)

        # create a list of the length of each word chosen
        len_word_list = [len(word.strip()) for word in test_words]

        # strip \n from each words from our list except each word at index 9
        index_nostrip = 6
        end_of_line = 0
        final_word_list = []
        lines_list = []
        line = ""

        for i in range(len(test_words)):
            if end_of_line == index_nostrip - 1:
                final_word_list.append(test_words[i])
                line += test_words[i].strip()
                lines_list.append(line)
                line = ""
                end_of_line = 0
            else:
                final_word_list.append(test_words[i].strip())
                line += f"{test_words[i].strip()} "
                end_of_line += 1

        # create the final string to be used in the test
        test_text = " ".join(final_word_list)

        # create a dict that contains information about each line in our text
        test_text_dict = {}
        line_key_index = 0
        line_properties = {}
        for line in lines_list:
            line_properties["line"] = line
            line_properties["words_length_list"] = len_word_list[0:6]
            # delete the length of words for the line after adding it to the dictionary
            del len_word_list[0:6]
            test_text_dict[line_key_index] = line_properties
            line_properties = {}
            line_key_index += 1
        return test_text, test_text_dict


test_text, test_text_dict = create_text()


class TestPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.container = container
        self.config(bg="#393e46")
        self.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.time = time
        self.start_test = False
        self.test_text, self.test_text_dict = create_text()
        # Variables to keep track of user progress during test
        self.line_index = 1
        self.word_index = 0
        self.char_index = 0
        self.chars_correct = 0
        self.words_correct = 0
        self.accuracy_percentage = 0
        self.chars_check = []
        self.total_finished_words = 0

        self.entry, self.timer, self.text, self.wpm, self.cpm, self.accuracy, self.retry_button, self.test_params_frame = self.create_page()

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
        timer_text.insert("1.0", f"{self.time} s")
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
        text.insert("1.0", self.test_text)
        text.tag_add("second", "1.0", "end")
        text.tag_config("second", justify="left", font=("Times New Roman", 20))
        text.config(state=DISABLED)
        text.pack()

        # --------------------------user Input entry  fame-------------------------#
        user_frame = Frame(self, bg="#393e46")
        user_frame.pack(fill="x", pady=10)

        # user entry widget
        entry = Entry(user_frame, width=40, font=("Times New Roman", 16), highlightthickness=2.8,
                      highlightbackground="#00adb5")
        entry.pack(side="left", padx=67)

        # button to retry
        retry_button = Button(self, bg="#00adb5", width=20, height=2, text="Try Again",
                              font=("Colfax", 10, "bold"), command=self.try_again)
        retry_button.pack(side="right")

        return entry, timer_text, text, wpm_text, cpm_text, accuracy_text, retry_button, test_params_frame

    def check_user_input(self):
        if self.entry.get() != "":
            self.start_test = True
        return self.start_test

    def update_test_screen(self):
        # update timer text
        self.timer.delete("1.0", END)
        self.timer.insert("1.0", f"{self.time} s")
        self.timer.tag_add("timer_tag", "1.0", "end")
        self.timer.tag_config("timer_tag", justify="center", font=("Times New Roman", 20))

        # update word\min text
        self.wpm.delete("1.0", END)
        self.wpm.insert("1.0", f"{self.words_correct}")
        self.wpm.tag_add("wpm_tag", "1.0", "end")
        self.wpm.tag_config("wpm_tag", justify="center", font=("Times New Roman", 20))

        # update char/min text
        self.cpm.delete("1.0", END)
        self.cpm.insert("1.0", f"{self.chars_correct}")
        self.cpm.tag_add("cpm_tag", "1.0", "end")
        self.cpm.tag_config("cpm_tag", justify="center", font=("Times New Roman", 20))

        # update accuracy text
        self.accuracy.delete("1.0", END)
        self.accuracy.insert("1.0", f"{self.accuracy_percentage}")
        self.accuracy.tag_add("accuracy_tag", "1.0", "end")
        self.accuracy.tag_config("accuracy_tag", justify="center", font=("Times New Roman", 20))

    def test_running(self):
        self.update_test_screen()
        user_input = self.entry.get()
        len_of_target_word = self.test_text_dict[self.line_index - 1]['words_length_list'][self.word_index]

        try:
            if user_input[-1] == " ":
                self.char_index += len_of_target_word + 1
                self.word_index += 1
                if False not in self.chars_check and len(self.chars_check) == len_of_target_word:
                    self.words_correct += 1

                self.total_finished_words += 1
                self.accuracy_percentage = int((self.words_correct / self.total_finished_words) * 100)

                if self.word_index == 6:
                    self.text.see(f"{self.line_index + 3}.0")
                    self.line_index += 1
                    self.word_index = 0
                    self.char_index = 0
                    # add 1 for the space at beginning of each line after first line
                    self.char_index = 1

                self.chars_correct += self.chars_check.count(True)
                self.entry.delete(0, "end")

            else:
                real_text = self.text.get(f"{self.line_index}.{self.char_index}",
                                          f"{self.line_index}.{len(user_input) + self.char_index}")
                self.chars_check = [user_input[x] == real_text[x] for x in range(len(user_input))]
                if len(self.chars_check) <= len_of_target_word:
                    for i in range(len(self.chars_check)):
                        if self.chars_check[i]:
                            self.text.tag_remove("wrong-word", f"{self.line_index}.{self.char_index + i}")
                            self.text.tag_add("correct-word", f"{self.line_index}.{self.char_index + i}")
                            self.text.tag_config("correct-word", foreground="green", background="#00adb5")
                        elif not self.chars_check[i]:
                            self.text.tag_remove("correct-word", f"{self.line_index}.{self.char_index + i}")
                            self.text.tag_add("wrong-word", f"{self.line_index}.{self.char_index + i}")
                            self.text.tag_config("wrong-word", foreground="red", background="#00adb5")


        except IndexError:
            pass

    def save_test_result(self):
        with open("test_results.txt", "r+") as results:
            if results.readline() == "":
                results.write(f"date,wpm,cpm,accuracy\n{datetime.datetime.now().strftime('%d/%b/%Y')},"
                              f"{self.words_correct},{self.chars_correct},{self.accuracy_percentage}")
            else:
                results.write(f"\n{datetime.datetime.now().strftime('%d/%b/%Y')},"
                              f"{self.words_correct},{self.chars_correct},{self.accuracy_percentage}")

    def try_again(self):
        self.destroy()
        self.__init__(self.container)
