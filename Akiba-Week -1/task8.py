
# Task 8: Exam Result Report

student_name = input("Enter student name: ")

python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
mathematics_score = float(input("Enter Mathematics score: "))

total_score = python_score + english_score + mathematics_score
average = total_score / 3

print("\n========================================")
print("             STUDENT RESULT")
print("========================================")

print(f"Student: {student_name}")
print()
print(f"Python:       {python_score:.2f}")
print(f"English:      {english_score:.2f}")
print(f"Mathematics:  {mathematics_score:.2f}")
print("----------------------------------------")
print(f"Total Score:  {total_score:.2f}")
print(f"Average:      {average:.2f}")
print("========================================")