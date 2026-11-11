"""Question 4: Polymorphism and abstraction."""

from abc import ABC, abstractmethod
from math import pi


# Part A: Polymorphism
class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Cow:
    def make_sound(self):
        return "Moo!"


# Part B: Abstraction
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        """Return the area of the shape."""
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2


if __name__ == "__main__":
    print("Part A: Polymorphism")
    animals = [Dog(), Cat(), Cow()]

    for animal in animals:
        print(animal.make_sound())

    print("\nPart B: Abstraction")
    shapes = [Rectangle(5, 3), Circle(4)]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.calculate_area():.2f}")
