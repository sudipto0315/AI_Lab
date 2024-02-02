import pandas as pd

# Assuming you have a DataFrame named 'time_df' with a column 'TimeStamp'
# containing DateTime format

# Creating a sample DataFrame
data = {'TimeStamp': ['2024-02-02 08:30:00', '2024-02-02 12:45:00', '2024-02-02 18:15:00']}
time_df = pd.DataFrame(data)
time_df['TimeStamp'] = pd.to_datetime(time_df['TimeStamp'])  # Convert to DateTime format

# Extracting the hour component and creating a new 'Hour' column
time_df['Hour'] = time_df['TimeStamp'].dt.hour

# Displaying the DataFrame with the new 'Hour' column
print("Original DataFrame:")
print(time_df)
