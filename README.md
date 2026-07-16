# Data Engineering Portfolio — Sushma Gummadi

ETL professional with 4+ years experience at Infosys Limited.
Transitioning into Data Engineering with hands-on projects
across Python, SQL Server, Azure, and PySpark/Spark.

📧 sushmagummadi92@gmail.com
🔗 linkedin.com/in/Sushmagummadi

---

## Project 1: Customer Data ETL Pipeline
**Folder:** customer-etl/
**Tools:** Python 3.14, pandas
**Dataset:** Kaggle Customer Personality Analysis (2,240 records)

**Pipeline:** Extract → Profile → Clean → Transform → Export

**What it does:**
- Loads raw CSV data into pandas DataFrame
- Profiles data — shape, null counts, distributions
- Cleans 24 missing Income values using mean imputation
- Filters customers by income and household composition
- Maps education categories via lookup join (LEFT JOIN equivalent)
- Exports cleaned and filtered datasets to CSV

**Key results:**
- 24 null Income values detected and fixed
- 1,156 high-income customers (Income > 50,000) identified
- 1,293 no-kids customers identified
- 5 education categories standardized

---

## Project 2: Python to SQL Server ETL Pipeline
**Folder:** python-sql-etl/
**Tools:** Python, pandas, pyodbc, sqlalchemy, SQL Server Express

**Pipeline:** Connect → Extract → Transform → Load → Verify

**What it does:**
- Connects Python to SQL Server using sqlalchemy engine
- Extracts customer data directly from SQL table via query
- Adds Age column calculated from Year_Birth
- Categorizes Income into Low/Medium/High/Very High buckets
- Loads 2,240 transformed records into new SQL table
- Verifies row count and column stats via SQL query

**Key results:**
- End-to-end Python to SQL Server pipeline working
- New derived columns added programmatically
- Transformed data written back to database successfully

---

## Project 3: Customer Intelligence SQL Report
**File:** customer_intelligence_report.sql
**Tools:** SQL Server, T-SQL, CTEs, Window Functions, Star Schema

**What it does:**
- Builds a star schema with fact and dimension tables
- Produces a 6-section business intelligence report using
  advanced SQL — CTEs, window functions, and aggregations

**Report sections:**
1. Overall summary — customers, avg income, revenue
2. Spending by education — ranked with % of total
3. Top 5 customers per education group (DENSE_RANK)
4. Year over year customer and spending growth (LAG)
5. Customer segmentation — Premium/Standard/Budget/Low Value
6. Data quality scorecard on star schema

**Key SQL concepts demonstrated:**
- Multi-step chained CTEs
- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
- Star schema design and loading
- CASE WHEN segmentation logic
- Percentage calculations with NULLIF

---

## Project 4: Azure Data Factory Cloud Pipeline
**Folder:** azure-adf-pipeline/
**Tools:** Azure Data Factory V2, Azure Blob Storage, ADF Data Flow

**Architecture:**

**What it does:**
- Stores raw data in Azure Blob Storage container
- Copy Activity moves data between storage locations
- Data Flow filters null Income rows using ADF expression
- Output files written to Blob Storage with _SUCCESS marker
- Daily trigger configured for automated scheduled runs

**Key results:**
- Both activities succeeded — Copy + Data Flow
- 2,216 records after filtering 24 null Income rows
- Output confirmed in Azure Blob Storage
- Pipeline status: Succeeded

---

## Project 5: PySpark ETL Pipeline on Databricks
**Folder:** pyspark-databricks/
**Tools:** PySpark, Apache Spark, Databricks

**Pipeline:** Load → Schema → Clean → Transform → Analyse → SQL

**What it does:**
- Loads CSV into Spark DataFrame with automatic schema inference
- Inspects schema — 29 columns correctly typed (int, string, date)
- Detects and fixes 24 null Income values using Spark mean
- Adds Age column using withColumn transformation
- Categorizes Income using when/otherwise (CASE WHEN equivalent)
- Filters 940 high-value customers (Income > 50k, Spending > 500)
- Runs Spark SQL on DataFrame via createOrReplaceTempView

**Key results:**
- 2,240 rows loaded, all 29 columns correctly typed
- 24 null incomes fixed using mean imputation
- 940 high-value customers identified
- Graduation segment: highest total spending (₹698,626)
- PhD segment: highest avg spending per customer (₹672.41)

---

## Skills demonstrated across all projects

| Skill | Level | Where used |
|---|---|---|
| Python | Intermediate | Projects 1, 2, 5 |
| pandas | Intermediate | Projects 1, 2 |
| PySpark | Beginner-Intermediate | Project 5 |
| SQL (Advanced) | Intermediate-Advanced | Projects 2, 3 |
| CTEs + Window Functions | Advanced | Project 3 |
| Star Schema Design | Intermediate | Project 3 |
| Azure Data Factory | Beginner-Intermediate | Project 4 |
| Azure Blob Storage | Beginner | Project 4 |
| SSIS | Intermediate | 4 years at Infosys |
| Data Quality | Intermediate | All projects |
| ETL Pipelines | Intermediate | All projects |

---

## Background
4+ years at Infosys Limited as System Engineer in BI & Analytics.
Built SSIS pipelines, SQL data models, and validation workflows
across HR, Finance, IT, and Asset management domains.
Maintained 99%+ data accuracy, resolved 90+ monthly issues,
passed 2 regulatory audits with zero findings.
