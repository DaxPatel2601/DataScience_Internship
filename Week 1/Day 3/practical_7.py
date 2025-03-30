import requests

data=requests.get("http://universities.hipolabs.com/search?country=india")
mydata=data.json()

# 1) How many main keys are there ?
print("This id a list formate so there is no any main keys in this API")

# 2) How many universities data is available ?
print("There is total ",len(mydata)," universities data are available in this API")

# 3) Print Atharva College of Engineering
print(mydata[0]["name"])

# 4) Print All university data using for loop as below format
for i in range(0,len(mydata)):
    print(i,")","University Name:",mydata[i]["name"],"\n\t","Website:",mydata[i]["web_pages"][0],"\n\t","Region:",mydata[i]["state-province"],"\n")


