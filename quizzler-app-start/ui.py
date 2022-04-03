from tkinter import *
from quiz_brain import QuizBrain
from tkinter import font
THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, 'italic')
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Not A Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz_brain.score}/{self.quiz_brain.list_len}",
                                 bg=THEME_COLOR, font=("Times", 12, "bold"), fg="white")
        self.score_label.grid(column=1, row=0)
        self.question_number_label = Label(text=f"Question: {self.quiz_brain.question_number + 1}",
                                           font=("Times", 12, "bold"), bg=THEME_COLOR, fg="white")
        self.question_number_label.grid(column=0, row=0)
        self.canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")

        self.question_text = self.canvas.create_text(int(CANVAS_WIDTH / 2),
                                                     int(CANVAS_HEIGHT / 2),
                                                     text="",
                                                     font=QUESTION_FONT,
                                                     width=CANVAS_WIDTH - 20)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_img, bg=THEME_COLOR, borderwidth=0, overrelief='sunken',
                                  activebackground="black", command=self.answer_true_on_click)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, bg=THEME_COLOR, borderwidth=0, overrelief='sunken',
                                   activebackground="black", command=self.answer_false_on_click)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            question_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text)
            self.format_score()
            self.format_question_number()
        else:
            self.show_end_score()
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true_on_click(self):
        is_correct = self.quiz_brain.check_answer('true')
        self.give_answer_feedback(is_correct)

    def answer_false_on_click(self):
        is_correct = self.quiz_brain.check_answer('false')
        self.give_answer_feedback(is_correct)

    def give_answer_feedback(self, is_correct: bool):
        if is_correct:
            self.canvas.config(bg="#60FB31")

        else:
            self.canvas.config(bg="#F8512D")

        self.canvas.after(1000, self.reset_canvas)

    def format_score(self):
        score = self.quiz_brain.score
        self.score_label.config(text=f"Score: {score}/{self.quiz_brain.list_len}")

    def format_question_number(self):
        question_number = self.quiz_brain.question_number
        self.question_number_label.config(text=f"Question: {question_number}")

    def reset_canvas(self):
        self.canvas.config(bg='white')
        self.get_next_question()

    def show_end_score(self):
        self.canvas.itemconfig(self.question_text, text=f"Final Score: {self.quiz_brain.score}",
                               font=('Comic Sans Ms', 34, 'bold'), fill='gray')
        self.canvas.config(bg="lightgray")