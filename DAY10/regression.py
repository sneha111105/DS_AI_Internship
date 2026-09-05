import pandas as pd

# Load dataset
df = pd.read_csv("DAY10\Student_Career_Success_Prediction.csv")
print(df)
# 7 features
features = [
    "CGPA",
    "Internships",
    "Projects",
    "Certifications",
    "Technical_Skills",
    "Communication_Skills",
    "Aptitude_Score"
]

# Features
X = df[features]

# Regression label
y = df["Placement_Package"]

print("Features:")
print(X.head())

print("\nRegression Label (placement package ):")
print(y.head())

