'''Create a base class "Shape" with methods to calculate the area and perimeter. Implement
derived classes "Rectangle" and "Circle" that inherit from "Shape" and provide their own area
and perimeter calculations.'''

import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle = Rectangle(length, width)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
