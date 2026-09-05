import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ------------------------------------------------
# Create Household Electricity Dataset
# ------------------------------------------------

data = {
    "Temperature": [
        22, 25, 28, 30, 32,
        24, 27, 29, 31, 33,
        23, 26, 30, 34, 35,
        21, 25, 28, 32, 36
    ],

    "Appliances": [
        3, 4, 5, 6, 7,
        4, 5, 6, 7, 8,
        3, 5, 6, 8, 9,
        2, 4, 5, 7, 9
    ],

    "People": [
        2, 3, 4, 5, 5,
        3, 4, 4, 5, 6,
        2, 4, 5, 6, 7,
        2, 3, 4, 5, 6
    ],

    "Usage_Hours": [
        4, 5, 6, 7, 8,
        5, 6, 7, 8, 9,
        4, 6, 7, 9, 10,
        3, 5, 6, 8, 10
    ],

    "Electricity_Consumption": [
        120, 160, 210, 260, 310,
        155, 205, 245, 290, 340,
        130, 215, 270, 350, 390,
        100, 165, 215, 300, 410
    ]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# ------------------------------------------------
# Define Features and Target
# ------------------------------------------------

X = df[
    [
        "Temperature",
        "Appliances",
        "People",
        "Usage_Hours"
    ]
]

y = df["Electricity_Consumption"]

# ------------------------------------------------
# Split Dataset
# ------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------------------
# Create Model
# ------------------------------------------------

model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# ------------------------------------------------
# Make Predictions
# ------------------------------------------------

y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

# ------------------------------------------------
# Model Evaluation
# ------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# ------------------------------------------------
# Predict New Household Consumption
# ------------------------------------------------

new_household = pd.DataFrame({
    "Temperature": [30],
    "Appliances": [6],
    "People": [4],
    "Usage_Hours": [7]
})

prediction = model.predict(new_household)

print("\nPredicted Electricity Consumption:")
print(prediction[0])