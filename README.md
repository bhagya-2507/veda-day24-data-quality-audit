# VEDA Technology — Day 24: Data Quality Audit

A Python-based data quality auditing project that identifies common data issues in a retail sales dataset and creates a separate cleaned dataset for further analysis.

## Project Overview

Data quality is essential for accurate reporting and business decision-making. This project audits a retail sales dataset to identify missing values, duplicate records, invalid quantities and prices, invalid dates, sales calculation mismatches, and inconsistent text formatting.

The project uses Python and Pandas to automate data quality checks while preserving the original raw dataset.

## Objectives

* Inspect the structure and dimensions of the dataset.
* Identify missing values and duplicate records.
* Detect invalid quantities and unit prices.
* Identify invalid or unparseable order dates.
* Validate sales totals against quantity and unit price.
* Detect inconsistent category and region formatting.
* Generate an issue log and audit summary.
* Create a separate cleaned dataset without overwriting the raw data.

## Technology Stack

* **Language:** Python
* **Data Analysis:** Pandas
* **Input/Output:** Excel and CSV
* **Development Environment:** Visual Studio Code
* **Version Control:** Git and GitHub

## Dataset Description

The project uses a retail sales dataset containing 50 original records and 9 columns.

| Column      | Description                            |
| ----------- | -------------------------------------- |
| Order_ID    | Unique identifier assigned to an order |
| Order_Date  | Date of the order                      |
| Customer_ID | Customer identifier                    |
| Product     | Product name                           |
| Category    | Product category                       |
| Quantity    | Number of units ordered                |
| Unit_Price  | Price per unit                         |
| Total_Sales | Recorded total sales value             |
| Region      | Sales region                           |

## Data Quality Checks

| Check               | Purpose                                            |
| ------------------- | -------------------------------------------------- |
| Missing Values      | Identify incomplete fields                         |
| Duplicate Records   | Detect repeated rows                               |
| Quantity Validation | Find zero or negative quantities                   |
| Price Validation    | Find zero or negative unit prices                  |
| Date Validation     | Detect invalid or unparseable dates                |
| Sales Validation    | Compare recorded totals with quantity × unit price |
| Text Consistency    | Identify inconsistent spacing and capitalization   |

## Project Workflow

1. Load the raw Excel dataset using Pandas.
2. Inspect the dataset dimensions, column names, and sample records.
3. Audit missing values and duplicate records.
4. Identify invalid quantities, prices, and dates.
5. Validate sales calculations.
6. Inspect category and region formatting.
7. Document the findings in an issue log.
8. Remove exact duplicate rows and standardize selected text fields in a separate copy.
9. Validate the cleaned output and export an audit summary.
10. Document the results and recommendations.

## Repository Contents

| File                        | Purpose                                                               |
| --------------------------- | --------------------------------------------------------------------- |
| `audit.py`                  | Python script containing the audit and validation logic               |
| `retail_sales_raw.xlsx`     | Original input dataset                                                |
| `retail_sales_cleaned.xlsx` | Separate dataset with duplicate removal and text standardization      |
| `issue_log.csv`             | Identified issues, affected orders, severity, and recommended actions |
| `audit_summary.csv`         | Summary of selected data quality metrics                              |
| `audit_report.md`           | Audit findings, cleaning activities, and recommendations              |

## How to Run the Project

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project folder

```bash
cd veda-day24-data-quality-audit
```

### 3. Install dependencies

```bash
python -m pip install pandas openpyxl
```

### 4. Run the audit script

```bash
python audit.py
```

The script reads `retail_sales_raw.xlsx` from the project directory. Run it from that directory so the input and output file paths resolve correctly.

## Results

The initial audit identified:

* 3 missing cells
* 1 duplicate row
* 2 records with invalid quantities
* 2 records with invalid unit prices
* 2 records with invalid dates
* 2 records with sales calculation mismatches

The audit also checks for inconsistent category and region formatting. Refer to the generated files and console output for the detailed findings.

## Cleaning and Validation Notes

The current cleaning workflow:

* Removes exact duplicate rows.
* Standardizes whitespace and capitalization in `Category` and `Region`.
* Preserves the original raw dataset.
* Exports the cleaned data separately.

Missing values and invalid business values are not automatically replaced. They require verification against the source data before correction. The cleaned dataset should therefore be treated as a partially cleaned dataset until all unresolved issues are reviewed.

## Key Learnings

* Performing data quality checks with Pandas.
* Detecting missing and duplicate records.
* Validating numeric and date fields.
* Checking business rules and calculated values.
* Standardizing text fields.
* Exporting audit results to CSV and Excel.
* Maintaining raw data separately from cleaned outputs.

## Conclusion

This project demonstrates a structured approach to auditing retail sales data using Python and Pandas. It identifies common quality issues, documents recommended actions, and creates a separate dataset for subsequent validation and analysis.

**Organization:** VEDA Technology
**Assignment:** Day 24 — Data Quality Audit
**Focus:** Data Cleaning, Validation, and Quality Reporting
