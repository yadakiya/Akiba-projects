class Student:
    # Constructor initializes student information
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # Method to display student information
    def display_info(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("-" * 30)


# Create three student objects
student1 = Student("Abebe", 21, "Software Engineering")
student2 = Student("Hana", 22, "Computer Science")
student3 = Student("Dawit", 20, "Information Technology")

# Display information of all students
print("\n========== TASK 1 ==========")
student1.display_info()
student2.display_info()
student3.display_info()