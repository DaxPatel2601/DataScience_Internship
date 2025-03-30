import requests
import pandas as pd
from openpyxl.utils import column_index_from_string

data=requests.get("https://api.rootnet.in/covid19-in/stats/latest")
mydata=data.json()

my_dic={}

for i in range(0,len(mydata["data"]["regional"])):
    my_dic[mydata["data"]["regional"][i]["loc"]]=mydata["data"]["regional"][i]["totalConfirmed"]

df=pd.DataFrame(my_dic.items(),columns=["State","Cases"])
print(df)

