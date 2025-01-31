# polymorphism_demo.py
import math

# Base class Shape
class Shape:
    def area(self):
        """Method to be overridden in derived classes."""
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate the area of a rectangle."""
        return self.length * self.width

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override area method to calculate the area of a circle."""
        return math.pi * (self.radius ** 2)

