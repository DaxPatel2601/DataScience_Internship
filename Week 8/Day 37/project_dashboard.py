# AI-Driven Intelligent Skill-Based Role Recommendation Model for Optimized Recruitment

import pandas as pd
import streamlit as st
import os
from click import password_option
from streamlit import session_state
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import random
import smtplib
from email.message import EmailMessage
import time

# streamlit run app.py --server.address 0.0.0.0 --server.port 8501
# http://<your-computer-IP>:8501

gender_group = ["Male", "Female", "Transgender"]
education_group = ["10th", "12th", "B.E.", "B.Tech", "M.E", "M.Tech"]
technology_group = ["Cloud Computing", "Data Science", "Web Development", "App Development", "UI/UX Designer",
                    "Cyber Security"]
place_group = ["Aheamdabad", "Gandhinagar", "Surat", "Rajkot", "Vadodara"]
skill_group = ["Python", "Sql", "Numpy", "Pandas", "Matplotlib", "Seaborn", "Xlrd", "Data Cleaning",
               "Data Preprocessing", "Data Visualization", "Machine Learning", "NLP", "Deep Learning"]
mode_group = ["On-Side", "Remote", "Internship"]


# Reset session state on page reload
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if "OTP" not in st.session_state:
    st.session_state.OTP = ""


# Check query params
query_params = st.query_params
if "auth" in query_params and query_params["auth"] == "true":
    st.session_state.logged_in = True

