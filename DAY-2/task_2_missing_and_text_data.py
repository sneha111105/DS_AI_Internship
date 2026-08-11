"""Task 2: Handling missing and text data with Pandas."""

import pandas as pd


# Names use different cases, and None represents a missing value.
names = pd.Series(["ALICE", "Bob", None, "CHARLIE", "diana", None], name="names")

print("Original Series:\n", names)

# Detect missing values.
print("\nMissing values:\n", names.isna())
print("Number of missing values:", names.isna().sum())

# Fill missing entries, then normalize the text to lowercase.
filled_names = names.fillna("Unknown")
lowercase_names = filled_names.str.lower()

print("\nNames after filling missing values:\n", filled_names)
print("\nNames in lowercase:\n", lowercase_names)

# Filter names that contain the letter "a" (case-insensitive after normalization).
names_with_a = lowercase_names[lowercase_names.str.contains("a", na=False)]
print("\nNames containing the letter 'a':\n", names_with_a)
