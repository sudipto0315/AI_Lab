def transpose_and_flatten(matrix):
    # Calculate the transpose
    transpose_result = []
    for col in range(len(matrix[0])):
        transposed_row = []
        for row in range(len(matrix)):
            transposed_row.append(matrix[row][col])
        transpose_result.append(transposed_row)

    # Flatten the matrix
    flatten_result = []
    for row in matrix:
        for element in row:
            flatten_result.append(element)

    return transpose_result, flatten_result

# Take user input for the matrix size
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# Take user input for the matrix elements
matrix = []
for i in range(num_rows):
    row = [int(x) for x in input("Enter space-separated elements for row {}: ".format(i + 1)).split()]
    matrix.append(row)

# Call the function
transpose_result, flatten_result = transpose_and_flatten(matrix)

# Print the results
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose_result:
    print(row)


print("\nFlattened Matrix:")
print(flatten_result)