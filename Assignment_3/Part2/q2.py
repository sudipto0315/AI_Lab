import numpy as np

# Assuming you have a 2D NumPy array named 'arr'
# Creating a sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Extracting the second column and the last row
second_column = arr[:, 1]
last_row = arr[-1, :]

# Displaying the extracted parts
print("Original Array:")
print(arr)

print("\nSecond Column:")
print(second_column)

print("\nLast Row:")
print(last_row)
