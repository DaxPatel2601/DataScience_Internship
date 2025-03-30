import pandas as pd
# import streamlit as st
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv("orders.csv (plr) - Sheet1.csv")

plt.scatter(df.id,df.amount)

poly=PolynomialFeatures(degree=3)
x_poly=poly.fit_transform(df[["id"]])

model=LinearRegression()
model.fit(x_poly,df[["amount"]])
plt.plot(df[["id"]].values,model.predict(x_poly))
plt.show()


