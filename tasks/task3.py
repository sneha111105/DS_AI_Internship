import pandas as pd

# Read dataset from CSV file
df = pd.read_csv("tasks\student_performance (1).csv")

# Display dataset
print("Original Dataset:")
print(df)

# Shape
print("\nShape of Dataset:")
print(df.shape)

# Missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df[df.duplicated()])

# Number of duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# Fill missing marks with column mean
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Reset index
df = df.reset_index(drop=True)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Verify duplicates
print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

# Final shape
print("\nFinal Shape:")
print(df.shape)