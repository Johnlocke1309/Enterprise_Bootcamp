import pandas as pd

# Load the Excel file
df = pd.read_excel('Telco_customer_churn_demographics.xlsx')

# Preview the first few rows
print(df.head())

# Check data info
print(df.info())

# Get summary statistics
print(df.describe())