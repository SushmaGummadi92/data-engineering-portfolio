# Python ETL Pipeline — SQL Server

**Author:** Sushma Gummadi  
**Tech:** Python, pandas, SQLAlchemy, SQL Server

## What this does
End-to-end ETL pipeline connecting Python to SQL Server.
Extracts raw customer data, cleans and transforms it using pandas,
loads results into a new SQL table, and logs every step automatically.

## Pipeline Steps
1. Connect to SQL Server via SQLAlchemy
2. Extract — pull customer_data table into pandas
3. Transform — fix null incomes, add Age, categorize Income
4. Load — write to customer_data_transformed table
5. Verify — confirm row counts and stats

## How to run
python sql_connection.py

## Output
- New SQL table: customer_data_transformed (2,240 rows)
- Log file: pipeline.log (timestamped entry per step)
