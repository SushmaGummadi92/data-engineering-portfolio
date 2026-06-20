# Data Engineering Portfolio — Sushma Gummadi

## Project 1: Customer Data ETL Pipeline
**Tools:** Python, pandas  
**Dataset:** Kaggle Customer Personality Analysis (2,240 records)

### What this project does:
- Loads raw customer data from CSV
- Profiles data — shape, null counts, distributions
- Cleans missing Income values using mean imputation
- Filters customers by income and household composition
- Transforms data by mapping education categories via lookup join
- Exports cleaned dataset and filtered subsets to new CSV files

### Key findings:
- 24 null Income values detected and imputed
- 1,156 high-income customers (Income > 50,000)
- 1,293 customers with no children at home
- 5 education categories mapped to standardized labels


