Akiba Technologies - Week 4 Python Assignment
Assignment: Mutability, References, and Memory Model in Python  
Student: Yadeni Getu Fufa
Files
`questions.py` — Demonstrations and code for Questions 1–5.
`student_marks_manager.py` — Student Marks Manager mini-project.
Question 1: Mutable and Immutable Objects
A mutable object can be changed after it is created. A Python list is
mutable, so we can replace, add, or remove its elements. An immutable
object cannot be changed after creation. A string is immutable. An
operation such as string concatenation creates a new string rather
than changing the original string object.
In `questions.py`, changing `numbers[0]` changes the existing list.
Concatenating text creates a new string and assigns it to `message`.
Question 2: References and Object Identity
Expected output:
```text
a is b: True
a is c: False
a == c: True
```
`is` checks object identity: whether two variables refer to the exact
same object. `==` checks value equality. `b = a` makes `b` refer to
the same list as `a`. The expression `c = [10, 20, 30]` creates a
separate list with equal contents, so `a == c` is true but `a is c`
is false.
Question 3: Shared References and Side Effects
Expected output before copying:
```text
numbers: [1, 2, 3, 4]
values: [1, 2, 3, 4]
```
`values = numbers` does not create another list. Both names refer to
one list object. Therefore, appending through `values` also changes
what we see through `numbers`.
To avoid this, use `values = numbers.copy()`. This creates a separate
list, so appending to `values` does not change `numbers`.
Question 4: Function Arguments and Mutability
The first example prints:
```text
[50, 60, 70, 100]
```
The function receives a reference to the same mutable list. Calling
`append()` changes that list object, so the caller sees the change.
The second function copies the list first and returns the copy. Its
output is:
```text
Original scores: [50, 60, 70]
New scores: [50, 60, 70, 100]
```
The original list stays unchanged.
Question 5: Memory Management and Garbage Collection
Python stores objects in memory and variables hold references (names)
to those objects. `del variable` removes that name/reference; it does
not necessarily destroy the object. If another variable still refers
to the object, the object remains accessible.
When an object has no remaining references, it becomes eligible for
cleanup. CPython mainly uses reference counting and also has a cyclic
garbage collector to find unreachable cycles of objects. Exact cleanup
timing should not be relied upon in application code.
Mini-Project: Student Marks Manager
The project creates five marks, assigns a second name to the same
original list, and creates an independent copy using `.copy()`.
It appends `95` only to the copied list.
Expected output:
```text
Original marks: [75, 80, 65, 90, 85]
Shared reference: [75, 80, 65, 90, 85]
Copied marks: [75, 80, 65, 90, 85, 95]

Original and shared reference are identical: True
Original and copied lists have equal values: False
Original and copied lists are identical: False
```
Project reflection
Why does modifying a shared reference affect the original list?  
Because both variable names refer to the same list object. A change
through either name changes that one object.
Why does modifying the copied list not affect the original list?  
Because `.copy()` creates a new list object. The two lists can be
changed independently. This is a shallow copy; for nested mutable
objects, inner objects may still be shared.
What is the difference between equality and identity?  
Equality (`==`) compares values. Identity (`is`) checks whether two
names refer to the same object.
How to run
Open a terminal in this folder and run:
```bash
python questions.py
python student_marks_manager.py
```
Both programs use only Python's standard library.