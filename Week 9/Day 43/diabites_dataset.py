from sklearn.datasets import load_diabetes
import pandas as pd

diabetes=load_diabetes()

inputes=diabetes.data
output=diabetes.target
columns=diabetes.feature_names

df=pd.DataFrame(inputes,columns=columns)
df["data"]=output
print(df)
df.to_csv("diabetes.csv")
