# Import pandas
import pandas as pd

# Import evaluation metrics
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    ConfusionMatrixDisplay
)

# Import matplotlib
import matplotlib.pyplot as plt


# ------------------------------------------------
# STEP 1: Load the dataset
# ------------------------------------------------

df = pd.read_csv("DAY11\student_pass_fail.csv")

print("Student Dataset:")
print(df)


# ------------------------------------------------
# STEP 2: Get Actual and Predicted values
# ------------------------------------------------

actual = df["Actual"]
predicted = df["Predicted"]


# ------------------------------------------------
# STEP 3: Confusion Matrix
# ------------------------------------------------

cm = confusion_matrix(actual, predicted)

print("\nConfusion Matrix:")
print(cm)


# ------------------------------------------------
# STEP 4: Accuracy
# ------------------------------------------------

accuracy = accuracy_score(actual, predicted)

print("\nAccuracy:", accuracy)
print("Accuracy Percentage:", accuracy * 100, "%")


# ------------------------------------------------
# STEP 5: Precision
# ------------------------------------------------

precision = precision_score(actual, predicted)

print("\nPrecision:", precision)
print("Precision Percentage:", precision * 100, "%")


# ------------------------------------------------
# STEP 6: Recall
# ------------------------------------------------

recall = recall_score(actual, predicted)

print("\nRecall:", recall)
print("Recall Percentage:", recall * 100, "%")


# ------------------------------------------------
# STEP 7: Display Confusion Matrix as Graph
# ------------------------------------------------

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Fail", "Pass"]
)

display.plot()

plt.title("Student Pass/Fail Confusion Matrix")
plt.show()