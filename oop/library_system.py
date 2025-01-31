# library_system.py

# Base class for Book
class Book:
    def __init__(self, title, author):
        """Initialize Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of Book."""
        return f"Book: {self.title} by {self.author}"

# Derived class for EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file_size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation of EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page_count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class to demonstrate composition
class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)

