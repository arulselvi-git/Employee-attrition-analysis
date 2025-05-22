import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a beautiful style for all plots
sns.set(style="whitegrid")

# Step 1: Load dataset
df = pd.read_csv('HR_Attrition.csv')

# Step 2: Show first few rows
print(" Preview of Dataset:")
print(df.head())

# Step 3: Create SalaryLevel column
def get_salary_level(salary):
    if salary < 55000:
        return 'Low'
    elif salary <= 65000:
        return 'Medium'
    else:
        return 'High'

df['SalaryLevel'] = df['Salary'].apply(get_salary_level)

# Step 4: Countplot - Salary Level vs Attrition
plt.figure(figsize=(8, 6))
sns.countplot(x='Attrition', hue='SalaryLevel', data=df, palette='Set2')
plt.title("Attrition Count by Salary Level", fontsize=14)
plt.xlabel("Attrition", fontsize=12)
plt.ylabel("Number of Employees", fontsize=12)
plt.legend(title="Salary Level")
plt.tight_layout()
plt.show()

# Step 5: Boxplot - Satisfaction vs Attrition
plt.figure(figsize=(8, 6))
sns.boxplot(x='Attrition', y='Satisfaction', data=df, palette='Pastel1')
plt.title("Satisfaction Level by Attrition", fontsize=14)
plt.xlabel("Attrition", fontsize=12)
plt.ylabel("Satisfaction (0 to 1)", fontsize=12)
plt.tight_layout()
plt.show()

# Step 6: Heatmap - Correlation between numeric features
plt.figure(figsize=(7, 5))
corr = df[['Salary', 'Satisfaction', 'Workload']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=14)
plt.tight_layout()
plt.show()