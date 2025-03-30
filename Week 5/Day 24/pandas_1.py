import pandas as pd

data_pd=pd.read_csv("Sales_Data.csv")

# print(data_pd)

# print columns
# print(data_pd.columns)

# print rows and columns
# print(data_pd.shape)

# print first column
print(data_pd["TransactionID"])

#check for null values

print(data_pd.isnull().sum())

# information of data_pd

print(data_pd.info())

# handle null values
# data_pd.dropna()
# print(data_pd())

# fill
data_pd=data_pd.fillna(data_pd["Price"].mean())
print(data_pd)
print(data_pd.info())

# print product names
x=data_pd["Product"].unique()
print(x)

print(data_pd["Product"].value_counts())

# print sum of price
print(data_pd["Price"].sum())

# print average of price
print(data_pd["Price"].mean())