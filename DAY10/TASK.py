# ============================================
# HOUSEHOLD ELECTRICITY CONSUMPTION PREDICTION
# ============================================

# 1. Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# 2. Load the dataset
df = pd.read_csv("DAY10\household_electricity_consumption.csv")


# 3. Display the dataset
print("First 5 Rows:")
print(df.head())


# 4. Convert Time of Day into numerical values
# Morning = 1
# Afternoon = 2
# Evening = 3
# Night = 4
df["Time_of_Day"] = df["Time_of_Day"].map({
    "Morning": 1,
    "Afternoon": 2,
    "Evening": 3,
    "Night": 4
})
# 5. Select input features (X)
X = df[
    [
        "Temperature_C",
        "Appliances_Used",
        "Time_of_Day",
        "Previous_Usage_kWh"
    ]
]

# 6. Select target/output (y)
y = df["Current_Consumption_kWh"]

# 7. Split the data into training and testing sets
# 80% → Training
# 20% → Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 8. Create the Linear Regression model
model = LinearRegression()


# 9. Train the model using training data
model.fit(X_train, y_train)


# 10. Make predictions using test data
y_pred = model.predict(X_test)


# 11. Display actual and predicted values
print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)


# 12. Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# 13. Final insights
print("\nInsights:")
print("- More appliances generally increase electricity consumption.")
print("- Evening has the highest average consumption.")
print("- Night has the lowest average consumption.")
print("- The model predicts electricity consumption in kWh.")