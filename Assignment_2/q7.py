# Given array
array = [[10, 16, 71, 9], [71, 91, 31, 51]]

# Print the dimension of the array
dimension = len(array), len(array[0])
print("i. Dimension of the array:", dimension)

# Print the shape of the array
if len(array) == len(array[0]):
    print("ii. Square matrix")
else:
    print("ii. Rectangular matrix")

# Print the size of the array
size = sum(len(row) for row in array)
print("iii. Size of the array:", size)