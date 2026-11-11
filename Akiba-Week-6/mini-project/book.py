"""Book model for the Library Management System."""


class Book:
    def __init__(self, title, author, isbn):
        if not title.strip() or not author.strip() or not isbn.strip():
            raise ValueError("Title, author, and ISBN are required.")

        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.__is_available = True

    @property
    def is_available(self):
        """Read-only access to the book's availability."""
        return self.__is_available

    def update_availability(self, is_available):
        if not isinstance(is_available, bool):
            raise TypeError("Availability must be True or False.")
        self.__is_available = is_available

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {status}")

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"
