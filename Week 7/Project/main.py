import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# color theme :
# [theme]
# primaryColor="#ff9800"
# backgroundColor="#0f172a"
# secondaryBackgroundColor="#1e293b"
# textColor="#eaecef"


def side_bar():
    with st.sidebar:
        selected2=option_menu("Side Bar",["Dashboard","Project Detail","Dataset","Project Code","Visualization","About Admin","Settings","Login","LogOut"],icons=["rocket","info","table","code","signal","people","gear","lock","unlock"],menu_icon=["house"],default_index=0,orientation="virtical")

def data_set():
    df=pd.read_csv("filepath3")
    return df

side_bar()