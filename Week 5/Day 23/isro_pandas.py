import requests
import pandas as pd
import numpy as np

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()
data_dic={}

for i in range(0,len(mydata["spacecrafts"])):
    data_dic[mydata["spacecrafts"][i]["id"]]=mydata["spacecrafts"][i]["name"]

data_pd=pd.Series(data_dic)
print(data_pd)

