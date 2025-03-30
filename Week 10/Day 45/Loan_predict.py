import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("Bank_data.csv")
st.header("Loan Status Prediction!")

le=LabelEncoder()

df[["Gender","MaritalStatus"]]=df[["Gender","MaritalStatus"]].apply(le.fit_transform)
df.to_csv("encoded_Bank_data.csv")

with st.form("loan"):
    st.subheader("Parameter")
    age = st.slider("Age",min_value=18,max_value=100)
    income = st.slider("Income",min_value=0,max_value=160000)
    gender=st.selectbox("Gender",["Male","Female"])
    creditScore = st.slider("Creditscore",min_value=200,max_value=1000)
    MaritalStatus = st.selectbox("Marital Status",["Married","Single","Divorced"])
    Loan_amount=st.slider("Loan Amount",min_value=800,max_value=60000)
    submit=st.form_submit_button("Predict")
    if gender=="Male":
        gender=1
    elif gender=="Female":
        gender=0

    if MaritalStatus=="Married":
        MaritalStatus=1
    elif MaritalStatus=="Single":
        MaritalStatus=2
    elif MaritalStatus=="Divorced":
        MaritalStatus=0

    if submit:
        model = DecisionTreeClassifier()
        x_train = df[["Age","Gender", "Income" ,"CreditScore","MaritalStatus","LoanAmount"]]
        train=np.array([[age ,gender, income , creditScore,MaritalStatus,Loan_amount]])
        model.fit(x_train , df[["LoanStatus"]])
        result = model.predict(train)
        if result==1:
            st.error("Rejected")
        else:
            st.success("Approved")


