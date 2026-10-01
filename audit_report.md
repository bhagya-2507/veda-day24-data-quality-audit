
# Data Quality Audit Report

## 1. Project Overview
**Organization:** VEDA Technology  
**Project:** Day 24 - Data Quality Audit  
**Dataset:** Retail Sales Dataset  
**Tool:** Python, Pandas, Excel  

## 2. Objective
The objective of this project is to identify data quality
issues in a retail sales dataset and create a separate
cleaned dataset without modifying the original data.

## 3. Dataset Overview
- Original rows: 50
- Columns: 9
- Dataset type: Retail sales data

## 4. Audit Findings
- Missing values: 3
- Duplicate records: 1
- Invalid quantity records: 2
- Invalid unit price records: 2
- Invalid date records: 2
- Total sales mismatches: 2
- Text formatting inconsistencies: See audit output

## 5. Cleaning Performed
- Removed exact duplicate rows.
- Standardized Category formatting.
- Standardized Region formatting.
- Preserved the original raw dataset.

## 6. Output Files
- retail_sales_raw.xlsx
- retail_sales_cleaned.xlsx
- issue_log.csv
- audit_summary.csv
- audit.py

## 7. Limitations and Recommendations
Missing values and invalid business data should be verified
against the original source before correction. Sales
mismatches should also be investigated before changing values.

## 8. Conclusion
The audit identified missing values, duplicate records,
invalid quantities and prices, invalid dates, sales
calculation mismatches, and formatting inconsistencies.
A separate cleaned copy was created, and further validation
is required before the dataset is used for business analysis.