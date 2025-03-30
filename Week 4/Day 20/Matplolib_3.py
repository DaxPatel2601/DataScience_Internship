import matplotlib.pyplot as plt
import requests

# Graph 3 :
#
# Create graphs as shown in below output,  to compare for state wise confirmed cases and state wise death cases from below API.
#
# API : https://api.rootnet.in/covid19-in/stats/latest
#

url=("https://api.rootnet.in/covid19-in/stats/latest")
data=requests.get(url)
mydata=data.json()

state=[]
cases=[]
deaths=[]

for i in range(0,len(mydata["data"]["regional"])):
    state.append(mydata["data"]["regional"][i]["loc"])
    cases.append(mydata["data"]["regional"][i]["totalConfirmed"])
    deaths.append(mydata["data"]["regional"][i]["deaths"])

fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Plot total cases
axs[0].barh(state,cases)
axs[1].barh(state,cases)

# Adjust layout
plt.tight_layout()
plt.show()

