import tkinter as tk
from datetime import datetime

def update_time():
    current_time = datetime.now().strftime('%H:%M:%S')
    label_time.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Watch")

label_time = tk.Label(root, text="", font=("Helvetica", 40))
label_time.pack(pady=20)

update_time()

root.mainloop()

