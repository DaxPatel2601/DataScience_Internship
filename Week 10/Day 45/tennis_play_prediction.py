from operator import index

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
import numpy as np

df=pd.read_csv("PlayTennis.csv")
# print(df)

le=LabelEncoder()

df[["outlook","temp","humidity","windy","play"]]=df[["outlook","temp","humidity","windy","play"]].apply(le.fit_transform)


df.to_csv("encoded_PlayTennis.csv",index=False)
# print(df)

# For classification
dt_classifier = DecisionTreeClassifier(criterion="entropy", max_depth=5)

X_train=df[["outlook","temp","humidity","windy"]]
y_train=df[["play"]]
dt_classifier.fit(X_train, y_train)


outlook=int(input("OUTLOOK:(overcast:0,rainy:1,sunny:2)"))
temp=int(input("TEMP:(cool:0,hot:1,mild:2)"))
humidity=int(input("HUMIDITY:(high:0,normal:1)"))
windy=int(input("WINDY:(False:0,True:1)"))
X_test=np.array([[outlook,temp,humidity,windy]])
# print(X_test)

predictions = dt_classifier.predict(X_test)

if predictions==0:
    print("NO")
elif predictions==1:
    print("YES")
else:
    print("Error")
