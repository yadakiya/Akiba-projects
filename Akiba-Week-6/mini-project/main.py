"""Menu-driven command-line Library Management System."""

from book import Book
from library import Library
from member import StudentMember, TeacherMember


def show_menu():
    print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Register Member")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Display Members")
    print("8. Exit")


def main():
    library = Library()
    members = {}  # Member ID -> Member object

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()

            try:
                library.add_book(Book(title, author, isbn))
            except ValueError as error:
                print(f"Could not add book: {error}")

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            search_term = input("Enter title, author, or ISBN: ")
            library.search_book(search_term)

        elif choice == "4":
            name = input("Enter member name: ").strip()
            member_id = input("Enter a unique member ID: ").strip()

            if member_id in members:
                print("A member with that ID already exists.")
                continue

            print("1. Student Member (borrowing limit: 3)")
            print("2. Teacher Member (borrowing limit: 5)")
            member_type = input("Choose member type: ").strip()

            if member_type == "1":
                member = StudentMember(name, member_id)
            elif member_type == "2":
                member = TeacherMember(name, member_id)
            else:
                print("Invalid member type.")
                continue

            members[member_id] = member
            print(f"{member.name} registered successfully.")

        elif choice == "5":
            member_id = input("Enter member ID: ").strip()
            member = members.get(member_id)

            if member is None:
                print("Member not found. Please register first.")
                continue

            isbn = input("Enter book ISBN: ").strip()
            member.borrow_book(library, isbn)

        elif choice == "6":
            member_id = input("Enter member ID: ").strip()
            member = members.get(member_id)

            if member is None:
                print("Member not found.")
                continue

            isbn = input("Enter book ISBN to return: ").strip()
            member.return_book(isbn)

        elif choice == "7":
            if not members:
                print("No registered members.")
            else:
                for member in members.values():
                    print("\n------------------------------")
                    member.display_member_info()
                    if member.borrowed_books:
                        print("Borrowed books:")
                        for book in member.borrowed_books:
                            print(f"- {book.title} (ISBN: {book.isbn})")

        elif choice == "8":
            print("Thank you for using the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
