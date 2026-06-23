# ============================================
# Portfolio Project 2 — Python to SQL Server
# Author: Sushma Gummadi
# Steps: Connect → Extract → Transform → Load
# ============================================

import pandas as pd
import pyodbc
from sqlalchemy import create_engine, text
import logging

# ============================================
# LOGGING SETUP
# ============================================

logging.basicConfig(
    filename='pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ============================================
# STEP 1 — CONNECT TO SQL SERVER
# ============================================

SERVER = 'LAPTOP-28C5HMFV\SQLEXPRESS'
DATABASE = 'DQ_Practice'

print("Connecting to SQL Server...")
logging.info("Pipeline started")
logging.info(f"Connecting to server: {SERVER}, database: {DATABASE}")

try:
    connection_string = (
        f"mssql+pyodbc://{SERVER}/{DATABASE}"
        f"?driver=ODBC+Driver+17+for+SQL+Server"
        f"&trusted_connection=yes"
    )
    engine = create_engine(connection_string)

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connected successfully!")
        logging.info("Connected to SQL Server successfully")

except Exception as e:
    print(f"Connection failed: {e}")
    logging.error(f"Connection failed: {e}")
    exit()

# ============================================
# STEP 2 — EXTRACT
# ============================================

print("\nExtracting data from SQL Server...")
logging.info("STEP 2 — Extract started")

try:
    query = "SELECT * FROM customer_data"
    df = pd.read_sql(query, engine)
    print(f"Rows extracted: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nFirst 3 rows:")
    print(df.head(3))
    logging.info(f"Extracted {df.shape[0]} rows, {df.shape[1]} columns from customer_data")

except Exception as e:
    print(f"Extract failed: {e}")
    logging.error(f"Extract failed: {e}")
    exit()

# ============================================
# STEP 3 — TRANSFORM
# ============================================

print("\nTransforming data...")
logging.info("STEP 3 — Transform started")

try:
    # Fix null incomes
    nulls_before = df["Income"].isnull().sum()
    df["Income"] = df["Income"].fillna(df["Income"].mean())
    nulls_after = df["Income"].isnull().sum()
    print(f"Null incomes fixed: {nulls_before} → {nulls_after}")
    logging.info(f"Null incomes fixed: {nulls_before} → {nulls_after}")

    # Add Age column
    df["Age"] = 2024 - df["Year_Birth"]
    print(f"Age column added. Range: {df['Age'].min()} to {df['Age'].max()}")
    logging.info(f"Age column added. Range: {df['Age'].min()} to {df['Age'].max()}")

    # Add Income_Category column
    df["Income_Category"] = pd.cut(
        df["Income"],
        bins=[0, 30000, 60000, 90000, float("inf")],
        labels=["Low", "Medium", "High", "Very High"]
    )
    print("Income categories added:")
    print(df["Income_Category"].value_counts())
    logging.info(f"Income categories added: {df['Income_Category'].value_counts().to_dict()}")

except Exception as e:
    print(f"Transform failed: {e}")
    logging.error(f"Transform failed: {e}")
    exit()

# ============================================
# STEP 4 — LOAD
# ============================================

print("\nLoading transformed data back to SQL Server...")
logging.info("STEP 4 — Load started")

try:
    df.to_sql(
        name="customer_data_transformed",
        con=engine,
        if_exists="replace",
        index=False
    )
    print("Data loaded successfully into customer_data_transformed table!")
    logging.info(f"Loaded {len(df)} rows into customer_data_transformed")

except Exception as e:
    print(f"Load failed: {e}")
    logging.error(f"Load failed: {e}")
    exit()

# ============================================
# STEP 5 — VERIFY
# ============================================

print("\nVerifying loaded data...")
logging.info("STEP 5 — Verify started")

try:
    verify_query = """
        SELECT 
            COUNT(*) AS total_rows,
            AVG(Income) AS avg_income,
            AVG(Age) AS avg_age,
            MIN(Age) AS youngest,
            MAX(Age) AS oldest
        FROM customer_data_transformed
    """
    result_df = pd.read_sql(verify_query, engine)
    print(result_df)
    logging.info(f"Verification result: {result_df.to_dict(orient='records')}")

except Exception as e:
    print(f"Verify failed: {e}")
    logging.error(f"Verify failed: {e}")

print("\nPipeline completed successfully.")
print("Check SSMS — you should see a new table: customer_data_transformed")
logging.info("Pipeline completed successfully")
