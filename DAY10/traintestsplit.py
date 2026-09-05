import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("DAY10\Student_Career_Success_Prediction.csv")

# Select 7 features
features = [
    "CGPA",
    "Internships",
    "Projects",
    "Certifications",
    "Technical_Skills",
    "Communication_Skills",
    "Aptitude_Score"
]

# Separate features and label
X = df[features]
y = df["Career_Success"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Verify sizes
print("Original dataset:", df.shape)

print("X_train size:", X_train.shape)
print("X_test size:", X_test.shape)

print("y_train size:", y_train.shape)
print("y_test size:", y_test.shape)