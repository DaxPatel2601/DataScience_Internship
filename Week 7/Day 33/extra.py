# Import Necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
var1=[1,2,3,4,5,6,7,8,5]
names=["dsad","sgdf","fgdf","drtg","srtg","srtg","Xrg","srtg","tdy"]
c1,c2,c3=st.columns(3)

plt.bar(names,var1)
st.write(plt.show())