import numpy as np

# Assuming you have a 2D NumPy array of size 5x6
# Creating a sample 2D array
arr_2d = np.array([[1, 2, 3, 2, 1, 4],
                   [5, 6, 5, 4, 6, 7],
                   [8, 9, 8, 8, 7, 7],
                   [3, 2, 1, 4, 5, 6],
                   [1, 2, 3, 4, 5, 6]])

# Flatten the 2D array
arr_flat = arr_2d.flatten()

# Find unique values and their counts
unique_values, counts = np.unique(arr_flat, return_counts=True) # return_counts=True returns the counts of each unique value

# Displaying the results
print("Original 2D Array:")
print(arr_2d)

print("\nFlattened Array:")
print(arr_flat)

print("\nUnique Values:")
print(unique_values)

print("\nCounts:")
print(counts)
