import pandas as pd
import numpy as np

# Create student performance dataset
data = {
    "Student_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115,
        103
    ],
    "Name": [
        "Rahul", "Priya", "Arjun", "Sneha", "Kiran",
        "Anjali", "Vikram", "Neha", "Rohan", "Pooja",
        "Amit", "Divya", "Manoj", "Kavya", "Suresh",
        "Arjun"
    ],
    "Maths": [
        85, 90, np.nan, 76, 88,
        92, 79, 95, np.nan, 84,
        73, 89, 91, 78, 86,
        78
    ],
    "Science": [
        88, 92, 85, np.nan, 90,
        94, 81, 96, 87, np.nan,
        75, 91, 89, 80, 88,
        85
    ],
    "English": [
        82, 89, 80, 75, np.nan,
        91, 78, 94, 86, 83,
        72, 90, 88, np.nan, 85,
        80
    }
}

df = pd.DataFrame(data)

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

print("\nCleaned Dataset:")
print(df)

# Verify missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

print("\nFinal Shape:")
print(df.shape)