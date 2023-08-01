import tkinter as tk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.books = []

        self.label_title = tk.Label(root, text="Library Management System", font=("Helvetica", 20, "bold"))
        self.label_title.pack(pady=20)

        self.label_book_name = tk.Label(root, text="Book Name:")
        self.label_book_name.pack()
        self.entry_book_name = tk.Entry(root, font=("Helvetica", 14))
        self.entry_book_name.pack()

        self.label_author = tk.Label(root, text="Author:")
        self.label_author.pack()
        self.entry_author = tk.Entry(root, font=("Helvetica", 14))
        self.entry_author.pack()

        self.button_add = tk.Button(root, text="Add Book", command=self.add_book)
        self.button_add.pack(pady=10)

        self.listbox_books = tk.Listbox(root, font=("Helvetica", 14), width=50, height=10)
        self.listbox_books.pack()

    def add_book(self):
        book_name = self.entry_book_name.get()
        author = self.entry_author.get()

        if book_name and author:
            self.books.append({"Book Name": book_name, "Author": author})
            self.update_books_list()
            self.clear_inputs()
            messagebox.showinfo("Success", "Book added successfully.")
        else:
            messagebox.showerror("Error", "Please enter both Book Name and Author.")

    def update_books_list(self):
        self.listbox_books.delete(0, tk.END)
        for book in self.books:
            self.listbox_books.insert(tk.END, f"{book['Book Name']} - {book['Author']}")

    def clear_inputs(self):
        self.entry_book_name.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()

