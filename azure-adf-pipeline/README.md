## Project 4: Azure Data Factory ETL Pipeline

**Tools:** Azure Data Factory, Azure Blob Storage, 
           ADF Data Flow, Cloud ETL

**Architecture:**
Azure Blob Storage (CSV) 
→ ADF Copy Activity 
→ ADF Data Flow (Filter + Transform) 
→ Azure Blob Storage (cleaned output)

**Pipeline components:**
- Linked Service: Azure Blob Storage connection
- Source Dataset: marketing_campaign.csv (tab-delimited)
- Sink Dataset: cleaned output CSV
- Copy Activity: Copy_Customer_CSV — Succeeded
- Data Flow: df_customer_transform
  - Source: CustomerSource (2,240 rows)
  - Filter: FilterValidIncome (!isNull(Income))
  - Sink: CustomerOutput (2,216 rows after filtering)
- Trigger: Daily schedule (tr_daily_customer_etl)

**Result:** 
Pipeline status — Succeeded
Both activities completed — Copy + Data Flow
Output files confirmed in Azure Blob Storage
_SUCCESS marker file generated confirming clean run
