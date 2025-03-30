import requests
import pandas as pd

data=requests.get("https://api.rootnet.in/covid19-in/stats/history")
mydata=data.json()

my_dic={}
state=[]
date=[]


for i in range(0,len(mydata["data"])):
    cases=[]
    for j in range(0,len(mydata["data"][i]["regional"])):
        cases.append(mydata["data"][i]["regional"][j]["totalConfirmed"])
    date.append(mydata["data"][i]["day"])
    my_dic[mydata["data"][i]["day"]]=cases

for i in range(0,len(mydata["data"][0]["regional"])):
    state.append(mydata["data"][0]["regional"][i]["loc"])


df=pd.DataFrame(my_dic.items(),columns=["Name","Cases"])
# df[state]=df[[my_dic.values()]]

# for j in my_dic.values():
#     for i in j:
#         df["date"]=date

print(df)

