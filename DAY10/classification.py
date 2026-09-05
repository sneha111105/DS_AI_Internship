import pandas as pd

# Load dataset
df = pd.read_csv("DAY10\Student_Career_Success_Prediction.csv")

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

# Classification label
y = df["Career_Success"]

print("Features:")
print(X.head())

print("\nClassification Label:")
print(y.head())