import pandas as pd

# Create Pandas Series
marks = pd.Series(
    [85, 92, 78, 88, 95],
    index=["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
)

print("Student Marks:")
print(marks)

# Access using position
print("\nMarks using position:")
print("First subject:", marks.iloc[0])
print("Third subject:", marks.iloc[2])

# Access using labels
print("\nMarks using labels:")
print("Mathematics:", marks["Mathematics"])
print("Computer Science:", marks["Computer Science"])

# Access multiple values
print("\nMultiple subjects:")
print(marks[["Physics", "English"]])