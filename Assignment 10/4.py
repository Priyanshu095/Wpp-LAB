import numpy as np

N = int(input("Enter the number of points (N >= 10): "))
cartesian_points = np.array([list(map(float, input(f"Enter x and y for point {i+1}: ").split())) for i in range(N)])

r = np.sqrt(cartesian_points[:, 0]**2 + cartesian_points[:, 1]**2)
theta = np.arctan2(cartesian_points[:, 1], cartesian_points[:, 0])

polar_coordinates = np.column_stack((r, theta))
print("\nPolar Coordinates:\n", polar_coordinates)
