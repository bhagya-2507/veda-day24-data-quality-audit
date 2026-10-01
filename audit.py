import pandas as pd

# Load the raw sales dataset
df = pd.read_excel("retail_sales_raw.xlsx")

# Display first 5 rows
print(df.head())

# Display dataset dimensions
print("Rows and columns:", df.shape)

# Display column names
print("Column names:")
print(df.columns.tolist())
# Check missing values in each column
print("\n--- MISSING VALUES AUDIT ---")

missing_values = df.isnull().sum()

print(missing_values)

# Calculate total missing cells
total_missing = missing_values.sum()

print("\nTotal missing values:", total_missing)

# Check duplicate records
print("\n--- DUPLICATE RECORDS AUDIT ---")

duplicate_count = df.duplicated().sum()

print("Total duplicate rows:", duplicate_count)

# Display duplicate records
duplicates = df[df.duplicated(keep=False)]

print("\nDuplicate records:")
print(duplicates)
# Check invalid quantity
print("\n--- INVALID QUANTITY AUDIT ---")

invalid_quantity = df[df["Quantity"] <= 0]

print(invalid_quantity[
    ["Order_ID", "Product", "Quantity"]
])

print("Invalid quantity records:", len(invalid_quantity))


# Check invalid unit price
print("\n--- INVALID UNIT PRICE AUDIT ---")

invalid_price = df[df["Unit_Price"] <= 0]

print(invalid_price[
    ["Order_ID", "Product", "Unit_Price"]
])

print("Invalid price records:", len(invalid_price))# Check invalid dates
print("\n--- INVALID DATE AUDIT ---")

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

invalid_dates = df[df["Order_Date"].isna()]

print(invalid_dates[["Order_ID", "Order_Date"]])

print("Invalid date records:", len(invalid_dates))

# Check sales calculation mismatch
print("\n--- TOTAL SALES AUDIT ---")

expected_sales = df["Quantity"] * df["Unit_Price"]

sales_mismatch = df[
    df["Total_Sales"].notna()
    & expected_sales.notna()
    & ((df["Total_Sales"] - expected_sales).abs() > 0.01)
]

print(sales_mismatch[
    ["Order_ID", "Quantity", "Unit_Price", "Total_Sales"]
])

print("Sales mismatch records:", len(sales_mismatch))

# Check inconsistent text formatting
print("\n--- TEXT FORMATTING AUDIT ---")

for col in ["Category", "Region"]:
    original = df[col].astype("string")
    normalized = original.str.strip().str.title()

    inconsistent = df[
        original.notna() & (original != normalized)
    ]

    print(f"\nInconsistent values in {col}:")
    print(inconsistent[["Order_ID", col]])

    print("Inconsistent records:", len(inconsistent))
    
# Create a data quality issue log
print("\n--- CREATING ISSUE LOG ---")

issues = [
    {
        "Issue_Type": "Missing Customer_ID",
        "Affected_Orders": "1014",
        "Severity": "Medium",
        "Recommended_Action": "Verify customer details"
    },
    {
        "Issue_Type": "Missing Quantity",
        "Affected_Orders": "1024",
        "Severity": "High",
        "Recommended_Action": "Verify quantity from source"
    },
    {
        "Issue_Type": "Missing Unit_Price",
        "Affected_Orders": "1046",
        "Severity": "High",
        "Recommended_Action": "Verify product price"
    },
    {
        "Issue_Type": "Duplicate Record",
        "Affected_Orders": "1015",
        "Severity": "Medium",
        "Recommended_Action": "Verify and remove duplicate"
    },
    {
        "Issue_Type": "Invalid Quantity",
        "Affected_Orders": "1007, 1034",
        "Severity": "High",
        "Recommended_Action": "Verify quantity; must be positive"
    },
    {
        "Issue_Type": "Invalid Unit Price",
        "Affected_Orders": "1013, 1027",
        "Severity": "High",
        "Recommended_Action": "Verify price from source"
    },
    {
        "Issue_Type": "Invalid Order Date",
        "Affected_Orders": "1012, 1031",
        "Severity": "Medium",
        "Recommended_Action": "Verify and correct dates"
    },
    {
        "Issue_Type": "Total Sales Mismatch",
        "Affected_Orders": "1009, 1025",
        "Severity": "High",
        "Recommended_Action": "Verify Quantity x Unit_Price"
    },
    {
        "Issue_Type": "Inconsistent Text Formatting",
        "Affected_Orders": "Check audit output",
        "Severity": "Low",
        "Recommended_Action": "Standardize spaces and capitalization"
    }
]

issue_log = pd.DataFrame(issues)

issue_log.to_csv("issue_log.csv", index=False)

print("Issue log created successfully: issue_log.csv")
print(issue_log)

# Create a separate copy for cleaning
print("\n--- DATA CLEANING ---")

clean_df = df.copy()

# 1. Remove exact duplicate rows
clean_df = clean_df.drop_duplicates()

# 2. Standardize text formatting
clean_df["Category"] = (
    clean_df["Category"].astype("string").str.strip().str.title()
)

clean_df["Region"] = (
    clean_df["Region"].astype("string").str.strip().str.title()
)

# 3. Save the cleaned copy
clean_df.to_excel("retail_sales_cleaned.xlsx", index=False)

print("Original rows:", len(df))
print("Rows after removing duplicates:", len(clean_df))
print("Cleaned dataset saved as retail_sales_cleaned.xlsx")

# Validate the cleaned dataset
print("\n--- CLEANED DATASET VALIDATION ---")

cleaned_df = pd.read_excel("retail_sales_cleaned.xlsx")

print("Cleaned dataset shape:", cleaned_df.shape)

print("Remaining duplicate rows:", cleaned_df.duplicated().sum())

print("\nRemaining missing values:")
print(cleaned_df.isnull().sum())

print("\nSample cleaned records:")
print(cleaned_df.head())

# Final data quality audit summary
print("\n--- FINAL DATA QUALITY SUMMARY ---")

raw_df = pd.read_excel("retail_sales_raw.xlsx")
clean_df = pd.read_excel("retail_sales_cleaned.xlsx")

summary = {
    "Metric": [
        "Original Rows",
        "Original Columns",
        "Missing Cells",
        "Duplicate Rows",
        "Invalid Quantity Records",
        "Invalid Unit Price Records",
        "Invalid Date Records",
        "Cleaned Rows",
        "Cleaned Duplicate Rows"
    ],
    "Result": [
        len(raw_df),
        len(raw_df.columns),
        int(raw_df.isnull().sum().sum()),
        int(raw_df.duplicated().sum()),
        int((raw_df["Quantity"] <= 0).sum()),
        int((raw_df["Unit_Price"] <= 0).sum()),
        int(pd.to_datetime(raw_df["Order_Date"], errors="coerce").isna().sum()),
        len(clean_df),
        int(clean_df.duplicated().sum())
    ]
}

summary_df = pd.DataFrame(summary)

summary_df.to_csv("audit_summary.csv", index=False)

print(summary_df)
print("\nAudit summary saved as audit_summary.csv")