import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

with st.sidebar:
    selected=option_menu("Admin Panel",["Login","Upload Dataset","Revenue Forcasting","Growth Analysis","About us","Contact Us","Settings"],icons=["lock","table","graph-up-arrow","bar-chart-fill","people","telephone-fill","gear-fill"],menu_icon=["house"],default_index=0,orientation="vertical")


emails=["jimipatel@gmail.com","dakshbhesdadiya2601@gmail.com","user@gmail.com","admin@gmail.com"]
passwords=["5103","2601","1234","4321"]

if selected=="Login":
    st.header("Login Here")
    with st.form(key="loginform"):
        email=st.text_input("Enter Email")
        password=st.text_input("Password",type="password")
        submit=st.form_submit_button(label="Login")

        if submit:
            if email in emails:
                user_index = emails.index(email)
                if password == passwords[user_index]:
                    st.success("Login successfully")
                else:
                    st.error("Invalid email or password")
            else:
                st.error("Invalid email or password")


if selected=="Upload Dataset":

    st.header("📊 Upload Historical Business Data")
    st.write("Upload your business's historical revenue data in CSV or Excel format.")

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success("✅ File Uploaded Successfully!")
            st.subheader("📂 Preview of Uploaded Data")
            st.dataframe(df)

            st.subheader("📈 Data Summary")
            st.write(df.describe())

        except Exception as e:
            st.error(f"❌ Error: {e}")

if selected=="About us":
    st.header("AI-Driven Revenue Forecasting and Trend Analysis for Business Growth ")
    st.markdown(
        """
        **Project Description/Abstract:** 
        AI-Driven Revenue Forecasting and Trend Analysis for Business 
        Growth" is a machine learning project that predicts future revenue trends by analyzing historical data. 
        It identifies patterns, detects anomalies, and forecasts revenue. The system accounts for seasonal 
        fluctuations, market conditions, and consumer behavior, providing businesses with actionable insights. 
        It aids in financial planning, risk mitigation, and strategic resource allocation. The solution is adaptable 
        to various industries such as retail, e-commerce, and SaaS. Ultimately, it enables data-driven decision
        making for sustained business growth.
        
        **Problems in the Existing System** 
        1. Inaccurate Revenue Predictions – Traditional forecasting methods lack precision. 
        2. Limited Consideration of Market Trends – Many forecasting models ignore external factors 
           like economic shifts. 
        3. Inability to Detect Anomalies – Unexpected market disruptions remain unaccounted for. 
        4. Manual Data Analysis – Businesses rely on time-consuming and error-prone manual 
           calculations. 
        5. Poor Financial Planning – Lack of accurate revenue forecasts leads to ineffective budgeting 
           and resource allocation.
           
        **Purpose of the Project** 
        • To predict future revenue trends using machine learning. 
        • To analyze historical financial data and identify revenue patterns. 
        • To detect anomalies and fluctuations for proactive decision-making. 
        • To provide accurate and actionable financial insights for business growth. 
        • To support strategic resource allocation and risk mitigation.   
        
        **Functional Requirements**
        1. Data Ingestion & Preprocessing – Collects, cleans, and normalizes historical revenue data. 
        2. Trend Analysis & Visualization – Generates charts and insights on revenue trends. 
        3. Revenue Forecasting Model – Uses ML algorithms to predict future revenue. 
        4. Anomaly Detection – Identifies outliers and revenue discrepancies. 
        5. Report Generation – Provides detailed financial summaries for stakeholders. 
        6. Industry-Specific Adaptability – Customizable for various business domains. 
        7. User Dashboard – Interactive UI displaying real-time analytics and insights.
        
        **System Modules**
        1. Data Collection Module – Gathers historical revenue and market data. 
        2. Preprocessing & Feature Engineering – Cleans and prepares data for analysis. 
        3. Machine Learning Model – Predicts revenue trends and detects anomalies. 
        4. Visualization & Reporting Module – Displays graphs, reports, and insights. 
        5. User Management Module – Allows different user roles (admin, analyst, manager).
        
        **System Requirements**
        
        *Hardware Requirements:* \n
           • Processor: Intel i5 or higher 
           • RAM: 8GB minimum 
           • Storage: 250GB SSD or more 
           • Internet Connectivity: Stable broadband connection 
        *Software Requirements:* \n
           • Operating System: Windows 
           • Pycharm , python 
           • Required AI Libraries 
           
        **Front End and Back End of System**
           • Front End (Client-Side): StreamLit \n
           • Back End (Server-Side): Python , Machine Learning Models , AI models   
        """
    )




