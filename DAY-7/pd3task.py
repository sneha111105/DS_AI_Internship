import pandas as pd

# 1. Load the CSV file
df = pd.read_csv('C:\\Users\\Admin\\DS_AI_Internship\\DAY-7\\student_performance.csv')
print(df)

print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)
print("\nMissing Values Count:\n", df.isnull().sum())
print("\nDuplicate Rows Count:", df.duplicated().sum())
print("\n data info:",df.info())

#Remove Duplicate Rows
df = df.drop_duplicates().reset_index(drop=True)

#  Clean whitespace 
df['Name'] = df['Name'].astype(str).str.strip().str.title()

#Fill numeric columns 
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].mean())

# Fill percentage column with rounded mean
df['Attendance_%'] = df['Attendance_%'].fillna(round(df['Attendance_%'].mean(), 1))

# Fix Data Types
df['Student_ID'] = df['Student_ID'].astype(int)

# 6. Detect and Handle Outliers (Filtering realistic ranges, e.g., scores between 0 and 100)
df = df[(df['Math_Score'] >= 0) & (df['Math_Score'] <= 100)]
df = df[(df['Science_Score'] >= 0) & (df['Science_Score'] <= 100)]

print("\n Cleaned Dataset ")
print(df)
print("\nFinal Shape:", df.shape)

#