def side_bar():
    with st.sidebar:
        side_bar_select=option_menu("RecruitWise",["Home","Add New Data","Upload Data Set","Existing Files","Data Set","Filter","Chart Analysis","Role Recommendation","About Project","Log-out"],default_index=0,menu_icon="pie-chart",icons=["house","plus-square","table","back","clipboard","filter","bar-chart-fill","lightbulb","bell","lock"])


    if side_bar_select=="Home":
        st.toast(" Welcome To RecruitWise",icon="🎊")
        st.success(f'Login Successfully ✅ ')
        st.header("AI-Driven Intelligent Skill-Based Role Recommendation Model for Optimized Recruitment")
        st.image("image1.jpg")

        with st.expander("See More Info 🔽"):
            st.write('''The AI-Driven Resume and Job Matching System for Optimal Talent Acquisition is designed to 
                                        enhance the recruitment process by intelligently connecting candidates with the most relevant job 
                                        opportunities. Utilizing advanced machine learning algorithms and natural language processing, the 
                                        system analyzes job requirements and candidate profiles to identify the best-fit opportunities. By 
                                        leveraging data-driven insights and predictive analytics, it ensures a seamless and efficient hiring 
                                        experience for both employers and job seekers. This system optimizes talent acquisition by fostering 
                                        meaningful connections, reducing hiring complexities, and improving overall workforce alignment.''')






    Add_New_Data(side_bar_select)

    Upload_Data_Set(side_bar_select)

    Existing_Files(side_bar_select)

    Filter(side_bar_select)

    Chart_Analysis(side_bar_select)

    Data_set(side_bar_select)

    About_Project(side_bar_select)

    if side_bar_select == "Log-out":
        if st.button("Log Out"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.query_params.clear()
            st.rerun()

# add home page
# add filter page and chart page

def Upload_Data_Set(side_bar_select):
    if side_bar_select=="Upload Data Set":
        st.subheader("Upload Your Csv File Here")
        with st.form(key="Form 1"):
            for i in range(0,1):
                uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
            submit=st.form_submit_button("Submit")

            if submit:
                try:
                    progress_bar = st.progress(0)

                    for percent in range(1, 101, 10):
                        time.sleep(0.2)  # Simulate loading
                        progress_bar.progress(percent)
                    df=pd.read_csv(uploaded_file)
                    st.success("File Upload Successfully")
                    st.subheader(uploaded_file.name)
                    st.dataframe(df)
                    df.to_csv(f"uploaded_file/{uploaded_file.name}", index=False)

                except AttributeError and ValueError:
                    if not uploaded_file :
                        st.error("First Upload Csv file!!")

        st.subheader("CSV File Formate :")
        st.write("File Type Must be CSV")
        formate_csv=pd.read_csv("users_data/user_data_formate.csv")
        st.dataframe(formate_csv,hide_index=True)


        st.write("Download empty CSV file with correct formate")
        pdf_file_path = "users_data/user_data_formate.csv"  # Change this to your PDF file path

        # Open the file in binary mode
        with open(pdf_file_path, "rb") as file:
            csv_data = file.read()

        # Create a download button
        st.download_button(
            label="Download CSV File",
            data=csv_data,
            file_name="CSV_formate.csv",
        )

def Existing_Files(side_bar_select):
    if side_bar_select=="Existing Files":
        directory_path = r"C:\Users\DAKSH\PycharmProjects\PythonProject\new_project\DataScience_Internship\Week 8\Day 37\uploaded_file"
        if os.path.exists(directory_path):
            files = os.listdir(directory_path)
            st.subheader("Select Existing File")
            existing_file=[]
            for file in files:
                existing_file.append(file)

            with st.form(key="Form2"):
                filename=st.selectbox("Select File",existing_file,index=0)
                submit2=st.form_submit_button("Submit")

                if submit2:
                    try:
                        progress_bar = st.progress(0)

                        for percent in range(1, 101, 10):
                            time.sleep(0.2)  # Simulate loading
                            progress_bar.progress(percent)
                        if filename=="main_google.xlsx":
                            add_data_from_gfrom()
                        else:
                            df=pd.read_csv(f"uploaded_file/{filename}")
                            st.dataframe(df,hide_index=True)
                    except AttributeError and ValueError:
                        st.error("First Select File Name!!")

        else:
            st.error("Directory not found. Please check the path.")

def Add_New_Data(side_bar_select):
    if side_bar_select=="Add New Data":
        st.subheader("Add New Data")
        with st.form(key="form3"):
            name=st.text_input("Name :")
            number=st.text_input("Phone Number :")
            email=st.text_input("Enter Your Email Id :")
            gender=st.selectbox("Gender :",gender_group)
            age=st.number_input("Age :",min_value=15,max_value=40)
            education=st.selectbox("Higher Education :",education_group)
            technology=st.selectbox("Technology which you like to or work on :",technology_group)
            skills=st.multiselect("Skills :",skill_group)
            place=st.multiselect("City You Like To Do Work :",place_group,default=None)
            mode=st.selectbox("Mode Do You Prefer To Work :",mode_group)
            experience=st.number_input("Experience :",min_value=0,max_value=10,step=1)
            current_position=st.text_input("Enter Your Current Position (Mention fresher if you do not have any) :")
            linkedin_link=st.text_input("Enter Your LinkeIn Linke :")
            github_link=st.text_input("Enter Your GitHub Link :")
            resume=st.file_uploader("Upload Yor Latest resume(file formate must be pdf)", type=["pdf"])
            submit3=st.form_submit_button("Submit")

            if submit3:
                try:
                    progress_bar = st.progress(0)

                    for percent in range(1, 101, 10):
                        time.sleep(0.2)  # Simulate loading
                        progress_bar.progress(percent)
                    # Ensure the directory exists
                    upload_folder = "users_data/uploaded_resume"
                    if not os.path.exists(upload_folder):
                        os.makedirs(upload_folder)

                    if resume is not None:
                        # Save the uploaded file
                        with open(os.path.join(upload_folder, resume.name), "wb") as f:
                            f.write(resume.getbuffer())
                        resume_path=f"{resume.name}"
                        add_data(name,number,email,gender,age,education,technology,place,mode,skills,experience,current_position,linkedin_link,github_link,resume_path)
                        st.success("Successfully Uploaded Data.")

                except AttributeError and ValueError:
                    st.error("Fill All Details First")

        st.subheader("Google Form Link")
        st.write("If you want to fill form through Google forms or share to someone, here is the link")
        st.markdown('<a href="https://docs.google.com/forms/d/e/1FAIpQLSdp-ZI09-5rkhSGLFcehc29Ytu1yBAs346fxBVtGAAHoxSpxQ/viewform?usp=header" target="_blank">Google Form</a>', unsafe_allow_html=True)

def Filter(side_bar_select):
    if side_bar_select=="Filter":
        directory_path = r"C:\Users\DAKSH\PycharmProjects\PythonProject\new_project\DataScience_Internship\Week 8\Day 37\uploaded_file"
        if os.path.exists(directory_path):
            files = os.listdir(directory_path)
            st.subheader("Select Existing File")
            existing_file = []
            for file in files:
                existing_file.append(file)

            with st.form(key="Form2"):
                filename = st.selectbox("Select File", existing_file)
                submit2 = st.form_submit_button("Submit")
            if submit2:
                progress_bar = st.progress(0)

                for percent in range(1, 101, 10):
                    time.sleep(0.2)  # Simulate loading
                    progress_bar.progress(percent)
                st.write(f"Selected File : {filename}")

            with st.form(key="Form3"):
                df=pd.read_csv(f"uploaded_file/{filename}")
                unique_technology=[]
                find_unique(df,unique_technology,"Technology")
                unique_education=df["Education"].unique()
                unique_gender=df["Gender"].unique()
                unique_place=[]
                find_unique(df,unique_place,"Place")
                unique_mode=df["Mode"].unique()
                unique_current_position=[]
                find_unique(df,unique_current_position,"Current Position")

                df["Experience"] = df["Experience"].replace(r'(\d+) years', r'\1', regex=True)
                df["Experience"] = df["Experience"].replace(r'(\d+) year', r'\1', regex=True)
                df["Experience"] = df["Experience"].replace('Fresher', '0')
                df["Experience"] = df["Experience"].replace('No', '0')
                df["Experience"] = df["Experience"].replace('no', '0')
                df["Experience"] = df["Experience"].replace('5+ years', '5')
                df["Experience"]=df["Experience"].astype(int)
                st.dataframe(df, hide_index=True)

                age_range = st.slider("Select Age:", 0, 100, (10, 15),key="age")
                experience_range=st.slider("Select Experience",0,20,(2,4),key="experience")
                select_gender=st.multiselect("Select Gender",unique_gender)
                select_education=st.multiselect("Select Education",unique_education)
                select_technology=st.multiselect("Select Technology",unique_technology)
                select_place=st.multiselect("Select Place",unique_place)
                select_mode=st.multiselect("Select Mode",unique_mode)

                all_skills = set()
                for skill_list in df['Skills']:
                    skills = [skill.strip() for skill in skill_list.split(',')]
                    all_skills.update(skills)
                all_skills = sorted(list(all_skills))

                select_skills=st.multiselect("Select Skills",all_skills)
                select_current_position=st.multiselect("Select Current Position",unique_current_position)
                submit3=st.form_submit_button("Submit")

                if submit3:
                    progress_bar = st.progress(0)

                    for percent in range(1, 101, 10):
                        time.sleep(0.2)  # Simulate loading
                        progress_bar.progress(percent)
                    if not select_place:  # Enforce required field manually
                        select_place=unique_place
                    if not select_mode:
                        select_mode=unique_mode
                    if not select_current_position:
                        select_current_position=unique_current_position
                    if not select_technology:
                        select_technology=unique_technology
                    if not select_education:
                        select_education=unique_education
                    if not select_gender:
                        select_gender=unique_gender
                    if not age_range:
                        age_range[0]=0
                        age_range[1]=df["Age"].max()
                    if not experience_range:
                        experience_range=0
                    if not select_skills:
                        select_skills=all_skills

                    # Applying multiple filters at once
                    filtered_df = df[
                        ((df["Age"]>=age_range[0]) & (df["Age"]<=age_range[1])) &
                        ((df["Experience"]>=experience_range[0])&(df["Experience"]<=experience_range[1])) &
                        (df["Gender"].isin(select_gender)) &
                        (df["Education"].isin(select_education)) &
                        (df["Technology"].isin(select_technology)) &
                        (df["Place"].isin(select_place)) &
                        (df["Mode"].isin(select_mode)) &
                        (df["Current Position"].isin(select_current_position)) &
                        (df["Skills"].apply(lambda x: all(skill in x for skill in select_skills)))
                        ]

                    st.dataframe(filtered_df,hide_index=True)


def Chart_Analysis(side_bar_select):
    if side_bar_select=="Chart Analysis":
        directory_path = r"C:\Users\DAKSH\PycharmProjects\PythonProject\new_project\DataScience_Internship\Week 8\Day 37\uploaded_file"
        if os.path.exists(directory_path):
            files = os.listdir(directory_path)
            st.subheader("Select Existing File")
            existing_file = []
            for file in files:
                existing_file.append(file)

        with st.form(key="Form2"):
            filename = st.selectbox("Select File", existing_file)
            submit2 = st.form_submit_button("Submit")
        if submit2:
            progress_bar = st.progress(0)

            for percent in range(1, 101, 10):
                time.sleep(0.2)  # Simulate loading
                progress_bar.progress(percent)

            df = pd.read_csv(f"uploaded_file/{filename}")
            st.dataframe(df)
            gender_counts=df['Gender'].value_counts()

            st.subheader("Gender Wise Analysis")
            fig , ax = plt.subplots(figsize=(8,45))
            ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig)

            st.subheader("Age Wise Analysis")
            fig1 , ax1 = plt.subplots(figsize=(15   ,5))
            ax1.bar(df["Age"].unique(),df['Age'].value_counts())
            plt.xticks(df["Age"].unique())
            st.pyplot(fig1)

            st.subheader("Education Wise Analysis")
            education_counts = df['Education'].value_counts()
            fig2, ax2 = plt.subplots(figsize=(8,5))
            ax2.pie(education_counts, labels=education_counts.index, autopct='%1.1f%%', startangle=90)
            st.pyplot(fig2)





