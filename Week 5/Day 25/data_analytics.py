#https://docs.google.com/document/d/1tidt0ZVpbuDCfxaANyNrWdRal-v9SGsMW5HKjfriAok/edit?tab=t.0

# 1. Data Cleaning & Preprocessing
# Check for missing values and handle them appropriately.
# Detect and remove duplicate rows, if any.
# Convert the Order_Date column into a datetime format for analysis.

import pandas as pd

df=pd.read_csv("ecommerce_sales_large.csv")

# # check where is null values

x=df[df.isnull().any(axis=1)]
print(x)

