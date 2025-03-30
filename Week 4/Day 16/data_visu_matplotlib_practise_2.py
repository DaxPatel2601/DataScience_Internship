import matplotlib.pyplot as plt
import numpy as np

data = {"CASES":[
   {"state":"GUJARAT","total":275000},
   {"state":"MAHARASHTRA","total":1275000},
   {"state":"GOA","total":75000},
   {"state":"MP","total":475000}
]}

states=[]
totals=[]

for i in range(0,len(data["CASES"])):
   states.append(data["CASES"][i]["state"])
   totals.append(data["CASES"][i]["total"])

plt.yticks([100000 * i for i in range(0,16)],[f"{i}L" for i in range(0,16)])
plt.bar(states,totals)
plt.show()