def Data_set(side_bar_select):

    if side_bar_select=="Data Set":
        datafrmae_file = pd.read_csv("users_data/main.csv")
        st.dataframe(datafrmae_file,hide_index=True)

def About_Project(side_bar_select):
    if side_bar_select=="About Project":

        st.title("Project Title:")
        st.write("AI-Driven Intelligent Skill-Based Role Recommendation Model for Optimized Recruitment")

        st.subheader("Abstract:")
        st.write('''The AI-Driven Resume and Job Matching System for Optimal Talent Acquisition is designed to 
                    enhance the recruitment process by intelligently connecting candidates with the most relevant job 
                    opportunities. Utilizing advanced machine learning algorithms and natural language processing, the 
                    system analyzes job requirements and candidate profiles to identify the best-fit opportunities. By 
                    leveraging data-driven insights and predictive analytics, it ensures a seamless and efficient hiring 
                    experience for both employers and job seekers. This system optimizes talent acquisition by fostering 
                    meaningful connections, reducing hiring complexities, and improving overall workforce alignment.''')

        st.subheader("Problems in the Existing System")
        st.write('''1. Time-Consuming Manual Screening – HR professionals spend excessive time reviewing resumes.''')
        st.write('''2. Mismatch in Job Selection – Candidates often apply for roles that do not match their skills.''')
        st.write('''3. Lack of Data-Driven Insights – Traditional hiring processes do not leverage predictive analytics.''')
        st.write('''4. Inefficient Talent Acquisition – Employers struggle to find the best-fit candidates efficientl''')
        st.write('''5. Bias in Recruitment – Human-led screening can lead to unconscious bias in hiring.''')

        st.subheader("Purpose of the Project ")
        st.write('''• To automate and optimize the recruitment process using AI-driven algorithms.''')
        st.write('''• To provide accurate job recommendations for candidates based on their profiles.''')
        st.write('''• To enable employers to quickly identify the best-fit candidates.''')
        st.write('''• To enhance data-driven decision-making in hiring.''')
        st.write('''• To minimize bias and increase fairness in the recruitment process.''')

        st.subheader("Functional Requirements")
        st.write('''1. Resume Parsing & Analysis – Extract key skills, experience, and qualifications from resumes.''')
        st.write('''2. Job Matching Algorithm – AI-based matching of candidates with job postings.''')
        st.write('''3. Job Posting & Management – Employers can create, edit, and manage job listings.''')
        st.write('''4. Recommendation System – Personalized job recommendations for candidates.''')
        st.write('''5. Feedback & Review System – Employers can provide feedback on applications.''')

        st.subheader("System Modules")
        st.write('''1. AI Job Matching Module – NLP-based resume analysis and job compatibility scoring.''')
        st.write('''2. Application Module – candidate applications and employer responses.''')
        st.write('''3. Recommendation System – Provides job suggestions based on user behavior and data.''')

        st.subheader("System Requirements")
        st.write('''Hardware Requirements:''')
        st.write('''        • Processor: Intel i5 or higher''')
        st.write('''        • RAM: 8GB minimum''')
        st.write('''        • Storage: 250GB SSD or more''')
        st.write('''        • Internet Connectivity: Stable broadband connection''')

        st.write('''Software Requirements:''')
        st.write('''        • Operating System: Windows''')
        st.write('''        • Pycharm , python''')
        st.write('''        • Required AI Libraries''')

        st.subheader("Front End and Back End of System")
        st.write('''• Front End (Client-Side): StreamLit''')
        st.write('''• Back End (Server-Side): Python , Machine Learning Models , AI models''')

        st.subheader("Download Pdf of Project Overview")
         # File path of the PDF to be shared
        pdf_file_path = "AI-Driven Intelligent Skill-Based Role Recommendation.pdf"  # Change this to your PDF file path

        # Open the file in binary mode
        with open(pdf_file_path, "rb") as file:
            pdf_data = file.read()

        # Create a download button
        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name="AI-Driven Intelligent Skill-Based Role Recommendation.pdf",
            mime="application/pdf"
        )

