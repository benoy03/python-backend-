class Book:
    """A class representing a book with title, author, and ISBN."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        """Returns a formatted string with book details."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    """A class to manage a collection of Book objects."""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self.books.append(book)
        print(f"Added book: {book.title}")

    def remove_book(self, isbn):
        """Removes a book from the collection by its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed book with ISBN: {isbn}")
                return
        print(f"Book with ISBN {isbn} not found.")

    def list_books(self):
        """Returns a list of display_info strings for all books."""
        if not self.books:
            return ["No books in the library."]
        return [book.display_info() for book in self.books]


print("\n--- Exercise 4: Library System with User Input ---")
library = Library()
while True:
    print("\n--- Library Menu ---")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        new_book = Book(title, author, isbn)
        library.add_book(new_book)
    elif choice == '2':
        isbn = input("Enter the ISBN of the book to remove: ")
        library.remove_book(isbn)
    elif choice == '3':
        print("\n--- All Books ---")
        for info in library.list_books():
            print(info)
    elif choice == '4':
        print("Exiting library system.")
        break
    else:
        print("Invalid choice.")
print("-" * 25)
