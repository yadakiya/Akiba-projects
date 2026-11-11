"""Library members and specialized member types."""


class Member:
    def __init__(self, name, member_id):
        if not name.strip() or not member_id.strip():
            raise ValueError("Member name and ID are required.")

        self.name = name.strip()
        self.member_id = member_id.strip()
        self.__borrowed_books = []

    def get_borrowing_limit(self):
        """Default borrowing limit; child classes override this method."""
        return 2

    @property
    def borrowed_books(self):
        # Return a copy to protect the member's internal collection.
        return self.__borrowed_books.copy()

    def borrow_book(self, library, isbn):
        book = library.get_book(isbn)

        if book is None:
            print("Borrowing failed: book not found in this library.")
            return False
        if not book.is_available:
            print("Borrowing failed: this book is already borrowed.")
            return False
        if len(self.__borrowed_books) >= self.get_borrowing_limit():
            print(
                f"Borrowing failed: {self.__class__.__name__} "
                f"can borrow at most {self.get_borrowing_limit()} books."
            )
            return False

        book.update_availability(False)
        self.__borrowed_books.append(book)
        print(f'{self.name} borrowed "{book.title}".')
        return True

    def return_book(self, isbn):
        for book in self.__borrowed_books:
            if book.isbn == isbn:
                self.__borrowed_books.remove(book)
                book.update_availability(True)
                print(f'{self.name} returned "{book.title}".')
                return True

        print("Return failed: this member did not borrow that book.")
        return False

    def display_member_info(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print(f"Member type: {self.__class__.__name__}")
        print(f"Borrowing limit: {self.get_borrowing_limit()}")
        print(f"Currently borrowed: {len(self.__borrowed_books)}")


class StudentMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 3


class TeacherMember(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)

    def get_borrowing_limit(self):
        return 5
