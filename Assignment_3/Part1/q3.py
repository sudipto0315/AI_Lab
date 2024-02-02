import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read an image using matplotlib
image_path = 'Assignment_3/Part1/pic.jpg'
img=plt.imread(image_path)

# Display the image
plt.imshow(img)
plt.title('Original Image')
plt.show()

# Convert the image to a matrix
img_matrix = np.array(img)

# save the matrix to a csv file using pandas
df = pd.DataFrame(img_matrix.reshape(-1, img_matrix.shape[-1]), columns=[f'Pixel_{i}' for i in range(img_matrix.shape[-1])])
df.to_csv('Assignment_3/Part1/pic.csv', index=False)

# Import Excel data from the CSV file excluding the last row and last column
df_excel = pd.read_csv('Assignment_3/Part1/pic.csv')
df_excel = df_excel.iloc[:-1, :-1] # Exclude the last row and last column

# Save the modified Excel data to a new Excel file
df_excel.to_excel('Assignment_3/Part1/pic.xlsx', index=False)