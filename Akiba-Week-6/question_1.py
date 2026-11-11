"""Question 1: Classes, objects, constructors, and methods."""


class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")

    def introduce(self):
        print(
            f"Hello! My name is {self.name}. "
            f"I study {self.department}."
        )


if __name__ == "__main__":
    student1 = Student("Yadeni Getu", "7202/16", "Software Engineering")
    student2 = Student("Abebe Kebede", "7101/16", "Computer Science")
    student3 = Student("Sara Alemu", "7305/16", "Information Technology")

    for student in (student1, student2, student3):
        student.display_info()
        student.introduce()
        print("-" * 40)
