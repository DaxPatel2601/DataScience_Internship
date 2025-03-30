import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Streamlit Sidebar for Login & Signup
def side_bar():
    with st.sidebar:
        sidebar_select = option_menu("Main", ["Log-in", "Sign-Up"], default_index=0, menu_icon="house", icons=["lock", "unlock"], orientation="vertical")

    if st.session_state.logged_in:
        st.success(f"Welcome, {st.session_state.username}! 🎉")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()

    elif sidebar_select == "Log-in":
        login_form()

    elif sidebar_select == "Sign-Up":
        signup_form()


# Login Form
def login_form():
    with st.form("Form1"):
        st.title("Log In")
        username = st.text_input("Enter Your Username")
        password = st.text_input("Enter Your Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            is_valid = check_user_data(username, password)
            if is_valid:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login Successfully")
                st.rerun()
            else:
                st.error("User name or Password is Wrong, please enter correct one")


# Signup Form
def signup_form():
    with st.form("Form2"):
        st.title("Sign Up")
        new_username = st.text_input("Enter Your Username")
        new_password = st.text_input("Enter Your Password", type="password")
        submit2 = st.form_submit_button("Submit")

        if submit2:
            is_available = check_user_available(new_username)
            if is_available:
                st.error("User Name Already Taken")
            else:
                enter_new_data(new_username, new_password)
                st.success("User Successfully Registered 🎉")


# Check User Login Data
def check_user_data(username, password):
    df = pd.read_excel("userdata.xlsx")
    rows, cols = df.shape
    is_data_in = False

    for i in range(rows):
        if df.iat[i, 1] == username and df.iat[i, 2] == int(password):
            is_data_in = True
            break

    return is_data_in


# Save New User Data
def enter_new_data(username, password):
    file_path = "userdata.xlsx"
    existing_data = pd.read_excel(file_path)

    new_data = pd.DataFrame([{'No': len(existing_data) + 1, 'User Name': username, 'Password': int(password)}])

    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_excel(file_path, index=False)


# Check if Username Already Exists
def check_user_available(username):
    df = pd.read_excel("userdata.xlsx")
    return username in df['User Name'].values


# Run the Sidebar Function
side_bar()
