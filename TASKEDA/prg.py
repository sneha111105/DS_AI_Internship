# ==========================================================
# COMPLETE EDA - SALES DATASET
# ==========================================================

# STEP 1: Import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================================
# STEP 2: LOAD DATASET
# ==========================================================

df = pd.read_csv("Sales_data.csv")

print("First 5 rows:")
print(df.head())


# ==========================================================
# STEP 3: UNDERSTAND THE DATA
# ==========================================================

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe())


# ==========================================================
# STEP 4: CHECK MISSING VALUES
# ==========================================================

print("\nMissing values:")
print(df.isnull().sum())


# ==========================================================
# STEP 5: CHECK DUPLICATES
# ==========================================================

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())


# Remove duplicates if any

df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)


# ==========================================================
# STEP 6: CHECK UNIQUE VALUES
# ==========================================================

print("\nProducts:")
print(df["Product"].unique())

print("\nCategories:")
print(df["Category"].unique())

print("\nCities:")
print(df["City"].unique())


# ==========================================================
# STEP 7: UNIVARIATE ANALYSIS
# ==========================================================

# Univariate = studying ONE variable


print("\n========== UNIVARIATE ANALYSIS ==========")


# Sales statistics

print("\nSales Statistics")

print("Mean:", df["Sales"].mean())
print("Median:", df["Sales"].median())
print("Minimum:", df["Sales"].min())
print("Maximum:", df["Sales"].max())
print("Standard Deviation:", df["Sales"].std())


# Profit statistics

print("\nProfit Statistics")

print("Mean:", df["Profit"].mean())
print("Median:", df["Profit"].median())
print("Minimum:", df["Profit"].min())
print("Maximum:", df["Profit"].max())
print("Standard Deviation:", df["Profit"].std())


# Quantity statistics

print("\nQuantity Statistics")

print("Mean:", df["Quantity"].mean())
print("Median:", df["Quantity"].median())
print("Minimum:", df["Quantity"].min())
print("Maximum:", df["Quantity"].max())


# ==========================================================
# STEP 8: HISTOGRAM
# ==========================================================

# Histogram shows distribution


plt.hist(df["Sales"], bins=10)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()


# ==========================================================
# STEP 9: SALES BOX PLOT
# ==========================================================

# Box plot helps identify outliers


plt.boxplot(df["Sales"])

plt.title("Sales Box Plot")
plt.ylabel("Sales")

plt.show()


# ==========================================================
# STEP 10: PRODUCT ANALYSIS
# ==========================================================

print("\n========== PRODUCT ANALYSIS ==========")

print(df["Product"].value_counts())


# Product bar chart

df["Product"].value_counts().plot(kind="bar")

plt.title("Number of Orders by Product")
plt.xlabel("Product")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.show()


# ==========================================================
# STEP 11: CATEGORY ANALYSIS
# ==========================================================

print("\n========== CATEGORY ANALYSIS ==========")

print(df["Category"].value_counts())


# Category bar chart

df["Category"].value_counts().plot(kind="bar")

plt.title("Number of Orders by Category")
plt.xlabel("Category")
plt.ylabel("Number of Orders")

plt.show()


# ==========================================================
# STEP 12: SALES BY CATEGORY
# ==========================================================

print("\n========== SALES BY CATEGORY ==========")

category_sales = df.groupby("Category")["Sales"].sum()

print(category_sales)


category_sales.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()


# ==========================================================
# STEP 13: SALES BY CITY
# ==========================================================

print("\n========== SALES BY CITY ==========")

city_sales = df.groupby("City")["Sales"].sum()

print(city_sales)


city_sales.plot(kind="bar")

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")

plt.show()


# ==========================================================
# STEP 14: SALES BY PRODUCT
# ==========================================================

print("\n========== SALES BY PRODUCT ==========")

product_sales = df.groupby("Product")["Sales"].sum()

print(product_sales)


product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.show()


# ==========================================================
# STEP 15: SKEWNESS ANALYSIS
# ==========================================================

print("\n========== SKEWNESS ANALYSIS ==========")


# Sales skewness

sales_skew = df["Sales"].skew()

print("\nSales Skewness:", sales_skew)

if sales_skew > 0:
    print("Sales are positively skewed.")
    
elif sales_skew < 0:
    print("Sales are negatively skewed.")
    
else:
    print("Sales are approximately symmetric.")


# Profit skewness

profit_skew = df["Profit"].skew()

