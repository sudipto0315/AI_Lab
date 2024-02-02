import numpy as np

# Generate a random coefficient matrix A (3x3)
A = np.random.rand(3, 3)

# Generate a random vector b (3x1)
b = np.random.rand(3, 1)

# Solve the system of linear equations Ax = b
x = np.linalg.solve(A, b)

# Display the results
print("Coefficient Matrix A:")
print(A)

print("\nVector b:")
print(b)

print("\nSolution x:")
print(x)
