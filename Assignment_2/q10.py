import numpy as np

# i. Create a 4x5 matrix with values ranging from 1 to 20
matrix = np.arange(1, 21).reshape(4, 5)
print("Matrix:\n", matrix)

# ii. Create an array of 10 zeros,10 ones, 10 fives
zeros = np.zeros(10)
ones = np.ones(10)
fives = np.ones(10) * 5
print("Zeros: ", zeros)
print("Ones: ", ones)
print("Fives: ", fives)

# iii. Create an array of all the even integers from 10 to 50
evens = np.arange(10, 51, 2)
print("Evens: ", evens)

# iv. Generate a random number between 0 and 1
random_num = np.random.rand()
print("Random number: ", random_num)

# v. Save the matrix to a text file and load it
np.savetxt('Assignment_2/matrix.txt', matrix, fmt='%d') # fmt='%d' to save as integers
loaded_matrix = np.loadtxt('matrix.txt')
print("Loaded matrix:\n", loaded_matrix)