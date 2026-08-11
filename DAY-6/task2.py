import pandas as pd
import numpy as np

# 1. Create a Series with different cases and missing values
names = pd.Series(['Alice', 'BOB', np.nan, 'Charlie', 'DAVID', None, 'eve'])
print("--- Original Series ---")
print(names)

# 2. Detect missing values
print("\n--- Missing Values ---")
print(names.isnull())

# 3. Fill missing values with a default placeholder
names_filled = names.fillna('Unknown')
print("\n--- After Filling Missing Values ---")
print(names_filled)

# 4. Convert all names to lowercase using .str operations
names_lower = names_filled.str.lower()
print("\n--- Lowercase Names ---")
print(names_lower)

# 5. Filter names containing the letter 'a'
filtered_names = names_lower[names_lower.str.contains('a')]
print("\n--- Names containing letter 'a' ---")
print(filtered_names)