print("\nProfit Skewness:", profit_skew)

if profit_skew > 0:
    print("Profit is positively skewed.")
    
elif profit_skew < 0:
    print("Profit is negatively skewed.")
    
else:
    print("Profit is approximately symmetric.")


# Quantity skewness

quantity_skew = df["Quantity"].skew()

print("\nQuantity Skewness:", quantity_skew)

if quantity_skew > 0:
    print("Quantity is positively skewed.")
    
elif quantity_skew < 0:
    print("Quantity is negatively skewed.")
    
else:
    print("Quantity is approximately symmetric.")


# ==========================================================
# STEP 16: CORRELATION ANALYSIS
# ==========================================================

print("\n========== CORRELATION ANALYSIS ==========")


correlation = df[
    ["Quantity", "Unit_Price", "Sales", "Profit"]
].corr()

print(correlation)


# ==========================================================
# STEP 17: CORRELATION HEATMAP
# ==========================================================

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()


# ==========================================================
# STEP 18: BIVARIATE ANALYSIS
# ==========================================================

# Bivariate = studying TWO variables


# Quantity vs Sales

plt.scatter(
    df["Quantity"],
    df["Sales"]
)

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.show()


# Sales vs Profit

plt.scatter(
    df["Sales"],
    df["Profit"]
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()


# Unit Price vs Sales

plt.scatter(
    df["Unit_Price"],
    df["Sales"]
)

plt.title("Unit Price vs Sales")
plt.xlabel("Unit Price")
plt.ylabel("Sales")

plt.show()


# ==========================================================
# STEP 19: OUTLIER DETECTION USING IQR
# ==========================================================

print("\n========== OUTLIER ANALYSIS ==========")


# Q1

Q1 = df["Sales"].quantile(0.25)

# Q3

Q3 = df["Sales"].quantile(0.75)

# IQR

IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)


# Lower limit

lower_limit = Q1 - 1.5 * IQR

# Upper limit

upper_limit = Q3 + 1.5 * IQR

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)


# Find outliers

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\nOutliers:")
print(outliers)


# ==========================================================
# STEP 20: TOTAL SALES
# ==========================================================

total_sales = df["Sales"].sum()

print("\nTotal Sales:", total_sales)


# ==========================================================
# STEP 21: TOTAL PROFIT
# ==========================================================

total_profit = df["Profit"].sum()

print("Total Profit:", total_profit)


# ==========================================================
# STEP 22: AVERAGE SALES
# ==========================================================

average_sales = df["Sales"].mean()

print("Average Sales:", average_sales)


# ==========================================================
# STEP 23: AVERAGE PROFIT
# ==========================================================

average_profit = df["Profit"].mean()

print("Average Profit:", average_profit)


# ==========================================================
# STEP 24: HIGHEST SALE
# ==========================================================

highest_sale = df["Sales"].max()

print("Highest Sale:", highest_sale)


# ==========================================================
# STEP 25: LOWEST SALE
# ==========================================================

lowest_sale = df["Sales"].min()

print("Lowest Sale:", lowest_sale)


# ==========================================================
# STEP 26: BEST PRODUCT
# ==========================================================

best_product = df.groupby("Product")["Sales"].sum().idxmax()

print("Best Selling Product:", best_product)


# ==========================================================
# STEP 27: BEST CITY
# ==========================================================

best_city = df.groupby("City")["Sales"].sum().idxmax()

print("Best Performing City:", best_city)


# ==========================================================
# STEP 28: BEST CATEGORY
# ==========================================================

best_category = df.groupby("Category")["Sales"].sum().idxmax()

print("Best Performing Category:", best_category)


# ==========================================================
# STEP 29: FINAL CHECK
# ==========================================================

print("\n========== FINAL CHECK ==========")

print("Number of rows:", len(df))

print("Number of columns:", len(df.columns))

print("Missing values:")
print(df.isnull().sum())

print("Duplicate rows:", df.duplicated().sum())


# ==========================================================
# STEP 30: FINAL CONCLUSION
# ==========================================================

print("\n========== EDA COMPLETED ==========")

print("""
Sales EDA was completed successfully.

The analysis included:

1. Dataset understanding
2. Missing value checking
3. Duplicate checking
4. Univariate analysis
5. Bivariate analysis
6. Skewness analysis
7. Correlation analysis
8. Outlier detection
9. Data visualization
10. Sales analysis
11. Profit analysis
12. Pattern identification
""")