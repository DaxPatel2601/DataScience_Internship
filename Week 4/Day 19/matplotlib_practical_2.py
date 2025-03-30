from http.client import responses

import matplotlib.pyplot as plt
import requests
from Tools.scripts.generate_re_casefix import alpha

# GRAPH 2 :   http://universities.hipolabs.com/search?country={countrynamehere}
#
# Completely dynamic graph. Allow user to insert names of countries until user enter stop. When user enters stop,
# print bar graph of countries vs total universities in that country of all inserted countries.

country=[]
total_uni=[]

while True:
    user_input=input("Enter Country name :").lower()
    if user_input!="stop":
        url = ("http://universities.hipolabs.com/search?country=") + user_input
        data = requests.get(url)
        mydata = data.json()
        country.append(user_input)
        total_uni.append(len(mydata))
    else:
        print(country)
        print(total_uni)
        plt.bar(country,total_uni)
        plt.ylabel("Universities")
        plt.xlabel("Country")
        plt.grid(alpha=0.5)
        plt.show()
        break


