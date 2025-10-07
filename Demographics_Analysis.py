import pandas as pd

# Load the Excel file
df = pd.read_excel('Telco_customer_churn_demographics.xlsx')

# Preview the first few rows
print(df.head())

# Check data info
print(df.info())

# Get summary statistics
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (update the filename if needed)
df = pd.read_excel('Telco_customer_churn_demographics.xlsx')

# 1. Gender Distribution
print("Gender Distribution:\n", df['Gender'].value_counts())
df['Gender'].value_counts().plot(kind='bar')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 2. Age Distribution
plt.hist(df['Age'], bins=20, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

print("Age Stats:\n", df['Age'].describe())

# 3. Distribution of Customers Under 30 and Senior Citizens
print("Customers Under 30:\n", df['Under 30'].value_counts())
df['Under 30'].value_counts().plot(kind='bar')
plt.title('Customers Under 30')
plt.show()

print("Senior Citizens:\n", df['Senior Citizen'].value_counts())
df['Senior Citizen'].value_counts().plot(kind='bar')
plt.title('Senior Citizens')
plt.show()

# 4. Marital Status Breakdown
married_counts = df['Married'].value_counts()
married_counts.plot(kind='bar')
plt.title('Marital Status Distribution')
plt.xlabel('Marital Status')
plt.ylabel('Number of Customers')
plt.show()

# 5. Dependents Analysis:
print("Average Dependents by Gender:\n", df.groupby('Gender')['Number of Dependents'].mean())
print("Average Dependents by Marital Status:\n", df.groupby('Married')['Number of Dependents'].mean())

# Histogram for dependents count
plt.hist(df['Number of Dependents'], bins=range(0, 10))
plt.title('Dependents Count Distribution')
plt.xlabel('Number of Dependents')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()

# 6. Correlation between Age and Dependents
print("Correlation between Age and Dependents:\n", df[['Age', 'Number of Dependents']].corr())

# Heatmap for correlation matrix
sns.heatmap(df.corr(), annot=True)
plt.title('Correlation Matrix')
plt.show()

# 7. Segmentation: Age Groups
bins = [18, 30, 40, 50, 60, 70, 80]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70-79']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

print("Customer count in each age group:\n", df['Age Group'].value_counts())
df['Age Group'].value_counts().sort_index().plot(kind='bar')
plt.title('Customer Distribution by Age Group')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()