# Graph 4 :
#
# Allow user to insert correct names of 4 states, print 4 graphs ( 2 in first row, 2 in second row )
#
# https://api.rootnet.in/covid19-in/stats/latest
#
# Bar : States vs Confirmed
# Bar : States vs Deaths
# Pie : Confirmed cases ( percentage )
# Pie : Deaths ( percentage )


import requests
import matplotlib.pyplot as plt

url=("https://api.rootnet.in/covid19-in/stats/latest")
data=requests.get(url)
mydata=data.json()

states=[]
deaths=[]
cases=[]

while True:
    user_input=input("Enter Country name :").capitalize()
    if user_input!="Stop":
        for i in range(0,len(mydata["data"]["regional"])):
            if user_input==mydata["data"]["regional"][i]["loc"]:
                states.append(mydata["data"]["regional"][i]["loc"])
                cases.append(mydata["data"]["regional"][i]["totalConfirmed"])
                deaths.append(mydata["data"]["regional"][i]["deaths"])
    else:
        fig, axs = plt.subplots(2, 2, figsize=(15, 5))
        axs[0,0].barh(states, cases)
        axs[0,0].set_title("States vs Confirmed")
        axs[0,1].barh(states, deaths)
        axs[0, 1].set_title("States vs Deaths")
        axs[1,0].pie(cases,labels=states,autopct="%.2f%%")
        axs[1,0].set_title("Confirmed cases ( percentage )")
        axs[1,1].pie(deaths,labels=states,autopct="%.2f%%")
        axs[1,1].set_title("Deaths ( percentage )")
        plt.tight_layout()
        plt.show()
        break


