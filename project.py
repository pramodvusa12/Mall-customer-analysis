import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
 
df = pd.read_csv("Mall_Customers.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Check null values
print(df.isnull().sum())

# If any missing values exist
df = df.dropna()
#average age 
print("Average Age:", np.mean(df["Age"]))
#gender count
print(df["Gender"].value_counts())
#average income
print("Average Income:", np.mean(df["Annual Income (k$)"]))
#age distribution
plt.hist(df["Age"])
plt.title("Age Distribution")
plt.show()
#income vs spending score
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Behavior")
plt.show()
#Customer Segmentation
def segment_customer(row):
    if row["Annual Income (k$)"] > 70 and row["Spending Score (1-100)"] > 60:
        return "Rich Spenders"
    elif row["Annual Income (k$)"] > 70:
        return "Rich Savers"
    elif row["Spending Score (1-100)"] > 60:
        return "Careless Spenders"
    else:
        return "Budget Customers"

df["Category"] = df.apply(segment_customer, axis=1)

print(df.head())
#Segment Analysis
print(df["Category"].value_counts())
df.to_excel("Customer_Segmentation_Output.xlsx", index=False)
