# ============================================================
# Akiba Technologies - Week 4
# Mutability, References, and Memory Model in Python
# ============================================================

# ------------------------------------------------------------
# Question 1: Mutable and Immutable Objects
# ------------------------------------------------------------

# Lists are mutable: their contents can be changed in place.
# Strings are immutable: a string cannot be changed in place.
numbers = [1, 2, 3]
message = "Python"

print("\nQUESTION 1: MUTABLE AND IMMUTABLE OBJECTS")
print("Original list:", numbers)
numbers[0] = 100
print("Modified list:", numbers)

print("Original string:", message)
message = message + " Programming"
print("New string:", message)

# Explanation:
# The list itself was modified. With the string, concatenation
# created a new string object and message was assigned to it.


# ------------------------------------------------------------
# Question 2: References and Object Identity
# ------------------------------------------------------------

a = [10, 20, 30]
b = a
c = [10, 20, 30]

print("\nQUESTION 2: REFERENCES AND OBJECT IDENTITY")
print("a is b:", a is b)
print("a is c:", a is c)
print("a == c:", a == c)

# Expected output:
# a is b: True
# a is c: False
# a == c: True
#
# is checks whether two variables refer to the same object.
# == checks whether their values are equal.
# a and c are separate list objects containing equal values.


# ------------------------------------------------------------
# Question 3: Shared References and Side Effects
# ------------------------------------------------------------

numbers = [1, 2, 3]
values = numbers

values.append(4)

print("\nQUESTION 3: SHARED REFERENCES")
print("numbers:", numbers)
print("values:", values)

# Expected output:
# numbers: [1, 2, 3, 4]
# values: [1, 2, 3, 4]
#
# Both variables refer to the same list. Therefore, a change
# made through values is visible through numbers.

# Use copy() to create an independent list:
numbers = [1, 2, 3]
values = numbers.copy()
values.append(4)

print("After making a copy:")
print("numbers:", numbers)
print("values:", values)

# Expected output:
# numbers: [1, 2, 3]
# values: [1, 2, 3, 4]


# ------------------------------------------------------------
# Question 4: Function Arguments and Mutability
# ------------------------------------------------------------

def update_list(items):
    items.append(100)

scores = [50, 60, 70]
update_list(scores)

print("\nQUESTION 4: FUNCTION ARGUMENTS AND MUTABILITY")
print("After update_list:", scores)

# Expected output: [50, 60, 70, 100]
#
# The function receives a reference to the same list object.
# append() mutates that original list.

def create_updated_list(items):
    new_items = items.copy()
    new_items.append(100)
    return new_items

original_scores = [50, 60, 70]
new_scores = create_updated_list(original_scores)

print("Original scores:", original_scores)
print("New scores:", new_scores)

# Expected output:
# Original scores: [50, 60, 70]
# New scores: [50, 60, 70, 100]


# ------------------------------------------------------------
# Question 5: Memory Management and Garbage Collection
# ------------------------------------------------------------

print("\nQUESTION 5: MEMORY MANAGEMENT")

first_reference = ["red", "green", "blue"]
second_reference = first_reference

print("Before del:")
print("first_reference:", first_reference)
print("second_reference:", second_reference)
print("Same object:", first_reference is second_reference)

del first_reference

print("After del first_reference:")
print("second_reference:", second_reference)

# del removes the variable name/reference; it does not
# necessarily destroy the object.
# The list remains available because second_reference still
# refers to it. When an object has no remaining references,
# it becomes eligible for cleanup. CPython primarily uses
# reference counting and also has a cyclic garbage collector
# to detect groups of objects that refer to one another.
