import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target
df["species"] = df["target"].map({
    0: "setosa",
    1: "versicolor",
    2: "virginica"
})

print("First 5 rows:")
print(df.head())

# ------------------------------------------------
# 1. Basic Information
# ------------------------------------------------

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------------
# 2. Missing Values
# ------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------------
# 3. Duplicate Values
# ------------------------------------------------

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ------------------------------------------------
# 4. Univariate Analysis
# ------------------------------------------------

numeric_columns = iris.feature_names

for column in numeric_columns:
    plt.figure(figsize=(7, 4))
    plt.hist(df[column], bins=20)
    plt.title("Distribution of " + column)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# ------------------------------------------------
# 5. Boxplots for Outlier Detection
# ------------------------------------------------

for column in numeric_columns:
    plt.figure(figsize=(7, 4))
    plt.boxplot(df[column])
    plt.title("Boxplot of " + column)
    plt.ylabel(column)
    plt.show()

# ------------------------------------------------
# 6. Skewness Analysis
# ------------------------------------------------

print("\nSkewness:")
print(df[numeric_columns].skew())

# ------------------------------------------------
# 7. Bivariate Analysis
# ------------------------------------------------

plt.figure(figsize=(7, 5))
plt.scatter(
    df["sepal length (cm)"],
    df["sepal width (cm)"]
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width")
plt.show()

# ------------------------------------------------
# 8. Correlation Analysis
# ------------------------------------------------

correlation = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation)

# Correlation visualization
plt.figure(figsize=(8, 6))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(
    range(len(numeric_columns)),
    numeric_columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(numeric_columns)),
    numeric_columns
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# ------------------------------------------------
# 9. Outlier Detection using IQR
# ------------------------------------------------

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\nColumn:", column)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))

# ------------------------------------------------
# 10. Species Distribution
# ------------------------------------------------

print("\nSpecies Distribution:")
print(df["species"].value_counts())

plt.figure(figsize=(6, 4))
df["species"].value_counts().plot(kind="bar")
plt.title("Species Distribution")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()