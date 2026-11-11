"""Question 3: Inheritance, method overriding, and super()."""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"Salary: {self.salary:.2f}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print("Manager information")
        super().display_info()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print("Developer information")
        super().display_info()
        print(f"Programming language: {self.programming_language}")


if __name__ == "__main__":
    manager = Manager("Mekdes", 45000, "Human Resources")
    developer = Developer("Dawit", 40000, "Python")

    manager.display_info()
    print("-" * 40)
    developer.display_info()