def add_data(name,number,email,gender,age,education,technology,place,mode,skills,experience,current_position,linkedin_link,github_link,resume_path):
    # Load existing data
    file_path = "users_data/main.csv"
    existing_data = pd.read_csv(file_path)
    rows, cols = existing_data.shape

    # second file data
    file_path_2="uploaded_file/main.csv"
    existing_data_2 = pd.read_csv(file_path_2)
    rows_2 ,cols_2 = existing_data_2.shape

    # New data
    new_data = pd.DataFrame(
        [{'No': rows + 1, 'Name': name, 'Number': int(number),'Email':email,'Gender':gender,'Age':age,"Education":education,'Technology':technology,'Place':place,'Mode':mode,'Skills':skills,'Experience':experience,'Current Position':current_position,'Linkedin Link':linkedin_link,'Github Link':github_link,'Resume':resume_path}])

    # New data
    new_data_2 = pd.DataFrame(
        [{'No': rows_2 + 1, 'Name': name, 'Number': int(number), 'Email': email, 'Gender': gender, 'Age': age,
          "Education": education, 'Technology': technology, 'Place': place, 'Mode': mode, 'Skills': skills,
          'Experience': experience, 'Current Position': current_position, 'Linkedin Link': linkedin_link,
          'Github Link': github_link, 'Resume': resume_path}])

    # Append and save
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv(file_path, index=False)

    # Append and save another file
    updated_data_2 = pd.concat([existing_data_2,new_data_2],ignore_index=True)
    updated_data_2.to_csv(file_path_2,index=False)

