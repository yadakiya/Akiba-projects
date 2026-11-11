class StudentScore:
    # Class attribute shared by all student objects
    school_name = "Akiba Academy"

    def __init__(self, name, score, department):
        # Instance attributes
        self.name = name
        self.score = score
        self.department = department

    def display(self):
        print("School:", self.school_name)
        print("Name:", self.name)
        print("Score:", self.score)
        print("Department:", self.department)
        print("-" * 30)


# Create three student objects
score_student1 = StudentScore("Abebe", 75, "Software Engineering")
score_student2 = StudentScore("Hana", 85, "Computer Science")
score_student3 = StudentScore("Dawit", 90, "Information Technology")

print("\n========== TASK 3 ==========")

# Display original scores
score_student1.display()
score_student2.display()
score_student3.display()

# Update only the first student's score
score_student1.score = 95

print("After updating Abebe's score:")

score_student1.display()
score_student2.display()
score_student3.display()