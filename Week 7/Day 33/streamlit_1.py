import streamlit as st

# st.header("Hello")
# st.subheader("My self Dax Patel")
# st.write("210160116054")
# st.text("GEC Modasa")
#
# st.button("Click Me!!")
#
# if st.button:
#     print("DD")
#
#
# name=st.text_input("Enter Your Name Here:")
# phone_no=st.text_input("Enter Your Number Here:")
#
# st.write(name)
# st.write(phone_no)
#
# course=st.selectbox("Select Your Course Name : ",["IT","CS","ME","EE","AE"])
# skills=st.multiselect("Enter Skill do you have",["ML","DL","DS","DA"])

with st.form(key="Form1"):
    st.header("Give Your Information")
    name = st.text_input("Enter Your Name Here:")
    phone_no = st.text_input("Enter Your Number Here:")
    course = st.selectbox("Select Your Course Name : ", ["IT", "CS", "ME", "EE", "AE"])
    skills = st.multiselect("Enter Skill do you have", ["ML", "DL", "DS", "DA"])

    submit=st.form_submit_button(label="submit")

with st.form(key="form2"):
    if submit:
        st.write(name)
        st.write(phone_no)
        st.write(course)
        st.write(skills)



