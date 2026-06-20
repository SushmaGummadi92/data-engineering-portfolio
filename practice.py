import pandas as pd

# Load the CSV (update this path to match your actual file location)
df = pd.read_csv("C:\Users\HP\Downloads\marketing_campaign.csv", sep="\t")

# Look at the first 5 rows
print("First 5 rows:")
print(df.head())

# Check how many rows and columns
print("\nShape (rows, columns):", df.shape)

# Filter: customers with income above 50000
high_income = df[df["Income"] > 50000]
print("\nHigh income customers:", len(high_income))

# Filter: customers with no kids at home
no_kids = df[df["Kidhome"] == 0]
print("No-kids customers:", len(no_kids))