"""Library class: stores, searches, adds, and removes books."""


class Library:
    def __init__(self, name="Akiba Library"):
        self.name = name
        self.__books = {}  # ISBN -> Book object

    def add_book(self, book):
        from book import Book

        if not isinstance(book, Book):
            print("Error: only Book objects can be added.")
            return False
        if book.isbn in self.__books:
            print("A book with this ISBN already exists.")
            return False

        self.__books[book.isbn] = book
        print(f'"{book.title}" was added to the library.')
        return True

    def remove_book(self, isbn):
        book = self.__books.get(isbn)
        if book is None:
            print("Book not found.")
            return False
        if not book.is_available:
            print("This book is currently borrowed and cannot be removed.")
            return False

        del self.__books[isbn]
        print(f'"{book.title}" was removed from the library.')
        return True

    def search_book(self, search_term):
        term = search_term.strip().lower()
        results = [
            book for book in self.__books.values()
            if term in book.title.lower()
            or term in book.author.lower()
            or term == book.isbn.lower()
        ]

        if results:
            print("\nSearch results:")
            for book in results:
                print(book)
        else:
            print("No matching books found.")
        return results

    def display_books(self):
        print(f"\n========== {self.name.upper()} ==========")
        if not self.__books:
            print("There are no books in the library.")
            return

        for number, book in enumerate(self.__books.values(), start=1):
            print(f"{number}. {book}")

    def get_book(self, isbn):
        """Find a book by ISBN; used by the member borrowing workflow."""
        return self.__books.get(isbn)

    @property
    def books(self):
        """Return a copy so callers cannot modify the internal dictionary."""
        return self.__books.copy()
