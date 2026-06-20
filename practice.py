# ============================================
# Portfolio Project 1 — Customer Data ETL
# Author: Sushma Gummadi
# Dataset: Kaggle Customer Personality Analysis
# Steps: Load → Profile → Clean → Transform → Export
# ============================================

import pandas as pd

# --- EXTRACT ---
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# --- PROFILE ---
print("First 5 rows:")
print(df.head())

print("\nShape (rows, columns):", df.shape)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nCustomers by education level:")
print(df.groupby("Education").size())

# --- FILTER ---
high_income = df[df["Income"] > 50000]
print("\nHigh income customers:", len(high_income))

no_kids = df[df["Kidhome"] == 0]
print("No-kids customers:", len(no_kids))

# --- CLEAN ---
print("\nIncome nulls before:", df["Income"].isnull().sum())
df["Income"] = df["Income"].fillna(df["Income"].mean())
print("Income nulls after:", df["Income"].isnull().sum())

# --- TRANSFORM ---
education_map = pd.DataFrame({
    "Education": ["Graduation", "PhD", "Master", "Basic", "2n Cycle"],
    "Education_Level": ["Undergraduate", "Doctorate", "Postgraduate",
                        "School", "Secondary"]
})

df = df.merge(education_map, on="Education", how="left")

print("\nNew column added:")
print(df[["Education", "Education_Level"]].drop_duplicates())
high_income.to_csv("high_income_customers.csv", index=False)
df.to_csv("cleaned_customers.csv", index=False)
high_income.to_csv("C:/DE_Practices/high_income_customers.csv", index=False)
df.to_csv("C:/DE_Practices/cleaned_customers.csv", index=False)
print("\nSaved both output files to DE_Practices folder")
