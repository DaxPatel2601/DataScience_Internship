import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import numpy as np


df=pd.read_csv("salary.csv ( decision tree) - Sheet1.csv")
print(df)

le=LabelEncoder()

df[["company","job","degree"]]=df[["company","job","degree"]].apply(le.fit_transform)
df.to_csv("encoded_salary.csv")
print(df)

# For classification
dt_classifier = DecisionTreeClassifier(criterion="entropy", max_depth=5)

X_train=df[["company","job","degree"]]
y_train=df[["salary_more_then_100k"]]
dt_classifier.fit(X_train, y_train)

company=int(input("Company:(abc pharma:0,facebook:1,Google:2)"))
job=int(input("Job:(business manager:0,computer programmer:1,sales executive:2)"))
degree=int(input("Degree:(bachelors:0,masters:1)"))

X_test=np.array([[company,job,degree]])
# print(X_test)

predictions = dt_classifier.predict(X_test)

if predictions==0:
    print("No, You can not be able to get Salary more then 100K")
elif predictions==1:
    print("Yes, You can not be able to get Salary more then 100K")
else:
    print("Error")
