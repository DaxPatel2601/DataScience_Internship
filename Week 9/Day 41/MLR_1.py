import pandas as pd
import streamlit as st
from pandas.core.computation.common import result_type_many
from sklearn import linear_model
import matplotlib.pyplot as plt

with st.form("form1"):
    df=pd.read_csv("orderdata.csv")
    st.dataframe(df)
    users = st.number_input("Enter users", min_value=0)
    orders = st.number_input("Enter orders", min_value=0)
    age = st.number_input("Enter age", min_value=0)
    submit = st.form_submit_button("Submit")

    if submit:
        model=linear_model.LinearRegression()
        model.fit((df[["users","orders","age"]]),df[["amount"]])
        result=model.predict([[users,orders,age]])
        st.info(result)



