import numpy as np

# Create two random arrays of dimension 3x3
array1 = np.random.rand(3, 3)
array2 = np.random.rand(3, 3)

# i. Concatenate two arrays
concatenated = np.concatenate((array1, array2))
print("Concatenated array:")
print(concatenated)

# ----------------------------------------
print()
# ----------------------------------------

# ii. Sort both the arrays
sorted_array1 = np.sort(array1, axis=None)
sorted_array2 = np.sort(array2, axis=None)
print("Sorted array1:")
print(sorted_array1)
print("Sorted array2:")
print(sorted_array2)

# ----------------------------------------
print()
# ----------------------------------------

# iii. Add the two arrays
added = np.add(array1, array2)
print("Added array:")
print(added)

# ----------------------------------------
print()
# ----------------------------------------

# iv. Subtract the two arrays
subtracted = np.subtract(array1, array2)
print("Subtracted array:")
print(subtracted)

# ----------------------------------------
print()
# ----------------------------------------

# v. Multiply two arrays
multiplied = np.multiply(array1, array2)
print("Multiplied array:")
print(multiplied)

# ----------------------------------------
print()
# ----------------------------------------

# vi. Divide the two arrays
divided = np.divide(array1, array2)
print("Divided array:")
print(divided)

# ----------------------------------------