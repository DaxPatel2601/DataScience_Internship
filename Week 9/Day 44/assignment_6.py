from sklearn.datasets import load_diabetes
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import fetch_openml
import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

def diabetes_data():
    diabetes=load_diabetes()
    input=diabetes.data
    output=diabetes.target
    columns=diabetes.feature_names
    df=pd.DataFrame(input , columns=columns)
    df["result"]=output
    # print(df.isnull().sum())
    #there is no any null values in this dataset
    # save data set into csv file
    df.to_csv("Dataset/diabetes_origin.csv")
    y_depend="result"
    return df , columns , y_depend

def california_housing_data():
    california=fetch_california_housing()
    input=california.data
    output=california.target
    columns=california.feature_names
    df=pd.DataFrame(input,columns=columns)
    df["Result"]=output
    # print(df)

    # check  null
    # print(df.isnull().sum())
    # save data set into csv file
    df.to_csv("Dataset/california_housing_origin.csv")
    y_depend = "result"
    return df, columns, y_depend

def boston_data():
    # Load the Boston housing dataset
    boston = fetch_openml(name="boston", version=1, as_frame=True)
    input=boston.data
    output=boston.target
    columns=boston.feature_names
    df=pd.DataFrame(input,columns=columns)
    df["result"]=output

    # # check for null values
    # print(df.isnull().sum())
    # save data set into csv file
    df.to_csv("Dataset/boston_origin.csv")
    y_depend = "result"
    return df, columns, y_depend

def linear_regression(df,x_values,y_value,input_variable):
    model = LinearRegression()
    model.fit(df[[x_values]], df[[y_value]])
    result = model.predict([[input_variable]])
    return result

def main():
    with st.form("form1"):
        dataset=st.selectbox("Select Dataset ",["Diabetes","housing","boston"])
        model_name=st.selectbox("Select regression model",["Linear Regression","Multiple Linear Regression","Polynomial Regression"])
        submit=st.form_submit_button("Submit")

        if submit:
            if dataset=="Diabetes":
                df, x_indi , y_depend = diabetes_data()
                st.dataframe(df.head(5))

                with st.form("diabetes_form"):
                    age=st.number_input()
                    sex=st.number_input()
                    bmi=st.number_input()
                    bp=st.number_input()
                    s1=st.number_input()
                    s2=st.number_input()
                    s3=st.number_input()
                    s4=st.number_input()
                    s5=st.number_input()
                    s6=st.number_input()



            elif dataset=="housing":
                df, x_indi , y_depend = california_housing_data()
                st.dataframe(df.head(5))

            elif dataset=="boston":
                df, x_indi , y_depend = boston_data()
                st.dataframe(df.head(5))

            else:
                st.error("Somthing Went Wrong")

main()