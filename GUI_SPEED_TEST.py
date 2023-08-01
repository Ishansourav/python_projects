import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.words = ["hello", "world", "python", "programming", "speed", "typing", "test", "challenge", "practice", "coding"]
        self.sentence_length = 5
        self.sentence = ""
        self.start_time = 0

        self.label_sentence = tk.Label(root, text="", font=("Helvetica", 14))
        self.label_sentence.pack(pady=20)

        self.entry_input = tk.Entry(root, font=("Helvetica", 14))
        self.entry_input.pack(pady=10)
        self.entry_input.bind("<Return>", self.check_input)

        self.label_result = tk.Label(root, text="", font=("Helvetica", 14))
        self.label_result.pack(pady=20)

        self.generate_sentence()

    def generate_sentence(self):
        self.sentence = " ".join(random.choices(self.words, k=self.sentence_length))
        self.label_sentence.config(text=self.sentence)
        self.start_time = time.time()

    def check_input(self, event):
        user_input = self.entry_input.get().strip()

        if user_input == self.sentence:
            elapsed_time = time.time() - self.start_time
            words_per_minute = self.calculate_typing_speed(self.sentence, elapsed_time)
            self.label_result.config(text=f"Congratulations!\nYour typing speed: {words_per_minute:.2f} words per minute.")
        else:
            self.label_result.config(text="Oops! Your input does not match the given sentence.")

        self.generate_sentence()
        self.entry_input.delete(0, tk.END)

    @staticmethod
    def calculate_typing_speed(sentence, elapsed_time):
        words = sentence.split()
        num_words = len(words)
        words_per_minute = (num_words / elapsed_time) * 60
        return words_per_minute

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()

