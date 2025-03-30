from sklearn.datasets import fetch_california_housing
import pandas as pd

housing= fetch_california_housing()

input=housing.data
output=housing.target
cols=housing.feature_names

df=pd.DataFrame(input,columns=cols)

df["price"]=output

# check null values
print(df.isnull().sum())

# check rows and cols
print(df.shape)
print(df)

# save the data into csv file

df.to_csv("Housing.csv")
