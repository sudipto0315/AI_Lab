import numpy as np

# Create a random matrix of size 8x7
matrix = np.random.rand(8, 7)

# Find the maximum value from each feature
max_values = np.max(matrix, axis=0)

# Find the minimum value from each feature
min_values = np.min(matrix, axis=0)

print("Matrix:\n", matrix)
print("Max values: ", max_values)
print("Min values: ", min_values)