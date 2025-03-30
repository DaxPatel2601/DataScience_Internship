import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Reset session state on page reload
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

# Check query params
query_params = st.query_params
if "auth" in query_params and query_params["auth"] == "true":
    st.session_state.logged_in = True

# Main Application UI
def main():
    with st.sidebar:
        sidebar = option_menu("IPL Analytics",
                              ["Home", "Overall Team Performance", "Player Insights", "Venue Analysis",
                               "Head-to-Head Analysis", "Season Overview", "Logout"],
                              default_index=0, menu_icon="🏠", icons=[""], orientation="vertical")

    if sidebar == "Home":
        st.success(f"Welcome, {st.session_state.username}! 🎉")

    elif sidebar == "Logout":
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.query_params.clear()
            st.rerun()

# Login System
def login():
    with st.sidebar:
        sidebar_select = option_menu("Main", ["Log-in", "Sign-Up"], default_index=0,
                                     menu_icon="house", icons=["lock", "unlock"], orientation="vertical")

    if st.session_state.logged_in:
        st.query_params["auth"] = "true"
        main()
    elif sidebar_select == "Log-in":
        login_form()
    elif sidebar_select == "Sign-Up":
        signup_form()


# Login Form
def login_form():
    with st.form("LoginForm"):
        st.title("Log In")
        username = st.text_input("Enter Your Username")
        password = st.text_input("Enter Your Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            if check_user_data(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.query_params["auth"] = "true"
                st.success("Login Successfully ✅")
                st.rerun()
            else:
                st.error("Invalid Username or Password ❌")

# Signup Form
def signup_form():
    with st.form("SignupForm"):
        st.title("Sign Up")
        new_username = st.text_input("Enter Your Username")
        new_password = st.text_input("Enter Your Password", type="password")
        submit = st.form_submit_button("Submit")

        if submit:
            if check_user_available(new_username):
                st.error("Username already taken ❌")
            else:
                enter_new_data(new_username, new_password)
                st.success("User Successfully Registered 🎉")

# Check if user credentials are correct
def check_user_data(username, password):
    try:
        df = pd.read_excel("userdata.xlsx")
        return any((df["User Name"] == username) & (df["Password"].astype(str) == password))
    except FileNotFoundError:
        return False
    except Exception as e:
        st.error(f"Error reading user data: {e}")
        return False

# Store new user credentials
def enter_new_data(username, password):
    file_path = "userdata.xlsx"
    try:
        existing_data = pd.read_excel(file_path)
    except FileNotFoundError:
        existing_data = pd.DataFrame(columns=["No", "User Name", "Password"])

    new_data = pd.DataFrame([{'No': len(existing_data) + 1, 'User Name': username, 'Password': str(password)}])
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_excel(file_path, index=False)

# Check if username is already taken
def check_user_available(username):
    try:
        df = pd.read_excel("userdata.xlsx")
        return username in df['User Name'].values
    except FileNotFoundError:
        return False

# Redirect based on login state
if st.session_state.logged_in:
    main()
else:
    login()

