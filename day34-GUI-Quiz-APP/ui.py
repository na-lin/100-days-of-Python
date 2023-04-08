from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInter:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.loop = ""
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text="Score:0", fg="white", bg=THEME_COLOR, font=FONT)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Question",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_img,
            bg=THEME_COLOR,
            relief="flat",
            command=self.true_pressed
        )
        self.true_button.grid(column=0, row=2)
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_img,
            bg=THEME_COLOR,
            relief="flat",
            command=self.check_is_false
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label.config(text=f"Score:{self.quiz.score}")
        self.active_button()
        try:
            self.window.after_cancel(self.loop)
        except ValueError:
            pass
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz", fill=THEME_COLOR)
            self.disable_button()

    def disable_button(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def active_button(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def true_pressed(self):
        self.disable_button()
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_is_false(self):
        self.disable_button()
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # change canvas bg to red or green
        # then change canvas bg into white again after 1s and show next question
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")

        self.loop = self.window.after(1000, self.get_next_question)
