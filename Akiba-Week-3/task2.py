
def validate_student_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False


def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    total = 0

    for student in students:
        total += student["score"]

    if len(students) == 0:
        return 0

    return total / len(students)


def find_highest_score(students):
    if len(students) == 0:
        return None

    highest = students[0]["score"]

    for student in students:
        if student["score"] > highest:
            highest = student["score"]

    return highest


def find_lowest_score(students):
    if len(students) == 0:
        return None

    lowest = students[0]["score"]

    for student in students:
        if student["score"] < lowest:
            lowest = student["score"]

    return lowest


def count_passed_students(students):
    passed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1

    return passed


def count_failed_students(students):
    failed = 0

    for student in students:
        if student["score"] < 50:
            failed += 1

    return failed


def find_above_average_students(students):
    average = calculate_average(students)
    above_average = []

    for student in students:
        if student["score"] > average:
            above_average.append(student)

    return above_average


def generate_class_report(students):
    # Validate all student scores
    for student in students:
        if not validate_student_score(student["score"]):
            raise ValueError(
                f"Invalid score for {student['name']}: "
                f"{student['score']}. Score must be 0-100."
            )

    # Calculate class statistics
    average = calculate_average(students)
    highest = find_highest_score(students)
    lowest = find_lowest_score(students)
    passed = count_passed_students(students)
    failed = count_failed_students(students)
    above_average = find_above_average_students(students)

    # Print the report
    print("=" * 45)
    print("       STUDENT PERFORMANCE REPORT")
    print("=" * 45)

    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        status = "PASS" if score >= 50 else "FAIL"

        print(
            f"Name: {name:<10} "
            f"Score: {score:>3}  "
            f"Grade: {grade}  "
            f"Status: {status}"
        )

    print("-" * 45)
    print(f"Number of students: {len(students)}")
    print(f"Class average:      {average:.2f}")
    print(f"Highest score:      {highest}")
    print(f"Lowest score:       {lowest}")
    print(f"Students passed:    {passed}")
    print(f"Students failed:    {failed}")

    print("\nStudents above the class average:")
    for student in above_average:
        print(f"- {student['name']}: {student['score']}")

    print("=" * 45)

    # Return the report data for future use
    return {
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "above_average": above_average
    }


# Student data
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

# Generate the report
try:
    report = generate_class_report(students)
except ValueError as error:
    print("Error:", error)
