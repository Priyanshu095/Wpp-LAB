'''Create a class for representing any 2-D point or vector. The methods inside this class include
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for
calculating the distance between two vectors, dot product, cross product of two vectors. Extend
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.'''

import math
 
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
 
    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector2D(x, y)
 
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
 
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y
 
    def cross_product(self, other):
        return self.x * other.y - self.y * other.x
    
    def display(self):
        print(f"({self.x}, {self.y})") 
    
class Vector3D(Vector2D) :      
      
        
        