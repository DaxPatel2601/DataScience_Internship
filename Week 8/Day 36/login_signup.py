import streamlit as st
from click import password_option
from streamlit import session_state
from streamlit_option_menu import option_menu
import pandas as pd

# streamlit run app.py --server.address 0.0.0.0 --server.port 8501
# http://<your-computer-IP>:8501

def side_bar():
    with st.sidebar:
        sidebar_select=option_menu("Main",["Log-in","Sign-Up"],default_index=0,menu_icon="house",icons=["lock","unlock"],orientation="vertical")

    if sidebar_select=="Log-in":
        with st.form("Form1"):
            st.title("Log In")
            UserEnterUserName=st.text_input("Enter Your Username")
            UserEnterPassword=st.text_input("Enter Your Password",type="password")

            submit=st.form_submit_button("Submit")
            is_data_save=check_user_data(UserEnterUserName,UserEnterPassword)

            if submit:
                if is_data_save==True:
                    st.success("Login Successfully")
                else:
                    st.error("User name or Password is Wrong, please enter correct one")

    if sidebar_select=="Sign-Up":
        with st.form("Form2"):
            st.title("Sign Up")
            UserEnterNewUserName=st.text_input("Enter Your Username")
            UserEnterNewPassword=st.text_input("Enter Your Password",type="password")
            submit2 = st.form_submit_button("Submit")
            is_data_save = check_user_availabel(UserEnterNewUserName, UserEnterNewPassword)

            if submit2:
                if is_data_save==True:
                    st.error("User Name Already Taken")
                else:
                    enter_new_data(UserEnterNewUserName,UserEnterNewPassword)
                    st.success("User Successfully Register")


def check_user_data(UserEnterUserName,UserEnterPassword):
    df = pd.read_excel("userdata.xlsx")
    rows , cols = df.shape
    is_data_in=False

    for i in range(0,rows):
        if df.iat[i,1]==UserEnterUserName:
            for j in range(0,cols):
                if df.iat[i,2]==int(UserEnterPassword):
                    is_data_in=True
                    break

    return is_data_in


def enter_new_data(UserEnterNewUserName,UserEnterNewPassword):

    # Load existing data
    file_path = "userdata.xlsx"
    existing_data = pd.read_excel(file_path)
    rows , cols = existing_data.shape

    # New data
    new_data = pd.DataFrame([{'No': rows+1, 'User Name':UserEnterNewUserName, 'Password':int(UserEnterNewPassword)}])

    # Append and save
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_excel(file_path, index=False)


def check_user_availabel(UserEnterNewUserName,UserEnterNewPassword):
    df = pd.read_excel("userdata.xlsx")
    rows, cols = df.shape
    is_data_in = False

    for i in range(0, rows):
        if df.iat[i, 1] == UserEnterNewUserName:
            is_data_in = True
            break

    return is_data_in


side_bar()


