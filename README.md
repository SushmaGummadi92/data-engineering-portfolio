# Data Engineering Portfolio — Sushma Gummadi

ETL professional with 4+ years at Infosys.
Transitioning into Data Engineering — building 
hands-on skills in Python, SQL Server, and Azure.

---

## Project 1: Customer Data ETL Pipeline
**Folder:** customer-etl/  
**Tools:** Python, pandas  
**Dataset:** Kaggle Customer Personality Analysis (2,240 records)

Pipeline: Extract → Profile → Clean → Transform → Export

Key results:
- 24 null Income values detected and fixed
- 1,156 high-income customers identified
- 5 education categories standardized

---

## Project 2: Python to SQL Server Pipeline
**Folder:** python-sql-etl/  
**Tools:** Python, pandas, pyodbc, sqlalchemy, SQL Server

Pipeline: Connect → Extract → Transform → Load → Verify

Key results:
- Connected Python to SQL Server using sqlalchemy
- Added Age column calculated from Year_Birth
- Created Income categories: Low/Medium/High/Very High
- Loaded 2,240 transformed records into new SQL table

---

## Project 3: Customer Intelligence SQL Report
**Tools:** SQL Server, CTEs, Window Functions, Star Schema  
**File:** customer_intelligence_report.sql

### Report sections:
1. Overall summary — total customers, avg income, revenue
2. Spending by education — ranked with % of total
3. Top 5 customers per education group
4. Year over year customer growth + spending growth
5. Customer segmentation — Premium/Standard/Budget/Low Value
6. Data quality check on star schema

### Key findings:
- Low Value segment has most customers.
- Year 2013 has the hirghest growth with 94.270000000000%.
- Undergraduate level spends most.
- DQ status: PASS

## Project 4: Azure Data Factory ETL Pipeline

**Tools:** Azure Data Factory, Azure Blob Storage, 
           ADF Data Flow, Cloud ETL

**Architecture:**
Azure Blob Storage (CSV) → ADF Copy Activity 
→ ADF Data Flow (Filter + Transform) 
→ Azure Blob Storage (cleaned output)

**Pipeline components:**
- Linked Service: Azure Blob Storage connection
- Dataset (Source): marketing_campaign.csv (tab-delimited)
- Dataset (Sink): cleaned_customers.csv
- Copy Activity: Copy_Customer_CSV
- Data Flow: df_customer_transform
  - Source: CustomerSource (2,240 rows)
  - Filter: FilterValidIncome (!isNull(Income))
  - Sink: CustomerOutput (2,216 rows after filtering)
- Trigger: Daily schedule

**Result:** Pipeline status Succeeded
Both activities completed — Copy + Data Flow
Output CSV written to Azure Blob Storage
