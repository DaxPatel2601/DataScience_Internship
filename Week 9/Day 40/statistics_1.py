import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.preprocessing import PolynomialFeatures

with st.form("form1"):
    st.subheader("Predict Value of Y")
    df = pd.read_excel("Stat1.xlsx")
    st.dataframe(df)
    independent_element=st.number_input("Enter Independent element:",min_value=0)
    submit=st.form_submit_button("Submit")

    if submit:
        model = LinearRegression()
        model.fit(df[["x"]], df[["y"]])
        result=model.predict([[independent_element]])
        st.info(result)

        fig, ax = plt.subplots()
        ax.scatter(df[["x"]], df[["y"]])
        model.fit(df[["x"]], df[["y"]])
        ax.plot(df[["x"]].values, model.predict("y"))
        st.pyplot(fig)



