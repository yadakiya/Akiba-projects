class Rectangle:
    # Constructor initializes length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Calculate rectangle area
    def area(self):
        return self.length * self.width

    # Calculate rectangle perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)


# Create two rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

print("\n========== TASK 2 ==========")

print("Rectangle 1")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

print("\nRectangle 2")
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())