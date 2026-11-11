# Library Management System

A menu-driven command-line library application built with Python and object-oriented programming.

## Features

- Add, remove, display, and search for books (remove is supported by the `Library` class).
- Register student and teacher members.
- Borrow and return books.
- Prevent borrowing unavailable books.
- Prevent returning books that the member did not borrow.
- Enforce different borrowing limits through overridden `get_borrowing_limit()` methods: students can borrow 3 books; teachers can borrow 5.

## Files

- `book.py`: Book model and availability state.
- `library.py`: Library collection and book operations.
- `member.py`: Member, StudentMember, and TeacherMember.
- `main.py`: Interactive command-line menu.

## Run

Open a terminal in this `mini_project` directory and run:

```bash
python main.py
```

Use menu option 1 to add books before borrowing them. Register a member with option 4, then borrow and return books using options 5 and 6.

## OOP concepts demonstrated

- Classes, objects, constructors, attributes, and instance methods.
- Encapsulation through private collections and controlled availability updates.
- Inheritance through `StudentMember` and `TeacherMember`.
- Method overriding: `StudentMember` and `TeacherMember` each override `get_borrowing_limit()`.
- `super()` to initialize the parent `Member`.
- Polymorphism: both member types can be handled through the common `Member` interface while using their own borrowing limits.
- Composition/object relationships: a `Library` stores `Book` objects, and a `Member` stores borrowed `Book` objects.
