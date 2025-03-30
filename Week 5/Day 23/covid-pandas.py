import requests
import pandas as pd

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

data_dic={}

for i in range(0,len(mydata["data"]["regional"])):
    data_dic[mydata["data"]["regional"][i]["loc"]]=mydata["data"]["regional"][i]["totalConfirmed"]

data_pd=pd.Series(data_dic)
# print(data_pd)

#average
# print(data_pd.mean())

#apply sort
# print(data_pd.sort_values())

#calculate sum
print(data_pd.sum())

#print top 5
print(data_pd.head())

#print bottom 5
print(data_pd.tail())

#print sample
print(data_pd.sample())