# ============================================================
# DAY 11 - LOAN APPROVAL PREDICTION
# Classification using Random Forest
# ============================================================

# 1. Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------
# 2. Read the CSV dataset
# ------------------------------------------------------------

df = pd.read_csv("DAY11\loan_approval_dataset.csv")

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nDATASET INFORMATION:")
df.info()

# ------------------------------------------------------------
# 3. Check the data
# ------------------------------------------------------------

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

print("\nLOAN STATUS COUNT:")
print(df["Loan_Status"].value_counts())

# ------------------------------------------------------------
# 4. Simple EDA
# ------------------------------------------------------------

print("\nNUMERICAL SUMMARY:")
print(df.describe())

# Visualize approved/rejected applications
df["Loan_Status"].value_counts().plot(kind="bar")
plt.title("Loan Approval Distribution")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")
plt.show()

# ------------------------------------------------------------
# 5. Convert categorical columns into numbers
# ------------------------------------------------------------

# Employment_Type:
# Salaried = 1
# Self-employed = 0

df["Employment_Type"] = df["Employment_Type"].map({
    "Salaried": 1,
    "Self-employed": 0
})

# Existing_Loan:
# Yes = 1
# No = 0

df["Existing_Loan"] = df["Existing_Loan"].map({
    "Yes": 1,
    "No": 0
})

# Target:
# Approved = 1
# Rejected = 0

df["Loan_Status"] = df["Loan_Status"].map({
    "Approved": 1,
    "Rejected": 0
})

# ------------------------------------------------------------
# 6. Select features and target
# ------------------------------------------------------------

# Applicant_ID is only an identifier.
# It should NOT be used as a predictive feature.

X = df[
    [
        "Income",
        "Credit_Score",
        "Loan_Amount",
        "Age",
        "Employment_Type",
        "Existing_Loan"
    ]
]

y = df["Loan_Status"]

# ------------------------------------------------------------
# 7. Split data into training and testing sets
# ------------------------------------------------------------

# 80% = training data
# 20% = testing data
#
# stratify=y keeps the Approved/Rejected proportion
# reasonably similar in train and test sets.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTRAINING SIZE:", X_train.shape)
print("TESTING SIZE:", X_test.shape)

# ------------------------------------------------------------
# 8. Create Random Forest model
# ------------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

# ------------------------------------------------------------
# 9. Train the model
# ------------------------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------------------------
# 10. Predictions
# ------------------------------------------------------------

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# ------------------------------------------------------------
# 11. Evaluate training and testing performance
# ------------------------------------------------------------

train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("\nTRAINING ACCURACY:", round(train_accuracy, 2))
print("TESTING ACCURACY:", round(test_accuracy, 2))

# ------------------------------------------------------------
# 12. Classification report
# ------------------------------------------------------------

print("\nCLASSIFICATION REPORT:")
print(classification_report(
    y_test,
    y_test_pred,
    target_names=["Rejected", "Approved"]
))

# ------------------------------------------------------------
# 13. Confusion matrix
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_test_pred)

print("\nCONFUSION MATRIX:")
print(cm)

ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Rejected", "Approved"]
).plot()

plt.title("Loan Approval - Confusion Matrix")
plt.show()

# ------------------------------------------------------------
# 14. Feature importance
# ------------------------------------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
}).sort_values(
    "Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE:")
print(importance)

importance.plot(
    x="Feature",
    y="Importance",
    kind="bar",
    legend=False
)

plt.title("Feature Importance")
plt.xlabel("Feature")
plt.ylabel("Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 15. Predict a NEW applicant
# ------------------------------------------------------------

# New applicant:
# Income = 60000
# Credit Score = 720
# Loan Amount = 400000
# Age = 35
# Salaried = 1
# Existing Loan = No = 0

new_applicant = pd.DataFrame({
    "Income": [60000],
    "Credit_Score": [720],
    "Loan_Amount": [400000],
    "Age": [35],
    "Employment_Type": [1],
    "Existing_Loan": [0]
})

prediction = model.predict(new_applicant)

if prediction[0] == 1:
    print("\nNEW APPLICANT RESULT: APPROVED")
else:
    print("\nNEW APPLICANT RESULT: REJECTED")

# ------------------------------------------------------------
# IMPORTANT CONCEPTS
# ------------------------------------------------------------

# Data Leakage:
# Never use information that becomes available AFTER the
# loan decision, su ch as future repayment status.
#
# Overfitting:
# Training accuracy is very high but testing accuracy is much
# lower. The model may have learned training-specific patterns.
#
# Underfitting:
# Both training and testing accuracy are low. The model may
# be too simple to learn important patterns.
