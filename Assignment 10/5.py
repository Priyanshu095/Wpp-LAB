import numpy as np

# Create a sample numpy array
arr = np.array(["apple", "banana", "cherry", "date", "elderberry"])

# Define a function to format the strings
def format_strings(array):
    centered = np.array([s.center(15, '_') for s in array])
    left_justified = np.array([s.ljust(15, '_') for s in array])
    right_justified = np.array([s.rjust(15, '_') for s in array])
    return centered, left_justified, right_justified

# Format the strings
centered, left_justified, right_justified = format_strings(arr)

# Print the results
print("Original Array:")
print(arr)
print("\nCentered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)