import pandas as pd
import numpy as np
# 2. Create Sample Dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Age": [23, 21, 25, np.nan, 24],
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Marks": [85, 90, 78, 88, np.nan],
    "City": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# 3. Data Loading & Saving (I/O)
# Save data to CSV
df.to_csv("students_data.csv", index=False)
# Load data from CSV
df_loaded = pd.read_csv("students_data.csv")
print("\nLoaded DataFrame:")
print(df_loaded)
# 4. Data Inspection & Understanding
print("\nFirst 3 rows:")
print(df.head(3))
print("\nLast 2 rows:")
print(df.tail(2))
print("\nData Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
# 5. Data Selection, Indexing & Slicing
# Select single column
print("\nNames column:")
print(df["Name"])
# Select multiple columns
print("\nName and Marks:")
print(df[["Name", "Marks"]])
# Select rows using iloc
print("\nFirst two rows using iloc:")
print(df.iloc[0:2])
# Select rows using loc
print("\nRows where City is Lahore:")
print(df.loc[df["City"] == "Lahore"])
# 6. Data Cleaning & Preprocessing
# Check missing values
print("\nMissing values:")
print(df.isnull().sum())
# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)
print("\nAfter filling missing values:")
print(df)
# 7. Sorting Operations
print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))
# 8. GroupBy & Aggregation
grouped = df.groupby("City")["Marks"].mean()
print("\nAverage Marks by City:")
print(grouped)
# 9. Summary Statistics
print("\nOverall Summary Statistics:")
print(df.describe())
# 10. Vectorized Operations
# Increase marks by 5 using vectorized operation
df["Marks"] = df["Marks"] + 5
print("\nMarks after adding bonus:")
print(df)
# 11. Column-wise Operations
# Create new column
df["Passed"] = df["Marks"] >= 50
print("\nPassed Column Added:")
print(df)
# 12. Apply, Map & Transform
# Apply function
df["Age_Group"] = df["Age"].apply(lambda x: "Young" if x < 23 else "Adult")
# Map function
gender_map = {"Male": "M", "Female": "F"}
df["Gender_Short"] = df["Gender"].map(gender_map)
# Transform function
df["Marks_Normalized"] = df.groupby("City")["Marks"].transform(lambda x: x - x.mean())
print("\nAfter apply, map and transform:")
print(df)
# 13. Missing Data Handling (Advanced)
df_cleaned = df.dropna()
print("\nCleaned DataFrame:")
print(df_cleaned)
# 14. Advanced Exporting Clean Data
# Export to CSV
df_cleaned.to_csv("clean_students_data.csv", index=False)
# Export to Excel
df_cleaned.to_excel("clean_students_data.xlsx", index=False)
print("\nClean data exported successfully!")