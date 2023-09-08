import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Madrid", "Paris"],
                "correct_option": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Jupiter"],
                "correct_option": "Mars"
            },
            {
                "question": "What is 2 + 2?",
                "options": ["3", "4", "5"],
                "correct_option": "4"
            }
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack()

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(3):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            messagebox.showinfo("Quiz Complete", f"You scored {self.score} out of {len(self.questions)}!")
            self.root.destroy()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        if question_data["options"][selected_option] == question_data["correct_option"]:
            self.score += 1
        self.current_question += 1
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

