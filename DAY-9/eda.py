# ==========================================================
# DAY 11 — EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# ==========================================================
# STEP 1 — CREATE EMPLOYEE DATA
# ==========================================================

data = {
    "Age": [25, 30, 35, 40, 28, 32, 45, 50, 23, 36, 29, 41],

    "Salary": [
        30000, 40000, 50000, 65000,
        42000, 48000, 80000, 90000,
        28000, 52000, 46000, 70000
    ],

    "Experience": [
        1, 3, 7, 10, 2, 5,
        15, 20, 1, 8, 4, 12
    ],

    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "IT", "Finance", "Finance",
        "HR", "IT", "HR", "Finance"
    ],

    "Gender": [
        "M", "F", "M", "M",
        "F", "F", "M", "M",
        "F", "F", "M", "F"
    ]
}


# Create DataFrame
df = pd.DataFrame(data)

print("\nEmployee Dataset:")
print(df)


# ==========================================================
# TOPIC 1 — DATASET INSPECTION
# ==========================================================

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nSummary Statistics:")
print(df.describe())


# ==========================================================
# TOPIC 2 — UNIVARIATE ANALYSIS
# ==========================================================

# Age Distribution
plt.figure()
sns.histplot(df["Age"], kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.show()


# Salary Distribution
plt.figure()
sns.histplot(df["Salary"], kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()


# Salary Boxplot
plt.figure()
sns.boxplot(x=df["Salary"])

plt.title("Salary Boxplot")
plt.xlabel("Salary")

plt.show()


# Department Counts
print("\nDepartment Counts:")
print(df["Department"].value_counts())


# Gender Counts
print("\nGender Counts:")
print(df["Gender"].value_counts())


# Department Distribution
plt.figure()
sns.countplot(x="Department", data=df)

plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.show()


# ==========================================================
# TOPIC 3 — BIVARIATE ANALYSIS
# ==========================================================

# Age vs Salary
plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)

plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")

plt.show()


# Experience vs Salary
plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()


# Salary by Gender
plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)

plt.title("Salary by Gender")
plt.xlabel("Gender")
plt.ylabel("Salary")

plt.show()


# Salary by Department
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)

plt.title("Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.show()


# ==========================================================
# TOPIC 4 — CORRELATION ANALYSIS
# ==========================================================

corr_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix:")
print(corr_matrix)


# Correlation Heatmap
plt.figure()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()


# ==========================================================
# TOPIC 5 — OUTLIER DETECTION
# ==========================================================

# Age Outliers
plt.figure()
sns.boxplot(x=df["Age"])

plt.title("Age Outliers")
plt.xlabel("Age")

plt.show()


# Experience Outliers
plt.figure()
sns.boxplot(x=df["Experience"])

plt.title("Experience Outliers")
plt.xlabel("Experience")

plt.show()


# Salary Outliers
plt.figure()
sns.boxplot(x=df["Salary"])

plt.title("Salary Outliers")
plt.xlabel("Salary")

plt.show()


# ==========================================================
# END
# ==========================================================

print("\nEDA Completed Successfully!")