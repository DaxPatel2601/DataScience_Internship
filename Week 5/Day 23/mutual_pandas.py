import requests
import pandas as pd
import numpy as np

data=requests.get("api.mfapi.in/mf")
mydata=data.json()

data_pd={}
print(len(mydata))
# for i in range(0,len(mydata)):
#     random_id=np.random.randint(100000,999999,size=len(mydata))
#     data_pd[random_id]=mydata[i]["schemeName"]
#
# print(mydata)