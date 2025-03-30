import requests
import matplotlib.pyplot as plt


# GRAPH 1 :   http://universities.hipolabs.com/search?country={countrynamehere}
#
# From above API create pie chart of count of universities in following countries.
# India, Pakistan, China, Nepal, Japan

user_country=["India", "Pakistan", "China", "Nepal", "Japan"]
total_uni=[]

for i in user_country:
    url=f"http://universities.hipolabs.com/search?country={i}"
    data=requests.get(url)
    mydata=data.json()
    total_uni.append(len(mydata))

plt.pie(total_uni,labels=user_country,autopct="%.2f%%")
plt.legend()
plt.show()