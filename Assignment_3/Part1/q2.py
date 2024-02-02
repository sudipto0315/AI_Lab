import pandas as pd
data={
    'Subject': ['Maths', 'Physics', 'Chemistry', 'Maths', 'Physics'],
    'Book_Author': ['Author1', 'Author2', 'Author3', 'Author4', 'Author5'],
    'No_of_Books': [10, 20, 15, 25, 30]
}
iiitg_library=pd.DataFrame(data)

# Calculating the total number of books for each subject across all book authors
totalBooksPerSubject=iiitg_library.groupby('Subject')['No_of_Books'].sum()

# Displaying the total number of books for each subject across all book authors
print(totalBooksPerSubject)