from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd


df=pd.read_csv("customers.csv ( encoding ) - Sheet1.csv")
print(df)

# first apply label encoding

lb=LabelEncoder()

df[["gender","purchased"]]=df[["gender","purchased"]].apply(lb.fit_transform)
print(df)

# apply ordinal encoding

oe=OrdinalEncoder()

df[["review","education"]]=oe.fit_transform(df[["review","education"]])
print(df)

df.to_csv("encoded customer data.csv")