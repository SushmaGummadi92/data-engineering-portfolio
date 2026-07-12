-- ================================================
-- Customer Intelligence Report
-- Author: Sushma Gummadi
-- Dataset: Customer Personality Analysis
-- Tools: SQL Server, Star Schema, CTEs, 
--        Window Functions
-- ================================================

USE DQ_Practice;
GO

-- ================================================
-- SECTION 1: Overall Summary
-- ================================================
PRINT 'SECTION 1: Overall Summary';

SELECT
    COUNT(*) AS total_customers,
    ROUND(AVG(f.Income), 2) AS avg_income,
    ROUND(AVG(CAST(Total_Spending AS FLOAT)), 2) AS avg_spending,
    SUM(Total_Spending) AS total_revenue,
    MIN(2024 - Year_Birth) AS youngest_age,
    MAX(2024 - Year_Birth) AS oldest_age
FROM FactCustomerSpending f
JOIN customer_data c ON f.Customer_ID = c.ID;

-- ================================================
-- SECTION 2: Spending by Education Level
-- ================================================
PRINT 'SECTION 2: Spending by Education Level';

WITH EducationSummary AS (
    SELECT
        e.Education_Level,
        COUNT(*) AS customer_count,
        ROUND(AVG(f.Income), 2) AS avg_income,
        SUM(f.Total_Spending) AS total_spending,
        ROUND(AVG(CAST(f.Total_Spending AS FLOAT)), 2) AS avg_spending
    FROM FactCustomerSpending f
    JOIN DimEducation e ON f.Education_ID = e.Education_ID
    GROUP BY e.Education_Level
),
Ranked AS (
    SELECT *,
        RANK() OVER (ORDER BY total_spending DESC) AS spending_rank,
        ROUND(100.0 * total_spending / SUM(total_spending) OVER(), 2) AS pct_of_total
    FROM EducationSummary
)
SELECT * FROM Ranked ORDER BY spending_rank;

-- ================================================
-- SECTION 3: Top 5 Customers Per Education Group
-- ================================================
PRINT 'SECTION 3: Top 5 Customers Per Education Group';

WITH CustomerRanked AS (
    SELECT
        f.Customer_ID,
        e.Education_Level,
        f.Income,
        f.Total_Spending,
        DENSE_RANK() OVER (
            PARTITION BY e.Education_Level
            ORDER BY f.Total_Spending DESC
        ) AS rank_in_group
    FROM FactCustomerSpending f
    JOIN DimEducation e ON f.Education_ID = e.Education_ID
)
SELECT
    Customer_ID,
    Education_Level,
    Income,
    Total_Spending,
    rank_in_group
FROM CustomerRanked
WHERE rank_in_group <= 5
ORDER BY Education_Level, rank_in_group;

-- ================================================
-- SECTION 4: Year over Year Customer Growth
-- ================================================
PRINT 'SECTION 4: Year over Year Customer Growth';

WITH YearlySummary AS (
    SELECT
        d.Year,
        COUNT(DISTINCT f.Customer_ID) AS new_customers,
        SUM(f.Total_Spending) AS yearly_spending
    FROM FactCustomerSpending f
    JOIN DimDate d ON f.Date_ID = d.Date_ID
    GROUP BY d.Year
),
YoY AS (
    SELECT
        Year,
        new_customers,
        yearly_spending,
        LAG(new_customers) OVER (ORDER BY Year) AS prev_customers,
        LAG(yearly_spending) OVER (ORDER BY Year) AS prev_spending
    FROM YearlySummary
)
SELECT
    Year,
    new_customers,
    prev_customers,
    ROUND(
        100.0 * (new_customers - prev_customers)
        / NULLIF(prev_customers, 0)
    , 2) AS customer_growth_pct,
    yearly_spending,
    ROUND(
        100.0 * (yearly_spending - prev_spending)
        / NULLIF(prev_spending, 0)
    , 2) AS spending_growth_pct
FROM YoY
ORDER BY Year;

-- ================================================
-- SECTION 5: Customer Segmentation
-- ================================================
PRINT 'SECTION 5: Customer Segmentation';

WITH Segmented AS (
    SELECT
        f.Customer_ID,
        e.Education_Level,
        m.Family_Type,
        f.Income,
        f.Total_Spending,
        CASE
            WHEN f.Income > 70000 
             AND f.Total_Spending > 1000 THEN 'Premium'
            WHEN f.Income > 40000 
             AND f.Total_Spending > 500  THEN 'Standard'
            WHEN f.Total_Spending > 500  THEN 'Budget High Spender'
            ELSE 'Low Value'
        END AS segment
    FROM FactCustomerSpending f
    JOIN DimEducation e ON f.Education_ID = e.Education_ID
    JOIN DimMarital m ON f.Marital_ID = m.Marital_ID
)
SELECT
    segment,
    COUNT(*) AS customer_count,
    ROUND(AVG(Income), 2) AS avg_income,
    ROUND(AVG(CAST(Total_Spending AS FLOAT)), 2) AS avg_spending,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_customers
FROM Segmented
GROUP BY segment
ORDER BY avg_spending DESC;

-- ================================================
-- SECTION 6: DQ Check on Star Schema
-- ================================================
PRINT 'SECTION 6: Data Quality Check';

WITH DQCheck AS (
    SELECT
        COUNT(*) AS total_rows,
        SUM(CASE WHEN Income IS NULL THEN 1 ELSE 0 END) AS null_income,
        SUM(CASE WHEN Total_Spending < 0 THEN 1 ELSE 0 END) AS negative_spending,
        SUM(CASE WHEN Education_ID IS NULL THEN 1 ELSE 0 END) AS missing_education,
        SUM(CASE WHEN Marital_ID IS NULL THEN 1 ELSE 0 END) AS missing_marital,
        SUM(CASE WHEN Date_ID IS NULL THEN 1 ELSE 0 END) AS missing_date
    FROM FactCustomerSpending
)
SELECT
    total_rows,
    null_income,
    ROUND(100.0 * null_income / total_rows, 2) AS null_income_pct,
    negative_spending,
    missing_education,
    missing_marital,
    missing_date,
    CASE
        WHEN null_income = 0
         AND negative_spending = 0
         AND missing_education = 0
        THEN 'PASS'
        ELSE 'FAIL'
    END AS overall_dq_status
FROM DQCheck;