import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.Entry(root, font="Helvetica 20 bold")
entry.pack(fill=tk.X, ipadx=8, padx=10, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row, col = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="Helvetica 18 bold", padx=20, pady=20)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

root.mainloop()

