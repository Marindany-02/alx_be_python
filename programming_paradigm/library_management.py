class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """
        Initialize a book with a title, author, and default availability.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if it is available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class representing a library."""

    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private attribute to store book instances

    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): An instance of the Book class.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by its title.
        
        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                    return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Return a book by its title.
        
        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"'{title}' has been returned.")
                    return
        print(f"'{title}' is not currently checked out.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

