original_marks = [75, 80, 65, 90, 85]


shared_reference = original_marks

# copy() creates a separate, independent list.
copied_marks = original_marks.copy()

# Add a new mark to the copied list only.
copied_marks.append(95)

print("Original marks:", original_marks)
print("Shared reference:", shared_reference)
print("Copied marks:", copied_marks)

print()
print("Original and shared reference are identical:",
      original_marks is shared_reference)
print("Original and copied lists have equal values:",
      original_marks == copied_marks)
print("Original and copied lists are identical:",
      original_marks is copied_marks)
