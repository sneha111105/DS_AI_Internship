# ==========================================================
# DAY 11 — EXPLORATORY DATA ANALYSIS (EDA) SCRIPT
# ==========================================================

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Improve plot appearance
sns.set_theme(style="whitegrid")

# ----------------------------------------------------------
# STEP 1 — Load Dataset
# ----------------------------------------------------------
# Dynamic path resolution to locate dataset.csv in the same folder
SCRIPT_DIR = Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "dataset.csv"

# Load the CSV file
df = pd.read_csv(r"C:\Users\Admin\DS_AI_Internship\DAY-9\dataset.csv")
print(df)
# ----------------------------------------------------------
# TOPIC 1 — DATASET INSPECTION
# ----------------------------------------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape (rows, columns):", df.shape)

print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# ----------------------------------------------------------
# TOPIC 2 — UNIVARIATE ANALYSIS
# ----------------------------------------------------------

# Distribution of Age
plt.figure()
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.show()

# Distribution of Salary
plt.figure()
sns.histplot(df["Salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

# Boxplot — Salary spread
plt.figure()
sns.boxplot(x=df["Salary"])
plt.title("Salary Boxplot")
plt.show()

# Categorical Frequency Counts
print("\nDepartment counts:")
print(df["Department"].value_counts())

print("\nGender counts:")
print(df["Gender"].value_counts())

# Bar Plot — Department Distribution
plt.figure()
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.show()

# ----------------------------------------------------------
# TOPIC 3 — BIVARIATE ANALYSIS
# ----------------------------------------------------------

# Age vs Salary
plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

# Experience vs Salary
plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

# Salary by Gender
plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("Salary by Gender")
plt.show()

# Salary by Department
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by Department")
plt.show()

# ----------------------------------------------------------
# TOPIC 4 — CORRELATION ANALYSIS
# ----------------------------------------------------------

corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ----------------------------------------------------------
# TOPIC 5 — OUTLIER DETECTION
# ----------------------------------------------------------

plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age Outliers")
plt.show()

plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience Outliers")
plt.show()

# ----------------------------------------------------------
# INSIGHTS SUMMARY
# ----------------------------------------------------------

print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")