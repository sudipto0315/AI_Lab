import pandas as pd
data={'Student_Name':['Tom','Jerry','Mickey','Donald','Popeye'],
      'Roll_No':[1,2,3,4,5],
      'CPI':[75.5,85.2,58.9,92.7,60.2]}
df=pd.DataFrame(data)

# a)Selecting rows where 'CPI' is greater than 60
print(df[df['CPI']>60.0])

# Calculating overall mean, median, and standard deviation
print("Mean: ",df['CPI'].mean())
print("Median: ",df['CPI'].median())
print("Standard Deviation: ",df['CPI'].std())