def find_unique(df,lst,string):
    for skills in df[string].dropna():
        for skill in skills.split(", "):
            if skill not in lst:
                lst.append(skill)

# Login System
def login():
    with st.sidebar:
        sidebar_select = option_menu("Main", ["Log-in", "Sign-Up"], default_index=0,
                                     menu_icon="house", icons=["lock", "unlock"], orientation="vertical")

    if st.session_state.logged_in:
        st.query_params["auth"] = "true"
        side_bar()
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
        new_username = st.text_input("Enter New Username")
        new_password = st.text_input("Enter Password", type="password")
        user_name=st.text_input("Enter Your Name")
        user_email=st.text_input("Enter Your Email Id")
        sendsubmit = st.form_submit_button("Send OTP")


    if sendsubmit:
        try:
            if new_username=="":
                st.error("Enter New Username")
            elif new_password=="":
                st.error("Enter New Password")
            elif user_name=="":
                st.error("Enter User Name")
            elif user_email=="":
                st.error("Enter Email")
            elif check_user_available(new_username):
                st.error("Username already taken ❌")
            else:
                st.session_state.OTP= mail_varify(user_email,user_name)

        except smtplib.SMTPRecipientsRefused:
            st.error("Enter Valid Email ID")

    if len(session_state.OTP)==6:
        with st.form("check_form"):
            user_otp = st.text_input("Enter OTP:")
            submit8=st.form_submit_button("submit")

            if submit8:
                if check_user_available(new_username):
                    st.success("User Successfully Registered 🎉")
                else:
                    if user_otp==st.session_state.OTP:
                        enter_new_data(new_username, new_password)
                        st.success("User Successfully Registered 🎉")

                    elif user_otp=="":
                        st.error("Enter OTP First")
                    else:
                        print(st.session_state.OTP)
                        st.error("Invalid OTP")

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


def mail_varify(user_mail,user_name):
    otp = ""

    for i in range(6):
        otp += str(random.randint(0, 9))

    # print(otp)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    from_mail = "pateldax2601@gmail.com"
    server.login(from_mail, "tvou ifug xacj nyha")
    to_mail = user_mail

    msg = EmailMessage()
    msg["Subject"] = "OTP Verification"
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg.set_content(f"{user_name} , Your OTP is :" + otp)
    server.send_message(msg)
    # print("Email Send")
    return otp

def add_data_from_gfrom():
    gfrom_df=pd.read_excel("uploaded_file/main_google.xlsx" )
    st.dataframe(gfrom_df)


# Redirect based on login state
if st.session_state.logged_in:
    side_bar()
else:
    login()

