import requests

data=requests.get("https://isro.vercel.app/api/spacecrafts")
mydata=data.json()

my_dic={}

for i in range(0,len(mydata["spacecrafts"])):
    my_dic[mydata["spacecrafts"][i]["id"]]=mydata["spacecrafts"][i]["name"]

print(my_dic)