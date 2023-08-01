class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.borrowers = {}

    def add_book(self, book_id, book_name, author, quantity):
        if book_id not in self.books:
            self.books[book_id] = {"Book Name": book_name, "Author": author, "Quantity": quantity, "Borrowed": 0}
            print("Book added successfully.")
        else:
            print("Book with the same ID already exists. Please enter a different Book ID.")

    def display_books(self):
        print("\nBooks in the Library:")
        for book_id, book in self.books.items():
            print(f"ID: {book_id}, Name: {book['Book Name']}, Author: {book['Author']}, Quantity: {book['Quantity']}, Borrowed: {book['Borrowed']}")

    def search_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            print(f"\nBook Found - ID: {book_id}, Name: {book['Book Name']}, Author: {book['Author']}, Quantity: {book['Quantity']}, Borrowed: {book['Borrowed']}")
        else:
            print("Book not found in the Library.")

    def borrow_book(self, book_id, borrower_name):
        if book_id in self.books:
            book = self.books[book_id]
            if book['Quantity'] > book['Borrowed']:
                book['Borrowed'] += 1
                self.borrowers[book_id] = borrower_name
                print("Book borrowed successfully.")
            else:
                print("All copies of this book are already borrowed.")
        else:
            print("Book not found in the Library.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book['Borrowed'] > 0:
                book['Borrowed'] -= 1
                self.borrowers.pop(book_id, None)
                print("Book returned successfully.")
            else:
                print("This book is not currently borrowed.")
        else:
            print("Book not found in the Library.")

if __name__ == "__main__":
    library = LibraryManagementSystem()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")
            author = input("Enter Author: ")
            quantity = int(input("Enter Quantity: "))
            library.add_book(book_id, book_name, author, quantity)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            book_id = input("Enter Book ID to search: ")
            library.search_book(book_id)

        elif choice == '4':
            book_id = input("Enter Book ID to borrow: ")
            borrower_name = input("Enter Borrower Name: ")
            library.borrow_book(book_id, borrower_name)

        elif choice == '5':
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == '6':
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

