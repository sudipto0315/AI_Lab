import pandas as pd

# Assuming you have a DataFrame named 'dirty_data'
# with columns 'Name', 'Age', and 'Salary'

# Creating a sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Charlie'],
        'Age': [25, 17, 30, 16],
        'Salary': [50000, -1000, 75000, 2000]}

dirty_data = pd.DataFrame(data)

# Removing rows where 'Age' is less than 18 or 'Salary' is negative
clean_data = dirty_data[(dirty_data['Age'] >= 18) & (dirty_data['Salary'] >= 0)]

# Displaying the cleaned DataFrame
print("Original DataFrame:")
print(dirty_data)

print("\nCleaned DataFrame:")
print(clean_data)
