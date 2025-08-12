
class Book:
    """A class to represent a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  

    def __str__(self):
        """A special method to return a string representation of the object."""
        return f'"{self.title}" by {self.author}'


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
  
        self.books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        self.books.append(book)
        print(f'Added book: {book}')

    def show_available_books(self):
        """Prints a list of all available books."""
        print("\n--- Available Books ---")
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            for book in available_books:
                print(f'- {book}')
        else:
            print("No books are currently available.")

    def borrow_book(self, title):
        """Marks a book as unavailable if found."""
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f'\nSuccessfully borrowed "{book.title}".')
                return
        print(f'\nSorry, the book "{title}" is not available or does not exist.')

    def return_book(self, title):
        """Marks a book as available if found and was previously borrowed."""
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                print(f'\nSuccessfully returned "{book.title}".')
                return
        print(f'\nCannot return "{title}". It was not borrowed from this library.')




if __name__ == '__main__':
    my_library = Library()

    my_library.add_book(Book("Galaxy", "Douglas Adams"))
    my_library.add_book(Book("Laynas life", "Frank Herbert"))
    my_library.add_book(Book("1948", "George Orwell"))

    while True:
        print("\n--- Library Menu ---")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Show available books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            new_book = Book(title, author)
            my_library.add_book(new_book)
        
        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            my_library.borrow_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            my_library.return_book(title)
        
        elif choice == '4':
            my_library.show_available_books()

        elif choice == '5':
            print("Thank you for using the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
