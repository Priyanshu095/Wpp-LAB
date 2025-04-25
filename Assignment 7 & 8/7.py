import math

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_x(self):
        return math.degrees(math.atan2(self.y, self.x))

    def dist(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return f"({self.x}, {self.y})"

class Vec3D(Vec2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def dist(self, other):
        return math.sqrt((other.x - self.x) ** 2 + 
                         (other.y - self.y) ** 2 + 
                         (other.z - self.z) ** 2)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vec3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Input for 2D vectors
x1, y1 = map(float, input("Enter first 2D vector (x y): ").split())
x2, y2 = map(float, input("Enter second 2D vector (x y): ").split())

v1 = Vec2D(x1, y1)
v2 = Vec2D(x2, y2)

print("\n2D Vector Operations:")
print(f"Vector 1: {v1}, Vector 2: {v2}")
print(f"Magnitude of v1: {v1.mag():.2f}")
print(f"Angle with X-axis of v1: {v1.angle_x():.2f} degrees")
print(f"Distance between v1 and v2: {v1.dist(v2):.2f}")
print(f"Dot Product: {v1.dot(v2):.2f}")
print(f"Cross Product: {v1.cross(v2):.2f}")

# Input for 3D vectors
x3, y3, z3 = map(float, input("\nEnter first 3D vector (x y z): ").split())
x4, y4, z4 = map(float, input("Enter second 3D vector (x y z): ").split())

v3 = Vec3D(x3, y3, z3)
v4 = Vec3D(x4, y4, z4)

print("\n3D Vector Operations:")
print(f"Vector 1: {v3}, Vector 2: {v4}")
print(f"Magnitude of v3: {v3.mag():.2f}")
print(f"Distance between v3 and v4: {v3.dist(v4):.2f}")
print(f"Dot Product: {v3.dot(v4)::.2f}")

cross3d = v3.cross(v4)
print(f"Cross Product: {cross3d}")

