# PySpark Marketing Campaign Pipeline — Databricks

**Author:** Sushma Gummadi  
**Tech:** PySpark, Databricks Serverless, Unity Catalog

## What this does
Replicates the pandas ETL pipeline using PySpark on Databricks.
Same dataset, same transformations — distributed engine.

## Steps
1. Read marketing_campaign.csv from Databricks Volume
2. Explore schema and data types
3. Fix null Income values using Spark mean
4. Add Age column from Year_Birth
5. Categorize Income — Low/Medium/High/Very High
6. GroupBy summary and describe stats

## Results match pandas pipeline exactly
- 2,240 rows processed
- Mean income: 52,247
- Age range: 28 to 131
